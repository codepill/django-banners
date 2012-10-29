from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
import Image
import mimetypes
import utils
import os


class Slot(models.Model):
    symbol = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=255)
    limit = models.PositiveIntegerField(null=True, blank=True)
    rotate = models.BooleanField(default=False)
    random = models.BooleanField(default=False)

    def __unicode__(self):
        return 'Banner Slot "%s"' % self.name

    @property
    def published_banners(self):
        qs = self.banner_set.all().published()
        if self.random:
            qs = qs.order_by('?')
        else:
            qs = qs.order_by('display_order', 'id')
        return qs


class BannerQuerySet(models.query.QuerySet):
    def published(self):
        return self.filter(is_published=True)


class BannerManager(models.Manager):
    def get_query_set(self):
        return BannerQuerySet(self.model).order_by('display_order')


class Banner(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    slot = models.ForeignKey(Slot)
    # TODO: temporary using file field, but will be changed to special field handling SWF/Image
    image = models.FileField(upload_to='uploads/banners/%y/%j/%H/%M%S/',
                             null=True, blank=True)
    image_rollover = models.FileField(max_length=255,
                                      null=True, blank=True, upload_to=os.path.join('uploads', 'banners'),
                                      verbose_name=_('on hover image'))
    is_published = models.BooleanField(default=False)
    destination = models.CharField(max_length=255, null=True, blank=True)
    popup = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    custom_html = models.TextField(null=True, blank=True)
    order_field = 'display_order'
    ordering = ('display_order', 'id',)

    objects = BannerManager()

    def order_link(self):
        model_type_id = ContentType.objects.get_for_model(self.__class__).id
        kwargs = {"model_type_id": model_type_id}
        url = reverse("admin_order", kwargs=kwargs)
        return '<a href="%s" class="order_link">%s</a>' % (url, str(self.pk) or '')

    order_link.allow_tags = True
    order_link.short_description = 'Order'  # If you change this you should change admin_sorting.js too

    @property
    def media_path(self):
        return self.image # bc

    @property
    def hover_media_path(self):
        return self.image_rollover # bc

    @property
    def section(self):
        return self.slot # bc

    def __init__(self, *args, **kw):
        super(Banner, self).__init__(*args, **kw)
        self._mime_type = None
        self._size = None

    def __unicode__(self):
        return self.title or 'Banner %d' % self.id

    @property
    def destination_url(self):
        return self.destination or None

    @property
    def mime_type(self):
        if not self._mime_type:
            self._mime_type = mimetypes.guess_type(os.path.join(settings.MEDIA_ROOT, str(self.media_path)))
        return self._mime_type

    # TODO: these fields should be moved to special SWFImageField
    @property
    def is_flash(self):
        return self.mime_type[0] == 'video/x-flv'

    @property
    def is_image(self):
        return self.mime_type[0].startswith('image/')

    def save(self, force_insert=False, force_update=False):
        if not self.display_order:
            self.display_order = self.section.banner_set.all().count() + 1
        return super(Banner, self).save(force_insert, force_update)

    @property
    def size(self):
        if not self._size:
            filename = os.path.join(settings.MEDIA_ROOT, str(self.media_path))
            if self.is_image:
                self._size = Image.open(filename).size
            elif self.is_flash:
                self._size = utils.get_flv_size(filename)
        return self._size

