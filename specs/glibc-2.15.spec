Name:           glibc
Version:        2.15
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://ftp.gnu.org
Source0:        http://ftp.gnu.org/gnu/glibc/glibc-2.15.tar.gz
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
--prefix=%{prefix}

make %{?_smp_mflags}

%install
make install

%files
 
%doc
 
%changelog
