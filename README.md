# Code-Dokumentation

Dieses Dokument dient zur Erläuterung des Ablaufs und der Funktionalität des bereitgestellten Codes. Der Code wurde in MicroPython für die Verwendung auf einem RaspberryPi Pico W geschrieben. Er erfasst Daten von verschiedenen Sensoren und speichert sie auf einer SD-Karte.

## Verwendete Bibliotheken

Der Code verwendet verschiedene Python-Bibliotheken für die Kommunikation mit Hardwarekomponenten. Die verwendeten Bibliotheken sind:

- `machine`: Enthält Funktionen zur Steuerung von Hardwarekomponenten.
- `time`: Wird für die Zeitverzögerungen und Pausen verwendet.
- `src.sd.sdcard`: Eine benutzerdefinierte Bibliothek für die Kommunikation mit der SD-Karte.
- `uos`: Bietet Funktionen zur Steuerung des Dateisystems.
- `src.ds1307.ds1307`: Eine benutzerdefinierte Bibliothek zur Steuerung der DS1307 Echtzeituhr (RTC).
- `src.BME280.bme280_float`: Eine benutzerdefinierte Bibliothek zur Steuerung der BME280-Temperatursensoren.
- `src.PicoUPSA.picoUPSa`: Eine benutzerdefinierte Bibliothek zur Steuerung des UPS-Boards (Stromverbrauch, Batteriespannung, etc).
- `src.mphx711.hx711`: Eine benutzerdefinierte Bibliothek zur Steuerung der HX711-Waage.

## Variablen

- `sleepTime`: Die Zeit, für die das System in den Schlafmodus versetzt wird (in Millisekunden).
- `scalesOffset`: Ein Offset für die Waage.
- `measurements`: Die Anzahl der Messungen, die für das Wiegen durchgeführt werden.
- `calFactor`: Ein Kalibrierungsfaktor für die Waage.

## Klassen

- `Scales`: Eine benutzerdefinierte Klasse, die die HX711-Waage steuert. Sie bietet Methoden zur Tarierung, zum Lesen von Rohdaten und zur Ermittlung des stabilen Gewichts.

## Initialisierung

In diesem Abschnitt werden verschiedene Hardwarekomponenten initialisiert, darunter LED, Waage, Temperatursensoren, Echtzeituhr, UPS-Board und SD-Karte.

## Funktionen

Der Code enthält verschiedene Funktionen, darunter:

- `goToSleep()`: Versetzt das System in den Schlafmodus.
- `getTime()`: Ruft die aktuelle Zeit von der Echtzeituhr ab.
- `printTime()`: Gibt die aktuelle Zeit auf der Konsole aus.
- `setTime()`: Setzt die Zeit in der Echtzeituhr.
- `mountSD()`: Mountet die SD-Karte.
- `unmountSD()`: Unmountet die SD-Karte.
- `writeSD(text)`: Schreibt Daten auf die SD-Karte.
- `getWeight()`: Ermittelt das Gewicht von Messungen auf der Waage.
- `getUPS()`: Ermittelt Informationen zum UPS-Board.

## Hauptprogramm

Im Hauptteil des Codes wird eine Endlosschleife ausgeführt. In dieser Schleife werden Daten erfasst, aufbereitet und auf der SD-Karte gespeichert. Anschließend wird das System in den Schlafmodus versetzt. Bei einem Fehler wird das System ebenfalls in den Schlafmodus versetzt.

Bitte beachten Sie, dass einige Teile des Codes auskommentiert sind, insbesondere die Teile, die auf die interne RTC und die BME280-Temperatursensoren zugreifen. Je nach Ihren Anforderungen können Sie diese Teile aktivieren oder deaktivieren. Zusätzlich ist der Code für die Verwendung mit einem bestimmten Mikrocontroller und Hardware konfiguriert.

# Credits

Dieses Projekt wurde unter Verwendung von Open-Source-Bibliotheken und -Ressourcen entwickelt. Wir möchten den folgenden Entwicklern und Projekten für ihre Beiträge danken:

- [BME280](https://github.com/robert-hh/BME280) - Bibliothek für den BME280-Temperatursensor von Robert Hh.
- [DS1307](https://github.com/peter-l5/DS1307) - Bibliothek für die DS1307-Echtzeituhr von Peter L5.
- [HX711](https://github.com/SergeyPiskunov/micropython-hx711) - Bibliothek für den HX711-Wägezellenverstärker von Sergey Piskunov.
- [PicoUPSa](https://www.waveshare.com/wiki/Pico-UPS-A) - Informationen und Ressourcen zum Pico-UPS-A von Waveshare.

<br>

Projekt entwickelt von [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/640px-LinkedIn_logo_initials.png" alt="LinkedIn-Logo" width="13"/> Philipp Gretscher](https://www.linkedin.com/in/philippgretscher)
[🌐 Website](https://philippg.de)

