%define upstream_name 	 XML-Parser-EasyTree
%define upstream_version 0.01

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	3

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl(XML::Parser)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
XML-Parser-EasyTree - adds a new "built-in" style called "EasyTree" to 
XML::Parser.  Like XML::Parser's "Tree" style, setting this style causes 
the parser to build a lightweight tree structure representing the XML document.

%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

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


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 401856
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.01-12mdv2009.0
+ Revision: 242255
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.01-10mdv2008.0
+ Revision: 64204
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.01-9mdv2008.0
+ Revision: 23510
- rebuild


* Wed May 03 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.01-8mdk
- Fix According to perl Policy
	- Source URL
	- BuildRequires
- Add URL
- use mkrel

* Wed Jun 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.01-7mdk
- rebuild

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-6mdk
- rebuild for new auto{prov,req}

