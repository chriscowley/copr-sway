Name: 		swaylock
Version:	1.3
Release:	1.3%{?dist}
Summary:	Screen locker for Wayland

License:	MIT
URL:		https://github.com/swaywm/swaylock
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	cairo-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	pam-devel
BuildRequires:	libxkb
BuildRequires:	scdoc

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
%{_bindir}/swaylock
%{_mandir}/man1/swaylock.1.gz

%changelog

