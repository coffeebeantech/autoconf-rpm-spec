%define _buildid .7

Summary:    A GNU tool for automatically configuring source code
Name:       autoconf
Version:    2.63
Release: 5.1%{?_buildid}%{?dist}
License:    GPLv3+ and GFDL
Group:      Development/Tools
Source:     http://ftp.gnu.org/gnu/autoconf/autoconf-%{version}.tar.bz2
Source1:    filter-provides-automake.sh
Source2:    filter-requires-automake.sh
# Fix for #556223
Patch0:     autoconf-erlang_fix.diff
URL:        http://www.gnu.org/software/autoconf/
BuildRequires:      m4 >= 1.4.7, emacs
Requires:           m4 >= 1.4.7
Requires(post):     /sbin/install-info
Requires(preun):    /sbin/install-info
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# filter out bogus perl(Autom4te*) dependencies
%define _use_internal_dependency_generator 0
%define __find_provides %{SOURCE1}
%define __find_requires %{SOURCE2}

%description
GNU Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to 
specify various configuration options.

You should install Autoconf if you are developing software and
would like to create shell scripts that configure your source code
packages. If you are installing Autoconf, you will also need to
install the GNU m4 package.

Note that the Autoconf package is not required for the end-user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not
their use.

%prep
%setup -q
%patch0 -p1 -b .erlang

%build
# use ./configure here to avoid copying config.{sub,guess} with those from the
# rpm package
./configure --prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
  --bindir=%{_bindir} --datadir=%{_datadir} --libdir=%{_libdir}
make #  %{?_smp_mflags}  The Makefile is not smp safe.

%check
make check VERBOSE=yes

%install
rm -rf ${RPM_BUILD_ROOT}
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
/sbin/install-info %{_infodir}/autoconf.info %{_infodir}/dir || :

%preun
if [ "$1" = 0 ]; then
    /sbin/install-info --del %{_infodir}/autoconf.info %{_infodir}/dir || :
fi

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_infodir}/autoconf.info*
# don't include standards.info, because it comes from binutils...
%exclude %{_infodir}/standards*
%{_datadir}/autoconf/
%dir %{_datadir}/emacs/
%{_datadir}/emacs/site-lisp/
%{_mandir}/man1/*
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO

%changelog
* Mon Jul 12 2010 19:09:47 UTC Cristian Gafton <gafton@amazon.com>
- rebuild against new libtool/automake

* Sat Jul 10 2010 00:34:05 UTC Cristian Gafton <gafton@amazon.com>
- rebuild

* Sat Jul 10 2010 00:32:58 UTC Cristian Gafton <gafton@amazon.com>
- use bz2 compressed tar archive

* Fri Jul 9 2010 21:36:39 UTC Cristian Gafton <gafton@amazon.com>
- import source package RHEL6/autoconf-2.63-5.1.el6

* Fri Jul 9 2010 21:36:38 UTC Cristian Gafton <gafton@amazon.com>
- import source package RHEL6/autoconf-2.63-4.el6

* Fri May 7 2010 00:39:08 UTC Cristian Gafton <gafton@amazon.com>
- import source package RHEL5/autoconf-2.59-12

* Fri May 7 2010 00:11:35 UTC Cristian Gafton <gafton@amazon.com>
- added submodule prep for package autoconf
