#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : netifaces
Version  : 0.10.5
Release  : 28
URL      : https://bitbucket.org/al45tair/netifaces/get/release_0_10_5.tar.gz
Source0  : https://bitbucket.org/al45tair/netifaces/get/release_0_10_5.tar.gz
Summary  : Portable network interface information.
Group    : Development/Tools
License  : MIT
Requires: netifaces-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
netifaces 0.10.4
================
.. image:: https://drone.io/bitbucket.org/al45tair/netifaces/status.png
:target: https://drone.io/bitbucket.org/al45tair/netifaces/latest
:alt: Build Status

%package python
Summary: python components for the netifaces package.
Group: Default

%description python
python components for the netifaces package.


%prep
%setup -q -n al45tair-netifaces-dc7c8e888476

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487187406
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 test.py
%install
export SOURCE_DATE_EPOCH=1487187406
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
