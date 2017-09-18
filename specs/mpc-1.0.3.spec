Name:           mpc
Version:        1.0.3
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://gcc.gnu.org
Source0:        http://mirrors.ustc.edu.cn/gnu/mpc/mpc-1.0.3.tar.gz
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
--with-gmp=/opt/gmp-6.1.0 \
--with-mpfr=/opt/mpfr-3.1.4

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
 
%doc
 
%changelog
