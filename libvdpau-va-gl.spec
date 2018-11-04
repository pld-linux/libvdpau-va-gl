Summary:	VDPAU driver with OpenGL/VAAPI backend
Summary(pl.UTF-8):	Sterownik VDPAU z backendem OpenGL/VAAPI
Name:		libvdpau-va-gl
Version:	0.4.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://github.com/i-rinat/libvdpau-va-gl/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8db21dcfd5cd14c6ec51b992e20369dc
URL:		https://github.com/i-rinat/libvdpau-va-gl
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	cmake >= 2.8.8
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libva-x11-devel
BuildRequires:	libvdpau-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDPAU driver with OpenGL/VAAPI backend.

%description -l pl.UTF-8
Sterownik VDPAU z backendem OpenGL/VAAPI.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DLIB_INSTALL_DIR:PATH=%{_libdir}/vdpau

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/vdpau/libvdpau_va_gl.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README.md doc/known-issues.md
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_va_gl.so.1
