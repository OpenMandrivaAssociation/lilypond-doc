%define _build_pkgcheck_set /bin/true
%define _build_pkgcheck_srpm /bin/true
%define _nonzero_exit_pkgcheck_terminate_build 0

Name:           lilypond-doc
Version:        2.17.97
Release:        1%{?dist}
Summary:        HTML documentation for LilyPond


License:        GPLv3
URL:            http://www.lilypond.org
Source0:        http://www.lilypond.org/download/binaries/documentation/lilypond-%{version}-1.documentation.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch


%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

This package contains the HTML documentation for LilyPond.


%prep
%setup -q -c


%build
# Remove empty files
rm -f input/mutopia/E.Satie/petite-ouverture-a-danser.png
rm -f input/mutopia/J.S.Bach/wtk1-fugue2.png
rm -f input/mutopia/W.A.Mozart/mozart-hrn-3.png


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
%doc license share
