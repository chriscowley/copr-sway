Name: Grim
Version:	1.1
Release:	1.1%{?dist}
Summary:	Grab images from a Wayland compositor.

License:	MIT
URL:		https://github.com/emersion/grim
Source0:	%{url}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?gitver}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	cairo-devel
BuildRequires:	pango-devel
BuildRequires:	scdoc
BuildRequires:	libjpeg-turbo-devel

%description
%{summary}

%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install


%files
%doc
%license LICENSE
%{_bindir}/grim
%{_mandir}/man1/grim.1.gz

%changelog

