%define module 	XML-Parser-EasyTree
%define version 0.01
%define release %mkrel 10

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl(XML::Parser)
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

%description
XML-Parser-EasyTree - adds a new "built-in" style called "EasyTree" to 
XML::Parser.  Like XML::Parser's "Tree" style, setting this style causes 
the parser to build a lightweight tree structure representing the XML document.

%prep
%setup -q  -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MANIFEST Changes
%{_mandir}/*/*
%{perl_vendorlib}/XML/*/*

