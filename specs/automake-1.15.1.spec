Name:           automake
Version:        1.15.1
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://gcc.gnu.org
Source0:        http://mirrors.ustc.edu.cn/gnu/automake/automake-1.15.1.tar.gz
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
   /usr/local/bin/aclocal
   /usr/local/bin/aclocal-1.15
   /usr/local/bin/automake
   /usr/local/bin/automake-1.15
   /usr/local/share/aclocal-1.15/amversion.m4
   /usr/local/share/aclocal-1.15/ar-lib.m4
   /usr/local/share/aclocal-1.15/as.m4
   /usr/local/share/aclocal-1.15/auxdir.m4
   /usr/local/share/aclocal-1.15/cond-if.m4
   /usr/local/share/aclocal-1.15/cond.m4
   /usr/local/share/aclocal-1.15/depend.m4
   /usr/local/share/aclocal-1.15/depout.m4
   /usr/local/share/aclocal-1.15/dmalloc.m4
   /usr/local/share/aclocal-1.15/extra-recurs.m4
   /usr/local/share/aclocal-1.15/gcj.m4
   /usr/local/share/aclocal-1.15/init.m4
   /usr/local/share/aclocal-1.15/install-sh.m4
   /usr/local/share/aclocal-1.15/internal/ac-config-macro-dirs.m4
   /usr/local/share/aclocal-1.15/lead-dot.m4
   /usr/local/share/aclocal-1.15/lex.m4
   /usr/local/share/aclocal-1.15/lispdir.m4
   /usr/local/share/aclocal-1.15/maintainer.m4
   /usr/local/share/aclocal-1.15/make.m4
   /usr/local/share/aclocal-1.15/missing.m4
   /usr/local/share/aclocal-1.15/mkdirp.m4
   /usr/local/share/aclocal-1.15/obsolete.m4
   /usr/local/share/aclocal-1.15/options.m4
   /usr/local/share/aclocal-1.15/prog-cc-c-o.m4
   /usr/local/share/aclocal-1.15/python.m4
   /usr/local/share/aclocal-1.15/runlog.m4
   /usr/local/share/aclocal-1.15/sanity.m4
   /usr/local/share/aclocal-1.15/silent.m4
   /usr/local/share/aclocal-1.15/strip.m4
   /usr/local/share/aclocal-1.15/substnot.m4
   /usr/local/share/aclocal-1.15/tar.m4
   /usr/local/share/aclocal-1.15/upc.m4
   /usr/local/share/aclocal-1.15/vala.m4
   /usr/local/share/aclocal/README
   /usr/local/share/automake-1.15/Automake/ChannelDefs.pm
   /usr/local/share/automake-1.15/Automake/Channels.pm
   /usr/local/share/automake-1.15/Automake/Condition.pm
   /usr/local/share/automake-1.15/Automake/Config.pm
   /usr/local/share/automake-1.15/Automake/Configure_ac.pm
   /usr/local/share/automake-1.15/Automake/DisjConditions.pm
   /usr/local/share/automake-1.15/Automake/FileUtils.pm
   /usr/local/share/automake-1.15/Automake/General.pm
   /usr/local/share/automake-1.15/Automake/Getopt.pm
   /usr/local/share/automake-1.15/Automake/Item.pm
   /usr/local/share/automake-1.15/Automake/ItemDef.pm
   /usr/local/share/automake-1.15/Automake/Language.pm
   /usr/local/share/automake-1.15/Automake/Location.pm
   /usr/local/share/automake-1.15/Automake/Options.pm
   /usr/local/share/automake-1.15/Automake/Rule.pm
   /usr/local/share/automake-1.15/Automake/RuleDef.pm
   /usr/local/share/automake-1.15/Automake/VarDef.pm
   /usr/local/share/automake-1.15/Automake/Variable.pm
   /usr/local/share/automake-1.15/Automake/Version.pm
   /usr/local/share/automake-1.15/Automake/Wrap.pm
   /usr/local/share/automake-1.15/Automake/XFile.pm
   /usr/local/share/automake-1.15/COPYING
   /usr/local/share/automake-1.15/INSTALL
   /usr/local/share/automake-1.15/am/check.am
   /usr/local/share/automake-1.15/am/check2.am
   /usr/local/share/automake-1.15/am/clean-hdr.am
   /usr/local/share/automake-1.15/am/clean.am
   /usr/local/share/automake-1.15/am/compile.am
   /usr/local/share/automake-1.15/am/configure.am
   /usr/local/share/automake-1.15/am/data.am
   /usr/local/share/automake-1.15/am/dejagnu.am
   /usr/local/share/automake-1.15/am/depend.am
   /usr/local/share/automake-1.15/am/depend2.am
   /usr/local/share/automake-1.15/am/distdir.am
   /usr/local/share/automake-1.15/am/footer.am
   /usr/local/share/automake-1.15/am/header-vars.am
   /usr/local/share/automake-1.15/am/header.am
   /usr/local/share/automake-1.15/am/inst-vars.am
   /usr/local/share/automake-1.15/am/install.am
   /usr/local/share/automake-1.15/am/java.am
   /usr/local/share/automake-1.15/am/lang-compile.am
   /usr/local/share/automake-1.15/am/lex.am
   /usr/local/share/automake-1.15/am/library.am
   /usr/local/share/automake-1.15/am/libs.am
   /usr/local/share/automake-1.15/am/libtool.am
   /usr/local/share/automake-1.15/am/lisp.am
   /usr/local/share/automake-1.15/am/ltlib.am
   /usr/local/share/automake-1.15/am/ltlibrary.am
   /usr/local/share/automake-1.15/am/mans-vars.am
   /usr/local/share/automake-1.15/am/mans.am
   /usr/local/share/automake-1.15/am/program.am
   /usr/local/share/automake-1.15/am/progs.am
   /usr/local/share/automake-1.15/am/python.am
   /usr/local/share/automake-1.15/am/remake-hdr.am
   /usr/local/share/automake-1.15/am/scripts.am
   /usr/local/share/automake-1.15/am/subdirs.am
   /usr/local/share/automake-1.15/am/tags.am
   /usr/local/share/automake-1.15/am/texi-vers.am
   /usr/local/share/automake-1.15/am/texibuild.am
   /usr/local/share/automake-1.15/am/texinfos.am
   /usr/local/share/automake-1.15/am/vala.am
   /usr/local/share/automake-1.15/am/yacc.am
   /usr/local/share/automake-1.15/ar-lib
   /usr/local/share/automake-1.15/compile
   /usr/local/share/automake-1.15/config.guess
   /usr/local/share/automake-1.15/config.sub
   /usr/local/share/automake-1.15/depcomp
   /usr/local/share/automake-1.15/install-sh
   /usr/local/share/automake-1.15/mdate-sh
   /usr/local/share/automake-1.15/missing
   /usr/local/share/automake-1.15/mkinstalldirs
   /usr/local/share/automake-1.15/py-compile
   /usr/local/share/automake-1.15/tap-driver.sh
   /usr/local/share/automake-1.15/test-driver
   /usr/local/share/automake-1.15/texinfo.tex
   /usr/local/share/automake-1.15/ylwrap
   /usr/local/share/doc/automake/amhello-1.0.tar.gz
   /usr/local/share/info/automake-history.info
   /usr/local/share/info/automake.info
   /usr/local/share/info/automake.info-1
   /usr/local/share/info/automake.info-2
   /usr/local/share/info/dir
   /usr/local/share/man/man1/aclocal-1.15.1
   /usr/local/share/man/man1/aclocal.1
   /usr/local/share/man/man1/automake-1.15.1
   /usr/local/share/man/man1/automake.1
%doc
 
%changelog
