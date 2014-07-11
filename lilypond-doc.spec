%define _build_pkgcheck_set /bin/true
%define _build_pkgcheck_srpm /bin/true
%define _nonzero_exit_pkgcheck_terminate_build 0
%define oname lilypond

Name:           lilypond-doc
Version:        2.18.2
Release:        3
Summary:        HTML documentation for LilyPond
Group:		Publishing

License:        GPLv3
URL:            http://www.lilypond.org
# I have low bandwidth in upload , the tarball is 250 mega 
# i'll just download it in prep , who can do better , please be my guest.Sflo
#Source0:        http://www.lilypond.org/download/binaries/documentation/lilypond-%{version}-1.documentation.tar.bz2
Source0:       get-doc
BuildRequires:	wget
BuildRequires:	bzip2
BuildArch:      noarch
Provides:	%{oname}-manual = %{version}

%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

This package contains the HTML documentation for LilyPond.


%prep
cp -R %{SOURCE0} . && chmod +x get-doc && ./get-doc

%build
# nothing to build


%install



%files
%doc %{oname}-documentation-%{version}/*





