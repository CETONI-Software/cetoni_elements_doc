Tubing Pump Plugin
==================

Introduction to Tubing Pump Plugin
-----------------------------------

.. image:: Pictures/1000000000000068000000579F580EDEB3E6712F.png
   :align: left

Press the :guilabel:`Tubing Pump` button in the side bar to show the tubing 
pump view. The view shows the operating panels for all tubing pumps.

|

.. image:: Pictures/10000000000002370000016FE8244C6EB3A2238E.png

Tubing Pump Operating Panel
---------------------------

Operating Parameters
~~~~~~~~~~~~~~~~~~~~


.. image:: Pictures/10000000000000BC0000016FB42FD11BDAB75F52.png

.. rst-class:: guinums

#. Pump Caption (customizable)
#. Tubing configuration (inner diameter)
#. Target value (flow rate, volume)
#. Start / stop dosing button
#. Activity and dosed volume indicators

Pump Caption
~~~~~~~~~~~~~~~~~~~~~~~

You can change the caption of each pump at any time to reflect the
function or fluids of the respective pump. To change the caption label,
directly click the description :guinum:`❶` and type in the new name.

Tubing Configuration
~~~~~~~~~~~~~~~~~~~~

The input box :guilabel:`Tube` :guinum:`❷` shows the name of the currently configured
tubing. Click on the wrench symbol right of the input area to change
the tubing configuration. This will open the *Tube Selection* dialog
(figure below).

.. image:: Pictures/100002010000020B0000018E4422B75A9DD5CE30.png

In the Tube Selection dialog you can either choose from a list of available 
tubes :guinum:`❶`, or define your own tube in the :guilabel:`Custom Tube` section 
:guinum:`❷`.

To select an existing tube, simply click on it in the list :guinum:`❶` and confirm
the selection by clicking :guilabel:`OK`. In the list, the name of each tube is
displayed in the first column (*tube*). The value in the second column
(*Milliliters per pumphead revolution*) indicates how many milliliters
are pumped during a complete revolution of the pump head.

If you want to configure your own tube, you can do this in the :guilabel:`Custom Tube`
:guinum:`❷` section. Enter a name for the tube and the millilitres that are
pumped through this tube during one revolution of the pump head. Confirm
the configuration by clicking :guilabel:`OK`.

Manual Dosing
-------------

Proceed as follows to configure a manual dosing task:

.. image:: Pictures/10000000000000BC000000EA4601210AAF5F0BB0.png

.. rst-class:: guinums

1. Enter your target flow rate in the :guilabel:`Flow` input box. A
   negative flow value causes a change in the rotating direction of the
   pump head. So you can switch between dispensing and aspiration by
   switching the sign of the entered flow value.
2. Now enter the volume to be dosed in the input box :guilabel:`Target Volume`.
   If you set the target volume to zero, the pump will be working in
   flow mode, i.e., the pump will work until manually stopped. A
   negative volume causes a change in the rotating direction of the pump
   head.
3. Start the pump by clicking :guilabel:`Start Dosage` and stop it by clicking
   the same button again.
4. The :guilabel:`Dosed Volume` info box will show the progress of the pumping
   process.

.. tip::
   The software treats a dosing volume set to     
   zero as unlimited continual flow. This is, once started, 
   the pump will continue to operate until it is manually   
   stopped by the user. 

.. tip::
   You can switch between dispensing and          
   aspiration by switching the sign of the entered flow or  
   volume value.

Script Functions
----------------

The plugin offers a number of script functions which can be used to
program automatic sequences or for time-controlled dosing of liquids.
The following script functions are available:

.. image:: Pictures/100002010000013E00000090BB3C192C92C4530C.png

Pump Volume
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000090100003505000035055D465DF5B68FF7A7.svg
   :width: 60
   :align: left

With this function, you can pump a specific volume at a
precisely defined flow rate. You can set all the parameters in the
configuration area, for example the dosing module :guinum:`❶`, the volume to be
dosed, and the flow rate :guinum:`❷`.

.. image:: Pictures/10000000000001EE000000FFE3C6610DEDC51BB5.png

You can also activate or deactivate the *Run to completion* :guinum:`❸` parameter in the
configuration area. When *Run to completion* is activated, the script execution is not
continued until the complete volume has been dosed and the dosing
process has ended. If this parameter is not active, the dosing is
started, and then the next script function is executed immediately. This
enables you, for example, to start a number of dosing modules almost
simultaneously.

.. tip::
   All the pump functions support the use of     
   variables. That means, in all input fields marked with  
   a coloured V in the script configuration panel (e.g.    
   flow rate and volume) you can enter variables.

Generate Flow
~~~~~~~~~~~~~

.. image:: Pictures/10000990000035050000350554270FC6A841A39C.svg
   :width: 60
   :align: left

This function is used to generate a constant flow rate. In
the configuration area, you can select the dosing module and set the
flow rate. If the *Run to completion* parameter is active, the next
script function is not executed until the module has stopped or reached
one of the limit positions.

Stop Pumping
~~~~~~~~~~~~

.. image:: Pictures/1000148E000034EB000034EB84F72DE5B6C09574.svg
   :width: 60
   :align: left

You can immediately stop an active dosing process of a pump
with this function.
