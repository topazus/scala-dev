%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname ccls

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        C/C++/ObjC language server
License:        ASL 2.0
URL:            https://github.com/google/re2
#Source0:

BuildRequires:  cmake gcc-c++ llvm-devel git ninja-build



%description
C/C++/ObjC language server supporting cross references, hierarchies, completion and semantic highlighting

%prep
git clone --depth=1 --recursive https://github.com/MaskRay/ccls .

%build
%cmake -H. -G Ninja -DBUILD_TYPE=Release -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check


%files
/usr/bin/ccls

%changelog
