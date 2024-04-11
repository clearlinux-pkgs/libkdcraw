#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v7
# autospec commit: f56f1fa
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : libkdcraw
Version  : 24.02.2
Release  : 74
URL      : https://download.kde.org/stable/release-service/24.02.2/src/libkdcraw-24.02.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.2/src/libkdcraw-24.02.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.2/src/libkdcraw-24.02.2.tar.xz.sig
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n libkdcraw-24.02.2
cd %{_builddir}/libkdcraw-24.02.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1712862625
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6 \
-DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6 \
-DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1712862625
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libkdcraw
cp %{_builddir}/libkdcraw-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/libkdcraw/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/libkdcraw-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/libkdcraw/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/libkdcraw.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KDcrawQt6/KDCRAW/DcrawInfoContainer
/usr/include/KDcrawQt6/KDCRAW/KDcraw
/usr/include/KDcrawQt6/KDCRAW/RawDecodingSettings
/usr/include/KDcrawQt6/KDCRAW/RawFiles
/usr/include/KDcrawQt6/kdcraw/dcrawinfocontainer.h
/usr/include/KDcrawQt6/kdcraw/kdcraw.h
/usr/include/KDcrawQt6/kdcraw/libkdcraw_export.h
/usr/include/KDcrawQt6/kdcraw/rawdecodingsettings.h
/usr/include/KDcrawQt6/kdcraw/rawfiles.h
/usr/include/KDcrawQt6/libkdcraw_version.h
/usr/lib64/cmake/KDcrawQt6/KDcrawQt6Config.cmake
/usr/lib64/cmake/KDcrawQt6/KDcrawQt6ConfigVersion.cmake
/usr/lib64/cmake/KDcrawQt6/KDcrawQt6Targets-relwithdebinfo.cmake
/usr/lib64/cmake/KDcrawQt6/KDcrawQt6Targets.cmake
/usr/lib64/libKDcrawQt6.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKDcrawQt6.so.5.0.0
/usr/lib64/libKDcrawQt6.so.5
/usr/lib64/libKDcrawQt6.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libkdcraw/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/libkdcraw/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
