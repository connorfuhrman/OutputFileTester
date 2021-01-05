import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uarizona-ece275-outputfileTester", # Replace with your own username
    version="0.0.1",
    author="Connor Fuhrman",
    author_email="connorfuhrman@email.arizona.edu",
    description="Packaage used to test and compare output files for ECE 275 @ the University of Arizona",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/connorfuhrman/OutputFileTester",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)