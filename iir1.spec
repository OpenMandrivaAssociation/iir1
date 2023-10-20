%define major 1
%define libname %mklibname iir
%define devname %mklibname iir -d
%define git 20231020

Name: iir1
Version: 1.9.5
Release: %{?git:0.%{git}.}1
Source0: https://github.com/berndporr/iir1/archive/refs/heads/master.tar.gz
Summary: DSP IIR realtime filter library
URL: https://github.com/iir1/iir1
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja

%description
An infinite impulse response (IIR) filter library which implements
Butterworth, RBJ, Chebychev filters.

%package -n %{libname}
Summary: IIR (infinite impulse response) filter library
Group: System/Libraries

%description -n %{libname}
An infinite impulse response (IIR) filter library which implements
Butterworth, RBJ, Chebychev filters.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

An infinite impulse response (IIR) filter library which implements
Butterworth, RBJ, Chebychev filters.

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
