%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Merge
Summary:	Text::Merge - General purpose text/data merging methods in Perl
Summary(pl):	Text::Merge - metody ogólnego przeznaczenia ³±cz±ce tekst lub dane w Perlu
Name:		perl-Text-Merge
Version:	0.34
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0d717a3003a9ff227cf1af460675c5ec
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Pakiet Text::Merge zosta³ zaprojektowany, aby dostarszyæ szybk±,
wszechstronn± i rozszerzaln± metodê do ³±czenia szablonów prezentacji
ze strukturami danych. Text::Merge próbuje zrobiæ to przy za³o¿eniu,
¿e szablony s± skonstruowane z tekstu, a obiekty zawieraj± dane i
funkcje operuj±ce na tych danych. Modu³ jest bardzo prosty pod tym
wzglêdem, ¿e dzia³± na jednym pliku i jednym obiekcie jednocze¶nie,
ale istnieje rozszerzenie do wy¶wietlania list (Text::Merge::Lists), a
sam Text::Merge mo¿e ³atwo byæ dalej rozszerzany.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Text/Merge.pm
%{perl_vendorlib}/Text/Merge
%{perl_vendorlib}/auto/Text/Merge
%{_mandir}/man3/*
