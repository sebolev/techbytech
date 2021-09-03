import os
from setuptools import setup
from distutils.util import convert_path


path_to_version_file = "version.py"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


main_ns = {}
version_path = convert_path(path_to_version_file)
with open(version_path) as ver_file:
    exec(ver_file.read(), main_ns)
setup(
    name="techbytech",

    description="Data project",

    version=main_ns['__version__'],

    author="Zouhir OUFTOU",

    long_description=read("README.md")
)
