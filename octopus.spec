%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname octopus

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        a regular expression library for c++

License:        ASL 2.0
URL:            https://github.com/google/re2
#Source0:

BuildRequires:  make gcc-c++ perl gcc-fortran git wget
BuildRequires:  libxc-devel blas-devel fftw-devel lapack-devel gsl-devel

%description
a regular expression library for c++

%prep
wget https://octopus-code.org/download/11.4/octopus-11.4.tar.gz

tar xf octopus-*.tar.gz && rm octopus-*.tar.gz


%build
cd octopus-*
export CXXFLAGS=-std=c++17
%configure
%make_build

%install
cd octopus-*
%make_install

%check


%files


%changelog
