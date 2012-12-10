%define version 0.4.2
%define rel	4
%define release %mkrel %rel

Summary:	Monopoly-like game client
Name:		gtkatlantic
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Games/Boards
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
Categories=Game;BoardGame;
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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-4mdv2011.0
+ Revision: 619285
- the mass rebuild of 2010.0 packages

* Wed May 13 2009 Samuel Verschelde <stormi@mandriva.org> 0.4.2-3mdv2010.0
+ Revision: 375264
- fix Group (fixes #49512)
- fix Licence
- fix desktop file

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.4.2-2mdv2009.0
+ Revision: 218421
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.4.2-2mdv2008.1
+ Revision: 131704
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import gtkatlantic


* Sun Mar 19 2006 Guillaume Bedot <littletux@zarb.org> 0.4.2-2mdk
- fix buildrequires to use gtk2

* Sun Mar 19 2006 Guillaume Bedot <littletux@zarb.org> 0.4.2-1mdk
- 0.4.2
- fix source URL
- mkrel

* Thu Dec 02 2004 Abel Cheung <deaddog@mandrake.org> 0.3.3-2mdk
- Fix BuildRequires

* Mon Jun 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.3.3-1mdk
- 0.3.3

* Wed Jun 09 2004 Abel Cheung <deaddog@deaddog.org> 0.3.2-1mdk
- First Mandrake package
