"""Setup pyhiveapi package."""

import os
import re

import unasync

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def requirements_from_file(filename="requirements.txt"):
    """Get requirements from file."""
    with open(os.path.join(os.path.dirname(__file__), filename)) as r:
        reqs = r.read().strip().split("\n")
    # Return non empty lines and non comments
    return [r for r in reqs if re.match(r"^\w+", r)]


setup(
    version="0.3.6",
    package_data={"pyhiveapi.pyhiveapi": ["*.json"]},
    cmdclass={
        "build_py": unasync.cmdclass_build_py(
            rules=[
                unasync.Rule(
                    "/apyhiveapi/",
                    "/pyhiveapi/",
                    additional_replacements={
                        "HiveAsync": "Hive",
                        "HiveApiAsync": "HiveApi",
                    },
                )
            ]
        )
    },
    install_requires=requirements_from_file(),
    extras_require={"dev": requirements_from_file("requirements_test.txt")},
)
