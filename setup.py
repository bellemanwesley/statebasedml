from setuptools import find_packages, setup
setup(
    name='statebasedml',
    packages=find_packages(include=['statebasedml']),
    version='0.0.1',
    author='Wesley Belleman',
    author_email="bellemanwesley@gmail.com",
    description="Machine learning package for state based ML.",
    url="https://github.com/bellemanwesley/statebasedml",
    license='MIT',
    install_requires=['random'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)