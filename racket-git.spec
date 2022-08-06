%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname racket

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        7%{?dist}
Summary:        General purpose programming language

License:        GPLv3 and LGPLv3 and MIT
URL:            https://racket-lang.org
#Source0:

BuildRequires:  make gcc racket tar git

# Racket heavily utilizes the system ffi library.
BuildRequires:  libffi-devel

# For the racket/gui library (via libffi)
BuildRequires:  gtk3

# For the racket/draw library (via libffi)
BuildRequires: cairo
BuildRequires: pango
BuildRequires: libpng
BuildRequires: libjpeg-turbo

%description
Racket is a general-purpose programming language and an ecosystem for language-oriented programming.

%prep
git clone --depth=1 https://github.com/racket/racket.git .

%build
%make_build


%install

# bash racket-8.5-x86_64-linux-cs.sh --unix-style=yes --dest %{buildroot}/usr

%files
cp racket/bin/* %{buildroot}/usr/bin
cp -r racket/collects %{buildroot}/usr/share/racket/
cp -r racket/lib/* %{buildroot}/usr/lib/racket
cp -r racket/doc/* %{buildroot}/usr/share/doc/racket
install -pDm644 etc/config.rktd %{buildroot}/etc/config.rktd
cp racket/man/man1/*.1 %{buildroot}/usr/share/man/man1
cp share/applications/*.desktop %{buildroot}/usr/share/applications
sed -i 's+.png++' %{buildroot}/usr/share/applications/{drracket,slideshow}.desktop

%changelog
