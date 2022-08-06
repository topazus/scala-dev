%global debug_package %{nil}

# Disable build-id symlinks to avoid conflicts
%global _build_id_links none
# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
# disable rpath checks
%define __brp_check_rpaths %{nil}

%global build_number 213.6461.79
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           intellij-idea-ultimate
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        An intelligent IDE for Java, Groovy and other programming languages
License:        custom
URL:            https://www.jetbrains.com/idea/
Source0:        https://download.jetbrains.com/idea/ideaIU-2022.2.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/intellij-idea-ultimate/intellij-idea-ultimate.desktop

BuildRequires:  pkg-config desktop-file-utils

%description
An intelligent IDE for Java, Groovy and other programming languages with advanced refactoring features intensely focused on developer productivity.

%prep
wget %{SOURCE1}
tar xf ideaIU-*.tar.gz
cd idea-IU-*/

# Replace python shebangs to make them compatible with fedora
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python|%{__python3}|g' \
                                    -i "{}" \;

find -type f -name "*.sh" -exec sed -e 's|/bin/sh|/usr/bin/sh|g' \
                                    -i "{}" \;

# Remove files for other CPU architectures
rm -rf lib/pty4j-native/linux/aarch64
rm -rf lib/pty4j-native/linux/arm
rm -rf lib/pty4j-native/linux/mips64el
rm -rf lib/pty4j-native/linux/ppc64le

# Remove files for other OS
rm -rf plugins/cwm-plugin/quiche-native/darwin-aarch64
rm -rf plugins/cwm-plugin/quiche-native/darwin-x86-64
rm -rf plugins/cwm-plugin/quiche-native/win32-x86-64

rm -rf plugins/maven/lib/maven3/lib/jansi-native/freebsd32
rm -rf plugins/maven/lib/maven3/lib/jansi-native/freebsd64
rm -rf plugins/maven/lib/maven3/lib/jansi-native/osx
rm -rf plugins/maven/lib/maven3/lib/jansi-native/windows32
rm -rf plugins/maven/lib/maven3/lib/jansi-native/windows64

rm -rf plugins/webp/lib/libwebp/win
rm -rf plugins/webp/lib/libwebp/mac

rm -rf **/*.dll
rm -rf **/*.dylib

# remove bundled jre
rm -rf jbr

%build

%install
cd idea-IU-*/
mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 bin/idea.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pDm644 bin/idea.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%dir /opt/%{name}
/opt/%{name}/*

%changelog
