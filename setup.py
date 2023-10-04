from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erp_consignment/__init__.py
from erp_consignment import __version__ as version

setup(
	name="erp_consignment",
	version=version,
	description="ERP Consignment",
	author="Midocean ",
	author_email="midocean@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
