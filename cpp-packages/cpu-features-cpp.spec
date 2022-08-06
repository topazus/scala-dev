%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname cpu-features-cpp

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A cross platform C99 library to get cpu features at runtime.

License:        ASL 2.0
URL:            https://github.com/google/cpu_features
#Source0:

BuildRequires:  cmake gcc-c++ git

%description
A cross platform C99 library to get cpu features at runtime.

%prep
git clone --depth=1 https://github.com/google/cpu_features.git .


%build
%cmake -DBUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check


%files
/usr/bin/list_cpu_features

/usr/include/cpu_features/cpu_features_cache_info.h
/usr/include/cpu_features/cpu_features_macros.h
/usr/include/cpu_features/cpuinfo_x86.h
/usr/lib64/cmake/CpuFeatures/CpuFeaturesConfig.cmake
/usr/lib64/cmake/CpuFeatures/CpuFeaturesConfigVersion.cmake
/usr/lib64/cmake/CpuFeatures/CpuFeaturesTargets-release.cmake
/usr/lib64/cmake/CpuFeatures/CpuFeaturesTargets.cmake
/usr/lib64/libcpu_features.so

%changelog
