Name:           libtool
Version:        2.4.6
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://gcc.gnu.org
Source0:        http://mirrors.ustc.edu.cn/gnu/libtool/libtool-2.4.6.tar.gz
#BuildRequires:  gcc
#Requires:       gcc, automake, autoconf
BuildRoot:      %_topdir/BUILDROOT
Prefix:         /opt/%{name}-%{version}

%description

%prep

%setup -q

%build
./configure

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
   /usr/local/bin/libtool
   /usr/local/bin/libtoolize
   /usr/local/include/libltdl/lt_dlloader.h
   /usr/local/include/libltdl/lt_error.h
   /usr/local/include/libltdl/lt_system.h
   /usr/local/include/ltdl.h
   /usr/local/lib/libltdl.a
   /usr/local/lib/libltdl.la
   /usr/local/lib/libltdl.so
   /usr/local/lib/libltdl.so.7
   /usr/local/lib/libltdl.so.7.3.1
   /usr/local/share/aclocal/libtool.m4
   /usr/local/share/aclocal/ltargz.m4
   /usr/local/share/aclocal/ltdl.m4
   /usr/local/share/aclocal/ltoptions.m4
   /usr/local/share/aclocal/ltsugar.m4
   /usr/local/share/aclocal/ltversion.m4
   /usr/local/share/aclocal/lt~obsolete.m4
   /usr/local/share/info/dir
   /usr/local/share/info/libtool.info
   /usr/local/share/info/libtool.info-1
   /usr/local/share/info/libtool.info-2
   /usr/local/share/libtool/COPYING.LIB
   /usr/local/share/libtool/Makefile.am
   /usr/local/share/libtool/Makefile.in
   /usr/local/share/libtool/README
   /usr/local/share/libtool/aclocal.m4
   /usr/local/share/libtool/build-aux/compile
   /usr/local/share/libtool/build-aux/config.guess
   /usr/local/share/libtool/build-aux/config.sub
   /usr/local/share/libtool/build-aux/depcomp
   /usr/local/share/libtool/build-aux/install-sh
   /usr/local/share/libtool/build-aux/ltmain.sh
   /usr/local/share/libtool/build-aux/missing
   /usr/local/share/libtool/config-h.in
   /usr/local/share/libtool/configure
   /usr/local/share/libtool/configure.ac
   /usr/local/share/libtool/libltdl/lt__alloc.h
   /usr/local/share/libtool/libltdl/lt__argz_.h
   /usr/local/share/libtool/libltdl/lt__dirent.h
   /usr/local/share/libtool/libltdl/lt__glibc.h
   /usr/local/share/libtool/libltdl/lt__private.h
   /usr/local/share/libtool/libltdl/lt__strl.h
   /usr/local/share/libtool/libltdl/lt_dlloader.h
   /usr/local/share/libtool/libltdl/lt_error.h
   /usr/local/share/libtool/libltdl/lt_system.h
   /usr/local/share/libtool/libltdl/slist.h
   /usr/local/share/libtool/loaders/dld_link.c
   /usr/local/share/libtool/loaders/dlopen.c
   /usr/local/share/libtool/loaders/dyld.c
   /usr/local/share/libtool/loaders/load_add_on.c
   /usr/local/share/libtool/loaders/loadlibrary.c
   /usr/local/share/libtool/loaders/preopen.c
   /usr/local/share/libtool/loaders/shl_load.c
   /usr/local/share/libtool/lt__alloc.c
   /usr/local/share/libtool/lt__argz.c
   /usr/local/share/libtool/lt__dirent.c
   /usr/local/share/libtool/lt__strl.c
   /usr/local/share/libtool/lt_dlloader.c
   /usr/local/share/libtool/lt_error.c
   /usr/local/share/libtool/ltdl.c
   /usr/local/share/libtool/ltdl.h
   /usr/local/share/libtool/ltdl.mk
   /usr/local/share/libtool/slist.c
   /usr/local/share/man/man1/libtool.1
   /usr/local/share/man/man1/libtoolize.1
%doc
 
%changelog
