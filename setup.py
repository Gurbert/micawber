import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='micawber_bs4_classes',
    version='0.4.3',
    description='a small library for extracting rich content from urls',
    long_description=readme,
    author='Charles Leifer',
    author_email='coleifer@gmail.com',
    url='https://github.com/Gurbert/micawber_bs4_classes/',
    install_requires=['beautifulsoup4',],
    download_url = 'https://github.com/Gurbert/micawber_bs4_classes/archive/0.4.3.tar.gz',
    packages=[p for p in find_packages() if not p.startswith('examples')],
    package_data = {
        'micawber_bs4_classes': [
            'contrib/mcdjango/templates/micawber_bs4_classes/*.html',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Flask',
    ],
    test_suite='runtests.runtests',
)
