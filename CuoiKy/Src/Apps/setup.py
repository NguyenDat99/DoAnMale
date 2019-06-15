from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('App.pyx'))
setup(ext_modules=cythonize('../BUS/Multivariable_Regression.pyx'))
setup(ext_modules=cythonize('../DAO/DataProcessing.py'))
setup(ext_modules=cythonize('../DTO/DataAdapter.py'))
