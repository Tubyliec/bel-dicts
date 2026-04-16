Name:           bel-dicts
Version:        0.1
Release:        1%{?dist}
Summary:        Belarusian dictionaries for Hunspell
License:        GPL-3.0-or-later
BuildArch:      noarch
Source0: %{name}-%{version}.tar

Requires:       hunspell

%description
Belarusian dictionaries (be-BY) for Hunspell.

%prep
%autosetup -n bel-dicts-%{version}

%build
ls -R

%install
mkdir -p %{buildroot}/usr/share/hunspell

if [ -f dict/be-BY.aff ]; then
    install -m 644 dict/be-BY.aff %{buildroot}/usr/share/hunspell/
    install -m 644 dict/be-BY.dic %{buildroot}/usr/share/hunspell/
else
    install -m 644 bel-dicts/dict/be-BY.aff %{buildroot}/usr/share/hunspell/
    install -m 644 bel-dicts/dict/be-BY.dic %{buildroot}/usr/share/hunspell/
fi

%post
if [ -d %{_datadir}/myspell/dicts ]; then
    ln -sf ../../hunspell/be-BY.aff %{_datadir}/myspell/dicts/be-BY.aff
    ln -sf ../../hunspell/be-BY.dic %{_datadir}/myspell/dicts/be-BY.dic
fi

%postun
if [ $1 -eq 0 ]; then
    rm -f %{_datadir}/myspell/dicts/be-BY.aff
    rm -f %{_datadir}/myspell/dicts/be-BY.dic
fi

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/hunspell
%{_datadir}/hunspell/be-BY.aff
%{_datadir}/hunspell/be-BY.dic

%changelog
* Wed Apr 15 2026 tubyliec <antikruk@vivaldi.net> - 0
- see git log