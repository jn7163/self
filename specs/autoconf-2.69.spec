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
 
%doc
 
%changelog
