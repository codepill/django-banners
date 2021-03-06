import banners
from setuptools import setup, find_packages

install_requires = [
    'PIL>=1.1.7',
]
setup(
    name='django-banners',
    version=banners.__version__,
    description="Banner management app for Django (might be some CodePill's project dependent)",
    author='Marcin Nowak, Piotr Adamowicz',
    author_email='marcin.nowak@codepill.com, piotr.adamowicz@codepill.com',
    url='https://github.com/codepill/django-banners',
    install_requires = install_requires,
    packages=find_packages(),
    package_dir={'banners': 'banners'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    include_package_data=True,
)