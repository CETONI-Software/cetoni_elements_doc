Vorgehensweise für die Einstellung von Reglerparametern
-------------------------------------------------------

Einfacher geschlossener Regelkreis und PID-Reglergleichung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Der Regler (z.B. PID-Regler) und die zu regelnde Strecke (z.B. zu
temperierendes System) bilden zusammen ein rückgekoppeltes System, den
einfachen geschlossenen Regelkreis. (siehe Abbildung unten)

.. image:: Pictures/1000020100000345000000BBD9E22878.png
   :alt: Einfacher geschlossener Regelkreis

Ein PID-Regler
ermittelt hierbei die Stellgröße *u* zum Zeitpunkt t\ :sub:`1` nach
folgender Gleichung.

.. image:: Pictures/math_08.png
   :scale: 20%

Die Stellgröße enthält 3 Anteile.

+----------+----------------------------------+
| |math09| | Der Proportionalanteil (P-Anteil)|
|          | bildet mittels des Faktors       |
|          | K\ :sub:`p` die direkte          |
|          | Auswirkung des Fehlers auf die   |
|          | Stellgröße.                      |
+----------+----------------------------------+
| |math10| | Der Integrieranteil (I-Anteil)   |
|          | errechnet die zeitliche Summe    |
|          | des Fehlers und bildet sie       |
|          | mittels K\ :sub:`p` und der      |
|          | Zeitkonstanten T\ :sub:`i` auf   |
|          | die Stellgröße ab. Je größer     |
|          | K\ :sub:`p` und je kleiner       |
|          | T\ :sub:`i`\ desto größer wird   |
|          | der I-Anteil der Stellgröße.     |
+----------+----------------------------------+
| |math11| | Der Differenzieranteil (D-Anteil)|
|          | richtet sich nach den zeitlichen |
|          | Änderungen des Istwertes und     |
|          | bildet diese über K\ :sub:`p` und|
|          | T\ :sub:`D` auf die Stellgröße   |
|          | ab.                              |
+----------+----------------------------------+


Vorbereitung der Reglereinstellung in CETONI Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Zunächst sollten sie sich den aktuellen Wert und die Stellgröße ihres
Regelkanals im Plot des Data-Loggers anzeigen lassen. (siehe Kapitel
:ref:`CSV-Datenlogger`)
Sie können sich auch den Sollwert anzeigen lassen :guinum:`❶` . Dies ist nicht
unbedingt erforderlich, da sie ihn im Allgemeinen kennen, erleichtert
aber die Orientierung im Plot. (siehe Abbildung unten)

.. image:: Pictures/100002010000033E000001B1025EE03C.png
   :alt: Konfiguration des graphischen Loggers für die Reglereinstellung

Die Einstellung im Bereich :guilabel:`Log Interval` :guinum:`❷` hängt von
der Änderungshäufigkeit des aktuellen Wertes des Reglerkanals ab. Sie
sollten einen brauchbaren Graphen erhalten, wenn sie für Log Interval
die gleiche Größe benutzen, die sie für den Wert Sample Time ihres
Reglerparametersatzes verwendet haben.

Auswahl des Parameters Sample Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Der Parameter Sample Time ist definiert als die Zeitdauer zwischen zwei
Berechnungen der Stellgröße des Reglers. Je kleiner dieser Wert gewählt
wird desto häufiger wird die Stellgröße berechnet. Als Faustformel kann
man sich merken, dass Sample Time nicht größer als ein Zehntel der
kleinsten im Regelkreis vorkommenden Zeitkonstante sein sollte.
Erfahrungsgemäß konnten bei folgenden Geräten mit den angegebenen
Zeitkonstanten brauchbare (stabile Regelung) Ergebnisse erzielt werden:

========================================= ================
Anwendung                                 Sample Time (ms)
========================================= ================
Qmix Q+                                   500
Druckregelung mit Nemesys und Qmix p      50
========================================= ================

.. admonition:: Tipp
   :class: tip

   Für die Sample Time sollten Werte gewählt
   werden, die kleiner oder gleich 1/10 der kleinsten im
   Regelkreis vorkommenden Zeitkonstante sind.


Festlegen der Stellgrößengrenzen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die minimale (U\ :sub:`min`) und maximale (U\ :sub:`max`) Stellgröße der
CETONI Elements-Regler kann limitiert werden. Die Stellgrößen sollten über
einen ausreichenden Hub verfügen, sodass die angestrebten Sollwerte
erreicht werden können. Gleichzeitig sollten sie darauf achten, dass
ihre Regelstrecke nicht durch zu groß gewählte Grenzwerte beschädigt
wird. (z.B. zu hohe Flußrate eines Nemesys Dosiersystems bei
Druckregelung führt zur Zerstörung des fluidischen Systems) Dies sollten
sie testen, indem sie ihre Regelstrecke mit dem oberen und unteren Limit
der Stellgröße beaufschlagen. (z.B. mit Flußrate, die dem
Stellgrößenlimit entspricht, dosieren) Weiterhin müssen sie einen Wert
wählen, den die Stellgröße annehmen soll, wenn der Reglerkanal
deaktiviert (U\ :sub:`disabled`) wird (im Allgemeinen Null).

.. admonition:: Achtung
   :class: caution

   Unzureichende Limitierung der Stellgrößen
   kann zur Beschädigung ihres zu regelnden Systems
   führen.

Ermittlung von PI-Reglerparametern am Beispiel einer Temperaturregelstrecke
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Eine Temperaturregelstrecke ist im Allgemeinen eine Regelstrecke welche
eine oder mehrere Verzögerungszeitkonstanten enthält. Häufig kann sie
durch eine Verzögerungstrecke 1. Ordnung approximiert werden.
Nachfolgend die Sprungantwort einer Verzögerungstrecke 1. Ordnung im
Bildbereich.

.. image:: Pictures/math_12.png
   :scale: 20%

Ziel der Reglereinstellung ist es, die Streckenzeitkonstante T\ :sub:`1`
zu kompensieren und die Reglerverstärkung K\ :sub:`p` anzupassen, sodass ein
gutes Führungsverhalten des geschlossenen Regelkreises erzielt wird. Da
T\ :sub:`1` in der Praxis häufig nicht bekannt ist, kann man sich durch
folgendes Verfahren schrittweise einem brauchbaren Ergebnis annähern.

.. image:: Pictures/graph01.png

.. rst-class:: steps

#. Die Werte für Sample Time, U\ :sub:`min`, U\ :sub:`max`
   und U\ :sub:`disabled` wählen sie entsprechend der Empfehlungen in den vorangegangenen Abschnitten.
   Die Werte der einzelnen Reglerzeitkonstanten setzen sie zu Null.
   Hiermit deaktivieren sie den I- und D-Anteil des PID-Reglers.
   Hieraus folgt eine vereinfachte Reglergleichung.

   .. math:: U = {K_{p} \cdot e}

   Wählen sie für den P-Anteil einen moderaten Verstärkungsfaktor.
   Bedenken sie, dass sich der Fehler der Regelgröße über K\ :sub:`p`
   direkt auf die Stellgröße U auswirkt. Ein zu großer Wert für
   K\ :sub:`P` kann den Regler somit permanent in die Sättigung
   treiben.

#. Beaufschlagen sie ihren Regelkreis mit einem Sollgrößensprung, zum
   Beispiel indem sie die Solltemperatur von Raumtemperatur auf 50°C
   ändern und die Regelung aktivieren. (siehe Abschnitt
   :ref:`Sollwert eingeben` und :ref:`Regelung ein- / ausschalten`)

#. Bei einer Verzögerungsstrecke 1. Ordnung wird sich der Istwert wie
   in folgender Abbildung dargestellt verhalten.

   .. image:: Pictures/graph02.png

   In Abhängigkeit von der gewählten
   Reglerverstärkung K\ :sub:`p` wird sich die Istgröße unterschiedlich
   schnell in die Nähe des Sollwertes begeben. Außerdem wird sich eine
   bleibende Regelabweichung einstellen. Ein P-Regler ist nämlich nicht
   in der Lage eine Verzögerungstrecke 1. Ordnung vollständig
   auszuregeln. Ist K\ :sub:`p` zu klein eingestellt, verläuft die
   Istwertkurve zu flach und es dauert sehr lang, bis sich der Istwert
   in der Nähe des Sollwertes befindet. (siehe Abbildung oben, Verlauf
   für K\ :sub:`p` = 1) Ein zu großer Wert für K\ :sub:`p` führt
   dagegen zum Überschwingen, gegebenenfalls zu einer Dauerschwingung
   um den Sollwert. (siehe Abbildung oben, Verlauf für K\ :sub:`p` =
   1)  Im dargestellten Beispiel erreicht der Istwert bei K\ :sub:`p` =
   3 recht zügig einen stationären Wert ohne überzuschwingen. Aus
   diesem Grund kann man mit diesem Wert weiterarbeiten.

#. Im nächsten Schritt müssen sie T\ :sub:`i` so einstellen, dass die
   bleibende Regelabweichung verschwindet. Beginnen sie zunächst mit
   einer großen Zeitkonstanten T\ :sub:`i` (kleiner Integrieranteil).

#. Beaufschlagen sie ihren Regelkreis mit einem Sollgrößensprung, zum
   Beispiel indem sie die Solltemperatur von Raumtemperatur auf 50°C
   ändern und die Regelung aktivieren. (siehe Abschnitt
   :ref:`Sollwert eingeben` und :ref:`Regelung ein- / ausschalten`)

#. Sie können die Zeitkonstante T\ :sub:`i` verringern, wenn sie die
   Zeit bis zum dauerhaften Erreichen des Sollwertes verringern
   möchten. Sie müssen hierbei beachten, dass eine zu klein gewählte
   Zeitkonstante T\ :sub:`i` (großer Integrieranteil) zum Schwingen des
   Regelkreises führen kann. Im dargestellten Diagramm kann man sehen,
   dass eine Integrierzeitkonstante von T\ :sub:`i`\ =260s ein gutes
   Ergebnis liefert. Die Istgröße entspricht der Sollgröße und das
   System schwingt nicht. Mit T\ :sub:`i` = 1000s wird im dargestellten
   Zeitbereich die Sollgröße überhaupt nicht erreicht.
   T\ :sub:`i`\ =20s führt zu einem starken Überschwingen des Systems.
   (siehe Abbildung unten)

   .. image:: Pictures/10000000000001A7000000C4FD6D097D.png

#. In sehr vielen Fällen (z.B.
   Temperaturregelung) ist ein PI-Regler vollkommen ausreichend. Im
   stationären Zustand verbleibt keine Regelabweichung und die Dynamik
   ist zufriedenstellend. Soll der Regler auch robust gegenüber
   plötzlich auftretenden Störungen sein, so kann es sinnvoll sein,
   einen Differenzieranteil einzubeziehen. Die detaillierte Behandlung
   von Stabilität, Führungs- und Störverhalten der unterschiedlichen
   Regelkreissysteme würde diese praxisnahe Einführung übersteigen.
   Deshalb wird an dieser Stelle auf die Regelungstechnikliteratur
   verwiesen.

   .. image:: Pictures/graph03.png

#. Erstellen Sie nun ein PID Parameter Preset mit den Werten die Sie
   ermittelt haben und vergeben Sie einen eindeutigen Namen.





.. |image1| image:: Pictures/10004AA90000387200003872C4D36C50.svg
   :width: 40

.. |image2| image:: Pictures/100051AC0000387200003872CA0648E8.svg
   :width: 40

.. |image3| image:: Pictures/100046F500003872000038724548056A.svg
   :width: 40



.. |image18| image:: Pictures/10000BB30000388E0000388E998532D4.svg
   :width: 40

.. |image19| image:: Pictures/1000046A0000388E0000388EB24BAE1A.svg
   :width: 40

.. |image20| image:: Pictures/100002C10000388E0000388E08119BA0.svg
   :width: 40

.. |image21| image:: Pictures/100010A40000388E0000388EA92DC2A7.svg
   :width: 40

.. |image22| image:: Pictures/10000AC700003872000038724DFCC517.svg
   :width: 40

.. |image23| image:: Pictures/100015FC00003872000038727653FE88.svg
   :width: 40

.. |image24| image:: Pictures/100015DE0000387200003872946736F7.svg
   :width: 40



.. |math09| image:: Pictures/math_09.png
   :scale: 20%

.. |math10| image:: Pictures/math_10.png
   :scale: 20%

.. |math11| image:: Pictures/math_11.png
   :scale: 20%
