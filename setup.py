from setuptools import setup

setup(name='mpdiag',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='Load and process WRF and RAMS microphysics diagnostics output',
      url='http://github.com/mheikenfeld/mpdiag',
      author='Max Heikenfeld',
      author_email='max.heikenfeld@web.de',
      license='BSD-3-Clause',
      packages=['mpdiag'],
      install_requires=['wrfcube','ramscube'],
      zip_safe=False)
