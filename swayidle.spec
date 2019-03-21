Name: 		swayidle
Version:	1.2
Release:	1.2%{?dist}
Summary:	Idle management daemon for Wayland

License:	MIT
URL:		https://github.com/swaywm/swayidle
Source0:	%{url}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?gitver}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
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
%{_bindir}/swayidle
%{_mandir}/man1/swayidle.1.gz

%changelog

