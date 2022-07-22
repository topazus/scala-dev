%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname racket


Name:           %{appname}-snapshot
Version:        %{build_timestamp}
Release:        7%{?dist}
Summary:        General purpose programming language

License:        GPLv3 and LGPLv3 and MIT
URL:            https://racket-lang.org
#Source0:


BuildRequires:  make gcc racket tar


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
#git clone --depth=1 https://github.com/racket/racket.git .

#wget https://plt.cs.northwestern.edu/snapshots/current/installers/racket-test-current-src.tgz
#tar -xf racket-test-current-src.tgz && rm racket-test-current-src.tgz

wget https://download.racket-lang.org/installers/8.5/racket-8.5-src.tgz
tar -xf racket-*.tgz


%build
cd racket-*/src
%configure \
  --enable-pthread \
  --enable-shared \
  --enable-libffi \
  --disable-strip
%make_build


%install
cd racket-*/src
%make_install



%files
%license src/COPYING.txt



%changelog
