#
# TODO:
# - exclude bam to separate spec file and BR it
Summary:	Cute little buggers with guns
Summary(pl.UTF-8):	Takie fajne robaczki z gnatami.
Name:		teeworlds
Version:	0.4.2
Release:	1
License:	distributable
Group:		X11/Applications/Games
Source0:	http://www.teeworlds.com/files/%{name}-%{version}-src.tar.gz
# Source0-md5:	97f1833ea94015b472a0f828003693b8
Source1:	http://www.teeworlds.com/files/beta/bam.zip
# Source1-md5:	dd1937ce711927299a1b09edffa319ca
Source2:	%{name}.png
Source3:	%{name}.desktop
#Source4:	%{name}_srv.desktop
URL:		http://www.teeworlds.com/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	python
BuildRequires:	unzip
BuildRequires:	xorg-lib-libX11-devel
Obsoletes:	teewars <= 0.3.4
Provides:	teewars = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cute little buggers with guns. CTF, DM network game.

%description -l pl.UTF-8
Takie fajne robaczki z gnatami. Gra sieciowa typu CTF, DM.

%prep
%setup -q -a1 -n %{name}-%{version}-src
# Workaround for no possibility to pass location of data files
%{__sed} -i 's|"data/|"%{_datadir}/%{name}/data/|g' \
	datasrc/data.ds \
	src/game/client/{gc_map_image.cpp,gc_hooks.cpp,gc_skin.cpp} \
	src/game/editor/ed_editor.cpp \
	src/engine/e_map.c \
	src/engine/client/ec_client.c \
	src/engine/server/es_server.c

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
install %{name} %{name}_srv $RPM_BUILD_ROOT%{_bindir}
cp -rf data $RPM_BUILD_ROOT%{_datadir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt license.txt
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}_srv
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
