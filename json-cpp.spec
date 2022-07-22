%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname json-cpp


Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        3%{?dist}
Summary:        JSON for Modern C++

License:        ASL 2.0
URL:            https://json.nlohmann.me/
#Source0:


BuildRequires:  cmake gcc-c++ git


%description
JSON for Modern C++

%prep
git clone --depth=1 https://github.com/nlohmann/json.git .


%build
%cmake -DBUILD_TYPE=Release
%cmake_build


%install
%cmake_install

%check


%files
%license LICENSE.MIT
%doc README.md


%changelog
