# Einrichtung Raspberry Pi OS Bookworm
Diese Anleitung beschreibt, wie man das Raspberry Pi OS grundlegend einrichtet.

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
Nachdem das Image auf die microSD-Karte geschrieben wurde, entfernen Sie die microSD-Karte sicher und stecken Sie sie erneut in Ihren Computer ein. Es sollten nun zwei Laufwerke erscheinen, eines davon mit dem Namen boot.

##### 1. Headless-Setup (ohne Monitor und Tastatur)

1. WLAN aktivieren

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

2. SSH aktivieren:

Erstellen Sie eine leere Datei mit dem Namen ssh (ohne Dateierweiterung) im boot Verzeichnis der microSD-Karte. Diese Datei signalisiert dem Raspberry Pi beim Booten, dass der SSH-Dienst aktiviert werden soll.

Unter Windows:

* Öffnen Sie den Datei-Explorer.
* Navigieren Sie zum boot Verzeichnis der microSD-Karte.
* Rechtsklicken Sie in das Verzeichnis, wählen Sie Neu > Textdokument, benennen Sie es in ssh um und löschen Sie die .txt Erweiterung.

Unter macOS oder Linux:

* Öffnen Sie ein Terminal.
* Navigieren Sie zum boot Verzeichnis der microSD-Karte, z.B.:

```
cd /Volumes/boot
```

Erstellen Sie die ssh Datei:

```
touch ssh
```

* Entfernen Sie die microSD-Karte sicher von Ihrem Computer und stecken Sie sie in den Raspberry Pi.
* Schließen Sie das Netzteil an den Raspberry Pi an und schalten Sie ihn ein.
* Der Raspberry Pi sollte sich nun mit Ihrem WLAN verbinden und der SSH-Dienst sollte aktiviert sein.

##### 2. Setup mit Monitor und Tastatur

* Entfernen Sie die microSD-Karte sicher von Ihrem Computer und stecken Sie sie in den Raspberry Pi.
* Schließen Sie das Netzteil an den Raspberry Pi an und schalten Sie ihn ein.
* Melden Sie sich mit dem Standardbenutzer *pi* und dem Passwort *raspberry* an.
* Nach dem Starten des Betriebssystems sehen Sie die Desktop-Oberfläche.

1. WLAN einrichten

* Klicken Sie auf das Netzwerksymbol (meistens in der oberen rechten Ecke der Taskleiste).
* Eine Liste der verfügbaren WLAN-Netzwerke wird angezeigt.
* Wählen Sie Ihr WLAN-Netzwerk aus der Liste aus.
* Geben Sie das Passwort für Ihr WLAN-Netzwerk ein und klicken Sie auf "Verbinden".

Verbindung bestätigen:

* Nach erfolgreicher Verbindung sollte das Netzwerksymbol anzeigen, dass der Raspberry Pi mit dem WLAN verbunden ist.

2. SSH aktivieren

* Öffnen Sie ein Terminal und geben Sie den folgenden Befehl ein, um den SSH-Dienst zu aktivieren:
  
```
sudo raspi-config
```
Navigieren Sie zu Interfacing Options > SSH und wählen Sie Enable.

Alternativ können Sie SSH direkt im Terminal aktivieren, ohne raspi-config zu verwenden:

```
sudo systemctl enable ssh
sudo systemctl start ssh
```

   
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
