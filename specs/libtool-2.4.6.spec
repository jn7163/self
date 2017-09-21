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
Prefix:         /usr/local

%description

%prep

%setup -q

%build
./configure

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{prefix}/bin/libtool
%{prefix}/bin/libtoolize
%{prefix}/include/libltdl/lt_dlloader.h
%{prefix}/include/libltdl/lt_error.h
%{prefix}/include/libltdl/lt_system.h
%{prefix}/include/ltdl.h
%{prefix}/lib/libltdl.a
%{prefix}/lib/libltdl.la
%{prefix}/lib/libltdl.so
%{prefix}/lib/libltdl.so.7
%{prefix}/lib/libltdl.so.7.3.1
%{prefix}/share/aclocal/libtool.m4
%{prefix}/share/aclocal/ltargz.m4
%{prefix}/share/aclocal/ltdl.m4
%{prefix}/share/aclocal/ltoptions.m4
%{prefix}/share/aclocal/ltsugar.m4
%{prefix}/share/aclocal/ltversion.m4
%{prefix}/share/aclocal/lt~obsolete.m4
%{prefix}/share/info/dir
%{prefix}/share/info/libtool.info
%{prefix}/share/info/libtool.info-1
%{prefix}/share/info/libtool.info-2
%{prefix}/share/libtool/COPYING.LIB
%{prefix}/share/libtool/Makefile.am
%{prefix}/share/libtool/Makefile.in
%{prefix}/share/libtool/README
%{prefix}/share/libtool/aclocal.m4
%{prefix}/share/libtool/build-aux/compile
%{prefix}/share/libtool/build-aux/config.guess
%{prefix}/share/libtool/build-aux/config.sub
%{prefix}/share/libtool/build-aux/depcomp
%{prefix}/share/libtool/build-aux/install-sh
%{prefix}/share/libtool/build-aux/ltmain.sh
%{prefix}/share/libtool/build-aux/missing
%{prefix}/share/libtool/config-h.in
%{prefix}/share/libtool/configure
%{prefix}/share/libtool/configure.ac
%{prefix}/share/libtool/libltdl/lt__alloc.h
%{prefix}/share/libtool/libltdl/lt__argz_.h
%{prefix}/share/libtool/libltdl/lt__dirent.h
%{prefix}/share/libtool/libltdl/lt__glibc.h
%{prefix}/share/libtool/libltdl/lt__private.h
%{prefix}/share/libtool/libltdl/lt__strl.h
%{prefix}/share/libtool/libltdl/lt_dlloader.h
%{prefix}/share/libtool/libltdl/lt_error.h
%{prefix}/share/libtool/libltdl/lt_system.h
%{prefix}/share/libtool/libltdl/slist.h
%{prefix}/share/libtool/loaders/dld_link.c
%{prefix}/share/libtool/loaders/dlopen.c
%{prefix}/share/libtool/loaders/dyld.c
%{prefix}/share/libtool/loaders/load_add_on.c
%{prefix}/share/libtool/loaders/loadlibrary.c
%{prefix}/share/libtool/loaders/preopen.c
%{prefix}/share/libtool/loaders/shl_load.c
%{prefix}/share/libtool/lt__alloc.c
%{prefix}/share/libtool/lt__argz.c
%{prefix}/share/libtool/lt__dirent.c
%{prefix}/share/libtool/lt__strl.c
%{prefix}/share/libtool/lt_dlloader.c
%{prefix}/share/libtool/lt_error.c
%{prefix}/share/libtool/ltdl.c
%{prefix}/share/libtool/ltdl.h
%{prefix}/share/libtool/ltdl.mk
%{prefix}/share/libtool/slist.c
%{prefix}/share/man/man1/libtool.1
%{prefix}/share/man/man1/libtoolize.1
%doc
 
%changelog
