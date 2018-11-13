from setuptools import setup

setup(name='mpdiag',
      version='0.8',
      description='Load and process WRF and RAMS microphysics diagnostics output',
      url='http://github.com/mheikenfeld/mpdiag',
      author='Max Heikenfeld',
      author_email='max.heikenfeld@physics.ox.ac.uk',
      license='GNU',
      packages=['mpdiag'],
      install_requires=['wrfcube','ramscubE'],
      zip_safe=False)
