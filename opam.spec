%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname opam

%global bootstrap 0

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A source-based package manager
License:        LGPL
URL:            https://opam.ocaml.org/
#Source:

BuildRequires:  gcc gcc-c++ make git openssl
%if %bootstrap
BuildRequires:  ocaml ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc

BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-opam-file-format-devel
BuildRequires:  ocaml-base64-devel
BuildRequires:  ocaml-dose3-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-mccs-devel
BuildRequires:  ocaml-z3-devel
%endif

BuildRequires:  zlib-devel glpk-devel

Requires:       bubblewrap m4 patch

%description
Opam is a source-based package manager for OCaml. It supports multiple simultaneous compiler installations, flexible package constraints, and a Git-friendly development workflow.

%prep
git clone --depth=1 https://github.com/ocaml/opam.git .

%build
%if %bootstrap
make cold CONFIGURE_ARGS="--prefix %{buildroot}/usr"
%else
%configure
make
%endif

%install
%if %bootstrap
make cold-install
%else
%make_install
%endif

%check

%files
/usr/bin/opam
/usr/bin/opam-installer
/usr/share/man/man1/*.1.gz

%changelog
