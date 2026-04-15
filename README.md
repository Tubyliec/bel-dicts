# bel-dicts — Беларускі слоўнік для Hunspell

Слоўнік для [Hunspell](https://hunspell.github.io/).

Слоўнік створаны для сродку правярання арфаграфіі ад [МТГ «RэЗервацыЯ»](https://spell.by-reservation.com).
Бягучая версія: **0.5.2**

Створана з дапамогай [Корпусу беларускай мовы](https://bnkorpus.info/).

---

## Усталяванне

### openSUSE

```bash
sudo zypper addrepo https://download.opensuse.org/repositories/home:tubyliec:bel-dicts/openSUSE_Tumbleweed/home:tubyliec:bel-dicts.repo
sudo zypper install bel-dicts
```

### Ubuntu / Debian / KDE Neon

```bash
echo "deb https://download.opensuse.org/repositories/home:tubyliec:bel-dicts/xUbuntu_24.04/ ./" \
  | sudo tee /etc/apt/sources.list.d/bel-dicts.list
sudo apt update && sudo apt install bel-dicts
```

### Fedora

```bash
sudo dnf config-manager --add-repo \
  https://download.opensuse.org/repositories/home:tubyliec:bel-dicts/Fedora_40/home:tubyliec:bel-dicts.repo
sudo dnf install bel-dicts
```

---

## Праверка ўсталявання

```bash
hunspell -D 2>&1 | grep be
```

---

## Ліцэнзія