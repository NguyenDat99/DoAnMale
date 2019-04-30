from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('main.pyx'))
setup(ext_modules=cythonize('../BUS/Hc.pyx'))
setup(ext_modules=cythonize('../BUS/KMeans.pyx'))
setup(ext_modules=cythonize('../DAO/dataProcessing.pyx'))
setup(ext_modules=cythonize('../DTO/DataAdapter.pyx'))
