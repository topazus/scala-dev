%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname intel-oneapi-tbb


Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        3%{?dist}
Summary:        oneAPI Threading Building Blocks (oneTBB)

License:        ASL 2.0
URL:            https://oneapi-src.github.io/oneTBB/
#Source0:


BuildRequires:  cmake gcc-c++ git


%description
oneTBB is a flexible C++ library that simplifies the work of adding parallelism to complex applications, even if you are not a threading expert.



%prep
git clone https://github.com/oneapi-src/oneTBB.git .


%build
%cmake -DTBB_TEST=OFF \
  -DBUILD_TYPE=Release
%cmake_build


%install
%cmake_install

%check


%files
%license LICENSE.txt
%doc README.md
/usr/include/oneapi/tbb.h
/usr/include/oneapi/tbb/
/usr/include/tbb/*.h
/usr/lib64/cmake/TBB/*.cmake
/usr/lib64/libtbb*
/usr/lib64/pkgconfig/tbb.pc
/usr/share/doc/TBB/README.md

%changelog
