#
# TODO:
# - MAKE IT WORK; game isn't aware files are in /usr/share/teeworlds
# - optflags
# - needs test
#
Summary:	Cute little buggers with guns
Summary(pl.UTF-8):	Takie fajne robaczki z gnatami
Name:		teeworlds
Version:	0.6.1
Release:	0.1
License:	distributable
Group:		X11/Applications/Games
Source0:	http://www.teeworlds.com/files/%{name}-%{version}-source.tar.gz
# Source0-md5:	00de7195ecd1f23596dc3237341af512
Source1:	%{name}.png
Source2:	%{name}.desktop
#Source3:	%{name}_srv.desktop
URL:		http://www.teeworlds.com/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	bam >= 0.4.0
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Provides:	teewars = %{version}
Obsoletes:	teewars <= 0.3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cute little buggers with guns. CTF, DM network game.

%description -l pl.UTF-8
Takie fajne robaczki z gnatami. Gra sieciowa typu CTF, DM.

%prep
%setup -q -n %{name}-b177-r50edfd37-source
%{__sed} -i '/release_settings.cc.optimize = 1/a\Import("pld_config.bam")' bam.lua

%build
cat <<'EOF' > pld_config.bam
	release_settings.cc.flags:Add("%{rpmcxxflags}")
	release_settings.cc.c_compiler = "%{__cc}"
	release_settings.cc.cxx_compiler = "%{__cxx}"
	release_settings.link.linker = "%{__cxx}"
	release_settings.link.inputflags = "%{rpmcxxflags} %{rpmldflags}"
EOF

bam -v release

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/%{name}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{name} %{name}_srv $RPM_BUILD_ROOT%{_bindir}
cp -rf data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

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
