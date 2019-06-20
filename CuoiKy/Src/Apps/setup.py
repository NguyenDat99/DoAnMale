from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('App.pyx'))
setup(ext_modules=cythonize('../BUS/Multivariable_Regression.pyx'))
setup(ext_modules=cythonize('../DAO/DataProcessing.pyx'))
setup(ext_modules=cythonize('../DTO/DataAdapter.pyx'))
setup(ext_modules=cythonize('../BUS/Poly_Regression.pyx'))
setup(ext_modules=cythonize('../BUS/PCA.pyx'))
setup(ext_modules=cythonize('../BUS/KPCA.pyx'))
setup(ext_modules=cythonize('../BUS/LDA.pyx'))
#setup(ext_modules=cythonize('../BUS/Logistic Regression.pyx'))
