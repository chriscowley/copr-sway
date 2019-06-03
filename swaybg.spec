Name: 		swaybg
Version:	1.0
Release:	0%{?dist}
Summary:	Wallpaper tool for Wayland compositors

License:	MIT
URL:		https://github.com/swaywm/swaybg
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
%{_bindir}/swaybg
%{_mandir}/man1/swaygb.1.gz
/usr/share/bash-completion/completions/swaybg
/usr/share/fish/completions/swaybg.fish
/usr/share/zsh/site-functions/_swaybg

%changelog

