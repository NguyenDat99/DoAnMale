from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('main.pyx'))
setup(ext_modules=cythonize('../BUS/knn.pyx'))
setup(ext_modules=cythonize('../BUS/naiveBayes.pyx'))
setup(ext_modules=cythonize('../BUS/svm.pyx'))
setup(ext_modules=cythonize('../BUS/svmKernel.pyx'))
setup(ext_modules=cythonize('../DAO/dataProcessing.pyx'))
setup(ext_modules=cythonize('../DTO/DataAdapter.pyx'))