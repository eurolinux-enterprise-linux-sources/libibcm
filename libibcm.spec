Name: libibcm
Version: 1.0.5
Release: 8%{?dist}
Summary: Userspace InfiniBand Connection Manager
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/rdmacm/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel > 1.1.4
ExcludeArch: s390 s390x
%description
libibcm provides a userspace library that handles the majority of the low
level work required to open an RDMA connection between two machines.

%package devel
Summary: Development files for the libibcm library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}, libibverbs-devel >= 1.1
%description devel
Development files for the libibcm library.

%package static
Summary: Static version of libibcm libraries
Group: System Environment/Libraries
Requires: %{name}-devel = %{version}-%{release}
%description static
Static version of libibcm library.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libibcm*.so.*
%doc AUTHORS COPYING README

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.5-8
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Doug Ledford <dledford@redhat.com> - 1.0.5-4
- Bump and rebuild against latest libibverbs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 11 2010 Doug Ledford <dledford@redhat.com> - 1.0.5-2
- Switch from ExclusiveArch with a big list to ExcludeArch with a small list

* Thu Dec 03 2009 Doug Ledford <dledford@redhat.com> - 1.0.5-1
- Update to latest upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jun 08 2008 Doug Ledford <dledford@redhat.com> - 1.0.2-1
- Initial package for submission to Fedora review process
