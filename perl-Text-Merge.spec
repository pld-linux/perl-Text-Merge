%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Merge
Summary:	Text::Merge - v.0.34 General purpose text/data merging methods in Perl.
Name:		perl-Text-Merge
Version:	0.34
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The C<Text::Merge> package is designed to provide a quick, versatile,
and extensible way to combine presentation templates and data structures.
The C<Text::Merge> package attempts to do this by assuming that templates
are constructed with text and that objects consist of data and functions
that operate on that data.  C<Text::Merge> is very simple, in that it
works on one file and one object at a time, although an extension exists
to display lists (C<Text::Merge::Lists>) and C<Text::Merge> itself could
easily be extended further.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
