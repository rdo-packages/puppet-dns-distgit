%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name puppet-dns
%global commit d0c02af491cc2341607ca4bb068115ffc1eb0565
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:                   puppet-dns
Version:        5.0.1
Release:        1%{?alphatag}%{?dist}
Summary:                Manage the ISC BIND daemon
License:                Apache-2.0

URL:                    https://github.com/theforeman/puppet-dns

Source0:                https://github.com/theforeman/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:              noarch

Requires:               puppet-concat
Requires:               puppet-stdlib

Requires:               puppet >= 2.7.0

%description
Puppet module for configuring the ISC BIND server for Foreman.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/dns/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/dns/



%files
%{_datadir}/openstack-puppet/modules/dns/


%changelog
* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 5.0.1-1.d0c02afgit
- Pike update 5.0.1 (d0c02af491cc2341607ca4bb068115ffc1eb0565)

