from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('knn.pyx'))
setup(ext_modules=cythonize('naiveBayes.pyx'))
setup(ext_modules=cythonize('svm.pyx'))
setup(ext_modules=cythonize('svmKernel.pyx'))
