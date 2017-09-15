Name:           gcc
Version:        7.2.0
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://gcc.gnu.org
Source0:        http://mirrors.ustc.edu.cn/gnu/gcc/gcc-7.2.0/gcc-7.2.0.tar.gz
#BuildRequires:  gcc
#Requires:       gcc, automake, autoconf
BuildRoot:      %_topdir/BUILDROOT
Prefix:         /opt/test/%{name}-%{version}

%description

%prep

%setup -q

%build
##mkdir %_topdir/BUILD/
##cd 
../configure \
--prefix=%{prefix} \
-enable-threads=posix \
-enable-languages=c,c++ \
-disable-multilib \
--with-gmp=/opt/gmp-6.1.0 \
--with-mpfr=/opt/mpfr-3.1.4 \
--with-mpc=/opt/mpc-1.0.3 \
--with-isl=/opt/isl-0.16.1

make %{?_smp_mflags}

%install
make install

%files
 
%doc
 
%changelog
