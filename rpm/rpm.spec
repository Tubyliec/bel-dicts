Name:           bel-dicts
Version:        0.6.5
Release:        0%{?dist}
Summary:        Belarusian dictionaries for Hunspell and Myspell
License:        GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
Group:          Productivity/Text/Utilities
URL:            https://github.com/tubyliec/bel-dicts
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Belarusian hunspell dictionaries (affix and dictionary files) 
for spell-checking in applications like LibreOffice, Firefox, etc.

%prep
%setup -q

%build
# No build required for data files

%install
# Create directory structure
install -d %{buildroot}%{_datadir}/hunspell
install -d %{buildroot}%{_datadir}/myspell/dicts

# Install dictionary files
install -m 0644 dict/be-BY.aff %{buildroot}%{_datadir}/hunspell/be-BY.aff
install -m 0644 dict/be-BY.dic %{buildroot}%{_datadir}/hunspell/be-BY.dic

# Create symlinks for myspell compatibility
ln -sf %{_datadir}/hunspell/be-BY.aff %{buildroot}%{_datadir}/myspell/dicts/be-BY.aff
ln -sf %{_datadir}/hunspell/be-BY.dic %{buildroot}%{_datadir}/myspell/dicts/be-BY.dic

%files
%license LICENSE
%doc README.md
# Explicit directory ownership to satisfy openSUSE build checks
%dir %{_datadir}/hunspell
%dir %{_datadir}/myspell
%dir %{_datadir}/myspell/dicts
# Files and symlinks
%{_datadir}/hunspell/be-BY.aff
%{_datadir}/hunspell/be-BY.dic
%{_datadir}/myspell/dicts/be-BY.aff
%{_datadir}/myspell/dicts/be-BY.dic

%changelog
* Wed Apr 15 2026 tubyliec <antikruk@vivaldi.net> - 0.6.5
- Update to version 0.6.5
- Fix directory ownership for openSUSE compatibility

* Sun Apr 12 2026 tubyliec <antikruk@vivaldi.net> - 0.5.2
- Initial release for version 0.5.2
- Fix bogus date in changelog
