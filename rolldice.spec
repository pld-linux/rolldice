Summary:	A dice rolling software
Summary(pl.UTF-8):	Program do rzucania kośćmi
Name:		rolldice
Version:	1.10
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://ftp.debian.org/debian/pool/main/r/rolldice/%{name}_%{version}.orig.tar.gz
# Source0-md5:	c65d37f81e80d0d5db6c49c08cf3b484
Patch0:		%{name}-Makefile.patch
URL:		http://packages.debian.org/source/sid/rolldice
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rolldice is a simple command line tool for rolling dices with
different ways to compute.

%description -l pl.UTF-8
rolldice jest prostym narzędziem konsolowym, które symuluje rzut
kością na wiele różnych sposobów.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS Changelog README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
