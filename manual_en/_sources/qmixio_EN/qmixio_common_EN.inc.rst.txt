I/O Plugin
===============

I/O Plugin Overview
-------------------

The I/O plugin is used to integrate various CETONI I/O modules into
the CETONI Elements software and for displaying I/O channels of other
devices like Nemaxys positioning systems or Nemesys syringe pumps.

.. image:: Pictures/10000201000001F6000001EFFBB551A475EADF72.png

List of I/O channels
--------------------

All available I/O channels are shown in the I/O channels view.
You can distinguish the different types of I/Os (AI: analogue input, AO:
analogue output, DI: digital input, DO: digital output, Pressure:
pressure sensor) by their symbols and names (see figure above). If the
I/O list is not visible, you can display the window via the main menu of
the application :menuselection:`Window --> Show View --> I/O Channels`.

.. image:: Pictures/100002010000021B000000AB3B30B0CC6EFEE72A.png

The following columns are present:

-  **I/O Channel** - contains the name of the I/O channel and displays a
   symbol for the channel type.
-  **On** – a lit green LED indicates that a channel is switched on and
   that a digital channel is 1 (instead of 0), respectively.
-  **Actual Value** - Shows the current value of the channel - in the case
   of output channels, this is the value that is output, and in the case
   of input channels the value read from the device.

Channel types
~~~~~~~~~~~~~

The following types of channel are currently supported:

======== ===================================
|image1| analog inputs (voltage and current)
|image2| analog outputs
|image3| digital inputs
|image4| digital outputs
|image5| analog pressure sensor inputs
|image6| analog temperature sensor inputs
|image7| analog force sensor
|image8| analog flow sensor
|image9| virtual channels
======== ===================================

Grouped display
~~~~~~~~~~~~~~~

By default, the I/O channels are displayed in groups. This means that
the channels of a certain device are grouped under the device name, so
that a tree-like structure is created. I.e., you can show or hide the
display of channels for certain devices, e.g. for the Nemesys pumps. In
the following figure, for example, only the channels of the first
Nemesys pump are displayed.

.. admonition:: Important
   :class: note

   If you are still working with an older
   device configuration, you may have to save the device
   configuration in the Device Configurator again so that
   the I/O channels are displayed in groups.

|Figure 2: Grouping of I/O channels|

All I/O channels that do not
belong to a specific device or channels of devices that do not yet
support grouping are grouped together in the *Ungrouped Channels* group.

|Figure 3: Ungrouped Channels|

You can activate and deactivate the
grouping of channels at any time. Simply right-click in the list of I/O
channels and select :guilabel:`Group Channels` from the context menu (figure
below).

|image13|

If the channel grouping is deactivated, you get a flat
display of the I/O channels in list form.

|Figure 4: Display of I/O channels without grouping.|

Search I/O channels
~~~~~~~~~~~~~~~~~~~~~

If you want to quickly search for a specific channel in the list,
right-click in the first column (*I/O Channel*) and select
:guilabel:`Search in column` from the context menu.

|image14|

A search dialog is displayed in which you can enter the
search term. A list of possible hits is displayed as you enter the
search term. If you select an entry, the corresponding channel is
displayed in the I/O list and is highlighted in color.

Change Item Scaling
~~~~~~~~~~~~~~~~~~~

In order to increase clarity or improve readability, the display of the
list entries can be switched between three sizes. To do this, choose
:guilabel:`Set Item Scaling` from the context menu and then select the required
size:

.. image:: Pictures/100002010000022B000001231C920F293849CD41.png

Set outputs
-----------

The values of output channels can be changed by the user. Output
channels include digital and analog output channels as well as virtual
channels. Digital output channels can be switched on and off by clicking
on the LED in the *On column* of the channel.

|Figure 6: Switching digital output channels on and off|

Analog channels
can also be switched on and off by clicking on the LED. If an analog
channel is switched off, the value 0 is output. If an analog channel is
switched on, the value from the *Value column* is output. If you want
to change the analog value, simply double-click with the left mouse
button in the value column of a channel, or select the value column of
the channel and then start typing on the keyboard.

|Figure 7: Changing values of analog output channels|

This also allows
you to change the values of virtual channels.

I/O Channel Configuration
-------------------------

Changing channel captions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can change the caption of each channel at any time, for example, to
assign a memorable name suitable for your particular application. You
may change a caption by the following steps:

1. **Double-click** the name you want to change.
2. The name is now highlighted in yellow: Enter the new name (figure
   below).
3. Complete your entry by pressing the :kbd:`Return` key.

|Figure 8: Changing a channel name|

Activating the Configuration Dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to customizing the name, for most I/O channels there are
additional parameters that may be configured, such as the scaling of
analog in- and outputs. You will find these configuration parameters in
the respective configuration dialog of each channel.

|Figure 9: Opening the channel configuration panel|

To open the
configuration panel, right-click on the respective channel name from the
I/O channel list and select the context menu item
:guilabel:`Configure channel` (figure above).

Configuration Dialog
~~~~~~~~~~~~~~~~~~~~

In the configuration dialog you can configure all accessible parameters
of an analog in- and output channel:

.. image:: Pictures/1000020100000212000001862DB8297006D93319.png

.. rst-class:: guinums

#. The title bar shows the name of the channel you are configuring.
#. In the toolbar you can find the actions you can perform:

   +-----------+---------------------------------------------------------------+
   | |image21| | **Restore default settings** By clicking this button,         |
   |           | all parameters (channel name, decimal points, scaling,        |
   |           | *etc*.) are reset to their original values.                   |
   +-----------+---------------------------------------------------------------+
   | |image22| | **Select Scaling Preset** - opens a selection dialog          |
   |           | with predefined `Scaling Presets`_.                           |
   +-----------+---------------------------------------------------------------+
   | |image23| | **Reset Calibration**- resets the calibration of the          |
   |           | channel to the default settings (offset = 0, factor =         |
   |           | 1).                                                           |
   +-----------+---------------------------------------------------------------+

#. Here you can configure the general settings of the channel, such as
   name, decimal places or unit of measurement:

   -  *Caption* – Here you can set a new name for that channel, which is
      then displayed in the channel list.
   -  *Measuring Unit*– Enter the measurement unit in which the measured
      values are displayed. The unit must be compatible with the basic
      unit of the channel or sensor. For example, you can use the units
      **bar**, **psi**, or **Pa** for a pressure measurement channel,
      but not the units **mV**, **mA** or **kg**. The software
      automatically converts the measured values of the sensor into the
      selected unit.
   -  *Decimals* – This field is to set the number of decimal points of
      the scaled unit of measurement.

#. In the *Calibration* area, you can compensate measurement value
   deviations of channels by means of calibration.
#. For channels that support the connection of sensors (for example,
   voltage or current measuring inputs), you can display the operating
   elements for configuring the scaling of the sensor. To do this, click
   *Sensor / Actuator Configuration*.

.. tip::
   All changes will be activated only after
   being accepted by pressing :guilabel:`OK`. To cancel all
   changes use :guilabel:`Cancel`.

.. admonition:: Important
   :class: note

   Clicking :guilabel:`Restore default settings`
   will instantly reset all parameters to their original
   setting – clicking :guilabel:`OK` is not required.

Calibration
-----------

With the two-point calibration you can correct measurement deviations of
a channel. To do this, you record the measured value of the channel at
two points :guinum:`❶` and :guinum:`❷` :guilabel:`Value` and enter the actual corrected
value of the channel for these points :guilabel:`Calibrated value`.
The software calculates the slope (factor) and the offset of the scaling.

If you click on the :guilabel:`Capture current channel value` :guinum:`❸` button,
the current value of the channel is automatically entered into the :guilabel:`Value`
field.

.. image:: Pictures/100002010000024C000000FE0348D163BBF02B8A.png

.. admonition:: Important
   :class: note

   All calibration values are entered in
   the configured unit of measurement. If you change the
   unit of measurement or the scaling of the channel, you
   must check the calibration and adjust it if necessary.

Configure Sensor Scaling
------------------------

Sensor Scaling Overview
~~~~~~~~~~~~~~~~~~~~~~~~

For analogue channels that support the connection of sensors (such as
voltage or current measurement inputs), you can configure
sensor-specific scaling. This allows you to connect sensors to the
analog inputs and then scale the measured values to the value range of
the analog sensors and display them in the correct unit. To do this,
click on :guilabel:`Scaling Configuration` in the configuration dialog.

|Figure 12: Configuration scaling parameters|

Select Physical Quantity
~~~~~~~~~~~~~~~~~~~~~~~~~

In the *Physical Quantity* pane :guinum:`❶`, select the physical quantity to be
measured with the sensor. If the desired sensor type is not supported in
the :guilabel:`Type` selection box, simply select the *Custom* type for a
user-specific scaling. For a pressure sensor you simply select the
*Pressure* type.

In the :guilabel:`Unit` input field, enter the basic unit of the sensor. When
selecting a sensor type, a corresponding unit is already suggested to
you. The unit must be compatible with the selected physical quantity
(e.g., bar, psi, Pa or atm for pressure sensors).

Two-Point Scaling
~~~~~~~~~~~~~~~~~

The two-point scaling :guinum:`❷` is used to configure the conversion between the
analog measured values of the I/O channel (for example in mV or mA) and
the sensor readings of the sensor connected thereto (for example, bar or
° C). Normally you will find these values in the data sheet of the
sensor.

.. admonition:: Important
   :class: note

   Currently, the software only supports
   linear scaling of measurement values.

For example, if you have a pressure sensor with an analog input range
from 0.5 V to 4.5 V and a measurement range from 0 bar to 20 bar, you
can enter the following parameters. Enter the I/O channel range 500 mV
and 4500 mV in the first column (*Device value*) and the sensor range 0
and 20 bar in the second column (*Scaled value*).

.. admonition:: Important
   :class: note

   Make sure that the units used correspond
   to the units in the data sheet of the sensor.

Limits
~~~~~~

In the *Limits* :guinum:`❸` pane you define the measuring range of the sensor. In
many cases, this range matches the range that you entered in two-point
scaling pane. Therefore, the values for the two-point scaling are
automatically transferred to the range limits. Here, you can further
restrict or change the value range.

.. admonition:: Important
   :class: note

   Clicking :guilabel:`Restore default settings`
   will instantly reset all parameters to their original
   setting – clicking :guilabel:`OK` is not required.

User-specific Scaling
~~~~~~~~~~~~~~~~~~~~~

If you are using a sensor which is not yet supported in the :guilabel:`Type`
selection box, simply select the sensor type :guilabel:`Custom` :guinum:`❶`. In this case,
the input field measuring unit :guinum:`❷` is grayed out, since automatic unit
conversion is no longer possible.

.. image:: Pictures/1000020100000293000001A7CF54CF7D61FB34F6.png

Scaling presets
---------------

Some analog input and output channels offer a choice of predefined
configurations. These include pressure sensor configurations for the
analog inputs of Nemesys syringe pump devices.

.. admonition:: Important
   :class: note

   Predefined configurations are not
   offered by all analog channels. For those channels the
   menu item :guilabel:`Select scaling preset` is not displayed in
   the context menu.

|Figure 14: Opening predefined configurations dialog|

To select a
predefined configuration proceed as follows, right-click the respective
analog channel in order to show the context menu (see figure below).
Choose :guilabel:`Select scaling preset.` A dialog containing a selection of
scaling presets appears (figure below). Select the preset you are going
to use and confirm your choice by left-clicking :guilabel:`Ok`.

|Figure 15: Selecting predefined configurations|

To restore the default
channel settings, simply click the menu item :guilabel:`Restore default settings`
in the channel context menu (see figure below).

.. image:: Pictures/1000020100000210000000E26F7EC82ABD40B5A3.png

Virtual Channels
----------------

Creating virtual channels
~~~~~~~~~~~~~~~~~~~~~~~~~

The software allows the creation of virtual I/O channels. These channels
are not assigned to a physical I/O device, but they are a kind of
memory. You can write values into virtual channels and read them out
later - just like a memory. Using these channels, you can, for example,
show calculated values from a script in the graphical
logger. You only have to create the channel, add the channel to the
logger, and then you can write values from the script into the channel
and you will see them in the graphical logger.

To create a virtual channel, click with the right mouse button in the
I/O channel list and select the context menu item
:guilabel:`Create virtual channel`.

|Figure 17: Creating virtual channels|

A virtual channel will then be
added and you can configure the channel further - e.g. change the
channel name. If channel grouping is active, all virtual channels are
grouped together in the *Virtual Channels* group and inserted there when
they are created.

|Figure 18: Virtual channels in the list of I/O channels|

If channel
grouping is disabled, the newly created virtual channel is inserted at
the end of the list.

Access to virtual channels from a script program
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To access virtual channels out of script programs (read and
write access), you can use the script functions from the category
:ref:`Device Functions` (figure below).

|Figure 19: Read and write access to virtual channels|

Deleting virtual channels
~~~~~~~~~~~~~~~~~~~~~~~~~~

To delete a virtual channel, click with the right mouse button on the
channel in the I/O channel list, and then select from the context menu
the item :guilabel:`Delete virtual channel` (figure below).

|Figure 20: Deleting virtual channels|


.. |image1| image:: Pictures/analog_in.svg
   :width: 40

.. |image2| image:: Pictures/analog_out.svg
   :width: 40

.. |image3| image:: Pictures/dig_in.svg
   :width: 40

.. |image4| image:: Pictures/dig_out.svg
   :width: 40

.. |image5| image:: Pictures/10004C06000034EB000034EB3B64F50CF73C7319.svg
   :width: 40

.. |image6| image:: Pictures/100051AD000034EB000034EB615CA53F231E2071.svg
   :width: 40

.. |image7| image:: Pictures/10004C5E000034EB000034EB7FFDB68DD93E5C3E.svg
   :width: 40

.. |image8| image:: Pictures/100047B2000034EB000034EB7BBD43FF0627D5D3.svg
   :width: 40

.. |image9| image:: Pictures/1000000000000030000000305963F73F938F8699.png
   :width: 40

.. |Figure 2: Grouping of I/O channels| image:: Pictures/100002010000022A00000129BE2F20D0F3631291.png

.. |Figure 3: Ungrouped Channels| image:: Pictures/1000020100000211000000EC8C1F3E3DFF5B05B5.png

.. |image13| image:: Pictures/10000201000000BA0000009AEFB00DBBC09E8A96.png

.. |Figure 4: Display of I/O channels without grouping.| image:: Pictures/10000201000002410000010956222D3E3459DF4B.png

.. |image14| image:: Pictures/1000000000000164000000B8F8746536D6C09088.png

.. |Figure 6: Switching digital output channels on and off| image:: Pictures/10000201000001F1000000B04F8C214E5ED6F298.png

.. |Figure 7: Changing values of analog output channels| image:: Pictures/10000201000001F1000000B76EDE046BAAE032A0.png

.. |Figure 8: Changing a channel name| image:: Pictures/1000020100000210000000CFEE86A61E8D9261A1.png

.. |Figure 9: Opening the channel configuration panel| image:: Pictures/1000020100000210000000E26A44508AB4B23B66.png

.. |image21| image:: Pictures/1000046A00003505000035052554114A973E3AD6.svg
   :width: 40

.. |image22| image:: Pictures/10001183000034EB000034EBDFA4938505ACE302.svg
   :width: 40

.. |image23| image:: Pictures/100002C1000035050000350588E8C4C80407FC4C.svg
   :width: 40

.. |Figure 12: Configuration scaling parameters| image:: Pictures/10000201000002B700000137795168A3F5C0861B.png

.. |Figure 14: Opening predefined configurations dialog| image:: Pictures/10000201000002010000010D504DB5DF96F402B1.png

.. |Figure 15: Selecting predefined configurations| image:: Pictures/100000000000022D0000015CEA4C9E2A9528BEA1.png

.. |Figure 17: Creating virtual channels| image:: Pictures/100002010000023A00000102ED9CC097AC4CA17D.png

.. |Figure 18: Virtual channels in the list of I/O channels| image:: Pictures/10000201000001EB000000BFAE47483A07671078.png

.. |Figure 19: Read and write access to virtual channels| image:: Pictures/100002010000010B000000720E021D287C297538.png

.. |Figure 20: Deleting virtual channels| image:: Pictures/10000000000001E8000000D1A8C8F0B61AD24CD2.png
