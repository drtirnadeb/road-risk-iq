from setuptools import setup, find_packages

setup(
    name='accidents',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'scikit-learn'
    ],
    author='Your Name',
    description='A reusable module for risk analysis of US accidents data',
    python_requires='>=3.7'
)
