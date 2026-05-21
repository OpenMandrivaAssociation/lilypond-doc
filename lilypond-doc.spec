%global		_build_pkgcheck_set /bin/true
%global		_build_pkgcheck_srpm /bin/true
%global		_nonzero_exit_pkgcheck_terminate_build 0

%define		oname lilypond

Summary:	HTML documentation for LilyPond
Name:	lilypond-doc
Version:		2.26.0
Release:		1
License:		GPLv3+
Group:		Publishing
Url:		https://www.lilypond.org
Source0:	https://gitlab.com/lilypond/lilypond/-/releases/v%{version}/downloads/%{oname}-%{version}-documentation.tar.xz
#BuildRequires:		wget
#BuildRequires:		bzip2
BuildRequires:		xz
BuildArch:      noarch
Provides:	%{oname}-manual = %{version}

%description
LilyPond is an automated music engraving system. It formats music beautifully
and automatically, and has a friendly syntax for its input files.
This package contains the HTML documentation for LilyPond.

%files
%{_docdir}/%{oname}/*

#-----------------------------------------------------------------------------

%prep
#cp -R %%{SOURCE0} . && chmod +x get-doc && ./get-doc
%autosetup -p1 -n share


%build
# Nothing to do: only docs


%install
# Install only manuals... not interested in regression tests docs
mkdir -p %{buildroot}%{_docdir}/%{oname}
pwd
cp -a doc/%{oname}/html/Documentation/* %{buildroot}%{_docdir}/%{oname}/
cp doc/%{oname}/html/index.html %{buildroot}%{_docdir}/%{oname}/
cp doc/%{oname}/html/README.md %{buildroot}%{_docdir}/%{oname}/




