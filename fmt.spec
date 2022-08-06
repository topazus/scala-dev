%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname fmt

Name:           %{appname}-git
Version:        %{build_timestamp}

Release:        1%{?dist}
Summary:        A modern formatting library
License:        Apache License 2.0
URL:            https://fmt.dev/
#Source0:

BuildRequires:  gcc-c++
BuildRequires:  unzip zip
BuildRequires:  cmake ninja-build

BuildRequires:  git

%description
A modern formatting library

%prep
git clone --depth=1 https://github.com/fmtlib/fmt.git .

%build
%cmake -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_SHARED_LIBS=ON

%cmake_build

%install
%cmake_install

%files
/usr/include/fmt/*.h
/usr/lib64/cmake/fmt/fmt-config-version.cmake
/usr/lib64/cmake/fmt/fmt-config.cmake
/usr/lib64/cmake/fmt/fmt-targets-release.cmake
/usr/lib64/cmake/fmt/fmt-targets.cmake
/usr/lib64/libfmt.so*
/usr/lib64/pkgconfig/fmt.pc



%changelog
