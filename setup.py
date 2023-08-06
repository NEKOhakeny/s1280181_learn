import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='s1280181_learn',
    author='NEKOhakeny',
    author_email='s1280181@u-aizu.ac.jp',
    packages=setuptools.find_packages(),
    url='https://github.com/NEKOhakeny/s1280181_learn.git',
    license='MIT',
    install_requires=[            # All necessary packages utilized by our PAMI software
        'psutil',
        'pandas',
        'plotly',
        'matplotlib',
        'resource',
        'validators',
        'urllib3',
        'Pillow',
        'numpy',
        'PAMI'
    ],
    include_package_data=True,
    extras_require={
        'gpu':  ['cupy', 'pycuda'],
        'spark': ['pyspark'],
        'dev': ['twine', 'setuptools', 'build'],
        'all': ['cupy', 'pycuda', 'pyspark', 'twine', 'setuptools', 'build']
    },
    python_requires='>=3.5',
)