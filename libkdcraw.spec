#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : libkdcraw
Version  : 19.04.1
Release  : 7
URL      : https://download.kde.org/stable/applications/19.04.1/src/libkdcraw-19.04.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.1/src/libkdcraw-19.04.1.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.1/src/libkdcraw-19.04.1.tar.xz.sig
Summary  : A C++ interface used to decode RAW picture
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.1
Requires: libkdcraw-lib = %{version}-%{release}
Requires: libkdcraw-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : pkg-config
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)

%description
LibRaw C++ interface for KDE
-- AUTHORS -----------------------------------------------------------

%package dev
Summary: dev components for the libkdcraw package.
Group: Development
Requires: libkdcraw-lib = %{version}-%{release}
Provides: libkdcraw-devel = %{version}-%{release}
Requires: libkdcraw = %{version}-%{release}
Requires: libkdcraw = %{version}-%{release}

%description dev
dev components for the libkdcraw package.


%package lib
Summary: lib components for the libkdcraw package.
Group: Libraries
Requires: libkdcraw-license = %{version}-%{release}

%description lib
lib components for the libkdcraw package.


%package license
Summary: license components for the libkdcraw package.
Group: Default

%description license
license components for the libkdcraw package.


%prep
%setup -q -n libkdcraw-19.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557457943
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557457943
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkdcraw
cp COPYING %{buildroot}/usr/share/package-licenses/libkdcraw/COPYING
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/libkdcraw/COPYING-CMAKE-SCRIPTS
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/libkdcraw/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KDCRAW/KDCRAW/DcrawInfoContainer
/usr/include/KF5/KDCRAW/KDCRAW/KDcraw
/usr/include/KF5/KDCRAW/KDCRAW/RawDecodingSettings
/usr/include/KF5/KDCRAW/KDCRAW/RawFiles
/usr/include/KF5/KDCRAW/kdcraw/dcrawinfocontainer.h
/usr/include/KF5/KDCRAW/kdcraw/kdcraw.h
/usr/include/KF5/KDCRAW/kdcraw/libkdcraw_export.h
/usr/include/KF5/KDCRAW/kdcraw/rawdecodingsettings.h
/usr/include/KF5/KDCRAW/kdcraw/rawfiles.h
/usr/include/KF5/libkdcraw_version.h
/usr/lib64/cmake/KF5KDcraw/KF5KDcrawConfig.cmake
/usr/lib64/cmake/KF5KDcraw/KF5KDcrawConfigVersion.cmake
/usr/lib64/cmake/KF5KDcraw/KF5KDcrawTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KDcraw/KF5KDcrawTargets.cmake
/usr/lib64/libKF5KDcraw.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5KDcraw.so.5
/usr/lib64/libKF5KDcraw.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkdcraw/COPYING
/usr/share/package-licenses/libkdcraw/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/libkdcraw/COPYING.LIB
