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

mkdir -p %{buildroot}%{_menudir}
cat << _EOF_ > %{buildroot}%{_menudir}/%{name}
?package(%{name}): \
 command="%{_gamesbindir}/%{name}" \
 icon="strategy_section.png" \
 longtitle="Play Monopoly" \
 needs="x11" \
 section="More applications/Games/Boards" \
 title="GtkAtlantic"
_EOF_

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_menudir}/%{name}

