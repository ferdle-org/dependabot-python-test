import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coreka-db",
    version="0.0.1",
    license='no license',
    description="Provide exclusively for coreka-db project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/macromill-mint/coreka-db.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=[
        "coreka",
        "*.migrations",
        "coreka_db.coreka_models.management*"
    ]),
    python_requires=">=3.10",
)
