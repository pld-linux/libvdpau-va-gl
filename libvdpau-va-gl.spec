Summary:	VDPAU driver with OpenGL/VAAPI backend
Name:		libvdpau-va-gl
Version:	0.1.0
Release:	1
License:	LGPL v3
Group:		X11/Libraries
Source0:	https://github.com/i-rinat/libvdpau-va-gl/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	cd56ad6ca1b69986c25a6fe6f608123f
Patch0:		%{name}-link.patch
URL:		https://github.com/i-rinat/libvdpau-va-gl
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	cmake >= 2.6
BuildRequires:	ffmpeg-devel
BuildRequires:	glib2-devel
BuildRequires:	libva-glx-devel
BuildRequires:	libvdpau-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VDPAU driver with OpenGL/VAAPI backend.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
	-DLIB_INSTALL_DIR:PATH=%{_libdir}/vdpau

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/vdpau/libvdpau_va_gl.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_libdir}/vdpau/libvdpau_va_gl.so.1
