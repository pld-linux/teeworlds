#
# TODO:
# rename to teeworlds.spec on CVS
Name:		teeworlds
Summary:	Cute little buggers with guns.
Summary(pl.UTF-8):	Takie fajne robaczki z gnatami.
Version:	0.4.1
Release:	1
Group:		X11/Applications/Games
License:	distributable
Source0:	http://www.teeworlds.com/files/%{name}-%{version}-src.tar.gz
# Source0-md5:	d2977b5f46a83043b6e748999de7d5b8
Source1:	http://www.teeworlds.com/files/beta/bam.zip
# Source1-md5:	dd1937ce711927299a1b09edffa319ca
Source2:	teewars.png
Source3:	teewars.desktop
#Source4:	%{name}_srv.desktop
Source4:	teewars.sh
URL:		http://www.teeworlds.com/
BuildRequires:	alsa-lib-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	python
BuildRequires:	unzip
BuildRequires:	xorg-lib-libX11-devel
Obsoletes:	teewars
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cute little buggers with guns.
CTF,DM network game.

%description -l pl.UTF-8
Takie fajne robaczki z gnatami. Czyli:
Gra sieciowa typu CTF,DM.

%prep
%setup -q -a1 -n %{name}-%{version}-src
#%patch0 -p0

%build
cd bam
./make_unix.sh
cd ..
bam/src/bam release

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/%{name}/data}

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/%{name}.sh
install %{name} %{name}_srv $RPM_BUILD_ROOT%{_datadir}/%{name}/
cp -rf data $RPM_BUILD_ROOT%{_datadir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt license.txt
%attr(755,root,root) %{_bindir}/%{name}.sh
%attr(755,root,root) %{_datadir}/%{name}/%{name}*
%{_datadir}/%{name}
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
