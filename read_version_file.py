""" Read the version of the package.

At the time this package has been created, the "file:" directive does not work
in setup.cfg for "version".

Change:

version = attr: version.version

for:

version = file: requests_splash.VERSION

and delete this file if it works with newer version of setuptools.
"""
import pathlib

package = pathlib.Path(__file__).parent / 'requests_splash'
version_file = package / 'VERSION'
version = version_file.read_text().strip()
