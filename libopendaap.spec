Summary:	Open DAAP library - connecting to audio streams using DAAP
Summary(pl):	Biblioteka Open DAAP - ³±czenie ze strumieniami audio przy u¿yciu DAAP
Name:		libopendaap
Version:	0.4.0
Release:	1
License:	BSD-like/Apple Public Source License v2.0 (see COPYING)
Group:		Libraries
Source0:	http://crazney.net/programs/itunes/files/%{name}-%{version}.tar.bz2
# Source0-md5:	4edf92ac18c6ab8c05be7a4eb64a8a8d
URL:		http://crazney.net/programs/itunes/libopendaap.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for connecting to iTunes shares and streaming audio files.

%description -l pl
Biblioteka do ³±czenia z udzia³ami iTunes oraz obs³ugi strumieni z
plików d¼wiêkowych.

%package devel
Summary:	Header files for libopendaap library
Summary(pl):	Pliki nag³ówkowe biblioteki libopendaap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libopendaap library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libopendaap.

%package static
Summary:	Static libopendaap library
Summary(pl):	Statyczna biblioteka libopendaap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libopendaap library.

%description static -l pl
Statyczna biblioteka libopendaap.

%prep
%setup -q

%build
# rebuild - *.m4 and ltmain.sh are desynced
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_mandir}/man3/lib*.3*
%{_includedir}/daap
%{_pkgconfigdir}/opendaap.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
