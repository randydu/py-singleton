from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="py-singleton", 
    version="0.9.2",
    description = "singleton pattern for python 2 and 3",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/randydu/py-singleton.git",
    author="Randy Du",
    author_email="randydu@gmail.com",
    packages=["py_singleton"],
    keywords=["singleton"],
    license="MIT",
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers', 
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
  ],

)