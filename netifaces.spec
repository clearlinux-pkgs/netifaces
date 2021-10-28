#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : netifaces
Version  : 0.11.0
Release  : 68
URL      : https://files.pythonhosted.org/packages/a6/91/86a6eac449ddfae239e93ffc1918cf33fd9bab35c04d1e963b311e347a73/netifaces-0.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a6/91/86a6eac449ddfae239e93ffc1918cf33fd9bab35c04d1e963b311e347a73/netifaces-0.11.0.tar.gz
Summary  : Portable network interface information.
Group    : Development/Tools
License  : MIT
Requires: netifaces-license = %{version}-%{release}
Requires: netifaces-python = %{version}-%{release}
Requires: netifaces-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
================
        
        +-------------+------------------+
        | Linux/macOS | |BuildStatus|    |
        +-------------+------------------+
        | Windows     | |WinBuildStatus| |
        +-------------+------------------+

%package license
Summary: license components for the netifaces package.
Group: Default

%description license
license components for the netifaces package.


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
Provides: pypi(netifaces)

%description python3
python3 components for the netifaces package.


%prep
%setup -q -n netifaces-0.11.0
cd %{_builddir}/netifaces-0.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622560557
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
#PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 test.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/netifaces
cp %{_builddir}/netifaces-0.11.0/LICENSE %{buildroot}/usr/share/package-licenses/netifaces/d2974c6505102e9199d25bd4c993bfcceafbdf2e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/netifaces/d2974c6505102e9199d25bd4c993bfcceafbdf2e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
