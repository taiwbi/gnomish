%global commit 8b0275948eedec9ed0378f9bdda1aa4aac3062ba
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           troll
Version:        0.1
Release:        1%{?dist}
Summary:        Troll GJS library
License:        ISC
URL:            https://github.com/sonnyp/troll
Source0:        https://github.com/sonnyp/troll/archive/%{commit}.zip
BuildArch:      noarch

# Build dependencies
BuildRequires:  nodejs
BuildRequires:  npm
# Runtime dependencies
Requires:       gjs

%description
troll is an implementation of common JavaScript APIs for gjs and some helpers.

%prep
%autosetup -n %{name}-%{commit}

%build
npm install
./node_modules/.bin/rollup -c rollup.config.js

%install
# Create directories
mkdir -p %{buildroot}%{_datadir}/gjs-1.0/troll/
mkdir -p %{buildroot}%{_datadir}/doc/%{name}

# Install library files
cp -a src/ %{buildroot}%{_datadir}/gjs-1.0/troll/
cp -a dist/ %{buildroot}%{_datadir}/gjs-1.0/troll/

# Install documentation
cp -a README.md %{buildroot}%{_datadir}/doc/%{name}/
cp -a LICENSE %{buildroot}%{_datadir}/doc/%{name}/

%files
%license LICENSE
%doc README.md
%{_datadir}/gjs-1.0/troll/
%{_datadir}/doc/%{name}/

%changelog
* Mon Apr 07 2025 Taiwbi <taiwbii@proton.me> - 0.1-1
- Initial package
