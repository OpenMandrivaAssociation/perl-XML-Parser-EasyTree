%define upstream_name 	 XML-Parser-EasyTree
%define upstream_version 0.01

Name: 		perl-%{upstream_name}
Version:	0.01
Release:	3

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/E/EB/EBOHLMAN/XML-Parser-EasyTree-0.01.tar.gz

BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl(XML::Parser)
BuildArch: noarch

%description
XML-Parser-EasyTree - adds a new "built-in" style called "EasyTree" to 
XML::Parser.  Like XML::Parser's "Tree" style, setting this style causes 
the parser to build a lightweight tree structure representing the XML document.

%prep
%setup -q  -n XML-Parser-EasyTree-0.01

%build
perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix} 
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


