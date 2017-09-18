Name:           autoconf
Version:        2.69
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://gcc.gnu.org
Source0:        http://mirrors.ustc.edu.cn/gnu/autoconf/autoconf-2.69.tar.gz
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
   /usr/local/bin/autoconf
   /usr/local/bin/autoheader
   /usr/local/bin/autom4te
   /usr/local/bin/autoreconf
   /usr/local/bin/autoscan
   /usr/local/bin/autoupdate
   /usr/local/bin/ifnames
   /usr/local/share/autoconf/Autom4te/C4che.pm
   /usr/local/share/autoconf/Autom4te/ChannelDefs.pm
   /usr/local/share/autoconf/Autom4te/Channels.pm
   /usr/local/share/autoconf/Autom4te/Configure_ac.pm
   /usr/local/share/autoconf/Autom4te/FileUtils.pm
   /usr/local/share/autoconf/Autom4te/General.pm
   /usr/local/share/autoconf/Autom4te/Getopt.pm
   /usr/local/share/autoconf/Autom4te/Request.pm
   /usr/local/share/autoconf/Autom4te/XFile.pm
   /usr/local/share/autoconf/INSTALL
   /usr/local/share/autoconf/autoconf/autoconf.m4
   /usr/local/share/autoconf/autoconf/autoconf.m4f
   /usr/local/share/autoconf/autoconf/autoheader.m4
   /usr/local/share/autoconf/autoconf/autoscan.m4
   /usr/local/share/autoconf/autoconf/autotest.m4
   /usr/local/share/autoconf/autoconf/autoupdate.m4
   /usr/local/share/autoconf/autoconf/c.m4
   /usr/local/share/autoconf/autoconf/erlang.m4
   /usr/local/share/autoconf/autoconf/fortran.m4
   /usr/local/share/autoconf/autoconf/functions.m4
   /usr/local/share/autoconf/autoconf/general.m4
   /usr/local/share/autoconf/autoconf/go.m4
   /usr/local/share/autoconf/autoconf/headers.m4
   /usr/local/share/autoconf/autoconf/lang.m4
   /usr/local/share/autoconf/autoconf/libs.m4
   /usr/local/share/autoconf/autoconf/oldnames.m4
   /usr/local/share/autoconf/autoconf/programs.m4
   /usr/local/share/autoconf/autoconf/specific.m4
   /usr/local/share/autoconf/autoconf/status.m4
   /usr/local/share/autoconf/autoconf/types.m4
   /usr/local/share/autoconf/autom4te.cfg
   /usr/local/share/autoconf/autoscan/autoscan.list
   /usr/local/share/autoconf/autotest/autotest.m4
   /usr/local/share/autoconf/autotest/autotest.m4f
   /usr/local/share/autoconf/autotest/general.m4
   /usr/local/share/autoconf/autotest/specific.m4
   /usr/local/share/autoconf/m4sugar/foreach.m4
   /usr/local/share/autoconf/m4sugar/m4sh.m4
   /usr/local/share/autoconf/m4sugar/m4sh.m4f
   /usr/local/share/autoconf/m4sugar/m4sugar.m4
   /usr/local/share/autoconf/m4sugar/m4sugar.m4f
   /usr/local/share/autoconf/m4sugar/version.m4
   /usr/local/share/info/autoconf.info
   /usr/local/share/info/dir
   /usr/local/share/info/standards.info
   /usr/local/share/man/man1/autoconf.1
   /usr/local/share/man/man1/autoheader.1
   /usr/local/share/man/man1/autom4te.1
   /usr/local/share/man/man1/autoreconf.1
   /usr/local/share/man/man1/autoscan.1
   /usr/local/share/man/man1/autoupdate.1
   /usr/local/share/man/man1/config.guess.1
   /usr/local/share/man/man1/config.sub.1
   /usr/local/share/man/man1/ifnames.1
%doc
 
%changelog
