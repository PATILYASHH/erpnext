from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="foundry_erp",
    version="1.0.0",
    author="Foundry ERP",
    author_email="support@foundryerp.com",
    description="Custom ERP extensions built on top of ERPNext",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PATILYASHH/foundry_erp",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.10",
    install_requires=[
        # Dependencies are managed in pyproject.toml [tool.bench.frappe-dependencies]
        # ERPNext is listed in hooks.py required_apps and installed via bench
    ],
)
