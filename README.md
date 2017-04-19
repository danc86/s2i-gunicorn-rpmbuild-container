s2i-gunicorn-rpmbuild-container
===============================

Derived from: https://github.com/sclorg/s2i-python-container

but with the following differences:

* EPEL is enabled
* expects the application source tree to include an RPM .spec file, which is 
  built and installed
* only supports gunicorn for running the web application (must set 
  ``APP_MODULE``)
