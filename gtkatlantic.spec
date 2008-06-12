%define version 0.4.2
%define rel	2
%define release %mkrel %rel

Summary:	Monopoly-like game client
Name:		gtkatlantic
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Strategy
URL:		http://gtkatlantic.gradator.net/
Source:		http://gtkatlantic.gradator.net/downloads/v0.4/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel
BuildRequires:	png-devel
BuildRequires:	libxml2-devel

%description
monopd is a dedicated game server daemon for playing Monopoly-like board
games. Clients connect to the server and communicate using short commands
and XML messages.

%prep
%setup -q

%build
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name} 
Icon=strategy_section 
Comment=Play Monopoly 
Categories=BoardGame; 
Name=GtkAtlantic
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

