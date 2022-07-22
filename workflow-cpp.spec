%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname workflow-cpp


Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        3%{?dist}
Summary:        C++ Parallel Computing and Asynchronous Networking Engine

License:        ASL 2.0
URL:            https://oneapi-src.github.io/oneTBB/
#Source0:


BuildRequires:  cmake openssl-devel gcc-c++ git

Requires:       openssl

%description
C++ Parallel Computing and Asynchronous Networking Engine

%prep
git clone --depth=1 https://github.com/sogou/workflow .


%build
%cmake -DBUILD_TYPE=Release
%cmake_build


%install
%cmake_install

%check


%files
%license LICENSE
%doc README.md
/usr/include/workflow/*.h
/usr/include/workflow/*.inl
/usr/lib64/cmake/workflow/workflow-config-version.cmake
/usr/lib64/cmake/workflow/workflow-config.cmake
/usr/lib64/libworkflow*
/usr/share/doc/workflow-0.10.3/README.md

%changelog
