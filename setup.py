import setuptools

with open("README.md","r", encoding="utf-8")as f:
    long_descreption = f.read()


__version__ = "0.0.0"

REPO_NAME = "AI-Tex-Summraiser"
AUTHOR_NAME = "vandanvlog"
SRC_REPO = "ai_text_summariser"
AUTHOR_EAMIL = "vandanprajapati2276@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EAMIL,
    decription="A samll python package for Text Summarisation",
    long_descreption=long_descreption,
    long_descreption_context= "text/markdown ",
    url=f"hhtps://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_url={
        "AT Text Summraiser": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    package=setuptools.find_packages(where="src")
)