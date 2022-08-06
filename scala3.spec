%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname scala3

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A next-generation compiler for Scala
License:        ASL 2.0
URL:            https://github.com/lampepfl/dotty
#Source:

BuildRequires:  pkg-config java-17-openjdk
BuildRequires:  wget git

Requires:       java-17-openjdk

%description
A next-generation compiler for Scala

%prep
git clone --depth=1 https://github.com/lampepfl/dotty.git .

mkdir -p $HOME
wget https://github.com/sbt/sbt/releases/download/v1.6.1/sbt-1.6.1.tgz
tar xf sbt-*.tgz


%build
./sbt/bin/sbt dist/packArchive

%install
mkdir -p %{buildroot}/opt/scala
cd dist/target/pack/
cp -a * %{buildroot}/opt/scala

rm %{buildroot}/opt/scala/bin/*.bat

%post
if [ "$1" = 1 ]; then
  if [ ! -f /etc/environment ] ; then
    echo "export PATH=$PATH:/opt/scala/bin" > /etc/environment
  else
    grep -q "^export PATH=$PATH:/opt/scala/bin$" /etc/environment || echo "export PATH=$PATH:/opt/scala/bin" >> /etc/environment
    fi
fi

%postun
if [ "$1" = 0 ] && [ -f /etc/environment ] ; then
  sed -i '\!^export PATH=$PATH:/opt/scala/bin$!d' /etc/environment
fi

%check


%files
/opt/scala/

%changelog
