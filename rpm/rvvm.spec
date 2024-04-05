%global debug_package %nil
%define debug %nil
%global distribution %(grep -oP '(?<=^ID=).+' /etc/os-release | tr -d '"')

Name: rvvm
Version: 0.6
Release: 1%{dist}
Summary: The RISC-V Virtual Machine

License: GPLv3 or MPL 2.0
URL: https://github.com/LekKit/RVVM
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Group: Emulators

BuildRequires:	gcc make
BuildRequires:	pkgconfig(sdl2)
Requires: SDL2

%description
RVVM is a RISC-V CPU and system software implementation 
written in C. It boasts full compatibility with the 
RV64IMAFDC instruction set, supporting both RV32 and RV64
architectures, as well as SMP. Notable features include a
fast blazing JIT compiler, U-Boot compatibility, and
robust support for multiple operating systems including
Linux, FreeBSD, and Haiku. Additionally, RVVM supports
various real devices instead of virtual ones, providing
enhanced versatility for development and testing.

%package -n librvvm
Summary: Dynamic and static library for the RVVM

%description -n librvvm
This package contains libraries shared between applications
using RVVM.

%package devel
Summary: Development and include files for %{name}
Group: Development/C
Requires: librvvm = %{version}-%{release}

%description devel
This package contains headerfiles and libraries which are needed to
build applications using RVVM.

%prep
%setup -qn RVVM-%{version}

%build
%make_build lib all BINARY=rvvm GIT_COMMIT=%{distribution} USE_SDL=2

%install
%makeinstall BINARY=rvvm GIT_COMMIT=%{distribution} USE_SDL=2

# clean.
rm -rf %{buildroot}%{_datadir}/licenses/%{name}/*

%files
%{_bindir}/%{name}
%doc README.md LICENSE*

%files devel
%{_includedir}/%{name}/*

%files -n librvvm
%{_libdir}/*%{name}*

%changelog
* Fri Apr 5 2024 000exploit <illialoo99+rpm@gmail.com> - 0.6-1
- Some fixes from ROSA Linux (by djam)

* Sun Mar 31 2024 000exploit <illialoo99+rpm@gmail.com> - 0.6-1
- Initial release for RPM-enabled systems
