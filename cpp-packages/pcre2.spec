%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname pcre2

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        a regular expression library for c++

License:        ASL 2.0
URL:            https://github.com/google/re2
#Source0:

BuildRequires:  cmake gcc-c++ git

%description
a regular expression library for c++

%prep
git clone --depth=1 https://github.com/PCRE2Project/pcre2.git .

%build
%cmake -DBUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check


%files


%changelog
