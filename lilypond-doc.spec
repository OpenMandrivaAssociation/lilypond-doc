%define _build_pkgcheck_set /bin/true
%define _build_pkgcheck_srpm /bin/true
%define _nonzero_exit_pkgcheck_terminate_build 0

Name:           lilypond-doc
Version:        2.18.2
Release:        1
Summary:        HTML documentation for LilyPond
Group:		Publishing

License:        GPLv3
URL:            http://www.lilypond.org
# I have low bandwidth in upload , the tarball is 250 mega 
# i'll just download it in prep , who can do better , please be my guest.Sflo
Source0:        http://www.lilypond.org/download/binaries/documentation/lilypond-%{version}-1.documentation.tar.bz2
NoSource:       0

BuildArch:      noarch


%description
LilyPond is an automated music engraving system. It formats music
beautifully and automatically, and has a friendly syntax for its input
files.

This package contains the HTML documentation for LilyPond.


%prep
mkdir -p %{name}-documentation-%{version}
pushd %{name}-documentation-%{version}
wget http://download.linuxaudio.org/lilypond/binaries/documentation/%{name}-%{version}-1.documentation.tar.bz2
bunzip2 -dcq %{name}-%{version}-1.documentation.tar.bz2 | tar -xf -
find . -type f -exec chmod 644 {} \;
popd


%build
# Remove empty files
rm -f input/mutopia/E.Satie/petite-ouverture-a-danser.png
rm -f input/mutopia/J.S.Bach/wtk1-fugue2.png
rm -f input/mutopia/W.A.Mozart/mozart-hrn-3.png


%install
mkdir -p $RPM_BUILD_ROOT



%files
%doc %{name}-documentation-%{version}/*