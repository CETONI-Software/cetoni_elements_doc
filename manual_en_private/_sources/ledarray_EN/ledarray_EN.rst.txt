LED Array Plugin
================

Introduction
------------

.. image:: Pictures/100000000000006000000061CD30E97F.png
   :width: 80
   :align: left

Press the button :guilabel:`LED Array` in the side bar or use the menu item 
:menuselection:`Window --> Show View --> LED Array` to show the
:ref:`View <views>` of  the LED Array plug-in (figure below).

.. image:: Pictures/1000000000000382000002BC2FE3AAFD.png

The LED Array View contains a separate control panel for each connected 
LED array device.

Hardware Version
----------------

Depending on the LED array hardware version a corresponding LED array
control panel is displayed for every LED array. The following two
hardware versions are supported:

.. list-table::
   :header-rows: 1

   * - LED Array Hardware V1
     - LED Array Hardware V2 
   * - |image6|
     - |image7|
   * - :ref:`Hardware version 1 <LED Array Control Panel V1>` supports 12 independent LED array 
       channels with a resolution of 100 steps to adjust the brightness.
     - :ref:`Hardware version 2 <LED Array Control Panel V2>` supports a virtually infinite number 
       of independent LED channels with a resolution of 4096 steps to adjust the brightness. 

LED Array Control Panel V1
--------------------------

.. image:: Pictures/100000000000010E000002353ADBC6BA.png

.. rst-class:: guinums

#. Caption (customizable)
#. all LED channels on / off
#. adjust the brightness of individual LED channels (0 - 100%)
#. adjust the brightness of multiple LED channels (LED group) at the same time

You can change the caption of each LED array control panel at any time.
To change the caption, directly click the caption label :guinum:`❶` and type in
the new name. This name will be saved and reloaded the next time you
start the software.

Setting brightness of individual LED channels
---------------------------------------------

You can set the brightness of each LED channel by entering the value
directly in the field below the LED :guinum:`❷` (0 - 100%) or by clicking the
right mouse button on an LED and dragging the brightness slider :guinum:`❶` (see
figure below).

.. image:: Pictures/100000000000010A000000A8ED3768DB.png

Click with
the left mouse button on an LED to switch individual LED channels on and
off.

.. image:: Pictures/1000000000000106000000AE9333AD7C.png

As all LED channels are
normal analog output channels in the QmixElements software, you can also
adjust the brightness of individual LED channels via the
:ref:`I/O Channels <I/O Plugin Overview>` window (figure below).

.. image:: Pictures/10000000000001C300000100AD443E83.png

LED Group Control
---------------------

Introduction
~~~~~~~~~~~~

When multiple LED channels should work synchronously, you can combine
these channels into groups and control them together. The control panel
contains three sliders to adjust brightness of three different LED
channel groups.

Configuring LED channel groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To select the channels to be combined into a group, click the right
mouse button in the control area of a certain group to show its context
menu. Then select the menu item :menuselection:`Configure Group Channels` 
(see figure below).

.. image:: Pictures/100000000000013400000067B8EAA03B.png

In the LED group
configuration dialog (figure below) you can select all LED channels to
be grouped together. Check each channel to be part of this group :guinum:`❶` and
confirm your selection by clicking :guilabel:`OK` :guinum:`❷`.

.. image:: Pictures/10000000000001640000019EAE700D89.png

Controlling LED groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can change the brightness of an LED group with the slider :guinum:`❶` or by
entering the brightness value in the input box :guinum:`❷` (see figure below).

.. image:: Pictures/10000000000000F60000005AF5E326F1.png

With the check mark in the upper left
corner :guinum:`❸`, you can switch all LED channels in this group on /off
simultaneously.

Configuring Standby-Timer
-------------------------

The LED Array has a standby timer functionality. This means, all sectors
of the LED Array are automatically switched off after the last action of
the user in the software and after the standby time is over. Every
change in parameters in the software resets the standby timer and
reactivates the array.

.. admonition:: Important
   :class: note

   The standby timer value is saved in the  
   LED Array. I.e. even if the connection to the PC is     
   lost, the LED array is switched off after the standby   
   time is over.   

To configure the standby time, click with the right mouse button on a
blank area in the LED array control panel to display the context menu.
Then select the menu item :menuselection:`Configure Standby Timer` 
(figure below).

.. image:: Pictures/100000000000010700000096275DD1CF.png

In the
configuration dialog displayed (figure below), you can configure the
hours, minutes and seconds of the standby timer. Your changes are
accepted by clicking on :guilabel:`OK` and the standby time will be saved in the
device.

.. image:: Pictures/100000000000010A000000B3587F0120.png

.. admonition:: Important
   :class: note

   Enter a value of 0 for Hours, Minutes    
   and Seconds to deactivate the standby timer.

LED Array Control Panel V2
--------------------------

.. image:: Pictures/100000000000010900000224043E069F.png

You can change the caption of the LED array at any time. To change the
caption, click the caption label :guinum:`❶` and enter a new name for the LED
array. This name will be saved and reloaded the next time you start the
software.

Setting the Global Brightness
-----------------------------

You can set the global brightness of all LED channels at the same time
by using the slider :guinum:`❷` or the input field of :guilabel:`Global Brightness`. 
With the check mark in the top left corner :guinum:`❶` you can switch the global Enable
signal of the LED array. The array can be switched on and off this way
without changing the brightness of the individual channels.

.. image:: Pictures/10000000000000F20000008336288511.png

.. admonition:: Important
   :class: note

   The **Enable** signal must have been         
   activated for the LEDs of the array to light up. 

Setting the Brightness of LED Banks
-----------------------------------

LED banks are device-specific and hardware-specific groups of individual
LED channels in groups. LED banks group LED channels that also form a
physical group in the hardware, e.g. all LEDs on one board or all LEDs
of a certain type (e.g. warm white or cold white). These groups are
anchored in the firmware and cannot be changed by the user.

.. image:: Pictures/10000000000000EE00000084AF8E2BCD.png

To change the
brightness of a bank, select the bank in the :guilabel:`Bank` :guinum:`❶` input field and
then set the brightness of the selected bank using the slider or input
field :guinum:`❷`.

Setting the Brightness of Individual LED Channels 
-------------------------------------------------

In *LED Channel Brightness* you can set the brightness of individual LED
channels. For this purpose select the channel in the :guilabel:`Channel` :guinum:`❶` input
field. You can change the brightness by using the input field :guinum:`❷` or the
slider.

.. image:: Pictures/10000000000000F0000000821CC06826.png

To switch a
channel on or off, click the left mouse button on the relevant LED :guinum:`❸`.

As all LED channels are analogue output channels in the software, you can also
change the brightness of individual channels via the :ref:`I/O Channels <I/O Plugin Overview>`
window  (see figure below).

.. image:: Pictures/10000000000001C300000100AD443E83.png

LED Channel Groups
------------------

Introduction
~~~~~~~~~~~~

When multiple LED channels should work synchronously, you can combine
these channels into groups and control them together. The group channels
can then be used to jointly control all channels of an LED group.

Configuring the LED channel groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To configure LED channel groups, right click into the *LED Group Brightness*
panel and select the menu item :menuselection:`Configure LED Groups` from the
context menu.

.. image:: Pictures/100000000000012E000000A2EFE72B3A.png

The dialogue for the LED
group configuration will be shown now (see figure below).

.. image:: Pictures/10000000000002680000019589B3C1D4.png

To add LED
channels to a group, proceed as follows:

.. rst-class:: steps

#. First, go to the group list box :guinum:`❷` and select the group to be
   configured.
#. Now, select from the channel list :guinum:`❶` the channels to be added to the
   group by clicking with the mouse button.

   -  Select individual channels by clicking
   -  Select multiple connected channels by clicking with the mouse on the
      first channel on the first channel. Keep the :kbd:`Shift` key pressed
      while clicking on the last channel.

      |image19|

   -  Multiple independent channels can be selected by keeping
      the control key pressed while clicking.
      
      |image20| 

#. Now, add the selected channels to the group by clicking
   the :guilabel:`Plus` button :guinum:`❸`. To delete individual channels from the group,
   select the channels from the group list and then click the :guilabel:`Minus`
   button :guinum:`❹`. To delete all channels from the group, click the
   :guilabel:`Clear LED Group` :guinum:`❺` button.
#. After having configured all groups click :guilabel:`OK` :guinum:`❻`. The group
   configuration will then be transmitted to the device. If you want to
   permanently save the group configuration in the device, click Yes in
   the message window displayed (see figure below).

.. image:: Pictures/1000000000000222000000A673BE3A57.png

Setting the brightness of LED groups
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To change the brightness of a group, select the group from the
:guilabel:`Group` :guinum:`❶` input field and then set the brightness of the
selected group using the slider or the input field :guinum:`❷`.

.. image:: Pictures/10000000000000F300000083463C4BD3.png

Script Functions
----------------

The LED Array Plugin provides various script functions that can be used
to program automated exposure sequences or for time-controlled exposure.
The script functions are available in the categories of *LED Array
Functions* and *I/O Functions*.

|image21| 

|

|image22|

Set Global LED Array Brightness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/100002010000002E0000002EFB529AA2.png
   :width: 60
   :align: left

The global brightness of all LED channels of an LED array can
be set jointly by this script function. To configure the script
function, proceed as follows (see figure below):

.. image:: Pictures/10000000000001B100000084B2054C84.png

.. rst-class:: guinums

#. First, select the LED device from the list of devices.
#. Then, set the brightness (0 – 100%).

.. tip::
   This function supports script variables.      
   Variables can be used in the :guilabel:`Brightness` field.

Set LED Bank Brightness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000020100000030000000309FBA26F9.png
   :width: 60
   :align: left

You can set the brightness of entire LED banks by this script
function. To configure the script function, proceed as follows (see
figure below):

.. image:: Pictures/100000000000019100000099D6A36581.png

.. rst-class:: guinums

#. Select the LED Array device.
#. Select the bank the brightness of which is to be changed.
#. Set the brightness (0- 100%).

.. tip::
   This function supports script variables.      
   Variables can be used in the :guilabel:`Bank` and :guilabel:`Brightness` 
   field.

Set LED Channel Brightness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/100002010000003000000030BE44A04A.png
   :width: 60
   :align: left

This script function can be used to set the brightness of
individual LED channels. To configure the script function, proceed as
follows (see figure below):

.. image:: Pictures/100000000000016500000099E30E7287.png

.. rst-class:: guinums

#. Select the LED Array device.
#. Select the channel the brightness of which you want to set.
#. Set the brightness (0- 100%)

.. tip::
   This function supports script variables.      
   Variables can be used in the :guilabel:`Channel` and :guilabel:`Brightness` 
   field.

Set LED Group Brightness
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000020100000030000000309D549F7D.png
   :width: 60
   :align: left

You can use this function to set the brightness of an LED
group in a script-controlled manner. To configure the script function,
proceed as follows (see figure below):

.. image:: Pictures/10000000000001690000009BB63CA864.png

.. rst-class:: guinums

#. Select the LED Array device.
#. Select the group the brightness of which you want to set.
#. Set the brightness (0- 100%).

.. tip::
   This function supports script variables.      
   Variables can be used in the :guilabel:`Channel` and :guilabel:`Brightness` 
   field.

Set Multi Channel Brightness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000020100000030000000306620BC5F.png
   :width: 60
   :align: left

You can use this function to set simultaneously the
brightness of multiple LED channels in a script-controlled manner. To
configure the script function, proceed as follows (see figure below):

.. image:: Pictures/10000000000002260000018E1FF2911A.png

.. rst-class:: guinums

#. Select the LED Array device.
#. Set the brightness (0- 100%).
#. Check every channel of the list which is to be controlled.

.. admonition:: Important
   :class: note

   If a large number of channels have been  
   selected, the data transfer for all channels may take   
   some time so that not all channels will be switched     
   exactly synchronously.  If such delay is undesired, use 
   LED groups.  

.. tip::
   This function supports script variables.      
   Variables can be used in the :guilabel:`Brightness` field.

Set Analog Out
~~~~~~~~~~~~~~~~

.. image:: Pictures/analogout_script.svg
   :width: 60
   :align: left

All LED channels are normal analog output channels in the software. To adjust 
the brightness of individual channels, you can use the *Set Analog Out* function 
from the :ref:`I/O Functions <I/O Script Functions>` category.

.. image:: Pictures/10000000000001C0000000BCBE441A82.png

Select the relevant LED channel from the configuration menu :guilabel:`Analog Output`
:guinum:`❶` and enter the brightness value :guinum:`❷` (0 – 100%) in the
:guilabel:`Value` field.

.. tip::
   This function supports the use of variables,  
   i.e. you can enter in the :guilabel:`Value` field :guinum:`❷` the name of the  
   variable instead of a value which contains the          
   brightness value at the run time of the script.   

.. |image6| image:: Pictures/100000000000010E0000022483DA82B5.png
.. |image7| image:: Pictures/10000000000001090000022462F0E95C.png
.. |image19| image:: Pictures/10000000000004C90000026AF43AB254.png
   :width: 350
.. |image20| image:: Pictures/10000000000003890000026A2EE7BB04.png
   :width: 250
.. |image21| image:: Pictures/1000000000000111000000C6D2F2FCCA.png
.. |image22| image:: Pictures/10000000000000EA00000078FE1034F4.png

