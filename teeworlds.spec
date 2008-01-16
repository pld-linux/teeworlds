Name:		teewars
Summary:	3D billard simulation using OpenGL
Summary(pl.UTF-8):	Symulacja bilarda używająca OpenGL
Version:	0.3.3
Release:	0.1
Group:		X11/Applications/Games
License:	GPL
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
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3D billard simulation using OpenGL.

%description -l pl.UTF-8
Trójwymiarowa symulacja bilarda używająca OpenGL.

%prep
%setup -q -n %{name}-%{version}-src
unzip %{SOURCE1}
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
%{_datadir}/%{name}
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
