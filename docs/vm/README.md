# Maszyna wirtualna

## *Platforma hostująca opracowane rozwiązanie*

---

## Dostęp do maszyny

### Archiwum maszyny wirtualnej zostało udostępnione za pośrednictwem *Google Drive* i jest dostępne [tutaj](https://drive.google.com/file/d/1aYN6eRXr4Byipn_RBwVYD7CFmiu-qfvy/view?usp=share_link).

---

## System operacyjny

System wybrany i wstępnie przygotowany: **Debian 12 *Bookworm***

![Image](https://github.com/ITA-Flowers/Zostan_w_Swidnicy/assets/74451381/90982acf-9d5d-4ed7-be11-356f2f88a68b)

---

### Dane logowania

|Użytkownik|Hasło|
|---|---|
|`flower`|`Password1`|

---

## Konfiguracja sieciowa

Maszyna posiada skonfigurowane dwa adaptery sieciowe typów: **NAT** i **Host-only**

Adapter **NAT** zapewnia łączność z globalną siecią Internet i jego adres jest negocjowany za pomocą usługu DHCP

Adapter **Host-only** natomiast posiada stały adres, o czym więcej poniżej.

---

## Wirtualna sieć **Host-only**

### Konfiguracja sieci

Za pomocą narzędzia *vmware-netcfg* należy skonfigurować sieć typu **Host-only** zgodnie z poniższymi wytycznymi:

Adres podsieci: `172.16.245.0`
Maska podsieci: `255.255.255.0`

![image](https://github.com/ITA-Flowers/Zostan_w_Swidnicy/assets/74451381/94c35ce7-da6b-4144-a1b9-704107d55360)
*Konfigurator sieci VMWare*

### Konfiguracja maszyny

Maszyna posiada uprzednio skonfigurowany stały adres IP: `172.16.245.20 /24`

Pod tym adresem będzie wystawiona platforma dla testów implementacji nowych rozwiązań, oczywiście na odpowiednim porcie (w fazie testowania każdy moduł usługi otrzyma swój port dla zapewnienia bezpośredniego dostępu do API z maszyny *hosta*).

![image](https://github.com/ITA-Flowers/Zostan_w_Swidnicy/assets/74451381/428dbf01-6098-484a-830c-ab4e66f369b6)
*Konfigurator sieci na maszynie wirtualnej*

![image](https://github.com/ITA-Flowers/Zostan_w_Swidnicy/assets/74451381/45d8d9e9-bb23-4ed7-9fd3-6c4a18643b58)
*Sprawdzenie łączności z maszyną wirtualną*

---

### ***Pro-tip***

Dobrą praktyką może być zapis w pliku mapowań nazw domenowych w celu korzystania z nazwy domenowej zamiast adresu IP.

Dla **OS Linux** jest to plik `/etc/hosts`

Dla **OS Windows** jest to plik `C:\Windows\System32\drivers\etc\hosts`

Struktury plików są takie same, a poniżej przedstawiam konstrukcję wpisu:

``` text
# Zostan_w_Swidnicy VM Host-only virtual address
172.16.245.20    swidnica-tf
```

![image](https://github.com/ITA-Flowers/Zostan_w_Swidnicy/assets/74451381/22ba4ab2-bc8c-4157-bcd8-d3ee431442f3)
*Sprawdzenie łączności po zmapowaniu nazwy domenowej*
