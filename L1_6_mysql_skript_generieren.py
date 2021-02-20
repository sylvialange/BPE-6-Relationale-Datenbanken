# Text für MySQL-Umgebung generieren:

# Dieses Skript generiert die Befehle, die in der mysql-Umgebung ausgeführt werden müssen, um die benötigten SQL-User anzulegen. 
# Für jeden Schueler gibt es einen SQL-User, der dann Schreibrechte an einer gleichnamigen Datenbank hat.
# Die Datenbanken werden dann über Terminalbefehle angelegt. Diese werden von einem weiteren Pythonprogramm in ein Bashskript geschrieben.

# In das Array schueler alle Loginnamen der Schüler schreiben

schueler = ["Max", "Tom", "Tim"]

datei = open('mysql_skript.txt', 'a')

for s in schueler:
    datei.write("CREATE DATABASE /*!32312 IF NOT EXISTS*/ `"+s
                +"` /*!40100 DEFAULT CHARACTER SET utf8 */; \n create user "+s+" identified by 'secret'; \n grant all on "+s+".* to "+s+"@'%';\n\n")


datei.close()

