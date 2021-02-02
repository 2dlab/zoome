from setuptools import setup
from setuptools import find_packages


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='zoome',
    version='0.0.4',
    author='Gusarov Vladislav',
    author_email='tech@2dlab.ru',
    description='Python library for easy using Zoom-API-v2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/2dlab/zoome',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyJWT==2.0.0', 'requests'
    ]
)
