Summary:	Terminal program for packet radio
Summary(de):	Terminalprogramm f�r Packet Radio
Summary(pl):	Termina� dla Packet Radio
Name:		tnt
Version:	1.9.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.wspse.de/pub/packet_radio/tnt/%{name}-%{version}.tar.bz2
# Source0-md5:	3fbd9bc029611a462c7864cf79994ffa
Patch0:		%{name}-SUSE.patch
URL:		http://www.wspse.de/WSPse/Packet.php3
BuildRequires:	ncurses-devel
BuildRequires:	libax25-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TNT is a console based packet radio terminal for hostmode tncs. It
supports virtual channels and socket communication. It also can be
used with ax25 kernel or kiss interfaces together with TFkiss.

%description -l pl
TNT jest konsolowym termina�em Packet Radio dla TNC w trypie HOST.
Obs�uguje wirtualne kana�y oraz komunikacj� poprzez gniazdko. Mo�e by�
r�wnie� u�ywany bezpo�rednio z rdzeniem AX25 lub poprzez interfejs
KISS wraz z programem tfkiss.

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
