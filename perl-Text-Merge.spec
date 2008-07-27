#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	Merge
Summary:	Text::Merge - general purpose text/data merging methods in Perl
Summary(pl.UTF-8):	Text::Merge - metody ogólnego przeznaczenia łączące tekst lub dane w Perlu
Name:		perl-Text-Merge
Version:	0.36
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e95edd979ef207b42a2d1bcb1de9666d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Text::Merge package is designed to provide a quick, versatile, and
extensible way to combine presentation templates and data structures.
The Text::Merge package attempts to do this by assuming that templates
are constructed with text and that objects consist of data and
functions that operate on that data. Text::Merge is very simple, in
that it works on one file and one object at a time, although an
extension exists to display lists (Text::Merge::Lists) and Text::Merge
itself could easily be extended further.

%description -l pl.UTF-8
Pakiet Text::Merge został zaprojektowany, aby dostarczyć szybką,
wszechstronną i rozszerzalną metodę do łączenia szablonów prezentacji
ze strukturami danych. Text::Merge próbuje zrobić to przy założeniu,
że szablony są skonstruowane z tekstu, a obiekty zawierają dane i
funkcje operujące na tych danych. Moduł jest bardzo prosty pod tym
względem, że działa na jednym pliku i jednym obiekcie jednocześnie,
ale istnieje rozszerzenie do wyświetlania list (Text::Merge::Lists), a
sam Text::Merge może łatwo być dalej rozszerzany.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Text/Merge.pm
%{perl_vendorlib}/Text/Merge
%{perl_vendorlib}/auto/Text/Merge
%{_mandir}/man3/*
