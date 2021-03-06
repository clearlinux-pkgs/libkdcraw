#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkdcraw
Version  : 21.04.2
Release  : 30
URL      : https://download.kde.org/stable/release-service/21.04.2/src/libkdcraw-21.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.2/src/libkdcraw-21.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.2/src/libkdcraw-21.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: libkdcraw-data = %{version}-%{release}
Requires: libkdcraw-lib = %{version}-%{release}
Requires: libkdcraw-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : pkg-config
BuildRequires : pkgconfig(libraw)
BuildRequires : pkgconfig(libraw_r)

%description
LibRaw C++ interface for KDE
-- AUTHORS -----------------------------------------------------------

%package data
Summary: data components for the libkdcraw package.
Group: Data

%description data
data components for the libkdcraw package.


%package dev
Summary: dev components for the libkdcraw package.
Group: Development
Requires: libkdcraw-lib = %{version}-%{release}
Requires: libkdcraw-data = %{version}-%{release}
Provides: libkdcraw-devel = %{version}-%{release}
Requires: libkdcraw = %{version}-%{release}

%description dev
dev components for the libkdcraw package.


%package lib
Summary: lib components for the libkdcraw package.
Group: Libraries
Requires: libkdcraw-data = %{version}-%{release}
Requires: libkdcraw-license = %{version}-%{release}

%description lib
lib components for the libkdcraw package.


%package license
Summary: license components for the libkdcraw package.
Group: Default

%description license
license components for the libkdcraw package.


%prep
%setup -q -n libkdcraw-21.04.2
cd %{_builddir}/libkdcraw-21.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623363443
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623363443
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkdcraw
cp %{_builddir}/libkdcraw-21.04.2/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkdcraw/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/libkdcraw-21.04.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkdcraw/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/libkdcraw.categories

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
/usr/share/package-licenses/libkdcraw/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkdcraw/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
