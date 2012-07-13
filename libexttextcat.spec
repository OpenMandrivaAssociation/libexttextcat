%define lname exttextcat
%define major 0
%define libname %mklibname %{lname} %{major}
%define develname %mklibname %{lname} -d

Summary:	Text categorization library
Name:		libexttextcat
Version:	3.3.1
Release:	2
Group:		System/Libraries
License:	BSD
URL:		http://www.freedesktop.org/wiki/Software/libexttextcat
Source0:	http://dev-www.libreoffice.org/src/libexttextcat/%{name}-%{version}.tar.xz
BuildRequires: autoconf automake libtool

%description
%{name} is an N-Gram-Based Text Categorization library primarily
intended for language guessing.

%package -n	%{libname}
Summary:	Text categorization library
Group:		System/Libraries

%description -n	%{libname}
%{name} is an N-Gram-Based Text Categorization library primarily
intended for language guessing.


%package -n	%{develname}
Summary:	Development files and headers for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{lname}-devel = %{version}-%{release}
Provides:	textcat-devel = %{version}-%{release}
Obsoletes:	%{mklibname textcat -d} < 3.3.1
Provides:	%{mklibname textcat -d} = %{version}

%description -n	%{develname}
Development files and headers for %{name}.

%package	tools
Summary:	Tool for creating custom document fingerprints
Group:		Publishing
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{mklibname textcat -d} < 3.3.1

%description	tools
The %{name}-tools package contains the createfp program that allows
you to easily create your own document fingerprints.


%prep

%setup -q

%build
mkdir -p m4
autoreconf -fi
%configure2_5x \
    --disable-static \

%make

%check
make check

%install

%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc LICENSE README*
%{_libdir}/lib*.so.%{major}*
%{_datadir}/%{name}

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_libdir}/*.so
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/libexttextcat.vapi

%files tools
%{_bindir}/createfp
