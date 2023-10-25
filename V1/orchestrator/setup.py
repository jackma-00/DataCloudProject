"""Package setup"""
from setuptools import setup, find_packages

setup(
    name="orchestrator-v1",
    version="0.1.0",
    author="Jacopo Maragna",
    description="DataCloud Project Orchestrator Component Pipeline Version 1",
    packages=find_packages(),
    install_requires=[
        "httpx==0.23.3",
    ],
    extras_require={
        "dev": [
            "black==23.1.0",
            "pylint==2.17.0",
            "pytest==7.3.1",
            "httpx==0.23.3",
            "uvicorn==0.22.0",
        ]
    },
)
