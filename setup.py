from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        lines = (line.strip() for line in file)
        return [line for line in lines if line and not line.startswith('#')]

requirements = parse_requirements('requirements.txt')

setup(
    name="markingpal",
    version="0.1",
    description="AI agent for helping with constructive student feedback.",
    author="Marijan Beg",
    author_email="m.beg@imperial.ac.uk",
    url="https://github.com/marijanbeg/markingpal",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
)

