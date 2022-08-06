%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname clash

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A rule-based tunnel in Go
License:        GPL
URL:            https://github.com/Dreamacro/clash
#Source:

BuildRequires:  golang gcc
BuildRequires:  wget git

%description
A rule-based tunnel in Go.

%prep
git clone --depth=1 https://github.com/Dreamacro/clash.git .

%build
go build

%install
install -pDm755 clash %{buildroot}%{_bindir}/clash

%check


%files
/usr/bin/clash

%changelog
