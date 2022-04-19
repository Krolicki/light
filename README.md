Konfiguracja Raspberry Pi:

Raspberry Pi 4b 2GB

Moduł przekaźnika Iduino JQC-3FF-S-Z

 - zasilanie 5V - PIN 4 PWR
 - sygnał - GPIO 23 (PIN 16)
 - masa - PIN 6

Lokalizacja plików: /home/light

Uruchamianie skryptu ze startem urządzenia: 

na końcu pliku "/etc/rc.local" dopisać:

sudo python /home/light/light.py & > /home/pi/Desktop/startlog.txt 2>&1 exit 0

plik startlog.txt opcjonalny

Serwer działa na porcie 82

[adres Raspberry Pi]:82