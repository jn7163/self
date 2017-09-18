Name:           mpfr
Version:        3.1.4
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://gcc.gnu.org
Source0:        http://mirrors.ustc.edu.cn/gnu/mpfr/mpfr-3.1.4.tar.bz2
Source1:        http://mirrors.ustc.edu.cn/gnu/gmp/gmp-6.1.0.tar.bz2
#BuildRequires:  gcc
#Requires:       gcc, automake, autoconf
BuildRoot:      %_topdir/BUILDROOT
Prefix:         /opt/%{name}-%{version}

%description

%prep

%setup -q
tar -xjvf %_topdir/SOURCES/gmp-6.1.0.tar.bz2 -C %_topdir/BUILD/
%build
./configure \
--prefix=%{prefix} \
--with-gmp=%_topdir/BUILD/gmp-6.1.0

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
 
%doc
 
%changelog
