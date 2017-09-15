Name:           mpfr
Version:        3.1.4
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://gcc.gnu.org
Source0:        http://mirrors.ustc.edu.cn/gnu/mpfr/mpfr-3.1.4.tar.bz2
#BuildRequires:  gcc
#Requires:       gcc, automake, autoconf
BuildRoot:      %_topdir/BUILDROOT
Prefix:         /opt/test/%{name}-%{version}

%description

%prep

%setup -q

%build
./configure \
--prefix=%{prefix} \
--with-gmp=/opt/gmp-6.1.0

make %{?_smp_mflags}

%install
make install

%files
 
%doc
 
%changelog
