# Headless WLAN Einrichtung auf Raspberry Pi OS Bookworm
Diese Anleitung beschreibt, wie man das WLAN auf einem Raspberry Pi, der mit Raspberry Pi OS Bookworm läuft, ohne angeschlossenen Monitor oder Tastatur einrichtet.

## Voraussetzungen
* Raspberry Pi (alle Modelle mit WLAN-Unterstützung)
* microSD-Karte (mindestens 8 GB)
* Raspberry Pi Imager oder ein anderes Tool zum Flashen von Betriebssystemen auf die microSD-Karte
* WLAN-Zugangsdaten (SSID und Passwort)

## Schritt-für-Schritt-Anleitung
### 1. Raspberry Pi OS auf die microSD-Karte flashen
1. Laden Sie die neueste Version von Raspberry Pi OS Bookworm von der offiziellen Raspberry Pi Webseite herunter.
2. Installieren und öffnen Sie den Raspberry Pi Imager oder ein ähnliches Tool.
3. Wählen Sie das heruntergeladene Image und die microSD-Karte als Zielmedium aus.
4. Flashen Sie das Image auf die microSD-Karte.

### 2. WLAN und SSH für den ersten Start einrichten
Nachdem das Image auf die microSD-Karte geschrieben wurde:

1. Entfernen Sie die microSD-Karte sicher und stecken Sie sie erneut in Ihren Computer ein. Es sollten nun zwei Laufwerke erscheinen, eines davon mit dem Namen boot.

2. WLAN-Konfiguration:

Erstellen Sie eine Datei mit dem Namen wpa_supplicant.conf im boot Verzeichnis der microSD-Karte und fügen Sie den folgenden Inhalt ein:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=DE # Passen Sie das an Ihr Land an

network={
  ssid="YOUR_SSID"
  psk="YOUR_PASSWORD"
  key_mgmt=WPA-PSK
}
```

Ersetzen Sie YOUR_SSID durch den Namen Ihres WLANs und YOUR_PASSWORD durch Ihr WLAN-Passwort.

3. SSH aktivieren:

Erstellen Sie eine leere Datei mit dem Namen ssh im boot Verzeichnis der microSD-Karte. Dies aktiviert den SSH-Dienst beim ersten Start.

### 3. Raspberry Pi starten
1. Entfernen Sie die microSD-Karte sicher von Ihrem Computer und stecken Sie sie in den Raspberry Pi.
2. Schließen Sie das Netzteil an den Raspberry Pi an und schalten Sie ihn ein.
3. Der Raspberry Pi sollte sich nun mit Ihrem WLAN verbinden und der SSH-Dienst sollte aktiviert sein.
   
### 4. Verbindung zum Raspberry Pi herstellen
1. Finden Sie die IP-Adresse Ihres Raspberry Pi. Dies kann über Ihren Router oder mit einem Netzwerk-Scanner wie nmap erfolgen.

Beispiel für nmap:

```
nmap -sn 192.168.1.0/24
```
2. Stellen Sie eine SSH-Verbindung zum Raspberry Pi her:

```
ssh pi@IP-ADRESSE
```
Ersetzen Sie IP-ADRESSE durch die tatsächliche IP-Adresse des Raspberry Pi.

Das Standardpasswort für den Benutzer pi ist raspberry. Es wird empfohlen, das Passwort nach der ersten Anmeldung zu ändern:

```
passwd
```

### 5. Nachbereitung
Nach der ersten Anmeldung können Sie weitere Konfigurationen vornehmen, wie z.B. das Einrichten eines neuen Benutzers, das Aktualisieren des Systems oder das Installieren zusätzlicher Software.

```
sudo apt update
sudo apt upgrade
```

Mit diesen Schritten hast du erfolgreich ein WLAN headless auf deinem Raspberry Pi OS Bookworm eingerichtet. Du kannst nun den Raspberry Pi weiter konfigurieren und für deine Projekte nutzen.
