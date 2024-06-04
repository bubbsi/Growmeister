# Anleitung zum Einrichten eines Raspberry Pi als Klima Controller für eine Growbox

Diese Anleitung führt Sie durch die Einrichtung eines Raspberry Pi als Klima Controller für eine Growbox, indem Sie das Growmeister-Projekt verwenden. Folgen Sie den unten stehenden Schritten, um die erforderliche Software zu installieren und zu konfigurieren.

## Voraussetzungen
- Raspberry Pi mit Raspbian OS installiert
- Internetverbindung
- Grundkenntnisse in der Verwendung der Kommandozeile

## Schritt 1: Aktualisieren des Systems
Zuerst müssen wir sicherstellen, dass unser System auf dem neuesten Stand ist. Öffnen Sie ein Terminal und führen Sie die folgenden Befehle aus:

```bash
sudo apt update
sudo apt upgrade -y
```

## Schritt 2: Python Virtual Environment installieren
Um Konflikte zwischen verschiedenen Python-Paketen zu vermeiden, installieren wir das Python Virtual Environment:

```bash
sudo apt install python3-venv -y
```

## Schritt 3: Projektverzeichnis erstellen
Erstellen Sie ein Verzeichnis für Ihre Projekte und wechseln Sie in dieses Verzeichnis:

```bash
mkdir ~/projects
cd ~/projects
```

## Schritt 4: Growmeister-Projekt klonen
Klonen Sie das Growmeister-Projekt von GitHub:

```bash
git clone https://github.com/bubbsi/Growmeister.git
cd Growmeister/
```

## Schritt 5: Virtuelle Umgebung einrichten
Erstellen Sie eine virtuelle Umgebung im Projektverzeichnis und aktivieren Sie diese:

```bash
python -m venv .venv
source .venv/bin/activate
```

## Schritt 6: Abhängigkeiten installieren
Installieren Sie die benötigten Python-Pakete, die im `requirements.txt`-File definiert sind:

```bash
pip install -r requirements.txt
```

## Schritt 7: Shell-Skript aus dem Repository verwenden
Das Shell-Skript `clima_controller.sh`, das die virtuelle Umgebung aktiviert und das Hauptskript `clima_controller.py` ausführt, ist bereits im Repository vorhanden. Stellen Sie sicher, dass das Skript ausführbar ist:

```bash
chmod +x clima_controller.sh
```

Der Inhalt des Skripts sollte wie folgt aussehen:

```sh
#!/bin/sh
DIR=$(dirname "$(readlink -f "$0")")
. $DIR/.venv/bin/activate
python $DIR/clima_controller.py
```

## Schritt 8: Cronjob einrichten
Um das Growmeister-Skript beim Systemstart automatisch auszuführen, richten wir einen Cronjob ein. Öffnen Sie die Crontab-Konfiguration:

```bash
crontab -e
```

Fügen Sie die folgende Zeile hinzu, um das Skript beim Systemstart auszuführen:

```bash
@reboot /home/pi/projects/Growmeister/clima_controller.sh
```

## Schritt 9: Growmeister konfigurieren
Passen Sie die Konfigurationsdateien des Growmeister-Projekts an Ihre spezifischen Bedürfnisse und Sensoren an. Diese befinden sich in der Regel im Projektverzeichnis. Öffnen Sie die entsprechenden Dateien mit einem Texteditor (z.B. `nano`) und ändern Sie die Einstellungen entsprechend Ihrer Growbox-Konfiguration.

```bash
nano /home/pi/projects/Growmeister/config.yaml
```

## Schritt 10: Testen Sie die Installation
Testen Sie, ob alles funktioniert, indem Sie das Hauptskript manuell ausführen:

```bash
./clima_controller.sh
```

Überprüfen Sie die Ausgaben und Logs, um sicherzustellen, dass der Growmeister korrekt funktioniert und die Sensoren die richtigen Werte liefern.

## Schlussfolgerung
Ihr Raspberry Pi sollte nun als Klima Controller für Ihre Growbox eingerichtet sein und automatisch Daten sammeln und steuern. Passen Sie die Einstellungen und Skripte weiter an, um sicherzustellen, dass alles optimal funktioniert und Ihre Pflanzen die besten Wachstumsbedingungen haben.
