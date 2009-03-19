%define snap 20061130

Summary:	A tool for extracting portions of packet trace files
Name:		tcpslice
Version:	1.2a3
Release:	%mkrel 3.%{snap}.4
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


