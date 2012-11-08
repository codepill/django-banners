from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
import hexagonit.swfheader
import Image
import mimetypes
import os


class Slot(models.Model):
    symbol = models.CharField(max_length=64)
    language = models.CharField(max_length=6, default='en', choices=settings.LANGUAGES)
    name = models.CharField(max_length=255)
    limit = models.PositiveIntegerField(null=True, blank=True)
    random = models.BooleanField(default=False)

    class Meta:
        unique_together = ('symbol', 'language',)

    def __unicode__(self):
        return 'Banner Slot "%s (%s)"' % (self.name, self.language)

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
    title = models.CharField(max_length=255, blank=True, null=True, help_text=_('This will be used as alt for images.'))
    slot = models.ForeignKey(Slot)
    # TODO: temporary using file field, but will be changed to special field handling SWF/Image
    banner_file = models.FileField(upload_to='uploads/banners/%y/%j/%H/%M%S/',
                                   help_text=_('This can be any image such as PNG, JPG, GIF.'))
    image_rollover = models.FileField(max_length=255,
                                      null=True, blank=True, upload_to=os.path.join('uploads', 'banners'),
                                      verbose_name=_('on hover image'),
                                      help_text=_('This image will be shown if mouse will hover the banner.'))
    is_published = models.BooleanField(default=False)
    destination_url = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Destination URL'), help_text=_('Clicking banner will get user to this URL.'))
    popup = models.BooleanField(default=False, help_text=_("Open banner's destination in new window/tab."))
    display_order = models.IntegerField(default=0)
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
        return self.banner_file # bc

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
    def mime_type(self):
        if not self._mime_type:
            self._mime_type = mimetypes.guess_type(os.path.join(settings.MEDIA_ROOT, str(self.media_path)))
        return self._mime_type

    # TODO: these fields should be moved to special SWFImageField
    @property
    def is_flash(self):
        return self.mime_type[0] == 'application/x-shockwave-flash'

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
                self._size = (hexagonit.swfheader.parse(filename)['width'],
                              hexagonit.swfheader.parse(filename)['height'])
        return self._size

