#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mixin-Linewise
Version  : 0.108
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Mixin-Linewise-0.108.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Mixin-Linewise-0.108.tar.gz
Summary  : 'write your linewise code for handles; this does the rest'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Mixin-Linewise-license = %{version}-%{release}
Requires: perl-Mixin-Linewise-perl = %{version}-%{release}
Requires: perl(PerlIO::utf8_strict)
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Params::Util)
BuildRequires : perl(PerlIO::utf8_strict)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Install)

%description
This archive contains the distribution Mixin-Linewise,
version 0.108:
write your linewise code for handles; this does the rest

%package dev
Summary: dev components for the perl-Mixin-Linewise package.
Group: Development
Provides: perl-Mixin-Linewise-devel = %{version}-%{release}
Requires: perl-Mixin-Linewise = %{version}-%{release}

%description dev
dev components for the perl-Mixin-Linewise package.


%package license
Summary: license components for the perl-Mixin-Linewise package.
Group: Default

%description license
license components for the perl-Mixin-Linewise package.


%package perl
Summary: perl components for the perl-Mixin-Linewise package.
Group: Default
Requires: perl-Mixin-Linewise = %{version}-%{release}

%description perl
perl components for the perl-Mixin-Linewise package.


%prep
%setup -q -n Mixin-Linewise-0.108
cd %{_builddir}/Mixin-Linewise-0.108

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mixin-Linewise
cp %{_builddir}/Mixin-Linewise-0.108/LICENSE %{buildroot}/usr/share/package-licenses/perl-Mixin-Linewise/6f883c73668a2b7a2ad205ccda91c0ab9cad376a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mixin::Linewise.3
/usr/share/man/man3/Mixin::Linewise::Readers.3
/usr/share/man/man3/Mixin::Linewise::Writers.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mixin-Linewise/6f883c73668a2b7a2ad205ccda91c0ab9cad376a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Mixin/Linewise.pm
/usr/lib/perl5/vendor_perl/5.30.2/Mixin/Linewise/Readers.pm
/usr/lib/perl5/vendor_perl/5.30.2/Mixin/Linewise/Writers.pm
