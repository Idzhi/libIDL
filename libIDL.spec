Summary:	Library for parsing IDL (Interface Definition Language)
Summary(pl):	Biblioteka do parsowania IDL (j�zyka definicji interfejsu)
Name:		libIDL
Version:	0.8.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	f94a690454b4f9d448c2e51792f81365
Patch0:		%{name}-info.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.8
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libIDL is a library for parsing IDL (Interface Definition Language).
It can be used for both COM-style and CORBA-style IDL.

%description -l pl
libIDL to biblioteka do parsowania IDL (Interface Definition Language
- j�zyka definicji interfejsu). Mo�e by� u�ywana z IDL w stylu COM lub
CORBA.

%package devel
Summary:	Header files for libIDL
Summary(pl):	Pliki nag��wkowe libIDL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.2.0
Requires:	pkgconfig >= 0.8

%description devel
libIDL is a library for parsing IDL (Interface Definition Language).
It can be used for both COM-style and CORBA-style IDL.

This package contains the header files and libraries needed to write
or compile programs that use libIDL.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe potrzebne do kompilowania
program�w u�ywaj�cych libIDL.

%package static
Summary:	Static libIDL libraries
Summary(pl):	Statyczne biblioteki libIDL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libIDL libraries.

%description static -l pl
Statyczne biblioteki libIDL.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/libIDL-config-2
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*
%{_infodir}/*info*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
