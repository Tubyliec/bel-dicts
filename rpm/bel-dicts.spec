Name:           bel-dicts
Version:        0.1
Release:        1%{?dist}
Summary:        Belarusian dictionaries for Hunspell
License:        GPL-3.0-or-later
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

Requires:       hunspell

%description
Belarusian dictionaries (be-BY) for Hunspell.

%prep
# Extract the tarball created by tar service at buildtime
%setup -q
# Ensure dict directory exists
if [ ! -d dict ]; then
    mkdir -p dict
fi

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/hunspell

install -m 644 dict/be-BY.aff %{buildroot}%{_datadir}/hunspell/
install -m 644 dict/be-BY.dic %{buildroot}%{_datadir}/hunspell/

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
* Wed Apr 15 2026 tubyliec <antikruk@vivaldi.net> - 0.1
- Update dictionaries
