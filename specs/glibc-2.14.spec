Name:           glibc
Version:        2.14
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://ftp.gnu.org
Source0:        http://ftp.gnu.org/gnu/glibc/glibc-2.14.tar.gz
#BuildRequires:  gcc
#Requires:       gcc, automake, autoconf
BuildRoot:      %_topdir/BUILDROOT
Prefix:         /opt/test/%{name}-%{version}

%description

%prep

%setup -q

%build
mkdir %_topdir/BUILD/%{name}-%{version}/test
cd %_topdir/BUILD/%{name}-%{version}/test
../configure \
--prefix=%{prefix}

make %{?_smp_mflags}

%install
cd %_topdir/BUILD/%{name}-%{version}/test
make install DESTDIR=%{buildroot}

%files
 
%doc
 
%changelog
