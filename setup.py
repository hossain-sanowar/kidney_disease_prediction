import setuptools

#read readme.md and print
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0" #initial version of project

REPO_NAME = "Kidney_Disease_Classification_Deep_Learning_Project" #Github Repository name or project name 
AUTHOR_USER_NAME = "hossain-sanowar"  #Github author name or Project author name
SRC_REPO = "cnnClassifier" #project name
AUTHOR_EMAIL = "md.sanowar21@gmail.com"

#define for local packages as well as for github
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)