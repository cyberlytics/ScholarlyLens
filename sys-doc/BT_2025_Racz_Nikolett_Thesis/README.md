# oth-aw-abschlussarbeiten

Hier liegen LaTeX Vorlagen für Abschlussarbeitern an der Fakultät EMI der OTH Amberg-Weiden.

Einfach "make" eingeben zum Kompilieren.


-master.tex
    Hier werden die Dateien für die Kapitel eingebunden und die persönlichen Angaben wie Name, Matrikelnummer etc. gemacht.
    Es ist sinnvoll weitere nötige Usepackages hier einzubinden.
    Falls der name dieser Datei geändert wird muss er auch im Makefile geändert werden.

-kapitel1.tex, kapitel2.tex etc.
    Diese Dateien enthalten den tatsächlichen Inhalt der Abschlussarbeit und können natürlich erweitert und umbenannt werden.
    Sie fangen immer mit: "\chapter" an um ein neues Kapitel zu eröffnen. Weitere Unterteilung ist mit \subsection und \subsubsection möglich.

-formblatt_summary.tex; formblatt_selbststaendigkeitserklaerung
    Diese beiden Dateien erzeugen mit den Angaben aus master.tex die entsprechenden Dokumente und binden sie gleich an der richtigen Stelle der Abschlussarbeit ein
