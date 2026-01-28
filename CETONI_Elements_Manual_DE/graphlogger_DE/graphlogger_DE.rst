Grafischer Datenlogger
=======================

Einführung
----------

Neben der Datenaufzeichnung in CSV-Dateien können Sie mit dem
Datalogger-Plugin Prozessdaten in Diagrammen aufzeichnen und damit in
Echtzeit die zeitliche Veränderung dieser Prozessdaten grafisch
visualisieren. Zur Anzeige der Prozessdaten-Diagramme klicken Sie in der
Seitenleiste auf die Schaltfläche :guilabel:`Logging` :guinum:`❶` (siehe Abbildung unten)
oder blenden den Logging View über das Hauptmenü ein (::menuselection:`Window --> ShowView --> Logging`)
:guinum:`❷`.

.. image:: Pictures/10000201000002AB000001ABF50BD6283D944D83.png

In der Abbildung oben sehen Sie die wichtigsten
Bedienelemente:

.. rst-class:: guinums

1. **Logging-Schaltfläche** - Hiermit blenden Sie das
   Prozessdaten-Diagramm ein.
2. **View Menü** - damit kann das Prozessdaten Diagramm ebenfalls ein-
   und ausgeblendet werden
3. **Zeichenfläche** - Hier sehen Sie die Kurven aller Prozessdaten die
   von dem Diagramm aufgezeichnet werden.
4. **Legende** - Die Legende enthält die Bezeichnung aller Kurven die im
   Diagramm aufgezeichnet werden mit der entsprechenden Farbe. Über die
   Legende können Kurven selektiv ein- / und ausgeblendet werden.
5. **Werkzeugleiste** - Hier finden Sie Schaltflächen zur Konfiguration
   der Datenaufzeichnung, zum Starten und Stoppen der Aufzeichnung und
   zur Navigation innerhalb der Darstellung.

Werkzeugleiste
--------------

+-----------+---------------------------------------------------------+
| |image32| | Öffnet den Konfigurationsdialog zur Konfiguration des   |
|           | grafischen Prozessdatenloggers                          |
+-----------+---------------------------------------------------------+
| |image33| | Startet / stoppt die Aufzeichnung von Prozessdaten      |
+-----------+---------------------------------------------------------+
| |image34| | Handwerkzeug zum Verschieben des aktuellen Ausschnitts  |
|           | der im Diagramm angezeigt wird                          |
+-----------+---------------------------------------------------------+
| |image35| | Vergrößerungsrahmen aufziehen zum gezielten Vergrößern  |
|           | bestimmter Bereiche                                     |
+-----------+---------------------------------------------------------+
| |image36| | Passt die Skalierung der X-Achse so an, dass alle       |
|           | Messwerte auf den Bildschirm passen                     |
+-----------+---------------------------------------------------------+
| |image37| | Passt die Skalierung der Y-Achse so an, dass alle       |
|           | Messwerte auf den Bildschirm passen                     |
+-----------+---------------------------------------------------------+
| |image38| | Passt die Skalierung der X-Achse und Y-Achse so an,     |
|           | dass alle Messwerte auf den Bildschirm passen           |
+-----------+---------------------------------------------------------+
| |image39| | Aktiviert die automatische Skalierung – solange         |
|           | Messewerte aufgezeichnet werden, wird die Skalierung    |
|           | der X- und Y-Achse automatisch so angepasst, dass alle  |
|           | Messwerte auf den Bildschirm passen.                    |
+-----------+---------------------------------------------------------+
| |image40| | Alle Kurven anzeigen. Wenn Kurven ausgeblendet sind,    |
|           | werden diese wieder eingeblendet.                       |
+-----------+---------------------------------------------------------+
| |image41| | Löscht alle Daten aus dem Diagramm                      |
+-----------+---------------------------------------------------------+
| |image42| | Skalierung umschalten. Damit schalten Sie die           |
|           | Skalierung der X-Achse zwischen absolutem               |
|           | Zeit-/Datumsstempel und relativer Zeit in Sekunden und  |
|           | Millisekunden seit Start der Aufzeichnung um.           |
+-----------+---------------------------------------------------------+
| |image43| | Exportiert ein Bild des der aktuell dargestellten       |
|           | Ausschnitts                                             |
+-----------+---------------------------------------------------------+
| |image44| | Exportiert alle Daten des Plots als CSV-Datei           |
+-----------+---------------------------------------------------------+
| |image45| | Speichert die Plotdaten in eine Datei, die später       |
|           | wieder geladen werden kann                              |
+-----------+---------------------------------------------------------+
| |image46| | Lädt Plotdaten, die vorher gespeichert wurden.          |
+-----------+---------------------------------------------------------+


Konfigurationsdialog
--------------------

Übersicht Konfigurationsdialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/10002F2F000034EB000034EBDBA40A7FF6EF8292.svg
   :width: 60
   :height: 60
   :align: left

Klicken Sie in der Werkzeugleiste auf die Schaltfläche
:guilabel:`Configure process data graph`, um den Konfigurationsdialog (unten) zu
öffnen. Der Konfigurationsdialog besteht im Wesentlichen aus den folgenden
Bereichen:

.. image:: ../../img/datalogger/graph_logger_configuration_dialog.png
   :alt: Konfigurationsdialog grafischer Datenlogger

.. rst-class:: guinums

1. **Objektbaum (Object Tree)** - Der Objektbaum enthält einen Baum aller
   Objekte und deren Eigenschaften, die in der Applikation vorhanden sind.
   Mit verschiedenen Filtern können Sie den Objektbaum nach bestimmten Objekten
   filtern. Standardmäßig werden nur Geräte und Geräteeigenschaften angezeigt.

2. **Logger Channels** - hier sehen Sie in tabellarischer Form alle
   Kanäle die vom Logger aufgezeichnet werden.

3. **Logger Configuration** - in diesem Bereich können Sie verschiedene
   Einstellungen zur Aufzeichnung der Daten konfigurieren.


Der Objektbaum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Im Objektbaum finden Sie eine hierarchische Auflistung aller Objekte (z.B. Geräte)
und deren Kindobjekte (wie z.B. untergeordnete Geräte):

.. image:: ../../img/datalogger/object_tree.png

.. rst-class:: guinums

1. **Objekt** - Ein Objekt kann z.B. ein Gerät (hier **Nemesys_M_1**) oder
   ein anderes Anwendungsobjekt sein. In jedem Objekt finden Sie nach dem
   Aufklappen in der nächsten Ebene die beiden Elemente **Children** und
   **Properties**.

2. **Children** - Das Children Element gruppiert alle Kindobjekte des
   übergeordneten Objektes. In unserem Beispiel sind dies alle Objekte,
   bzw. Geräte, die dem Gerät **Nemesys_M_1** untergeordnet sind bzw. zu
   diesem Gerät gehören.

3. **Properties** - Das Properties Element gruppiert alle Eigenschaften des
   übergeordneten Objektes. In unserem Beispiel sind dies alle Eigenschaften
   des Gerätes **Nemesys_M_1**, welche im Logger aufgezeichnet werden können.

4. **Untergeordnetes Objekt** - In der **Children** Gruppe sind alle untergeordneten
   Objekte zu finden. Beim Beispiel **Nemesys_M_1** sind dies z.B. die
   digitalen und analogen Ein- und Ausgänge des Gerätes, wie z.B.
   **Nemesys_M_1_DigOUT1**. Diese Objekte können wiederum aufgeklappt werden,
   um deren Kindobjekte und Eigenschaften anzuzeigen.

5. **Eigenschaft** - In der **Properties** Gruppe finden sie alle Eigenschaften
   des übergeordneten Objektes. Beim Beispiel **Nemesys_M_1** sind dies z.B.
   die Eigenschaften **SyringeFillLevel** oder **ActualFlow**. Diese
   Eigenschaften können Sie einfach per Drag & Drop in die Kanalliste ziehen,
   um deren Werte aufzuzeichnen.


Objektbaum filtern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Über dem Objektbaum finden Sie verschiedene Filter, mit denen Sie den Objektbaum
nach bestimmten Kriterien filtern können. Standardmäßig ist die Checkbox
:guilabel:`Devices Only` :guinum:`❶` aktiviert. D.h. im Objektbaum werden nur
Geräte, die vom internen Gerätemanager (:guilabel:`Core.DeviceManager`) verwaltet
werden angezeigt. Wenn Sie diese Checkbox deaktivieren, werden Ihnen im
Objektbaum weitere Anwendungsobjekte angezeigt.

Ist die Checkbox :guilabel:`Devices Only`:guinum:`❶` aktiviert, wird Ihnen
eine Auswahlbox :guinum:`❷` angezeigt, mit der Sie den Gerätebaum nach einem
bestimmten Gerätetyp filtern können. In der Abbildung unten wurde z.B. nach
Spritzenpumpen gefiltert:

.. image:: ../../img/datalogger/object_tree_filter.png

Zusätzlich finden Sie direkt über dem Objektbaum ein Eingabefeld :guinum:`❸`,
mit dem Sie den Objektbaum nach einem bestimmten Begriff, z.B. einem
Gerätenamen oder eine Geräteeigenschaft, filtern können. In der Abbildung unten
wurde z.B. nach der Geräteeigenschaft **ActualFlow** gefiltert. D.h.,
es werden nur Objekte oder Geräte mit dieser Eigenschaft im Objektbaum
angezeigt:

.. image:: ../../img/datalogger/object_tree_filter_text.png


Liste der Logger-Kanäle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../img/datalogger/logger_channels_view.png

Die Kanalliste :guilabel:`Logger Channels` zeigt in tabellarischer Form die
Konfiguration des grafischen Loggers. Jede Zeile in der Tabelle
entspricht genau einer Kurve in der grafischen Darstellung, d.h. einem
Logger-Kanal. Folgende Spalten sind vorhanden:

-  **Object** - enthält den Namen des Objektes, von dem der Wert einer
   bestimmten Eigenschaft (Property) aufgezeichnet werden soll und das Icon des
   Objekts.
-  **Property** - dies ist der Name der Objekteigenschaft / des
   Prozessdatenwertes, der aufgezeichnet wird. Den Typ der
   Eigenschaft (numerischer oder boolescher Wert) können Sie an
   dem Typ-Icon einfach erkennen.

   ============ =================
   |icon-num|   Numerischer Wert
   |icon-bool|  Boolescher Wert
   |icon-text|  Text
   ============ =================

-  **Label** - hier können Sie eine eigene Bezeichnung des Kanals
   festlegen. Diese Bezeichnung erscheint dann in der Legende des
   Graphen.

Zum Hinzufügen eines Kanals zum Logger, führen Sie einfach
folgende Schritte durch:


Datenaufzeichnung konfigurieren
--------------------------------

Kanäle hinzufügen
~~~~~~~~~~~~~~~~~~~~

:step:`Schritt 1 - Kanäle hinzufügen`

.. image:: ../../img/datalogger/graph_logger_drag_and_drop.png
   :alt: Diagrammkurven via Drag & Drop hinzufügen

Ziehen Sie aus dem Objektbaum :guilabel:`Object Tree` die Objekteigenschaft,
welche Sie aufzeichnen möchten, per Drag & Drop in die Kanalliste
:guilabel:`Logger Channels`. Der neue Kanal wird in der Zeile eingefügt, an
der sie die Maustaste loslassen (siehe Abbildung unten).

.. admonition:: Tipp
   :class: tip

   Um die Auswahl einer Objekteigenschaft (Property) zu erleichtern, können Sie den
   Objektbaum nach verschiedenen Kriterien filtern.

:step:`Schritt 2 - Kanalbeschriftung festlegen`

In der Spalte :guilabel:`Label` können Sie für jeden Kanal eine eigene
Beschriftung vergeben. Diese Beschriftung wird später dann in der
Legende des Graphen als Beschriftung der Kurve angezeigt.

.. image:: ../../img/datalogger/log_channel_label.png
   :alt: Kanalbeschriftung ändern

Klicken Sie zum Ändern der
Beschriftung doppelt in die Tabellenzelle (siehe Abbildung oben) und
geben Sie dann die neue Bezeichnung ein.

:step:`Schritt 3 - Aufzeichnungsintervall festlegen`

.. image:: ../../img/datalogger/graph_logger_interval.png
   :alt: Log-Intervall konfigurieren


Im Feld :guilabel:`Log Interval` können Sie im Bereich :guilabel:`Logger Configuration`
das Intervall festlegen, in dem neue
Messwerte aufgezeichnet werden sollen. Sie können das Intervall mit
einer Auflösung von 0,1 Sekunden festlegen.

.. admonition:: Wichtig
   :class: note

   Wählen Sie das Intervall so groß wie
   möglich und so klein wie nötig um die Menge der
   aufzuzeichnenden Daten so gering wie möglich zu halten.

Die Konfiguration wird beim Beenden der Anwendung gespeichert und beim
erneuten Start wieder geladen.

Kanäle löschen
~~~~~~~~~~~~~~

Um einen oder mehrere Kanäle zu löschen, markieren Sie zuerst die Kanäle
mit der Maus. Sie können dann die Kanäle löschen, indem Sie entweder die
:kbd:`Delete`-Taste drücken oder mit der rechten Maustaste das Kontextmenü
aufrufen und den Menüpunkt :menuselection:`Delete Selection` auswählen.

|image58| |image59|

Sie können alle Kanäle des Loggers gleichzeitig löschen, indem Sie im
Kontextmenü den Punkt :menuselection:`Clear Logger` auswählen.


Datenaufzeichnung starten / stoppen
-----------------------------------

.. image:: Pictures/10001A4C000034EB000034EBE789A979D3788852.svg
   :width: 60
   :height: 60
   :align: left

Über die entsprechende Schaltfläche in der Werkzeugleiste
können Sie die Datenaufzeichnung starten und stoppen.

|


Diagramm Navigation und Bedienung
---------------------------------

Übersicht
~~~~~~~~~

Das Diagramm bietet Ihnen verschiedene Möglichkeiten die Darstellung
anzupassen, bestimmte Bereiche vergrößert darzustellen oder Kurven ein-
und auszublenden.

.. image:: Pictures/1000020100000304000001DECD37A2D16344540B.png
   :alt: Übersicht Prozessdatengraph

Das Diagramm besteht aus der
Zeichenfläche :guinum:`❶`, die durch die Zeitachse unten (X-Achse) :guinum:`❸` und die
Prozessdatenachse links (Y-Achse) :guinum:`❹` begrenzt wird. Die Zeitachse zeigt
Datum und Uhrzeit als absolute Werte an. Die Prozessdatenachse zeigt den
Messwert zu einem bestimmten Zeitpunkt an. Die Messwertachse ist
einheitenlos und stellt unterschiedlichste Werte und Einheiten dar.

Wenn Sie mit der rechten Maustaste in die Zeichenfläche klicken, wird
ein Kontextmenü :guinum:`❷` mit zusätzlichen Funktionen angezeigt.

Ausschnitt verschieben
~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/100005C7000035050000350518807CBDF5FF2BAE.svg
   :width: 60
   :height: 60
   :align: left

Mit dem Verschiebewerkzeug (*Pan Tool*) können Sie bequem den
Ausschnitt verschieben, der im Diagramm angezeigt wird. Aktivieren Sie
das Werkzeug durch anklicken der Schaltfläche. Klicken Sie nun in die
Zeichenfläche und bewegen Sie die Maus mit gedrückter Maustaste um den
Ausschnitt zu verschieben.

.. admonition:: Wichtig
   :class: note

   Das Verschieben des Ausschnittes bewirkt
   eine Deaktivierung der automatischen Skalierung.

Werte einer Kurve anzeigen
~~~~~~~~~~~~~~~~~~~~~~~~~~

Wenn das Verschiebewerkzeug (*Pan Tool*) aktiv ist, können Sie den
Mauszeiger über eine Kurve bewegen, um sich den Wert an der betreffenden
Position anzeigen zu lassen.

.. image:: Pictures/100002010000024C000000D8EF633321C7CB7321.png


Vergrößerung mit Mausrad einstellen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Durch drehen des Mausrades können Sie die Vergrößerung der Anzeige
erhöhen (hinein zoomen) oder verringern (heraus zoomen).

========= ==============================================
|image68| Vergrößerungsfaktor erhöhen (hinein zoomen)
|image69| Vergrößerungsfaktor verringern (heraus zoomen)
========= ==============================================

Ausschnittvergrößerung mit Vergrößerungsrahmen wählen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000100A000034EB000034EBFC7CEEC6D6B20A4B.svg
   :width: 60
   :height: 60
   :align: left

Mit dem Vergrößerungswerkzeug (*Zoom Tool*) können Sie
gezielt einen Ausschnitt auswählen, den Sie vergrößert darstellen
möchten. Gehen Sie dafür wie folgt vor (siehe Abbildung unten):

|

.. image:: Pictures/10000000000001FA0000015E46DAC1CBDA6E2854.png
   :alt: Vergrößerungsrahmen aufziehen

.. rst-class:: guinums


1. Klicken Sie mit der linken Maustaste in die Zeichenfläche um die
   erste Ecke des Vergrößerungsrahmens festzulegen.
2. Ziehen Sie nun mit gedrückter Maustaste ein Vergrößerungsrahmen auf
   die gewünschte Größe.
3. Sobald Sie die Maustaste loslassen, wird der gewählte Ausschnitt auf
   die aktuelle Größe der Anzeige skaliert.


Anzeige passend / automatisch skalieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die Werkzeugleiste und das Kontextmenü enthalten verschiedene Tools um
die Anzeige automatisch so anzupassen, dass alle Daten im sichtbaren
Bereich liegen.

Folgende Möglichkeiten der Anpassung sind vorhanden:

+-----------+---------------------------------------------------------+
| |image79| | Passt die Skalierung der X-Achse so an, dass alle       |
|           | Messwerte auf den Bildschirm passen                     |
+-----------+---------------------------------------------------------+
| |image80| | Passt die Skalierung der Y-Achse so an, dass alle       |
|           | Messwerte auf den Bildschirm passen                     |
+-----------+---------------------------------------------------------+
| |image81| | Passt die Skalierung der X-Achse und Y-Achse so an,     |
|           | dass alle Messwerte auf den Bildschirm passen           |
+-----------+---------------------------------------------------------+
| |image82| | Aktiviert die automatische Skalierung – solange         |
|           | Messewerte aufgezeichnet werden, wird die Skalierung    |
|           | der X- und Y-Achse automatisch so angepasst, dass alle  |
|           | Messwerte auf den Bildschirm passen.                    |
+-----------+---------------------------------------------------------+

Die automatische Skalierung können Sie auch über das Kontextmenü
getrennt für X- und Y-Achse aktivieren:

.. image:: Pictures/1000000000000109000001040CF9729CD97C9A4D.png
   :alt: Automatische Skalierung für X- und Y-Achse

.. admonition:: Wichtig
   :class: note

   Die Änderung der Vergrößerung oder das
   Verschieben des Ausschnittes bewirken eine
   Deaktivierung der automatischen Skalierung.

Kurven ein- und ausblenden
~~~~~~~~~~~~~~~~~~~~~~~~~~

Um die Skalierung und damit die Anzeige einzelner Kurven zu verbessern,
können Sie Kurven ein- und ausblenden. Klicken Sie dazu mit der rechten Maustaste
auf das gewünschte Element in der Diagrammlegende und wählen Sie die gewünschte
Funktion, um entweder nur die entsprechende Kurve auszublenden :menuselection:`Hide Curve`
oder alle anderen außer der entsprechenden Kurve :menuselection:`Show only this curve`,
wie in der Abbildung unten dargestellt.

.. image:: Pictures/10000000000001A40000005CD26CCB4A8D0DF1F9.png
   :alt: Kontextmenü Legendeneintrag

Wenn Sie alle ausgeblendeten Kurven wieder einblenden möchten,
aktivieren Sie in der Zeichenfläche das Kontextmenü mit der rechten
Maustaste und wählen Sie dann den Menüpunkt :menuselection:`Show all curves` (siehe
Abbildung unten).

.. image:: Pictures/1000000000000109000001041C877E8A24D5AB94.png

Kurvenfarbe ändern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Um eine andere Kurvenfarbe zu wählen, klicken Sie mit der rechten
Maustaste auf einen Eintrag in der Legende. Es wird nun das Kontextmenü
für diesen Legendeneintrag angezeigt (siehe Abbildung unten).

.. image:: Pictures/10000000000002100000007CF77B5C49CD7E0D88.png
   :alt: Kontextmenü Legendeneintrag - Farbwahl

Wählen Sie den
Menüpunkt :menuselection:`Select Color`. Es wird Ihnen nun ein Farbauswahldialog
angezeigt, in dem Sie eine beliebige Kurvenfarbe auswählen können.

.. image:: Pictures/100002010000020A000001B855540FDC883B53CF.png

Diagramm-Bild exportieren
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/10001855000034EB000034EBA6C6DA993124AA4C.svg
   :width: 60
   :height: 60
   :align: left

Über den Menüeintrag :menuselection:`Export plot image` im Kontextmenü
können Sie ein Bild des aktuellen Diagramms exportieren.

|

.. image:: Pictures/100002010000010C000000E1260A96B6F1A86108.png
   :alt: Diagramm-Bild exportieren

In dem Dateidialog der nun
eingeblendet wird (siehe Abbildung unten), wählen Sie zuerst ihr
Zielverzeichnis aus.

.. image:: Pictures/1000000000000293000001D6F3848773F9BE9543.png

Anschließend geben Sie
den Dateinamen der Bilddatei ein :guinum:`❶`. Dann wählen Sie in dem Auswahlfeld
den Dateityp :guinum:`❷` der Bilddatei aus. Die Exportfunktion unterstützt sowohl
Bilddateien (:file:`png, jpg...`) als auch skalierbare Vektorgrafiken
(:file:`pdf, svg...`). Wählen Sie das für Sie passende Bildformat aus.

Klicken Sie zum Abschluss auf :guilabel:`Save` :guinum:`❸`, um den Export zu starten.

CSV Export
~~~~~~~~~~

.. image:: Pictures/10000FBE000034EB000034EB9506C15D6D175810.svg
   :width: 60
   :height: 60
   :align: left

Über den Menüeintrag :menuselection:`Export CSV file` im Kontextmenü können
Sie alle Diagrammdaten in eine CSV-Datei exportieren.

|

Diagrammdaten löschen
~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/100019CB000035050000350509AD2B23340F765E.svg
   :width: 60
   :height: 60
   :align: left

Klicken Sie im Kontextmenü auf den Eintrag :menuselection:`Clear plot data`
um alle aufgezeichneten Daten zu löschen und mit einem leeren
Diagramm die Aufzeichnung neu zu beginnen.

.. image:: Pictures/100002010000010D000000D1835EC0ADB6A09475.png

Skalierung der X-Achse umschalten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/100018130000350500003505CADD59D81E3150FD.svg
   :width: 60
   :height: 60
   :align: left

Sie können die Skalierung der X-Achse zwischen zwei
verschiedenen Modi umschalten. Standardmäßig zeigt die X-Achse einen
absoluten Zeit- / Datumsstempel an.

|

.. image:: Pictures/100002010000022B0000006E35B772A9B9B293D2.png

Sie können die X-Achse aber auch auf die Anzeige der relativen Zeit in
Sekunden und Millisekunden umschalten. D.h. der Zeitpunkt t\ :sub:`0`
markiert hier den Zeitpunkt an dem die Aufzeichnung gestartet wurde .

.. image:: Pictures/100002010000022B000000660DDD07486701950A.png

Um die Achse umzuschalten, klicken Sie mit der rechten Maustaste in das
Diagramm und wählen Sie dann aus dem Kontextmenü den Punkt
:menuselection:`Toggle X-axis scale`.

.. image:: Pictures/100002010000010D000000C7FB8978837EA08B41.png

Plodaten speichern
~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000040D000035050000350542F550057A626C6D.svg
   :width: 60
   :height: 60
   :align: left

Wenn Sie die Schaltfläche :guilabel:`Save Plot Data` anklicken, werden
alle Plotdaten in eine Datei gespeichert (:file:`*.dat`), die später wieder
in den Plot geladen werden kann.

Plodaten laden
~~~~~~~~~~~~~~

.. image:: Pictures/1000044C000035050000350571A7475A9B633EF8.svg
   :width: 60
   :height: 60
   :align: left

Durch Klicken der Schaltfläche :guilabel:`Load Plot Data` können
Plotdaten, die vorher mit :guilabel:`Save Plot Data` gespeichert wurden wieder in
den Plot geladen werden.

.. admonition:: Important
   :class: note

   Es werden nur die Kurven geladen, die in der
   aktuellen Konfiguration des Loggers vorhanden sind. D.h. wenn Sie Daten
   aufzeichnen, diese mittels *Save Plot Data* speichern und später
   wieder Laden, sollte die **Loggerkonfiguration beim Speichern und Laden
   identisch** sein. Wenn Sie zwischen Speichern und Laden die
   Logger-Konfiguration ändern, z.B. Kanäle entfernen, werden ggf. nicht
   alle Kurven geladen.


.. |image32| image:: Pictures/10002F2F000034EB000034EBDBA40A7FF6EF8292.svg
   :width: 40
.. |image33| image:: Pictures/10001A4C000034EB000034EBE789A979D3788852.svg
   :width: 40
.. |image34| image:: Pictures/100005C7000035050000350518807CBDF5FF2BAE.svg
   :width: 40
.. |image35| image:: Pictures/1000100A000034EB000034EBFC7CEEC6D6B20A4B.svg
   :width: 40
.. |image36| image:: Pictures/10000AAD0000350500003505B065E97D3266EBF3.svg
   :width: 40
.. |image37| image:: Pictures/10000AA70000350500003505B68BB28A6EC24106.svg
   :width: 40
.. |image38| image:: Pictures/10000D410000350500003505737D2F8FEABFA448.svg
   :width: 40
.. |image39| image:: Pictures/10001744000034EB000034EBD90F77816321BB6E.svg
   :width: 40
.. |image40| image:: Pictures/1000032600003505000035052A2D87EA9B64D7C0.svg
   :width: 40
.. |image41| image:: Pictures/100019CB000035050000350509AD2B23340F765E.svg
   :width: 40
.. |image42| image:: Pictures/100018130000350500003505CADD59D81E3150FD.svg
   :width: 40
.. |image43| image:: Pictures/10001855000034EB000034EBA6C6DA993124AA4C.svg
   :width: 40
.. |image44| image:: Pictures/10000FBE000034EB000034EB9506C15D6D175810.svg
   :width: 40
.. |image45| image:: Pictures/1000040D000035050000350542F550057A626C6D.svg
   :width: 40
.. |image46| image:: Pictures/1000044C000035050000350571A7475A9B633EF8.svg
   :width: 40

.. |image58| image:: Pictures/100000000000012100000091DA9FF37806721579.png
.. |image59| image:: Pictures/10000000000001220000008F22C1F8D0316FE153.png


.. |image68| image:: Pictures/Mouse_Wheel_up.png
   :width: 80
.. |image69| image:: Pictures/Mouse_Wheel_down.png
   :width: 80


.. |image79| image:: Pictures/10000AAD0000350500003505B065E97D3266EBF3.svg
   :width: 40
.. |image80| image:: Pictures/10000AA70000350500003505B68BB28A6EC24106.svg
   :width: 40
.. |image81| image:: Pictures/10000D410000350500003505737D2F8FEABFA448.svg
   :width: 40
.. |image82| image:: Pictures/10001744000034EB000034EBD90F77816321BB6E.svg
   :width: 40

.. |icon-num| image:: ../../img/datalogger/property_number.svg
   :width: 40
.. |icon-bool| image:: ../../img/datalogger/property_bool.svg
   :width: 40
.. |icon-text| image:: ../../img/datalogger/property_text.svg
   :width: 40
