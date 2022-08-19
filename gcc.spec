%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname gcc

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        GNU Compiler Collection (GCC)
License:        GPL
URL:            http://gcc.gnu.org/
#Source:

BuildRequires: glibc-static
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, sharutils
BuildRequires: texinfo, texinfo-tex
BuildRequires: systemtap-sdt-devel
BuildRequires: gmp-devel mpfr-devel libmpc-devel
BuildRequires: python3-devel
BuildRequires: gcc, gcc-c++, make
BuildRequires:  git

%description
Powerful yet simple to use screenshot software.

%prep
#git clone --depth=1 https://github.com/gcc-mirror/gcc.git .
wget https://mirrorservice.org/sites/sourceware.org/pub/gcc/snapshots/13-20220807/gcc-13-20220807.tar.xz
tar xf gcc-*.tar.xz
cd gcc-*/

%build
cd gcc-*/
./configure \
	--enable-languages=c,c++,fortran \
	--prefix=%{buildroot}/opt/gcc-git \
	--enable-checking=release --with-system-zlib \
	--without-isl --disable-multilib
make -j4

%install
cd gcc-*/
make install

%check

%files
/opt/gcc-git/

%changelog
