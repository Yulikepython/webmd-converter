from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="webmd-converter",
    version="1.0.0",
    author="Hiroshi Nishito",
    author_email="author_email@example.com",
    description="Webページを簡単にMarkdownファイルに変換するツール",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yulikepython/webmd-converter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "html2text>=2020.1.16",
    ],
    entry_points={
        'console_scripts': [
            'webmd-converter=webmd_converter:main',
        ],
    },
)