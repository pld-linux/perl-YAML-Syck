#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	YAML
%define		pnam	Syck
Summary:	YAML::Syck - fast, lightweight YAML loader and dumper
Summary(pl):	YAML::Syck - szybki, lekki modu³ do wczytywania i zrzucania YAML-a
Name:		perl-YAML-Syck
Version:	0.71
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/YAML-Syck-%{version}.tar.gz
# Source0-md5:	c24b223c74504971b62cc7a94fee5f17
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-YAML >= 0.60
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the libsyck data
serialization library. It exports the Dump and Load functions for
converting Perl data structures to YAML strings, and the other way
around.

NOTE: If you are working with other language's YAML/Syck bindings
(such as Ruby), please set $YAML::Syck::ImplicitTyping to 1 before
calling the Load/Dump functions. The default setting is for preserving
backward-compatibility with YAML.pm.

%description -l pl
Ten modu³ udostêpnia perlowy interfejs do biblioteki serializacji
danych libsyck. Eksportuje funkcje Dump i Load do przekszta³cania
perlowych struktur danych na ³añcuchy YAML i z powrotem.

Uwaga: je¶li pracujemy z dowi±zaniami YAML/Sych dla innego jêzyka
(np. Ruby), nale¿y ustawiæ $YAML::Syck::ImplicitTyping na 1 przed
wywo³aniem funkcji Load/Dump. Domy¶lne ustawienie jest dla zachowania
wstecznej zgodno¶ci z YAML.pm.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/YAML/Syck.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/YAML
%{perl_vendorarch}/YAML/*.pm
%dir %{perl_vendorarch}/JSON
%{perl_vendorarch}/JSON/Syck.pm
%dir %{perl_vendorarch}/YAML/Dumper
%{perl_vendorarch}/YAML/Dumper/Syck.pm
%dir %{perl_vendorarch}/YAML/Loader
%{perl_vendorarch}/YAML/Loader/Syck.pm
%dir %{perl_vendorarch}/auto/YAML
%dir %{perl_vendorarch}/auto/YAML/Syck
%{perl_vendorarch}/auto/YAML/Syck/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/YAML/Syck/*.so
%{_mandir}/man3/*
