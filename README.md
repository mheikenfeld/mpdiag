# mpdiag
This package provides rotines for postprocessing microphysical process diagnostics from cloud-resolving model simulations.
Currently it includes code to use output from adapted versions of the Thompson and Morrison microphysics schemes in WRF and the standard microphysics scheme in RAMS.

Installation
------------
Required packages:  numpy iris wrfcube ramscube

You can directly install the package directly from github with pip and either of the two following commands:
```
pip install --upgrade git+ssh://git@github.com/mheikenfeld/mpdiag.git
pip install --upgrade git+https://github.com/mheikenfeld/mpdiag.git
```

You can also clone the package with any of the two following commands
```
git clone git@github.com:mheikenfeldmheikenfeld/mpdiag.git
git clone https://github.com/mheikenfeld/mheikenfeld/mpdiag.git
```
and install the package from the locally cloned version:
```
pip install mpdiag/
```
