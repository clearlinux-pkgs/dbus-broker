#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dbus-broker
Version  : 32
Release  : 22
URL      : https://github.com/bus1/dbus-broker/releases/download/v32/dbus-broker-32.tar.xz
Source0  : https://github.com/bus1/dbus-broker/releases/download/v32/dbus-broker-32.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: dbus-broker-bin = %{version}-%{release}
Requires: dbus-broker-filemap = %{version}-%{release}
Requires: dbus-broker-license = %{version}-%{release}
Requires: dbus-broker-services = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : expat-dev
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(systemd)
Patch1: use-private-network.patch

%description
# dbus-broker - Linux D-Bus Message Broker
The dbus-broker project is an implementation of a message bus as
defined by the D-Bus specification. Its aim is to provide high
performance and reliability, while keeping compatibility to the D-Bus
reference implementation. It is exclusively written for Linux systems,
and makes use of many modern features provided by recent linux kernel
releases.

%package bin
Summary: bin components for the dbus-broker package.
Group: Binaries
Requires: dbus-broker-license = %{version}-%{release}
Requires: dbus-broker-services = %{version}-%{release}
Requires: dbus-broker-filemap = %{version}-%{release}

%description bin
bin components for the dbus-broker package.


%package filemap
Summary: filemap components for the dbus-broker package.
Group: Default

%description filemap
filemap components for the dbus-broker package.


%package license
Summary: license components for the dbus-broker package.
Group: Default

%description license
license components for the dbus-broker package.


%package services
Summary: services components for the dbus-broker package.
Group: Systemd services

%description services
services components for the dbus-broker package.


%prep
%setup -q -n dbus-broker-32
cd %{_builddir}/dbus-broker-32
%patch1 -p1
pushd ..
cp -a dbus-broker-32 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659709356
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/dbus-broker
cp %{_builddir}/dbus-broker-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/dbus-broker/94c6ae483469d0109b64bb6ad7f33af3fa42435d
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/systemd/catalog/dbus-broker-launch.catalog
/usr/lib/systemd/catalog/dbus-broker.catalog

%files bin
%defattr(-,root,root,-)
/usr/bin/dbus-broker
/usr/bin/dbus-broker-launch
/usr/share/clear/optimized-elf/bin*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-dbus-broker

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dbus-broker/94c6ae483469d0109b64bb6ad7f33af3fa42435d

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/dbus-broker.service
/usr/lib/systemd/user/dbus-broker.service
