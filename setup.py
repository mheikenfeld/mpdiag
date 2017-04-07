from setuptools import setup

setup(name='wrf-mp-diag',
      version='0.1',
      description='Load and process WRF microphysics diagnostics output',
      url='http://github.com/mheikenfeld/wrf-mp-diag',
      author='Max Heikenfeld',
      author_email='max.heikenfeld@physics.ox.ac.uk',
      license='GNU',
      packages=['wrfcube'],
      install_requires=['wrfcube'],
      zip_safe=False)
