#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x687393EE37D128F8 (matthieu@herrb.eu)
#
Name     : libXtst
Version  : 1.2.3
Release  : 19
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXtst-1.2.3.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXtst-1.2.3.tar.bz2
Source1 : http://xorg.freedesktop.org/releases/individual/lib/libXtst-1.2.3.tar.bz2.sig
Summary  : The Xtst Library
Group    : Development/Tools
License  : HPND MIT
Requires: libXtst-lib = %{version}-%{release}
Requires: libXtst-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkg-config
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
Requires: libXtst-lib = %{version}-%{release}
Provides: libXtst-devel = %{version}-%{release}
Requires: libXtst = %{version}-%{release}

%description dev
dev components for the libXtst package.


%package dev32
Summary: dev32 components for the libXtst package.
Group: Default
Requires: libXtst-lib32 = %{version}-%{release}
Requires: libXtst-dev = %{version}-%{release}

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
Requires: libXtst-license = %{version}-%{release}

%description lib
lib components for the libXtst package.


%package lib32
Summary: lib32 components for the libXtst package.
Group: Default
Requires: libXtst-license = %{version}-%{release}

%description lib32
lib32 components for the libXtst package.


%package license
Summary: license components for the libXtst package.
Group: Default

%description license
license components for the libXtst package.


%prep
%setup -q -n libXtst-1.2.3
pushd ..
cp -a libXtst-1.2.3 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568868959
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1568868959
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libXtst
cp COPYING %{buildroot}/usr/share/package-licenses/libXtst/COPYING
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
/usr/share/man/man3/XTestCompareCurrentCursorWithWindow.3
/usr/share/man/man3/XTestCompareCursorWithWindow.3
/usr/share/man/man3/XTestDiscard.3
/usr/share/man/man3/XTestFakeButtonEvent.3
/usr/share/man/man3/XTestFakeKeyEvent.3
/usr/share/man/man3/XTestFakeMotionEvent.3
/usr/share/man/man3/XTestFakeRelativeMotionEvent.3
/usr/share/man/man3/XTestGrabControl.3
/usr/share/man/man3/XTestQueryExtension.3
/usr/share/man/man3/XTestSetGContextOfGC.3
/usr/share/man/man3/XTestSetVisualIDOfVisual.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXtst.so
/usr/lib32/pkgconfig/32xtst.pc
/usr/lib32/pkgconfig/xtst.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libXtst/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXtst.so.6
/usr/lib64/libXtst.so.6.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXtst.so.6
/usr/lib32/libXtst.so.6.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libXtst/COPYING
