Controller Channel List
------------------------------------------------------------

All controller channels are shown in the :guilabel:`Controller Channels` list.

|Figure 1: Controller Channel list|

You can identify the different types of channels (cooling module Q-,
heating module Q+...) by the different signs in front of the module
names (see Figure above). The list of controller channels is a
:ref:`View<Views>`,
that you can move freely at any time to another position in the
graphic interface by dragging and dropping the title bar, or you can
move it out of the interface to become a separate window.

The channel list shows all the available controller channels in
tabular form. The following columns are present:

-  **Controller** - shows the name of the controller module and indicates
   its type by a sign.
-  **On** - indicates by a green LED whether the controller is switched on
   or off. Click the LED to switch the control loop on / off.
-  **Setpoint** -contains the set setpoint of the controller channel
-  **Actual Value** - shows the actual value

Channel types
~~~~~~~~~~~~~

The following types of channels are currently supported:

======== ======================================
|image1| Qmix Q- cooling modules
|image2| Qmix Q+ heating modules
|image3| dynamically generated, custom channels
======== ======================================

Changing channel names
~~~~~~~~~~~~~~~~~~~~~~

You can change the name of a channel at any time and, for example,
assign a name suitable for your particular application.

|Figure 2: Changing channel names|

You change a name by the following steps:

.. rst-class:: steps

#. Double-click the table cell containing the name you want to change.
#. Enter the new name in the Editing window which now appears (Figure
   above).
#. Complete your entry by pressing the :kbd:`Return` key.

Switching control devices on / off
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Figure 3: Switching control devices on/off|

To switch the controller on or off, simply click the LED of the channel you
want to switch.

Entering setpoint
~~~~~~~~~~~~~~~~~

To input a setpoint, double-click in the :guilabel:`Setpoint` column of the channel
with the setpoint you want to change. Now enter the setpoint in the
editing window that opens (Figure below) or use the arrow buttons to
raise or lower the setpoint incrementally.

|Figure 4: Changing setpoint|

Context menu for control channels
----------------------------------------------------------------

By right-click into the control channel list you can display a context
menu with additional functions.

.. image:: Pictures/100002010000022300000129ACB2B97D.png

The context menu contains the following menu items:

+-----------+---------------------------------------------------------+
| |image18| | **Configure Channel...**                                |
|           |                                                         |
|           | Opens the configuration dialog of the channel for       |
|           | configuring all channel parameters.                     |
+-----------+---------------------------------------------------------+
| |image19| | **Restore Default Settings**                            |
|           |                                                         |
|           | Restores the default settings of the channel.           |
+-----------+---------------------------------------------------------+
| |image20| | **Reset Calibration**                                   |
|           |                                                         |
|           | Resets the two-point scaling to scale factor 1 and      |
|           | offset 0                                                |
+-----------+---------------------------------------------------------+
| |image21| | **Configure scaling...**                                |
|           |                                                         |
|           | Opens the configuration dialog displaying the page for  |
|           | configuration of the controller scaling.                |
+-----------+---------------------------------------------------------+
| |image22| | **Select PID parameters...**                            |
|           |                                                         |
|           | Opens the configuration dialog displaying the page for  |
|           | configuration of the PID control parameters.            |
+-----------+---------------------------------------------------------+
| |image23| | **Delete user channel**                                 |
|           |                                                         |
|           | If the selected channel is a user-specified channel, it |
|           | is deleted by selecting this menu item. For other       |
|           | channels this menu item is disabled.                    |
+-----------+---------------------------------------------------------+
| |image24| | **Create user channel**                                 |
|           |                                                         |
|           | Opens up the wizard for creating user-specified control |
|           | channels.                                               |
+-----------+---------------------------------------------------------+

Configure Channel Settings
--------------------------

For opening the scaling configuration dialog select :menuselection:`Configure channel`
in the context menu of the control channel.

|Figure 6: Configure scaling|

The configuration of the general channel
settings and the calibration of the controller channels are identical to
the configuration of the I/O channels of the :ref:`I/O Plugin`. For a
detailed description read the section :ref:`I/O Channel Configuration`.

Selection and configuration of controller parameters
----------------------------------------------------

Overview
~~~~~~~~

To set the optimal control behavior, you can adjust the controller
parameters of each single channel. For this you can either choose from a
list of predefined PID parameter sets or create new parameter sets.

To access the controller parameters selection, choose
:menuselection:`Select PID parameters` from the controller channel context
menu.

|Figure 7: Selecting a control parameter set|

The upper area shows the current parameters of the device :guinum:`❶`
:guilabel:`Current Channel Parameters`. In the lower area you will find a list
of :guilabel:`PID Parameter Presets` :guinum:`❷`.

Changing controller parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To edit the current controller parameters, double-click with the mouse
in the :guilabel:`Current Channel Parameters` area in the field you want to change
and enter the new value:

|Figure 8: Changing controller parameters|

Selecting a PID Parameter Preset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|Figure 9: Selecting a PID Parameter Preset|

Select a PID Preset from
the table of available presets by left-clicking on it :guinum:`❶` and then click
on the :guilabel:`Apply Preset` :guinum:`❷` button to apply the control parameters. The
values in the :guilabel:`Current Channel Parameters` :guinum:`❸` area are updated with the
new values from the preset. Complete the configuration by clicking the
:guilabel:`Ok` :guinum:`❹` button.

The PID parameter presets already contain default controller parameter
sets for different devices like Qmix Q+, Qmix Q- or Qmix TC or
certain accessories, i.e. syringe heating or tube heating.

.. tip::
   For optimum adaptation to the controlled
   systems in your application, you can create your own
   parameter sets with controller parameters.

Creating a PID Parameter Preset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By selecting the :guilabel:`Create Preset` button :guinum:`❶` you create a new set of
controller parameters :guinum:`❷`. (see figure below) You can then edit the
individual values of the parameter set by double-clicking in a field :guinum:`❸`
and entering a new value.

|Figure 10: Creating a PID Parameter Preset|

Enter a meaningful, unique
name for each parameter set and adapt the controller parameters to the
controlled system in your application. For finding adequate controller
parameters proceed as described in section :ref:`How to set controller parameters`.

Deleting PID Parameter Presets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select a set of controller parameters from the table :guinum:`❶` and left-click
the :guilabel:`Delete Selected Preset` button :guinum:`❷` for deleting it. (see figure
below).

.. image:: Pictures/1000020100000333000000D15C7BAB96.png

.. admonition:: Important
   :class: note

   Predefined controller parameters are
   locked and can not be deleted. Locked parameters can be
   recognized in the table by the lock symbol.

User defined control channels
-----------------------------

.. _user-defined-control-channels-introduction:

Introduction
~~~~~~~~~~~~

You can create customized control channels using arbitrary device
properties for control loop input and output. Thus using i.e. a pressure
measurement channel of a QmixP device and a Nemesys syringe pump you
can build up a pressure control.

Creating control channels
~~~~~~~~~~~~~~~~~~~~~~~~~

By right-clicking the control channel list and selecting the menu item
:menuselection:`Create user channel` in the context menu, you open the dialog
for creating custom control channels.

|Figure 12: Open controller channel creation dialog|

In the configuration wizard that is displayed now, proceed as follows:

|Figure 13: Selecting input and output values of the controller channel|

1. Select the device that provides the measurement value of the controller:
   :guilabel:`Controller Input`
2. Select the device property that is used as measurement value.
3. Select the device that provides the control value of the controller:
   :guilabel:`Controller Output`
4. Select the device property that is used as control value.
5. Click :guilabel:`Next` in order to proceed.

The final page of the wizard allows configuration of controller channel
parameters as described in section :ref:`Selection and configuration of
controller parameters`. You complete the control channel creation by clicking
the :guilabel:`Finish` button.

.. tip::
   You can change the controller parameters at
   any later time and adapt them perfectly to your
   controlled system.

Changing the output value scaling or unit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The output value is determined by the PID control algorithm and written
to the output device without any scaling information. This means that
you need to adjust the controller parameters, in particular the control
value limits, each time you change the scaling or the unit of the
appropriate device. With a Nemesys dosing module this is also true if
you change the syringe size.

.. admonition:: Important
   :class: note

   If you change the scaling or unit of a
   device beeing part of a control loop you must check the
   control parameters and adjust them if necessary. With a
   neMESYS dosing module this also applies if you change
   the syringe.

.. |Figure 1: Controller Channel list| image:: Pictures/10000000000001D5000000F75FCDB73E.png

.. |image1| image:: Pictures/10004AA90000387200003872C4D36C50.svg
   :width: 40

.. |image2| image:: Pictures/100051AC0000387200003872CA0648E8.svg
   :width: 40

.. |image3| image:: Pictures/100046F500003872000038724548056A.svg
   :width: 40

.. |Figure 2: Changing channel names| image:: Pictures/10000000000001D5000000F7561B0C23.png

.. |Figure 3: Switching control devices on/off| image:: Pictures/10000000000001D5000000D144CCA89A.png

.. |Figure 4: Changing setpoint| image:: Pictures/10000000000001D5000000F728D7F291.png

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

.. |Figure 6: Configure scaling| image:: Pictures/100002010000034C000001C3C2B07A89.png

.. |Figure 7: Selecting a control parameter set| image:: Pictures/100002010000034C000002287E739DAD.png

.. |Figure 8: Changing controller parameters| image:: Pictures/100002010000025A0000008921C42A7E.png

.. |Figure 9: Selecting a PID Parameter Preset| image:: Pictures/100002010000034C00000228CAC67298.png

.. |Figure 10: Creating a PID Parameter Preset| image:: Pictures/1000020100000335000000F62671DF1C.png

.. |Figure 12: Open controller channel creation dialog| image:: Pictures/100002010000022300000129BD54D696.png

.. |Figure 13: Selecting input and output values of the controller channel| image:: Pictures/1000020100000340000001A6ED2C69A6.png
