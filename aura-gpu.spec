%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     aura-gpu
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  i2c driver for AURA capable GPUs
License:  GPLv2
URL:      https://github.com/KyleGospo/aura-gpu-dkms

Source:   %{url}/archive/refs/heads/master.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
i2c driver for AURA capable GPUs

%prep
%setup -q -c aura-gpu-dkms-master

%files
%doc aura-gpu-dkms-master/README.md
%license aura-gpu-dkms-master/LICENSE

%changelog
{{{ git_dir_changelog }}}
