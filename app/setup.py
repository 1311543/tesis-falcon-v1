import api
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
from setuptools import setup, find_packages

long_description = "Api Tesis Falcon v1"
requirements = parse_requirements('requirements.txt', session=False)
install_requires = [str(r.req) for r in requirements]

setup(
    name             = 'api',
    description      = 'API Tesis Falcon v1',
    packages         = find_packages(),
    author           = 'Francis De La Cruz',
    author_email     = 'francis.delacruz [at] gmail.com',
    scripts          = ['bin/api'],
    install_requires = install_requires,
    version          = api.__version__,
    url              = 'https://github.com/1311543/tesis-falcon-v1.git',
    license          = "MIT",
    zip_safe         = False,
    keywords         = "api, falcon, rest",
    long_description = long_description,
    classifiers      = [
                        'Development Status :: 4 - Beta',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: MIT License',
                        'Topic :: Software Development :: Build Tools',
                        'Topic :: Software Development :: Libraries',
                        'Topic :: Software Development :: Testing',
                        'Topic :: Utilities',
                        'Operating System :: MacOS :: MacOS X',
                        'Operating System :: Microsoft :: Windows',
                        'Operating System :: POSIX',
                        'Programming Language :: Python :: 2.6',
                        'Programming Language :: Python :: 2.7',
                      ]
)
