import setuptools


with open('README.md','r') as fh:
    long_description = fh.read()
    
    
    
setuptools.setup(
    name = 'pami',
    version = '2023.07.25',
    author = 'Rage Uday Kiran',
    author_email = 'uday.rage@gmail.com',
    description=long_description,
    long_description_content_type='text/markdown',
    package=setuptools.find_packages(),
    url = 'https://github.com/udayLab/PAMI',
    license = 'GPLv3',
    install_requires=[
        'psutil',
        'pandas',
        'plotly',
        'matplotlib',
        'resource',
        'validators',
        'urllib3',
        'Pillow',
        'numpy',
    ],
    extras_require={
        'gpu': ['copy', 'pycuda'],
        'spark': ['pyspark'],
        'dev': ['twine', 'setuptools', 'build'],
        'all': ['cupy', 'pycuda', 'pyspark', 'twine', 'setuptools', 'build'],
    },
    classfiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3(GPLv3)',
        'Operating System :: OS Independent',
        
    ],
    python_requires='>=3.5',
    
)