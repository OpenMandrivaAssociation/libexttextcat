%define lname	exttextcat
%define api	2.0
%define major	0
%define libname %mklibname %{lname} %{api} %{major}
%define devname %mklibname %{lname} %{api} -d

Summary:	Text categorization library
Name:		libexttextcat
Version:	3.4.5
Release:	1
Group:		System/Libraries
License:	BSD
Url:		http://www.freedesktop.org/wiki/Software/libexttextcat
Source0:	http://dev-www.libreoffice.org/src/libexttextcat/%{name}-%{version}.tar.xz
BuildRequires: libtool

%description
%{name} is an N-Gram-Based Text Categorization library primarily
intended for language guessing.

%package -n	%{libname}
Summary:	Text categorization library
Group:		System/Libraries
Requires:	%{name}-data >= %{version}
Provides:	libexttextcat = %{version}-%{release}

%description -n	%{libname}
%{name} is an N-Gram-Based Text Categorization library primarily
intended for language guessing.

%package -n	%{devname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Development files and headers for %{name}.

%package tools
Summary:	Tool for creating custom document fingerprints
Group:		Publishing

%description tools
The %{name}-tools package contains the createfp program that allows
you to easily create your own document fingerprints.

%package data
Summary:	Data files for text categorization library
Group:		System/Libraries

%description data
Data files for %{name}.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -Qunused-arguments"
export CXXFLAGS="%{optflags} -Qunused-arguments"

%configure

%make

%check
make check

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libexttextcat-2.0.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_libdir}/*.so
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/libexttextcat.vapi

%files tools
%{_bindir}/createfp

%files data
%doc LICENSE README*
%{_datadir}/%{name}

