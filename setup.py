"""
Setup script for the Lens Reasoning SDK
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lens-reasoning-sdk",
    version="1.0.0",
    author="tupl",
    author_email="core@elitrotechnologies.com",
    description="Python SDK for the Lens Reasoning System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tupl-xyz/lens-sdk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "httpx>=0.25.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    keywords="reasoning, ai, lens, steering, contracts",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/lens-reasoning-sdk/issues",
        "Source": "https://github.com/yourusername/lens-reasoning-sdk",
    },
)