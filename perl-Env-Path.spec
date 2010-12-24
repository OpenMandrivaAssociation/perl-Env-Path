%define upstream_name    Env-Path
%define upstream_version 0.18

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Advanced operations on path variables
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Env/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Env::Path presents an object-oriented interface to _path variables_,
defined as that subclass of _environment variables_ which name an ordered
list of filesystem elements separated by a platform-standard _separator_
(typically ':' on UNIX and ';' on Windows).

Of course, core Perl constructs such

  $ENV{PATH} .= ":/usr/local/bin";

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/envpath
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*
