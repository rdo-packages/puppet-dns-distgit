%{!?upstream_version: %global upstream_version %{commit}}

%define upstream_name puppet-dns
%global commit 820cb719907aac3eb7e28a506eac72a236f846e3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:                   puppet-dns
Version:                8.0.0
Release:                1%{?alphatag}%{?dist}
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
* Tue Sep 29 2020 RDO <dev@lists.rdoproject.org> 8.0.0-1.820cb71git
- Update to post 8.0.0 (820cb719907aac3eb7e28a506eac72a236f846e3)


