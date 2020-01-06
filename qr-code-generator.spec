%global richname QR-Code-generator

Name: qr-code-generator
Version: 1.5.0
Release: 1%{?dist}

License: MIT
Summary: High-quality QR Code generator library
URL: https://github.com/nayuki/%{richname}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Backported upstream patch with some modifications.
Patch100: %{name}-build-fixes.patch

BuildRequires: gcc-c++
BuildRequires: gcc

%description
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegen
Summary: High-quality QR Code generator library (plain C version)

%description -n libqrcodegen
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegen-devel
Summary: Development files for libqrcodegen
Requires: libqrcodegen%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libqrcodegen-devel
Development files and headers for high-quality QR Code generator library
(plain C version).

%package -n libqrcodegencpp
Summary: High-quality QR Code generator library (C++ version)

%description -n libqrcodegencpp
This project aims to be the best, clearest QR Code generator library in
multiple languages.

The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation
comments.

%package -n libqrcodegencpp-devel
Summary: Development files for libqrcodegencpp
Requires: libqrcodegencpp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n libqrcodegencpp-devel
Development files and headers for high-quality QR Code generator library
(C++ version).

%prep
%autosetup -n %{richname}-%{version} -p1

%build
# Exporting correct build flags...
%set_build_flags

# Building plain C version...
pushd c
%make_build
popd

# Building C++ version...
pushd cpp
%make_build
popd

%install
# Installing plain C version...
pushd c
%make_install LIBDIR=%{buildroot}%{_libdir} INCLUDEDIR=%{buildroot}%{_includedir}/qrcodegen
popd

# Installing C++ version...
pushd cpp
%make_install LIBDIR=%{buildroot}%{_libdir} INCLUDEDIR=%{buildroot}%{_includedir}/qrcodegencpp
popd

%files -n libqrcodegen
%license Readme.markdown
%{_libdir}/libqrcodegen.so.*

%files -n libqrcodegen-devel
%{_includedir}/qrcodegen
%{_libdir}/libqrcodegen.so

%files -n libqrcodegencpp
%license Readme.markdown
%{_libdir}/libqrcodegencpp.so.*

%files -n libqrcodegencpp-devel
%{_includedir}/qrcodegencpp
%{_libdir}/libqrcodegencpp.so

%changelog
* Mon Jan 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.0-1
- Initial SPEC release.
