from setuptools import setup

setup(
    name="rainbowtables",
    version="1.0.5",
    author="JustBen",
    author_email="justben009@gmail.com",
    description="A python library allowing the user to create a rainbowtable.",
    keywords="rainbowtable",
    python_requires=">=3.7",
    packages=["rainbowtables"],
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JustBennnn/rainbowtables",
    project_urls={
        "Issue Tracker": "https://github.com/JustBennnn/rainbowtables/issues",
    },
    install_requires=["sympy"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
