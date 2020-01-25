%define		php_min_version 5.3.0
Summary:	PHP-JWT
Name:		php-firebase-jwt
Version:	4.0.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/firebase/php-jwt/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f71111383e4b366d9752a4815269a589
URL:		https://github.com/firebase/php-jwt
%if %{with phpdeps}
BuildRequires:	/usr/bin/php
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
%endif
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= %{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple library to encode and decode JSON Web Tokens (JWT) in PHP,
conforming to RFC 7519.

%prep
%setup -q -n php-jwt-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Firebase/JWT
cp -a src/* $RPM_BUILD_ROOT%{php_data_dir}/Firebase/JWT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{php_data_dir}/Firebase
%{php_data_dir}/Firebase/JWT
