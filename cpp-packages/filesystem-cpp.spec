%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname filesystem-cpp

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        3%{?dist}
Summary:        An implementation of C++17 std::filesystem for C++11/C++14/C++17/C++20

License:        ASL 2.0
URL:            https://github.com/gulrak/filesystem
#Source0:

BuildRequires:  cmake gcc-c++ git

%description
An implementation of C++17 std::filesystem for C++11 /C++14/C++17/C++20 on Windows, macOS, Linux and FreeBSD.

%prep
git clone --depth=1 https://github.com/gulrak/filesystem.git .

%build
%cmake -DBUILD_TYPE=Release
%cmake_build -j2

%install
%cmake_install

%check


%files
/usr/include/ghc/filesystem.hpp
/usr/include/ghc/fs_fwd.hpp
/usr/include/ghc/fs_impl.hpp
/usr/include/ghc/fs_std.hpp
/usr/include/ghc/fs_std_fwd.hpp
/usr/include/ghc/fs_std_impl.hpp
/usr/lib64/cmake/ghc_filesystem/ghc_filesystem-config.cmake
/usr/lib64/cmake/ghc_filesystem/ghc_filesystem-targets.cmake

%changelog
