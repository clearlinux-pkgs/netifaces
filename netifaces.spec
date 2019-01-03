#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : netifaces
Version  : 0.10.9
Release  : 50
URL      : https://files.pythonhosted.org/packages/0d/18/fd6e9c71a35b67a73160ec80a49da63d1eed2d2055054cc2995714949132/netifaces-0.10.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/0d/18/fd6e9c71a35b67a73160ec80a49da63d1eed2d2055054cc2995714949132/netifaces-0.10.9.tar.gz
Summary  : Portable network interface information.
Group    : Development/Tools
License  : MIT
Requires: netifaces-python = %{version}-%{release}
Requires: netifaces-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
netifaces 0.10.8
================
+-------------+------------------+
| Linux/macOS | |BuildStatus|    |
+-------------+------------------+
| Windows     | |WinBuildStatus| |
+-------------+------------------+

%package python
Summary: python components for the netifaces package.
Group: Default
Requires: netifaces-python3 = %{version}-%{release}

%description python
python components for the netifaces package.


%package python3
Summary: python3 components for the netifaces package.
Group: Default
Requires: python3-core

%description python3
python3 components for the netifaces package.


%prep
%setup -q -n netifaces-0.10.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546484901
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
