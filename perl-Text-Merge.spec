%include	/usr/lib/rpm/macros.perl
Summary:	Text-Merge perl module
Summary(pl):	Modu³ perla Text-Merge
Name:		perl-Text-Merge
Version:	0.34
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Merge-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Merge perl module.

%description -l pl
Modu³ perla Text-Merge.

%prep
%setup -q -n Text-Merge-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/Merge.pm
%{perl_sitelib}/Text/Merge
%{perl_sitelib}/auto/Text/Merge
%{_mandir}/man3/*
