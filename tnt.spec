Summary:        Terminal program for packet radio
Summary(de):    Terminalprogramm für Packet Radio
Summary(pl):    Termina³ dla Packet Radio
Name:		tnt
Version:	1.9.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.wspse.de/pub/packet_radio/tnt/CVS/%{name}-20000606.tar.bz2
Patch0:		%{name}-SUSE.patch
URL:		http://www.wspse.de/WSPse/Packet.php3
BuildRequires:	ncurses-devel
BuildRequires:	libax25-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TNT is a console based packet radio terminal for hostmode tncs. It
supports virtual channels and socket communication. It also can be
used with ax25 kernel or kiss interfaces together with TFkiss.

Authors:
- -------- Mark Wahl, DL4YBG <wahlm@berlin.snafu.de> Matthias Hensler
  <wsp@gmx.de> Berndt Josef Wulf, VK5ABN <wulf@ping.net.au> Walter Koch,
  DG9EP <walter@1409.org> Jonny Hanne, DH3MB <johnny@1409.org> and
  others

%prep
%setup -q
%patch0 -p0

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ax25k2 \
	--enable-hibaud \
	--enable-genuser
#	--enable-dpboxt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc examples/ AUTHORS AX25-NOTES ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/tnt/
%dir %{_datadir}/tnt/
%config %{_datadir}/tnt/conf/
%{_datadir}/tnt/doc/
%{_datadir}/tnt/sounds/
%{_var}/spool/tnt/
%{_infodir}/
