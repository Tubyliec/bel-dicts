Name:           bel-dicts
Version:        0.6.7
Release:        0%{?dist}
Summary:        Belarusian dictionaries for Hunspell and Myspell
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
Group:          Productivity/Text/Utilities
URL:            https://github.com/tubyliec/bel-dicts
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?fedora} || 0%{?rhel}
Requires:       hunspell
%endif

%if 0%{?suse_version}
Requires:       hunspell
Requires:       myspell-data
Supplements:    hunspell
%endif

%description
Belarusian hunspell dictionaries (affix and dictionary files)
for spell-checking in applications like LibreOffice, Firefox, etc.

%prep
%setup -q

%build
# No build required for data files

%install
install -d %{buildroot}%{_datadir}/hunspell
install -d %{buildroot}%{_datadir}/myspell/dicts

install -m 0644 dict/be-BY.aff %{buildroot}%{_datadir}/hunspell/be-BY.aff
install -m 0644 dict/be-BY.dic %{buildroot}%{_datadir}/hunspell/be-BY.dic

# Symlinks for myspell compatibility
ln -sf %{_datadir}/hunspell/be-BY.aff %{buildroot}%{_datadir}/myspell/dicts/be-BY.aff
ln -sf %{_datadir}/hunspell/be-BY.dic %{buildroot}%{_datadir}/myspell/dicts/be-BY.dic

%files
%license LICENSE
%doc README.md
%{_datadir}/hunspell/be-BY.aff
%{_datadir}/hunspell/be-BY.dic
%{_datadir}/myspell/dicts/be-BY.aff
%{_datadir}/myspell/dicts/be-BY.dic

%changelog
