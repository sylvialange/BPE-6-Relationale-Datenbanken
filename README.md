# BPE-6-Relationale-Datenbanken

Hier soll eine Übersetzung der Materialien von <https://informatik-bw.de> in Jupyter-Notebooks entstehen.

**HelferInnen sind willkommen!**

## Videos zur Erklärung von Jupyterhub und Nbgrader

[Erklärung für Schüler](https://vimeo.com/448597506)

[Erklärung für Lehrer](https://vimeo.com/448613640)

## nbgrader

Die Notebooks sind für **nbgrader** vorbereitet. Dies ist eine Zusatzsoftware für Jupyterhub, mit der die Aufgaben an die SchülerInnen ausgeteilt werden können.

<https://nbgrader.readthedocs.io/en/stable/>

Deshalb enthalten die Dateien bereits die **Lösungen**. Diese werden beim Austeilen an die SchülerInnen über nbgrader automatisch entfernt.

## Datenbanken, SQL-User und Rechte
Bis L1_5.9 werden nur Leserechte benötigt, da nur SELECT geübt wird. Die Skripte von https://informatik-bw.de sind also auf dem SQL-Server einzuspielen. In den Notebooks wird der SQL-User schueler verwendet. 

Wenn man daran etwas ändert, müsste man in allen Notebooks die Zelle mit %load_ext sql entsprechend ändern.

Ab L1_6 werden auch Schreibrechte benötigt. Jeder Schüler braucht bei diesen Aufgaben seine "eigene" Datenbank, um prüfen zu können, ob die Insert-Befehle gefruchtet haben. Dies habe ich so gelöst, dass jeder Schüler einen gleichnamigen SQL-User-Account erhält und alle Rechte für eine gleichnamige Datenbank.

Um die SQL-User und Datenbanken anzulegen habe ich ein Pythonprogramm geschrieben, das die benötigten SQL-Befehle generiert. (L1_6_mysql_skript_generieren.py) Diese angelegten Datenbanken sind zunächst leer.

Ein weiteres Python-Programm erzeugt die Terminalbefehle, um die benötigte Datenbank für alle Schüler zu klonen. (L1_6_terminal_skript_generieren.py)