%define upstream_name    Term-ProgressBar-Quiet
%define upstream_version 0.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Provide a progress meter if run interactively
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Interactive)
BuildRequires: perl(Term::ProgressBar)
BuildRequires: perl(Test::MockObject)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
the Term::ProgressBar manpage is a wonderful module for showing progress
bars on the terminal. This module acts very much like that module when it
is run interactively. However, when it is not run interactively (for
example, as a cron job) then it does not show the progress bar.

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
%doc CHANGES README
%{_mandir}/man3/*
%perl_vendorlib/*


