from setuptools import setup

setup(
    name='py_ratelimit',
    version='0.1.0',
    description='',
    url='',
    author='Conor Bergman',
    author_email='conorbergman@gmail.com',
    license='',
    packages=['py_ratelimit'],
    install_requires=[
        'djangorestframework>=3.12.4',
        'redis>=3.4.1',
        # TESTING
        'fakeredis',
        'pytest>=6.2.5',
        'requests-mock>=1.8.0',
    ],
    classifiers=[

    ],
)
