%define snap 20061130

Summary:	A tool for extracting portions of packet trace files
Name:		tcpslice
Version:	1.2a3
Release:	%mkrel 3.%{snap}.5
Group:		Monitoring
License:	BSD
URL:		http://www.tcpdump.org
Source0:	tcpslice-%{snap}.tar.bz2
Patch0:		tcpslice-libosip2-3.x.patch
Requires:	tcpdump >= 0.9.5
BuildRequires:	libpcap-devel >= 0.9.5
BuildRequires:	libnids-devel >= 1.21
BuildRequires:	libosip2-devel >= 3.0.3
BuildRequires:	libooh323c-devel >= 0.8.2
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A tool for extracting portions of packet trace files generated using tcpdump's
-w flag.

%prep

%setup -q -n %{name}
%patch0 -p0 -b .libsip23

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 tcpslice %{buildroot}%{_sbindir}
install -m0644 tcpslice.1 %{buildroot}%{_mandir}/man1/tcpslice.1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES CREDITS INSTALL README
%{_sbindir}/tcpslice
%{_mandir}/man1/tcpslice.1*




%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2a3-3.20061130.5mdv2010.0
+ Revision: 445382
- rebuild

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2a3-3.20061130.4mdv2009.1
+ Revision: 358007
- rebuild for latest libosip

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2a3-3.20061130.3mdv2009.1
+ Revision: 298409
- rebuilt against libpcap-1.0.0

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2a3-3.20061130.2mdv2009.0
+ Revision: 269413
- rebuild early 2009.0 package (before pixel changes)

* Thu May 29 2008 Funda Wang <fundawang@mandriva.org> 1.2a3-0.20061130.2mdv2009.0
+ Revision: 212980
- rebuild for new osip2

* Thu Jan 24 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2a3-0.20061130.1mdv2008.1
+ Revision: 157615
- Undo BuildRequire "fix" that was incorrect.
- Fix build requires (libosip2-devel not libosip-devel)
- Add patch for libosip2-3.x

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix libosip-devel BR

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.2a1-0.20061130.1mdv2008.1
+ Revision: 128294
- kill re-definition of %%buildroot on Pixel's request


* Mon Dec 18 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2a1-0.20061130.1mdv2007.0
+ Revision: 98565
- Import tcpslice

* Mon Dec 18 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2a1-0.20061130.1mdv2007.1
- new snap (20061130)
- fix deps

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2a1-0.20040517.3mdk
- rebuilt against new libpcap-0.9.1 (aka. a "play safe" rebuild)

* Sat Jun 04 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2a1-0.20040517.2mdk
- rebuild

* Tue May 18 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2a1-0.20040517.1mdk
- initial package
- added P0

