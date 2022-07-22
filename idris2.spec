%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname idris2

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        a purely functional programming language with first class types.
License:        custom
URL:            https://idris-lang.org/
#Source:

BuildRequires:  gcc make racket
BuildRequires:  git


%description
Idris 2 is a purely functional programming language with first class types.

%prep
git clone --depth=1 https://github.com/idris-lang/Idris2.git .


%build
make bootstrap-racket -j4


%install
mkdir -p %{buildroot}%{_libdir}
make install DESTDIR=%{buildroot} PREFIX=%{buildroot}%{_libdir}

mkdir -p %{buildroot}%{_bindir}
ln -s %{buildroot}%{_libdir}/bin/idris2 %{buildroot}%{_bindir}/idris2

#mv %{buildroot}%{_libdir}/bin/idris2 %{buildroot}%{_bindir}

#mv %{buildroot}%{_libdir}/lib/libidris2_support.so %{buildroot}%{_libdir}
#rm %{buildroot}%{_libdir}/idris2-*/lib/libidris2_support.so


%check

%files
%license LICENSE
%doc README.md
/usr/bin/idris2
/usr/lib64/bin/idris2
/usr/lib64/bin/idris2_app/idris2*
/usr/lib64/bin/idris2_app/libidris2_support.so
/usr/lib64/idris2-0.5.1/lib/libidris2_support.a
/usr/lib64/idris2-0.5.1/lib/libidris2_support.so
/usr/lib64/lib/libidris2_support.so

/usr/lib64/idris2-0.5.1/support/


%changelog
