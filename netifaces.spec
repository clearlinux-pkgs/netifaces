#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : netifaces
Version  : 0.10.5
Release  : 32
URL      : https://bitbucket.org/al45tair/netifaces/get/release_0_10_5.tar.gz
Source0  : https://bitbucket.org/al45tair/netifaces/get/release_0_10_5.tar.gz
Summary  : Portable network interface information.
Group    : Development/Tools
License  : MIT
Requires: netifaces-legacypython
Requires: netifaces-python3
Requires: netifaces-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
get access to a list of the network interfaces on the local machine, and to
        obtain the addresses of those network interfaces.
        
        The package has been tested on Mac OS X, Windows XP, Windows Vista, Linux
        and Solaris.  On Windows, it is currently not able to retrieve IPv6
        addresses, owing to shortcomings of the Windows API.
        
        It should work on other UNIX-like systems provided they implement
        either getifaddrs() or support the SIOCGIFxxx socket options, although the
        data provided by the socket options is normally less complete.

%package legacypython
Summary: legacypython components for the netifaces package.
Group: Default

%description legacypython
legacypython components for the netifaces package.


%package python
Summary: python components for the netifaces package.
Group: Default
Requires: netifaces-legacypython
Requires: netifaces-python3

%description python
python components for the netifaces package.


%package python3
Summary: python3 components for the netifaces package.
Group: Default

%description python3
python3 components for the netifaces package.


%prep
%setup -q -n al45tair-netifaces-dc7c8e888476

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506872096
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 test.py
%install
export SOURCE_DATE_EPOCH=1506872096
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
