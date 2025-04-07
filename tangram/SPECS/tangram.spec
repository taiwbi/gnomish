Name:           tangram
Version:        3.3
Release:        1%{?dist}
Summary:        Browser for your pinned tabs
License:        GPL-3.0-only
URL:            https://apps.gnome.org/Tangram/
Source0:        https://github.com/sonnyp/Tangram/archive/v%{version}/Tangram-%{version}.tar.gz
# Patch to fix gettext domain
Patch0:         tangram-gettext.patch

BuildArch:      noarch
BuildRequires:  meson
BuildRequires:  git
BuildRequires:  blueprint-compiler
BuildRequires:  appstream
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  gjs-devel
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel

Requires:       gdk-pixbuf2
Requires:       gjs
Requires:       glib2
Requires:       gstreamer1
Requires:       gtk4
Requires:       hicolor-icon-theme
Requires:       libadwaita
Requires:       libsoup3
Requires:       webkitgtk6.0

%description
Tangram is a GNOME app to organize your web apps and pinned tabs.

%prep
%autosetup -p1 -n Tangram-%{version}

# Clone the troll submodule properly
mkdir -p troll
curl -L https://github.com/sonnyp/troll/archive/refs/heads/main.tar.gz | tar xz --strip-components=1 -C troll

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

# Create symbolic link for binary
ln -s re.sonny.Tangram %{buildroot}%{_bindir}/tangram

%files
%license COPYING
%doc README.md
%{_bindir}/tangram
%{_bindir}/re.sonny.Tangram
%{_datadir}/applications/re.sonny.Tangram.desktop
%{_datadir}/glib-2.0/schemas/re.sonny.Tangram.gschema.xml
%{_datadir}/icons/hicolor/*/apps/re.sonny.Tangram*
%{_datadir}/locale/*/LC_MESSAGES/re.sonny.Tangram.mo
%{_datadir}/metainfo/re.sonny.Tangram.metainfo.xml
%{_datadir}/re.sonny.Tangram/
%{_datadir}/dbus-1/services/re.sonny.Tangram.service

%changelog
* Mon Apr 07 2025 Taiwbi <taiwbii@proton.me> - 3.3-1
- Initial package
