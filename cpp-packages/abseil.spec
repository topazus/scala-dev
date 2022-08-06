%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname abseil

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        3%{?dist}
Summary:        C++ Common Libraries

License:        ASL 2.0
URL:            https://abseil.io
#Source0:

BuildRequires:  cmake gcc-c++ git
# The default make backend would work just as well; ninja is observably faster
BuildRequires:  ninja-build

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

%prep
git clone --depth=1 https://github.com/abseil/abseil-cpp.git .

%build
%cmake \
  -GNinja \
  -DABSL_USE_EXTERNAL_GOOGLETEST:BOOL=ON \
  -DABSL_FIND_GOOGLETEST:BOOL=ON \
  -DABSL_ENABLE_INSTALL:BOOL=ON \
  -DBUILD_TESTING:BOOL=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_CXX_STANDARD:STRING=17
%cmake_build

%install
%cmake_install

%check


%files
/usr/include/absl/
/usr/lib64/cmake/absl/*.cmake
/usr/lib64/libabsl_*
/usr/lib64/pkgconfig/absl_*.pc

%changelog
