from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='django_masterpass',
    version='0.0.3',
    description='Django master password',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    keywords='django master password authentication authentication_backends',
    url='https://github.com/ulkoart/django-masterpass',
    author='Artem Ulko',
    author_email='ulkoart@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
    include_package_data=True
)
