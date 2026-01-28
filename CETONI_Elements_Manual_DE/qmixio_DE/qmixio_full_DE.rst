.. include:: qmixio_common_DE.inc.rst

I/O Script-Funktionen
-----------------------

Einführung
~~~~~~~~~~

Das I/O Plugin enthält Script-Funktionen zum Schalten der digitalen
Ausgänge und zum Setzten von Ausgangswerten der analogen Ausgänge.

.. image:: Pictures/1000020100000123000000778D7426E56265EAC3.png
   :alt: I/O Script-Funktionen

Funktion Digitalausgang setzen - *Set Digital Out*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000064300003505000035054FDB6D797453998C.svg
   :width: 60
   :align: left

Verwenden Sie diese Funktion zum Setzen bzw. Löschen eines
Digitalausgangs aus einem Script heraus. Wählen Sie im
Konfigurationsbereich der Funktion den digitalen Kanal aus und stellen
Sie dann den gewünschten Ausgangswert ein.

|

Funktion Analogausgang setzen - *Set Analog Out*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/10000F0E00003505000035054CE4E2663723FE52.svg
   :width: 60
   :align: left

Mit dieser Funktion können Sie aus einem Script heraus einen
Wert auf einen analogen Ausgangskanal schreiben. Wählen Sie dafür im
Konfigurationsbereich den analogen Kanal aus und konfigurieren Sie dann
den analogen Ausgangswert, der später beim Ausführen der Funktion
gesetzt werden soll.

Diese Funktion unterstützt die Verwendung von Variablen. D.h., im Feld
:guilabel:`Value` können Sie, statt eines Wertes, den Namen einer Variablen
eintragen, die den analogen Ausgangswert zur Laufzeit des Scripts
enthält (siehe Abbildung unten). Diese Variable kann dann anschließend für
Berechnungen oder zur Ausführung von wertbezogenen Funktionen verwendet werden.

.. image:: Pictures/1000020100000218000000BA59FD4FDF9E3D6F7B.png
   :alt: Set Analog Out Scriptkonfiguration

.. include:: qmixio_beckhoff_DE.inc.rst
