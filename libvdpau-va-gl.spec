Summary:	VDPAU driver with OpenGL/VAAPI backend
Summary(pl.UTF-8):	Sterownik VDPAU z backendem OpenGL/VAAPI
Name:		libvdpau-va-gl
Version:	0.3.1
Release:	1
License:	LGPL v3
Group:		X11/Libraries
Source0:	https://github.com/i-rinat/libvdpau-va-gl/archive/v%{version}.tar.gz
# Source0-md5:	2ec5c68282aac9720525e16e858cd599
URL:		https://github.com/i-rinat/libvdpau-va-gl
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	cmake >= 2.6
# libswscale
BuildRequires:	ffmpeg-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libva-glx-devel
BuildRequires:	libvdpau-devel
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
%cmake \
	-DLIB_INSTALL_DIR:PATH=%{_libdir}/vdpau \
	..

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
%doc ChangeLog README.md
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_va_gl.so.1
