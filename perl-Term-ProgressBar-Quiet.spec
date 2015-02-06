%define upstream_name    Term-ProgressBar-Quiet
%define upstream_version 0.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Provide a progress meter if run interactively
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Interactive)
BuildRequires:	perl(Term::ProgressBar)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
the Term::ProgressBar manpage is a wonderful module for showing progress
bars on the terminal. This module acts very much like that module when it
is run interactively. However, when it is not run interactively (for
example, as a cron job) then it does not show the progress bar.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 655220
- rebuild for updated spec-helper

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.310.0-1mdv2011.0
+ Revision: 485958
- import perl-Term-ProgressBar-Quiet


* Sun Jan 03 2010 cpan2dist 0.31-1mdv
- initial mdv release, generated with cpan2dist
