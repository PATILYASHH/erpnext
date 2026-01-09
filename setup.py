"""Setup script for Foundry ERP"""

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
	long_description = f.read()

setup(
	name="foundry_erp",
	version="1.0.0",
	description="Custom ERP extensions built on top of ERPNext",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="Foundry ERP",
	author_email="support@foundryerp.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[],
	python_requires=">=3.10",
)
