from setuptools import setup

setup(name='wrfmpdiag',
      version='0.1',
      description='Load and process WRF microphysics diagnostics output',
      url='http://github.com/mheikenfeld/wrfmpdiag',
      author='Max Heikenfeld',
      author_email='max.heikenfeld@physics.ox.ac.uk',
      license='GNU',
      packages=['wrfmpdiag'],
      install_requires=['wrfcube'],
      zip_safe=False)
