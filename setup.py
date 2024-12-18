from setuptools import setup, find_packages

setup(
    name="python-web-scraper",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "beautifulsoup4",
        "selenium",
        "scrapy",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
        ],
    },
    author="Fung Chung",
    author_email="chungtszfung2@gmail.com",
    description="Python web scraper for a client",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/varepsilon123/python-web-scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
        ],
    },
)
