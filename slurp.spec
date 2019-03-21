Name: 		Slurp
Version:	1.1
Release:	1.1%{?dist}
Summary:	Select a region in a Wayland compositor and print it to the standard output. 

License:	MIT
URL:		https://github.com/emersion/slurp
Source0:	%{url}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?gitver}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	cairo-devel
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
%{_bindir}/slurp
%{_mandir}/man1/slurp.1.gz

%changelog

