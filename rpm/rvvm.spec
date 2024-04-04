%global rvvm_version 0.6
%global debug_package %{nil}
%global distribution %(grep -oP '(?<=^ID=).+' /etc/os-release | tr -d '"')

Name: rvvm
Version: %{rvvm_version}
Release: 1%{dist}
Summary: The RISC-V Virtual Machine

License: GPL-3.0-or-MPL-2.0
URL: https://github.com/LekKit/RVVM
Source0: https://github.com/LekKit/RVVM/archive/refs/tags/v%{rvvm_version}.tar.gz

BuildRequires: gcc make
BuildRequires: pkgconfig(sdl2)
Requires: SDL2

%description
RVVM is a RISC-V CPU and system software implementation written in C. It boasts
full compatibility with the RV64IMAFDC instruction set, supporting both RV32
and RV64 architectures, as well as SMP. Notable features include a fast blazing
JIT compiler, U-Boot compatibility, and robust support for multiple operating
systems including Linux, FreeBSD, and Haiku. Additionally, RVVM supports various
real devices instead of virtual ones, providing enhanced versatility for
development and testing.

%package -n librvvm
Summary: Dynamic and static library for the RVVM

%description -n librvvm
This package contains libraries shared between applications
using RVVM.

%package devel
Summary: Header files and libraries for the RVVM
Requires: librvvm = %{version}-%{release}

%description devel
This package contains headerfiles and libraries which are needed to
build applications using RVVM.

%prep
rm -rf RVVM-%{rvvm_version}
tar -xzf %{SOURCE0}
%setup -n RVVM-%{rvvm_version} -T -D

%build
%make_build lib all BINARY=rvvm GIT_COMMIT=%{distribution} USE_SDL=2

%install
%make_install PREFIX="%{_prefix}" libdir=%{_libdir} BINARY=rvvm GIT_COMMIT=%{distribution} USE_SDL=2

%files
%{_bindir}/%{name}
%{_datadir}/licenses/%{name}/*

%files devel
%{_includedir}/%{name}/*

%files -n librvvm
%{_libdir}/*%{name}*

%changelog
* Sun Mar 31 2024 000exploit <illialoo99+rpm@gmail.com> - 0.6-1
- Initial release for RPM-enabled systems
