#
# spec file for package libopendaap
#
# Copyright (c) Joerg Cassens <jmt@cassens.org>
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://www.suse.de/feedback/
#
Name:		libopendaap
Summary:	connecting to audio streams using daap
Version:	0.2.2
Release:	0.1
License:	Other License(s), see package
Group:		Libraries
URL:		http://crazney.net/programs/itunes/libopendaap.html
Source0:	http://crazney.net/programs/itunes/files/%{name}-%{version}.tar.bz2
# Source0-md5:	a17e445c2c0de9cc61fc11b3fb42734a
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for connecting to iTunes shares and streaming audio files.

%package devel
Summary:  headers for libopendaap
Group:	Development/Libraries

%description devel
headers for libopendaap

%package static
Summary:  static libraries of libopendaap
Group:	Development/Libraries

%description static
static libraries of libopendaap


%prep

%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT/%{_libdir}/%{name}.0.0.1 $RPM_BUILD_ROOT/%{_libdir}/%{name}.so.0.0.1
ln -s %{name}.so.0.0.1 $RPM_BUILD_ROOT/%{_libdir}/%{name}.so

%clean
rm -fr $RPM_BUILD_ROOT

%post        -p /sbin/ldconfig

%postun      -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/*.so.*
%{_libdir}/pkgconfig/opendaap.pc

%files devel
%{_includedir}/daap/client.h
%{_libdir}/*.so
%{_libdir}/*.la

%files static
%{_libdir}/*.a
