Controller Plugin
======================

Einführung
-----------

Das Controller Plugin dient zur Einbindung der Qmix Reglermodule in
die CETONI Elements Software und zur Erzeugung benutzerdefinierter
Regelkreise. Folgende Module werden unterstützt:

.. image:: Pictures/controller_devices.png

.. rst-class:: guinums

#.  *Qmix Q-* - thermoelektrisches Kühlmodul
#.  *Qmix Q+* - zwei-kanaliges Heizmodul
#.  *Qmix TC*– zwei kanaliges Reglermodul für externe Heiz- / Kühlsysteme
    (z.B. für Spritzenheizung und Schlauchheizung)

.. include:: qmixcontroller_common_DE.inc.rst


Regler Script Funktionen
------------------------

Einführung
~~~~~~~~~~

Das Qmix Regler-Plugin enthält eine Script Funktion, um die
Regler-Parameter aus einem Script heraus zu ändern. Damit ist es z.B.
möglich, zeitgesteuerte Temperaturkurven zu realisieren.

.. image:: Pictures/10000201000001240000007754114FA5.png
   :alt: Qmix Regler Script Funktionen

Funktion Reglerparameter setzen - *Set Controller Param*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000067B0000388E0000388E578BCCCA.svg
   :width: 60
   :align: left

Mit dieser Funktion können Sie einen neuen Sollwert an den
Regelkanal übergeben oder den Regelkreis ein- und ausschalten. Klicken
Sie zum Ein- / Ausschalten einfach auf die LED :guilabel:`Control loop on / off`
im Konfigurationsbereich (Abbildung unten).

|

.. image:: Pictures/10000000000001A7000000C4FD6D097D.png
   :alt: Konfiguration Regler Script Funktion

.. _pid_reglerfunktion:

PID Regler Funktion – *PID Control*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Einführung
^^^^^^^^^^^^

.. image:: Pictures/10000B740000388E0000388E0BB445FF.svg
   :width: 60
   :align: left

Die PID Regler Funktion implementiert einen PID-Regler für
Anwendungen, die einen effizienten PID-Algorithmus erfordern. Der
PID-Algorithmus unterstützt die Begrenzung des Ausgangsbereiches mit
Integrator-Anti-Windup-Funktionalität.

Derzeit ist der PID-Algorithmus der am weitesten verbreitete
Regelalgorithmus der in der Industrie verwendet wird. PID Regelkreise
werden u.a. verwendet für die Regelung von Heiz- und Kühlsystemen, für
die Überwachung von Flüssigkeitsständen, für Durchflussregelung und
Druckregelung. Bei der PID Regelung geben Sie eine Prozessvariable und
eine Stellgröße vor. Die Prozessvariable ist dabei der Systemparameter,
den Sie steuern möchten, wie z.B. Druck, Temperatur oder Durchfluss. Der
Sollwert ist der gewünschte Wert für den Parameter welchen Sie regeln
möchten. Der PID Regler berechnet dann die Reglerausgangsgröße wie z.B.
Heizleistung oder Ventilposition. Diese Reglerausgangsgröße wird dann
auf das System angewendet, welches wiederum die Prozessvariable in
Richtung der Stellgröße treibt.

Konfiguration
^^^^^^^^^^^^^^

Im Konfigurationsbereich der Anwendung konfigurieren Sie alle Parameter
die für die PID Funktion benötigt werden.

Die folgenden Parameter müssen konfiguriert werden (siehe Abbildung
unten):

.. rst-class:: guinums

1. **Prozessvariable (Actual Value Input)** – die Prozessvariable ist
   der gemessene Wert der Prozessgröße (z.B. Temperatur) die geregelt
   wird. Dieser Wert ist gleich dem Istwert des Regelkreises. Tragen Sie
   hier eine Variable ein oder greifen Sie über
   einen :ref:`Prozessdatenbezeichner <Device Properties (Prozessdaten)>` direkt
   auf bestimmte Prozessdaten eines Gerätes zu.
2. **Stellgröße (Setpoint)** – geben Sie hier den Sollwert, den
   gewünschten Zielwert ein, auf den die Prozessvariable geregelt werden
   soll. Sie können einen festen Wert eingeben (z.B. 50°C) oder den Wert
   durch eine Variable übergeben.
3. **Reglerparameter (Control Loop Parameters)** – die PID-Verstärkungsfaktoren
   konfigurieren die Proportionalverstärkung (K), Nachstellzeit (T\ :sub:`I`\)
   und Vorhaltezeit (T\ :sub:`D`\) des Reglers und wirken damit
   unmittelbar auf das Regelverhalten des Reglers. Die Wirkung der
   einzelnen Regelparameter wird in folgendem Abschnitt erläutert.

   .. image:: ./Pictures/10000201000001F400000208F1F44DB1.png
      :alt: Konfiguration PID Regler Funktion

4. **Reglerausgang (Controller Output)** – dieser Bereich gruppiert
   alle Einstellungen zum Ausgang des Reglers.
   *Control Value Output* gibt den Ausgangswert des PID Algorithmus
   zurück, der auf den gesteuerten Prozess angewendet werden muss. D.h.
   bei einer Temperaturregelung wäre dieser Wert die Heizleistung die
   vom Heizer erzeugt werden muss. Tragen Sie in das Feld den Namen
   einer Variablen ein, die dann den ausgegebenen Wert speichern kann
   oder verwenden Sie
   einen :ref:`Prozessdatenbezeichner <Device Properties (Prozessdaten)>` um
   direkt die Prozessdaten eines Gerätes zu schreiben.

   .. image:: Pictures/10000000000001D7000000C159F1FF85.png
      :alt: Prozessdatenbezeichner über Kontextmenü eintragen

   Mit den Parametern U\ :sub:`max` und U\ :sub:`min` begrenzen Sie den
   Wertebereich des Reglerausganges. Wenn Sie z.B. über einen analogen
   Ausgang von 0 – 5 V die Heizleistung steuern, dann geben Sie für
   U\ :sub:`min`\ den Wert 0 und für U\ :sub:`max`\ den Wert 5 ein.
   Sollte der Regelalgorithmus Werte erzeugen, die außerhalb des
   Bereiches liegen, werden diese automatisch auf den Bereich begrenzt.

.. admonition:: Tipp
   :class: tip

   Sie können die PID Reglerfunktion auch
   verwenden, um eine P, PI oder PD Regler zu realisieren,
   indem Sie die entsprechenden nicht benötigten
   Verstärkungsfaktoren auf 0 setzen.

PID-Regelparameter
^^^^^^^^^^^^^^^^^^^^

Ein PID-Regelparametersatz besteht aus einem Proportional-, einem
Integrier- und einem Differenzieranteil.

Proportionalanteil
'''''''''''''''''''

Der Proportionalanteil (K-Anteil) bildet aus dem Sollwert (W) und dem
Istwert (X) die Regelabweichung,

.. image:: Pictures/math_01.png
   :scale: 20%

multipliziert diese mit der Proportionalverstärkung K und gibt den
errechneten Wert als Stellgröße (Y) auf die Regelstrecke aus. Der
Proportionalanteil folgt somit folgender Gleichung.

.. image:: Pictures/math_02.png
   :scale: 20%

Integrieranteil
'''''''''''''''

Der Integrieranteil (I-Anteil) bildet mathematisch die Fläche, welche
von Regelabweichung und Zeit *t*\ eingeschlossen wird. Liegt eine
konstante Regelabweichung vor, wird der I-Anteil rampenförmig
hochgefahren.

Für eine gleichbleibende Regelabweichung lautet die Reglergleichung:

.. image:: Pictures/math_03.png
   :scale: 20%

- Y\ :sub:`t0`: Stellgröße zu Beginn der Betrachtung
- T\ :sub:`i`: Integrierzeit

Entspricht der Istwert dem Sollwert verändert sich der Stellwert nicht.
Eine durch den I-Anteil aufgebaute Stellgröße bleibt erhalten. Erst wenn
der Istwert größer als der Sollwert wird, wird der I-Anteil abgebaut.
Bei Strecken mit Verzug (z.B. Temperaturregelstrecke) sorgt der I-Anteil
dafür, dass eine bleibende Regelabweichung ausgeregelt wird. Ein
Proportionalregler allein ist dazu nicht im Stande. Allgemein gilt für
den I-Anteil folgende Gleichung:

.. image:: Pictures/math_04.png
   :scale: 20%

Mit der Nachstellzeit T\ :sub:`I` kann die Geschwindigkeit des I-Anteils
verändert werden. Je kleiner T\ :sub:`I` desto schneller baut der
Integrieranteil seine Stellgröße auf. Aus der Gleichung geht hervor,
dass auch die Proportionalverstärkung K auf den I-Anteil wirkt. In
CETONI Elements können sie den I-Anteil nur in Verbindung mit einem
Proportionalanteil konfigurieren (PI-Regler). Die Reglergleichung
besteht somit immer aus der Summe von K- und I-Anteil.

.. image:: Pictures/math_05.png
   :scale: 20%

.. admonition:: Wichtig
   :class: note

   Der Integrieranteil ist für das Ausregeln
   einer bleibenden Regelabweichung verantwortlich.

Differenzieranteil
''''''''''''''''''

Der Differenzieranteil (D-Anteil) reagiert auf Änderungen des Istwertes
und wirkt diesen entgegen. Zwei Situationen können bezüglich der Wirkung
des D-Anteils betrachtet werden:

-  In einem Regelkreis hat der Istwert einen stabilen Endwert erreicht.
   Auf Grund einer Störung wird der Istwert geringer. Nun liefert der
   D-Anteil einen zusätzlichen positiven Stellwertanteil, welcher hilft,
   den Istwert wieder in Richtung größerer Werte zu bringen.
-  Erfolgt eine Sollwerterhöhung, wird in einem Regelkreis der Istwert
   ebenfalls größer werden. Der D-Anteil erkennt den steigenden Istwert
   und bremst durch einen negativen Stellwertanteil das Anfahren des
   Istwertes auf den neuen Endwert.

Der D-Anteil tritt in der Praxis nur in Verbindung mit einem K-Anteil
auf. Die Reglergleichung lautet.

.. image:: Pictures/math_06.png
   :scale: 20%

Je größer die Proportionalverstärkung K und die Vorhaltezeit
T\ :sub:`D`, desto stärker wirkt der D-Anteil und desto stärker wird der
Änderung der Istgröße entgegengewirkt (gedämpft).

Zusammenfassung
'''''''''''''''

Die folgende Tabelle fast die Wirkung der einzelnen Regelparameter
zusammen.

+---------------+----------------------+----------------------+
| PID-Parameter | Ausregeln einer      | Anfahren des         |
|               | Störung der          | Sollwerts            |
|               | Regelstrecke         | (Führungsverhalten)  |
|               | (Störverhalten)      |                      |
+===============+======================+======================+
| K größer      | stärkere Reaktion    | schnelleres Anfahren |
|               | (schwächer gedämpft) |                      |
+---------------+----------------------+----------------------+
| K kleiner     | schwächerer Reaktion | langsameres Anfahren |
|               | (stärker gedämpft)   |                      |
+---------------+----------------------+----------------------+
| TI größer     | schwächere Reaktion, | langsameres Anfahren |
|               | im Allgemeinen zeigt | und Ausregeln der    |
|               | der I-Anteil nur     | bleibenden           |
|               | eine geringe         | Regelabweichung bei  |
|               | Reaktion, gerade auf | Verzugsstrecken      |
|               | kurzzeitige          |                      |
|               | Störungen            |                      |
+---------------+----------------------+----------------------+
| TI kleiner    | stärkere Reaktion,   | schnelleres Anfahren |
|               | im Allgemeinen zeigt | und Ausregeln der    |
|               | der I-Anteil nur     | bleibenden           |
|               | eine geringe         | Regelabweichung bei  |
|               | Reaktion, gerade auf | Verzugsstrecken      |
|               | kurzzeitige          | (Überschwingen, wenn |
|               | Störungen            | T\ :sub:`I` zu       |
|               |                      | klein)               |
+---------------+----------------------+----------------------+
| TD größer     | stärkere Reaktion    | langsameres Anfahren |
|               |                      | (stärkere Wirkung    |
|               |                      | gegen                |
|               |                      | Istwertänderung)     |
+---------------+----------------------+----------------------+
| TD kleiner    | schwächere Reaktion  | schnelleres Anfahren |
|               |                      | (geringere Wirkung   |
|               |                      | gegen                |
|               |                      | Istwertänderung)     |
+---------------+----------------------+----------------------+

Programmierung des Regelkreises
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dieser Abschnitt zeigt Ihnen, wie Sie mit Hilfe der PID Regler Funktion
einen PID Regler in einem Scriptprogramm realisieren.

.. image:: Pictures/10000201000001A3000000BAB53FB1F8.png
   :alt: PID Regler Beispielscript

Um einen Regelkreis zu realisieren, gehen Sie wie folgt vor:

.. rst-class:: guinums

1. Der Regler muss zyklisch in einem festen Zeitintervall aufgerufen
   werden. Dafür verwenden Sie eine Schleife. In diesem Fall verwenden
   Sie eine `Conditional Loop` mit
   der Schleifenbedingung 1 - also eine Schleife die endlos läuft und
   nie abbricht, außer der Anwender stoppt das Scriptprogramm.
2. Nun erzeugen Sie eine :ref:`PID Regler Funktion<pid_reglerfunktion>` innerhalb der
   Schleife und konfigurieren alle Parameter.
3. Innerhalb der Schleife wird nun die :ref:`Verzögerungsfunktion<verzögerungsfunktion>`
   aufgerufen um eine definierte Verzögerungszeit von 200 Millisekunden
   einzufügen. Diese Zeit legt damit die Häufigkeit fest, mit der der
   Regelalgorithmus aufgerufen wird und damit das *dt* welches im
   Algorithmus bei der Berechnung der Regelparameter verwendet wird.

Damit haben Sie einen einfachen Regelkreis aufgebaut, der alle 200
Millisekunden die PID Regler Funktion aufruft.

.. admonition:: Tipp
   :class: tip

   Laut Regelungstheorie muss ein
   Regelungssystem einen physikalischen Prozess mit einer
   10 mal höheren Geschwindigkeit abtasten, als die
   schnellste Zeitkonstante in diesem physikalischen
   Prozess. Zum Beispiel ist eine Zeitkonstante von 60 s
   typisch für einen Temperaturregelkreis in einem kleinen
   System. In diesem Fall ist eine Zykluszeit von etwa 6 s
   ausreichend. Eine höhere Frequenz führt dann nicht zu
   einer Verbesserung der Leistung des Reglers.


.. include:: qmixcontroller_pid_DE.inc.rst
