%global debug_package %{nil}
%global real_version 12.0.1.1105_p3

Summary:	Firmware for Broadcom WIDCOMM Bluetooth devices
Name:		broadcom-bt-firmware
Version:	%(echo %real_version | tr '_' '.')
Release:	1%{?dist}
License:	WIDCOMM Bluetooth Software
URL:		https://github.com/winterheart/broadcom-bt-firmware
BuildArch:  noarch

Source0:	https://github.com/winterheart/broadcom-bt-firmware/archive/refs/tags/v%{real_version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/farena/broadcom-bt-firmware/master/brcm/BCM43142A0-14e4-4365.hcd

Requires:   linux-firmware

%description
This package intentended to provide firmware of Broadcom WIDCOMM® Bluetooth
devices (including BCM20702, BCM20703, BCM43142 chipsets and other) for Linux
kernel. Since February 2017, Broadcom ships their drivers directly to Windows
Update service.

Recently several vulnerabilities have been discovered in the Bluetooth stack
such as CVE-2018-5383, CVE-2019-9506 (KNOB), CVE-2020-10135 (BIAS) and more.
Since Broadcom has stopped active support for its consumer devices, your system
may be subject to security risks.

%prep
%autosetup -n %{name}-%{real_version}

%install
mkdir -p %{buildroot}%{_prefix}/lib/firmware/brcm/
install -m 644 brcm/* %{buildroot}%{_prefix}/lib/firmware/brcm/

%files
%license LICENSE.broadcom_bcm20702 LICENSE.MIT.txt
%doc README.md
%{_prefix}/lib/firmware/brcm/*

%changelog
* Fri Oct 01 2021 Simone Caronni <negativo17@gmail.com> - 12.0.1.1105.p3-1
- First build.
