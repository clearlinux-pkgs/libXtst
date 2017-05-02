#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x687393EE37D128F8 (matthieu@herrb.eu)
#
Name     : libXtst
Version  : 1.2.3
Release  : 15
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXtst-1.2.3.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXtst-1.2.3.tar.bz2
Source99 : http://xorg.freedesktop.org/releases/individual/lib/libXtst-1.2.3.tar.bz2.sig
Summary  : The Xtst Library
Group    : Development/Tools
License  : HPND MIT
Requires: libXtst-lib
Requires: libXtst-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32inputproto)
BuildRequires : pkgconfig(32recordproto)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xi)
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(recordproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : xmlto

%description
libXtst provides the Xlib-based client API for the XTEST & RECORD extensions.
The XTEST extension is a minimal set of client and server extensions
required to completely test the X11 server with no user intervention.
This extension is not intended to support general journaling and
playback of user actions.

%package dev
Summary: dev components for the libXtst package.
Group: Development
Requires: libXtst-lib
Provides: libXtst-devel

%description dev
dev components for the libXtst package.


%package dev32
Summary: dev32 components for the libXtst package.
Group: Default
Requires: libXtst-lib32
Requires: libXtst-dev

%description dev32
dev32 components for the libXtst package.


%package doc
Summary: doc components for the libXtst package.
Group: Documentation

%description doc
doc components for the libXtst package.


%package lib
Summary: lib components for the libXtst package.
Group: Libraries

%description lib
lib components for the libXtst package.


%package lib32
Summary: lib32 components for the libXtst package.
Group: Default

%description lib32
lib32 components for the libXtst package.


%prep
%setup -q -n libXtst-1.2.3
pushd ..
cp -a libXtst-1.2.3 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491879776
export CFLAGS="$CFLAGS -Os -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491879776
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/XTest.h
/usr/include/X11/extensions/record.h
/usr/lib64/libXtst.so
/usr/lib64/pkgconfig/xtst.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXtst.so
/usr/lib32/pkgconfig/32xtst.pc
/usr/lib32/pkgconfig/xtst.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libXtst/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXtst.so.6
/usr/lib64/libXtst.so.6.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXtst.so.6
/usr/lib32/libXtst.so.6.1.0
