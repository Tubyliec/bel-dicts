Name:           bel-dicts
Version:        0.5.2
Release:        1%{?dist}
Summary:        Belarusian dictionary for Hunspell
License:        LGPL-2.1+
URL:            https://github.com/tubyliec/bel-dicts
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?fedora} || 0%{?rhel}
Requires:       hunspell
%endif

%if 0%{?suse_version}
Requires:       hunspell
Supplements:    hunspell
%endif

%description
Hunspell spell-checking dictionary for the Belarusian language (be-BY).
Includes affix rules (.aff) and word list (.dic) for use with Hunspell,
LibreOffice, Firefox, Thunderbird, and other Hunspell-based applications.

%prep
%autosetup

%install
install -d %{buildroot}%{_datadir}/hunspell
install -m 644 dict/be-BY.aff %{buildroot}%{_datadir}/hunspell/be-BY.aff
install -m 644 dict/be-BY.dic %{buildroot}%{_datadir}/hunspell/be-BY.dic

install -d %{buildroot}%{_datadir}/myspell/dicts
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
* Sat Apr 12 2026 tubyliec <antikruk@vivaldi.net> - 0.5.2
- Initial release
