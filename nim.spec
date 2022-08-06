%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname nim

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A statically typed compiled systems programming language
License:        MIT
URL:            https://nim-lang.org/
#Source:

BuildRequires:  gcc make git

Requires:       pcre openssl

%description
Nim is a statically typed compiled systems programming language. It combines successful concepts from mature languages like Python, Ada and Modula. Its design focuses on efficiency, expressiveness, and elegance (in that order of priority).

%prep
git clone --depth=1 https://github.com/nim-lang/Nim.git .


%build
bash build_all.sh
bin/nim c -d:release koch
./koch boot -d:release
./koch tools


%install
install -Dpm 0755 bin/* -t %{buildroot}/usr/bin
# remove invalid files
rm %{buildroot}/usr/bin/empty.txt %{buildroot}/usr/bin/*.bat

mkdir -p %{buildroot}%{_prefix}/lib/nim %{buildroot}%{_includedir}

cp -a lib compiler %{buildroot}%{_prefix}/lib/nim

install -Dpm 0644 config/* -t %{buildroot}%{_sysconfdir}/nim

# completions
install -Dpm 0644 tools/nim.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/nim
install -Dpm 0644 tools/nim.zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_nim

install -Dpm 0644 dist/nimble/nimble.bash-completion %{buildroot}%{_datadir}/bash-completion/completions/nimble
install -Dpm 0644 dist/nimble/nimble.zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_nimble

%check

%files
/usr/bin/nim*
/usr/bin/atlas
%{_bindir}/testament

%{_prefix}/lib/nim/*

%dir %{_sysconfdir}/nim
%{_sysconfdir}/nim/config.nims
%{_sysconfdir}/nim/*.cfg
/etc/nim/build_config.txt

%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_*


%changelog
