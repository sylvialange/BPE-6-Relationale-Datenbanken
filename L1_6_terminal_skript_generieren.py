# Bashskript generieren

schueler = ["Max", "Tom", "Tim"]

datei = open('terminal_skript.sh', 'a')

for s in schueler:
    datei.write("mysqldump --opt -h localhost -u root -psecret fahrschule17 |  mysql -h localhost -u "
                +s+" -psecret "+s+"\n")

datei.close()
