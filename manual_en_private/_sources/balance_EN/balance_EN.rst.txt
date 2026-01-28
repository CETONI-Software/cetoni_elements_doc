Balances Plugin
===============

.. image:: Pictures/Balance_Header.png

Introduction to Balances Plugin
-------------------------------

This plugin is for integrating external laboratory balances into the
software. The following devices are currently supported:

============ ==============================
Manufacturer Supported Devices
============ ==============================
Sartorius    Entris, ED-, GK- and GW-scales
============ ==============================

Configuration of Sartorius Scales
---------------------------------

In order for the scale to work optimally with the software,
please set the following parameters on the device:

Device / RS232 Menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the DEVICE / RS232 menu, activate the following values marked in red:

.. image:: Pictures/10000201000003DA000002F7CD3B422CA333C488.png

Device / USB Menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the DEVICE / USB menu, activate the following values marked in red:

.. image:: Pictures/10000201000003DA000002F7CD3B422CA333C488.png

DATA.OUT. / COM. SBI Menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the DATA.OUT. / COM. SBI menu, activate the following values marked
in red:

.. image:: Pictures/10000201000003CC0000020A56B0A6CD74551F66.png

Adding a scale to a CETONI Elements device configuration
--------------------------------------------------------

In the *Device Configurator*, simply add a scale to the current device
configuration using drag & drop or double-click :guinum:`❶`. Then save the device
configuration :guinum:`❷` and activate it by clicking the :guilabel:`Activate Configuration`
button :guinum:`❸`.

.. image:: Pictures/1000020100000327000001CE56CDCFBB84CBB896.png

Operation
---------

Display / Read the values
~~~~~~~~~~~~~~~~~~~~~~~~~

For each balance that has been added to the device configuration, an
analogue input channel is displayed in the list of I/O channels. In the
picture below, this is the :guilabel:`Sartorius Balance 1` channel.

.. image:: Pictures/1000020100000193000000C89CA159222396D53F.png

This analogue channel shows the current value measured by the scale in
the *Value* column. Like any other analogue channel, this channel can be
added in the graphical logger or CSV logger or read in the script.

Tare balance
~~~~~~~~~~~~

To tare the balance, right-click on the channel :guinum:`❶` and then select
:menuselection:`Tare balance` :guinum:`❷` from the context menu.

.. image:: Pictures/10000201000001DA000000CA6CD29A54C4B5F66A.png

The taring of the scale can also be carried out in a script. To do this,
add the script function :guilabel:`Device Functions --> Write Device Property` :guinum:`❶` to
the script. Configure this function so that the value 1 :guinum:`❷` is written to
the property :code:`Tare` :guinum:`❸` of the scale channel (see figure below).

.. image:: Pictures/100002010000030A0000016ABF280E02DB3E0E44.png
