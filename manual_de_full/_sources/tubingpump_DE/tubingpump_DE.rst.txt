Schlauchpumpen Plugin
=====================

Einführung
----------

.. image:: Pictures/1000000000000068000000579F580EDEB3E6712F.png
   :align: left

Drücken Sie die Schaltfläche :guilabel:`Tubing Pump` in der Seitenleiste, um 
den Schlauchpumpe-View anzuzeigen. Der View zeigt die Bedienpanels für alle 
Schlauchpumpen an.

|

.. image:: Pictures/10000000000002370000016FE8244C6EB3A2238E.png
   :alt: Tubing Pump Arbeitsbereich

Schlauchpumpen Bedienpanel
--------------------------

Bedienelemente
~~~~~~~~~~~~~~

.. image:: Pictures/10000000000000BC0000016FB42FD11BDAB75F52.png

.. rst-class:: guinums

#. Pumpenbeschriftung (anpassbar)
#. Konfiguration der Schläuche (Innendurchmesser)
#. Zielwert (Durchflussmenge, Volumen)
#. Dosierung starten / stoppen -Taste
#. Indikatoren für Aktivität und dosiertes Volumen


Beschriftung ändern
~~~~~~~~~~~~~~~~~~~

Die Beschriftung der Pumpe kann von Ihnen jederzeit neu vergeben werden
um bestimmte Substanzen oder Nährmedien, die mit der Pumpe dosiert
werden, zu kennzeichnen. Klicken Sie zum Ändern der Beschriftung einfach
auf die Beschriftung :guinum:`❶` und geben Sie dann einen neuen Namen für die
Pumpe ein.

Schlauchkonfiguration
~~~~~~~~~~~~~~~~~~~~~

In dem Feld :guilabel:`Tube` :guinum:`❷` wird der Name des aktuell konfigurierten Schlauches
angezeigt. Klicken Sie zum Ändern der Schlauchkonfiguration auf den
Knopf mit dem Schraubenschlüssel rechts neben dem Eingabefeld.

.. image:: Pictures/100002010000020B0000018E4422B75A9DD5CE30.png
   :alt: Schlauch Auswahl Dialog

In dem Schlauch Auswahl Dialog
(*Tube Selection*) der nun angezeigt wird (Abbildung oben), können Sie
den Schlauch konfigurieren. Sie können dafür entweder aus einer Liste
von vorhandenen Schläuchen wählen :guinum:`❶`, oder einen eigenen Schlauch im
Bereich :guilabel:`Custom Tube` :guinum:`❷` definieren.

Zur Auswahl eines vorhandenen Schlauches, klicken Sie diesen einfach in
der Liste :guinum:`❶` an und bestätigen die Auswahl durch Klicken auf :guilabel:`OK`. In der
Liste wird Ihnen für jeden Schlauch in der ersten Spalte (*Tube*) der
Name angezeigt. Der Wert in der zweiten Spalte (*Milliliters per
pumphead revolution*) zeigt an, wie viel Milliliter bei einer
vollständigen Umdrehung des Pumpenkopfes gefördert werden.

Wenn Sie einen eigenen Schlauch konfigurieren möchten, geben Sie im Bereich 
:guilabel:`Custom Tube` :guinum:`❷` einen Namen für den Schlauch ein und die 
Milliliter, die bei einer Umdrehung des Pumpenkopfes durch diesen Schlauch gefördert 
werden. Bestätigen Sie dann auch hier die Konfiguration durch Klick auf *OK*.


Manuelle Dosierung
------------------

Um manuell zu Dosieren, gehen Sie wie folgt vor:

.. image:: Pictures/10000000000000BC000000EA4601210AAF5F0BB0.png
   :alt: Manuelle Dosierung

.. rst-class:: guinums

1. Geben Sie zuerst im Feld :guilabel:`Flow` die
   gewünschte Flussrate ein. Negative Flussraten bewirken eine Änderung
   der Drehrichtung des Pumpenkopfes. Sie können somit abgeben und
   aufsaugen.
2. Geben Sie dann im Feld :guilabel:`Target Volume` das Volumen, welches Sie
   dosieren möchten. Wenn Sie für das Volumen den Wert 0 eingeben,
   dosiert die Pumpe im Flussmodus. D.h. Die Pumpe dosiert solange, bis
   die Dosierung wieder manuell gestoppt wird. Ein negatives Volumen
   bewirkt eine Änderung der Drehrichtung des Pumpenkopfes.
3. Klicken Sie die Schaltfläche :guilabel:`Start Dosage` um die Dosierung zu
   starten und ein zweites Mal um die Dosierung wieder zu stoppen.
4. Im Bereich :guilabel:`Dosed Volume` wird nun der Fortschritt bei der Dosierung
   angezeigt

.. admonition:: Tipp
   :class: tip

   Ein Volumen von 0 kennzeichnet eine            
   unbegrenzte kontinuierliche Förderung. D.h. nach dem     
   Start der Pumpe fördert diese solange, bis die Dosierung 
   vom Anwender gestoppt wird.  

.. admonition:: Tipp
   :class: tip

   Durch Eingabe von negativen Werten im Feld     
   Flussrate, können Sie die Drehrichtung der Pumpe         
   umdrehen (z.B. für Saugbetrieb).    


Script Funktionen
-----------------

Das Schlauchpumpen-Plugin bietet eine Reihe von Scriptfunktionen die für
die Programmierung von automatischen Abläufen und Dosierplänen verwendet
werden können. Die folgenden Scriptfunktionen sind verfügbar:

.. image:: Pictures/100002010000013E00000090BB3C192C92C4530C.png
   :alt: Pumpen Scriptfunktionen

Funktion Volumendosierung - *Pump Volume*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000090100003505000035055D465DF5B68FF7A7.svg
   :width: 60
   :align: left

Mit dieser Funktion können Sie ein bestimmtes Volumen mit
einer genau definierten Flussrate dosieren. Alle Parameter, wie die
Pumpe :guinum:`❶`, das zu dosierende Volumen und die Flussrate :guinum:`❷` stellen Sie im
Konfigurationsbereich ein.

.. image:: Pictures/10000000000001EE000000FFE3C6610DEDC51BB5.png
   :alt: Pump Volume Script Konfiguration

Zusätzlich können Sie
im Konfigurationsbereich noch den Parameter *Run to completion* :guinum:`❸` ein-
oder ausschalten. Wenn *Run to completion* aktiviert ist, wir die
Skriptausführung erst fortgesetzt, wenn das komplette Volumen dosiert
wurde und der Dosiervorgang beendet ist. Ist dieser Parameter nicht
aktiv, wir die Dosierung gestartet, und dann sofort die nächste
Scriptfunktion bearbeitet. Damit können Sie z.B. mehrere Dosiermodule
nahezu gleichzeitig starten.

.. admonition:: Tipp
   :class: tip

   Alle Pumpfunktionen unterstützen die          
   Verwendung von Variablen. D.h. in allen Eingabefeldern  
   die im Konfigurationsbereich mit einem gelben V         
   gekennzeichnet sind (z.B. Flussrate und Volumen) können 
   Sie Variablen eintragen. 


Funktion Konstanter Fluss - *Generate Flow*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/10000990000035050000350554270FC6A841A39C.svg
   :width: 60
   :align: left

Diese Funktion dient zur Erzeugung einer konstanten
Flussrate. Im Konfigurationsbereich können Sie das Dosiermodul auswählen
und die Flussrate einstellen. Wenn der Parameter *Run to completion*
aktiv ist, wird die nächste Skriptfunktion erst bearbeitet, wenn das
Modul manuell vom Anwender gestoppt wurde.

Funktion Dosierung stoppen - *Stop Pumping*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000148E000034EB000034EB84F72DE5B6C09574.svg
   :width: 60
   :align: left

Mit dieser Funktion können Sie einen aktiven Pumpvorgang einer Pumpe sofort stoppen.