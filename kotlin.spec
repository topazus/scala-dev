%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname kotlin

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A modern programming language that makes developers happier
License:        APACHE-2.0
URL:            https://github.com/JetBrains/kotlin
#Source:

BuildRequires:  java-11-openjdk-devel ncurses-compat-libs git

Requires:  java-11-openjdk


%description
A modern programming language that makes developers happier.

%prep
git clone --depth=1 --branch=master https://github.com/JetBrains/kotlin.git .

%build
JAVA_HOME=/usr/lib/jvm/java-11-openjdk \
./gradlew :kotlin-native:dist

%install


%check


%files


%changelog
