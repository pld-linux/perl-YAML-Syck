#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	YAML
%define		pnam	Syck
Summary:	YAML::Syck - fast, lightweight YAML loader and dumper
Summary(pl.UTF-8):	YAML::Syck - szybki, lekki moduł do wczytywania i zrzucania YAML-a
Name:		perl-YAML-Syck
Version:	1.31
Release:	3
License:	MIT
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/YAML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2394bccf64c01cdc796cd5227bba237f
URL:		http://search.cpan.org/dist/YAML-Syck/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.59
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl.UTF-8
Ten moduł udostępnia perlowy interfejs do biblioteki serializacji
danych libsyck. Eksportuje funkcje Dump i Load do przekształcania
perlowych struktur danych na łańcuchy YAML i z powrotem.

Uwaga: jeśli pracujemy z dowiązaniami YAML/Sych dla innego języka
(np. Ruby), należy ustawić $YAML::Syck::ImplicitTyping na 1 przed
wywołaniem funkcji Load/Dump. Domyślne ustawienie jest dla zachowania
wstecznej zgodności z YAML.pm.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COMPATIBILITY Changes
%{perl_vendorarch}/YAML/Syck.pm
%{perl_vendorarch}/JSON/Syck.pm
%dir %{perl_vendorarch}/YAML/Dumper
%{perl_vendorarch}/YAML/Dumper/Syck.pm
%dir %{perl_vendorarch}/YAML/Loader
%{perl_vendorarch}/YAML/Loader/Syck.pm
%dir %{perl_vendorarch}/auto/YAML/Syck
%attr(755,root,root) %{perl_vendorarch}/auto/YAML/Syck/Syck.so
%{_mandir}/man3/JSON::Syck.3pm*
%{_mandir}/man3/YAML::Syck.3pm*
