from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="zotero2wordcloud",
    version="0.0.1",
    author="Roberto A. Gulli",
    author_email="robertoagulli@gmail.com",
    description="A package to create a word cloud from a specified field of papers in a Zotero collection.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/rgulli/zotero2wordcloud/",
    packages=find_packages(),
    install_requires=['wordcloud'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
