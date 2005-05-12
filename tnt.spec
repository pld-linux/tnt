#
# Conditional build:
%bcond_with genuser		# allow create users for TNT (FHS incomplance)
%bcond_with dpboxt		# support for dpboxt (doesn't compile - propably missing headers)
#
Summary:	Terminal program for packet radio
Summary(de):	Terminalprogramm für Packet Radio
Summary(pl):	Terminal dla Packet Radio
Name:		tnt
Version:	1.9.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.wspse.de/pub/packet_radio/tnt/CVS/%{name}-20000606.tar.gz
# Source0-md5:	aea30feb88b54eda10171f47776b9a3e
Patch0:		%{name}-SUSE.patch
URL:		http://www.wspse.de/WSPse/Packet.php3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libax25-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TNT is a console based packet radio terminal for hostmode tncs. It
supports virtual channels and socket communication. It also can be
used with ax25 kernel or kiss interfaces together with TFkiss.

%description -l pl
TNT jest konsolowym terminalem Packet Radio dla TNC w trypie HOST.
Obs³uguje wirtualne kana³y oraz komunikacjê poprzez gniazdko. Mo¿e byæ
równie¿ u¿ywany bezpo¶rednio z rdzeniem AX25 lub poprzez interfejs
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
	%{?with_genuser:--enable-genuser} \
	%{?with_dpboxt:--enable-dpboxt}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc examples/ AUTHORS AX25-NOTES ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/tnt
%dir %{_datadir}/tnt
%config %{_datadir}/tnt/conf
%{_datadir}/tnt/doc
%{_datadir}/tnt/sounds
%{_var}/spool/tnt
%{_infodir}/*.info*
