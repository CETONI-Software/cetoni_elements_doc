Ventil Plugin
==================

Einführung
----------

Das Ventil Plugin dient zur Steuerung der QmixV Ventil Module oder von
Ventilen, die Teil anderer Geräte sind (z.B. Ventile der Nemesys
Spritzenpumpen).

.. image:: Pictures/valve_devices_numbered.jpg
   :alt:  QmixV Ventil-Geräteliste

.. rst-class:: guinums

#. CETONI QmixV Ventilmodule
#. Ventilgeräte, die Teil anderer Geräte sind (z.B. Ventile, die auf Nemesys
   Spritzenpumpen montiert sind)
#. Unterstützte Ventile von anderen Herstellern (z.B. VICI-Ventile)


.. include:: qmixv_common_DE.inc.rst


Ventil Script Funktionen
-------------------------

.. image:: Pictures/10000201000000F70000003E8592638162A9459E.png

Das Ventil-Plugin enthält eine Script Funktion für das Umschalten
der Ventile aus einem Script heraus.

Funktion Ventil umschalten - Switch Valve
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/10002F3400003505000035057520F6A9E5AEC280.svg
   :width: 60
   :align: left

Verwenden Sie diese Funktion zum Umschalten der
Ventilposition. Im Konfigurationsbereich dieser Funktion können Sie das
Ventilmodul auswählen :guinum:`❶` und die Zielposition :guinum:`❷` an die das Ventil
geschaltet werden soll. Das Vorschaubild visualisiert die ausgewählte Zielposition :guinum:`❸`.

.. image:: Pictures/10000000000001A3000000A14DDC5565A638D882.png
   :alt: Konfiguration Scriptfunktion Switch Valve

Beide Auswahlboxen unterstützen die Verwendung von Variablen. Das heißt, in der
Geräteauswahlbox :guinum:`❶` können Sie eine Variable verwenden, die eine
Ventilgerätereferenz enthält.
In der Zielpositionsauswahlbox :guinum:`❷` können Sie eine Skriptvariable verwenden,
die einen Zielpositionsindex enthält.

Das folgende Beispiel zeigt ein Skript, das zwei Variablen :guinum:`❶` erstellt.
Die Variable :code:`$ProcessValve` speichert die Gerätereferenz auf das Ventilgerät
**Valve_0**. Die Variable :code:`$RefillPosition` speichert die Zielposition des
Ventils für das Nachfüllen der Spritze.

.. image:: Pictures/switch_valve_variables.png

Diese Variablen werden dann im Skript *Switch Valve* :guinum:`❷` für die Definition
von :guilabel:`Valve` und :guilabel:`Target Position` verwendet.


Unterstützte VICI-Ventile
--------------------------

Das Valve Plugin unterstützt VICI-Ventile mit USB- oder RS-232-Schnittstelle.

.. tip::
   Bei der Verwendung eines Ventils mit RS-232-Schnittstelle kann es zu Problemen bei der Kommunikation kommen, wenn Sie das Ventil über eine physische RS-232-Schnittstelle an Ihrem PC anschließen.

   Verwenden Sie stattdessen einen USB-zu-Seriell-Adapter und schließen Sie das Ventil darüber per USB an Ihren PC an!


.. image:: Pictures/Vici_Valve.jpg

Die folgende Liste zeigt alle Typen von VICI-Ventilen, die von der Software
unterstützt werden:

.. list-table::
   :widths: 20 80
   :header-rows: 0

   * - |image-vici-10pos11port|
     - 10-Positionen-Selektionsventil (SD) (z.B. `Niedrigdruck <https://www.vici.com/vval/sd.php>`_, `Hochdruck <https://www.vici.com/vval/sduw.php>`_)
   * - |image-vici-6pos7port|
     - 6-Positionen-Selektionsventil (SD) (z.B. `Niedrigdruck <https://www.vici.com/vval/sd.php>`_, `Hochdruck <https://www.vici.com/vval/sduw.php>`_)
   * - |image-vici-2pos6port|
     - 6-Port Injektionsventil (z.B. `GC Einspritzdüsen <https://www.vici.com/vval/vval_gc.php>`_, `HPLC-Einspritzdüsen <https://www.vici.com/vval/vval_hplc.php>`_)


.. |image-vici-10pos11port| image:: Pictures/10Pos11Port_PositionIcon0.svg
   :width: 60

.. |image-vici-6pos7port| image:: Pictures/6Pos7Port_PositionIcon0.svg
   :width: 60

.. |image-vici-2pos6port| image:: Pictures/2Pos6Port_PositionIcon1.svg
   :width: 60
