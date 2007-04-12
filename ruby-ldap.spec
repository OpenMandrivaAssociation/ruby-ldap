%define rname ldap
%define name ruby-%{rname}
%define version 0.9.7
%define release %mkrel 1

Summary: Ruby extension library for accessing LDAP API
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://ruby-ldap.sourceforge.net/
Source0: http://ovh.dl.sourceforge.net/sourceforge/ruby-ldap/ruby-%{rname}-%{version}.tar.bz2
License: BSD-like
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.8
BuildRequires: ruby-devel openldap-devel

%description
Ruby/LDAP is an extension module for ruby, it provides the interface to some
LDAP libraries (for example, OpenLDAP, UMich LDAP, Netscape SDK,
ActiveDirectory). The common API for application developments is described in
RFC1823, Most of libraries comply with it.
This package is build with OpenLDAP2.

%prep
%setup -q 

%build
ruby extconf.rb
make
chmod 0644 test/*.rb
chmod 0755 example/cgi/search.cgi

%install
rm -rf %buildroot
%makeinstall

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/*
%{ruby_sitearchdir}/*.so
%doc COPYING README FAQ ChangeLog example/ test/

