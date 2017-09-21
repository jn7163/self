Name:           Python
Version:        3.6.2
Release:        1%{?dist}
Summary:        Test
Group:          Test
License:        No
URL:            http://gcc.gnu.org
Source0:        Python-3.6.2.tar.xz
#BuildRequires:  gcc
#Requires:       gcc, automake, autoconf
BuildRoot:      %_topdir/BUILDROOT
Prefix:         /opt/%{name}-%{version}

%description

%prep

%setup -q

%build
./configure --enable-optimizations
sed -i 's/#zlib zlibmodul/zlib zlibmodul/g' /root/Python-3.6.2/Modules/Setup
sed -i '209,212s/#//g' /root/Python-3.6.2/Modules/Setup

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files

%doc
 
%changelog
