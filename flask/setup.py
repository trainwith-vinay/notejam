from setuptools import setup, find_packages
from os import path
try: # for pip >= 10
  from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
  from pip.req import parse_requirements

here = path.abspath(path.dirname(__file__))


PROJECT_URL = 'http://github.com/nordcloud/notejam'

DESCRIPTION = """
Notejam application implemented using Flask microframework for Nordcloud tech assignments.
"""

install_reqs = parse_requirements(
    path.join(here, 'requirements.txt'),
    session=False
)
install_reqs = list(install_reqs)
try:
    install_requirements = [str(ir.req) for ir in install_reqs]
except:
    install_requirements = [str(ir.requirement) for ir in install_reqs]

dev_reqs = parse_requirements(
    path.join(here, 'requirements.txt'),
    session=False
)
dev_reqs = list(dev_reqs)
try:
        development_requirements = [str(ir.req) for ir in dev_reqs]
except:
        development_requirements = [str(ir.requirement) for ir in dev_reqs]

setup(
    name='notejam',
    version='v1.0',
    description=DESCRIPTION,
    url=PROJECT_URL,
    download_url=PROJECT_URL + '/tarball/v' + "1.0",
    author='Greg Nagy',
    author_email='greg@nordcloud.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='notejam',
    packages=find_packages(),
    install_requires=install_requirements,
    extras_require={
        'dev': development_requirements
    },
)
