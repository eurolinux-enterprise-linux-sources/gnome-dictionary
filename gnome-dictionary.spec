Summary: A dictionary application for GNOME
Name:    gnome-dictionary
Version: 3.20.0
Release: 1%{?dist}
License: GPLv3+ and LGPLv2+ and GFDL
Group:   Applications/Text
#VCS: git:git://git.gnome.org/gnome-dictionary
Source:  https://download.gnome.org/sources/%{name}/3.20/%{name}-%{version}.tar.xz
URL:     https://wiki.gnome.org/Apps/Dictionary

BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: desktop-file-utils
BuildRequires: docbook-dtds
BuildRequires: /usr/bin/appstream-util

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes: gnome-utils <= 1:3.3
Obsoletes: gnome-utils-libs <= 1:3.3
Obsoletes: gnome-utils-devel <= 1:3.3

%description
gnome-dictionary lets you look up words in dictionary sources.

%package libs
Summary: Library for dictionary support
License: LGPLv2+

%description libs
This package contains the libgdict library.

%package devel
Summary: Development files for using libgdict
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
gnome-dictionary-devel contains header files and others that
are needed to build applications using the libgdict library.

%prep
%setup -q

%build
%configure
make %{_smp_mflags}

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%find_lang %{name} --with-gnome


%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/*.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop


%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%postun
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files
%doc NEWS AUTHORS README
%license COPYING COPYING.docs COPYING.libs
%{_bindir}/gnome-dictionary
%{_datadir}/appdata/org.gnome.Dictionary.appdata.xml
%{_datadir}/applications/org.gnome.Dictionary.desktop
%{_datadir}/dbus-1/services/org.gnome.Dictionary.service
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%{_mandir}/man1/gnome-dictionary.1*

%files libs -f %{name}.lang
%license COPYING.libs
%{_libdir}/girepository-1.0/Gdict-1.0.typelib
%{_libdir}/libgdict-1.0.so.*
%{_datadir}/gdict-1.0/

%files devel
%{_includedir}/gdict-1.0/
%{_libdir}/libgdict-1.0.so
%{_libdir}/pkgconfig/gdict-1.0.pc
%{_datadir}/gir-1.0/Gdict-1.0.gir
%{_datadir}/gtk-doc/html/gdict


%changelog
* Wed Feb 22 2017 Matthias Clasen <mclasen@redhat.com> - 3.20.0-1
- Rebase to 3.20.0
  Resolves: rhbz#1386890

* Wed Jun 29 2016 Matthias Clasen <mclasen@redhat.com> - 3.14.2-2
- Update translations
- Resolves: #1304290

* Thu Mar 19 2015 Richard Hughes <rhughes@redhat.com> - 3.14.2-1
- Update to 3.14.2
- Resolves: #1174558

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.0-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.0-3
- Mass rebuild 2013-12-27

* Tue Dec 3 2013 Alexander Larsson <alexl@redhat.com> - 3.8.0-2
- Rebuild to fix s390x intermittent issue
  Resolves: rhbz#1017314

* Mon Jul 22 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.0-1
- Update to 3.8.0
- Translation updates
- Rewritten help

* Wed Jun 26 2013 Matthias Clasen <mclasen@redhat.com> - 3.6.0-3
- Update the man page
- Trim %%changelog

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Richard Hughes <hughsient@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-2
- Silence rpm scriptlet output

* Tue Mar 27 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-2
- Obsolete all gnome-utils subpackages, and handle the epoch

* Thu Nov 10 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.2-1
- Initial packaging
