Name: 		swayidle
Version:	1.2
Release:	0%{?dist}
Summary:	Idle management daemon for Wayland

License:	MIT
URL:		https://github.com/swaywm/swayidle
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	scdoc
BuildRequires:	systemd-devel
BuildRequires:	cmake

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
%{_bindir}/swayidle
%{_mandir}/man1/swayidle.1.gz

%changelog

