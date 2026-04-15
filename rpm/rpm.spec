Name:           bel-dicts
Version:        0.1
Release:        1%{?dist}
Summary:        Belarusian dictionaries for Hunspell
License:        GPL-3.0-or-later
BuildArch:      noarch

Requires:       hunspell

%description
Belarusian dictionaries (be-BY) for Hunspell.

%prep
# Handle both tarball (from tar service) and direct source scenarios
if [ -f %{_sourcedir}/%{name}-%{version}.tar.* ]; then
    %setup -q
else
    # For obs_scm without tar service, work directly with sources
    cd %{_sourcedir}
    if [ ! -d dict ]; then
        if [ -d %{name}-%{version} ]; then
            cp -r %{name}-%{version}/dict . 2>/dev/null || true
        elif [ -d bel-dicts-* ]; then
            cp -r bel-dicts-*/dict . 2>/dev/null || true
        fi
    fi
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
%{_datadir}/hunspell/be-BY.aff
%{_datadir}/hunspell/be-BY.dic

%changelog
* Wed Apr 15 2026 tubyliec <antikruk@vivaldi.net> - 0.1-1
- Update dictionaries
