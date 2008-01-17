#
# TODO:
# - add BRs,R
Name:		teewars
Summary:	Cute little buggers with guns.
Summary(pl.UTF-8):	Takie fajne robaczki z gnatami.
Version:	0.3.3
Release:	0.2
Group:		X11/Applications/Games
License:	Please read license.txt
Source0:	http://www.teewars.com/files/%{name}-%{version}-src.tar.gz
# Source0-md5:	6f7ba385ab4cc7944802e5010c17a204
Source1:	http://www.teewars.com/files/beta/bam.zip
# Source1-md5:	2bd60d6790a2f92ba10e0a384e4c94b6
Source2:	%{name}.png
Source3:	%{name}.desktop
#Source4:	%{name}_srv.desktop
Patch0:		%{name}-sh.patch
URL:		http://www.teewars.com/
BuildRequires:	python
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cute little buggers with guns.
CTF,DM network game.

%description -l pl.UTF-8
Takie fajne robaczki z gnatami. Czyli:
Gra sieciowa typu CTF,DM.

%prep
%setup -q -a1 -n %{name}-%{version}-src
%patch0 -p0 

%build
cd bam
./make_unix.sh
cd ..
bam/src/bam release

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/%{name}/data}

install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install teewars.sh $RPM_BUILD_ROOT%{_bindir}
install teewars teewars_srv $RPM_BUILD_ROOT%{_datadir}/%{name}/
cp -rf data $RPM_BUILD_ROOT%{_datadir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt license.txt
%attr(755,root,root) %{_bindir}/teewars.sh
%attr(755,root,root) %{_datadir}/%{name}/teewars*
%{_datadir}/%{name}
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
