from setuptools import setup, find_packages

setup(
    name='django_masterpass',
    version='0.0.1',
    description='Django master password',
    long_description='Universal password for djangpo.',
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
