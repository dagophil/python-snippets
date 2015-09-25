from numpy.distutils.core import setup
from Cython.Build import cythonize
import sys

ext = cythonize("src/prime_lib.pyx",
                compiler_directives={"boundscheck": False,
                                     "wraparound": False,
                                     "nonecheck": False,
                                     "cdivision": True})

if not sys.platform.startswith("win"):
    ext[0].extra_compile_args = ["-O3 -std=c++11"]
    ext[0].extra_link_args = ["-O3"]

setup(
    name="prime_lib",
    packages=["prime_lib"],
    ext_modules=ext
)
