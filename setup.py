import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="persian-datetime",
    version="0.11.3",
    author="Ali Shekari",
    author_email="alishekari1991@outlook.com",
    description="Persian (jalali) datetime کلاس کار با تاریخ فارسی",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alishekari/python-persian-datetime",
    packages=setuptools.find_packages(),
    install_requires=['djangorestframework'],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
