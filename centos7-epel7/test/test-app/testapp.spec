Name:           testapp
Version:        0.1
Release:        1%{?dist}
Summary:        Example application to be deployed
License:        GPLv2+
URL:            https://github.com/sclorg/s2i-python-container
Source0:        testapp-0.1.tar.gz

BuildRequires:  python2-devel
Requires:       python-gunicorn

%description
%{summary}.

%prep
%setup -q

%build
%{py2_build}

%install
%{py2_install}

%files
%{python2_sitelib}/testapp.py*
%{python2_sitelib}/testapp*.egg-info

%changelog
