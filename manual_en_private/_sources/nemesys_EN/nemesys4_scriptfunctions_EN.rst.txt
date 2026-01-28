Nemesys Script Functions
------------------------

Introduction to Nemesys Script Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Nemesys plugin offers a number of script functions which can be used
to program automatic sequences. The following script functions are
available:

.. image:: ./Pictures/100002010000011B000000F6E6C15CD2AF9DE7DA.png

Automatically stop pumps at script stop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want all pumps to be stopped immediately when the user stops the
running script program, activate the corresponding button in the main
toolbar.

.. image:: ./Pictures/10000201000001D60000004893A82EEF2696F6A7.png

Dose Volume
~~~~~~~~~~~

.. image:: ./Pictures/100008FA000034EB000034EB3822C426C555871E.svg
   :width: 60
   :align: left

With this function, you can dose a specific volume at a
precisely defined flow rate. In the selection field Dosing Module :guinum:`❶` 
you select the dosing module you want to use for dosing. Alternatively, you
can also enter the name of a script variable in the field, which
contains a device reference of a pump.

.. image:: ./Pictures/10000201000001A8000000FED3ED286BF6ED76C6.png

All other parameters, such as
the volume to be dosed and the flow rate, can be set in the Target
Values :guinum:`❷` area.

You can also activate or deactivate the :guilabel:`Run to completion` :guinum:`❸` 
parameter in the configuration area. When :guilabel:`Run to completion` is activated, 
the script execution is not continued until the complete volume has been
dosed and the dosing process has ended. If this parameter is not active,
the dosing is started, and then the next script function is executed
immediately. This enables you, for example, to start a number of dosing
modules almost simultaneously.

.. tip::
   All the dosing functions support the use of    
   variables. That means, in all input fields marked with a 
   coloured V in the script configuration panel (e.g. flow  
   rate and volume) you can enter variables. 

Generate Flow
~~~~~~~~~~~~~

.. image:: ./Pictures/10003B74000034EB000034EB5935D7B503AF0C6A.svg
   :width: 60
   :align: left

This function is used to generate a constant flow rate. In the
configuration area, you can select the dosing module and set the flow
rate. If the :guilabel:`Run to completion` parameter is active, the next script
function is not executed until the module has stopped or reached one of
the limit positions. The configuration of the parameters corresponds to
the `Dose Volume`_ function.

.. tip::
   You can use script variables with device       
   references in the pump drop-down box. 

Set Syringe Level
~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/10003A2D000034EB000034EBBFEA0991D95C1B99.svg
   :width: 60
   :align: left

You can use this function in a script if you want to reach a
specific syringe fill level. The dosing module then doses until the
target fill level is reached. You can set the dosing module, the fill
level and the flow rate in the configuration area of this function. The
configuration of the parameters corresponds to the `Dose Volume`_ function.

Continuous Flow Function
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/10006B24000034EB000034EB2B72B9A4AEDF2E9A.svg
   :width: 60
   :align: left

This function allows you to start a continuous flow of two
pumps from a script. To do this, select the first dosing unit :guinum:`❶`
in the script configuration area of this function and then start
the *Continuous Flow Wizard* :guinum:`❷` to configure all parameters. For a
detailed description of the configuration, refer to the 
:ref:`Configuring Continuous Flow` section.

.. image:: ./Pictures/10000201000001BC00000132A166CAFDAC65CC2D.png

After configuration with the *Continuous Flow Wizard*, you will see the
configured flow rate in the :guilabel:`Flow` field :guinum:`❸`. 
If you have configured a certain volume for the continuous flow in the wizard,
the :guilabel:`Volume` field :guinum:`❹` is also displayed. You can use
the :guilabel:`Flow` and :guilabel:`Volume` fields to set the flow rate and 
volume using script variables.

With the checkbox :guilabel:`Run to completion` :guinum:`❺` you define when 
the next script function will be executed. If no check mark is set here, the
continuous flow is started and the next script function is executed
immediately. If :guilabel:`Run to completion` is active, the script is only
continued when the abort condition configured in the wizard occurs -
i.e. when the configured volume has been dosed or the set time has
elapsed.

Change Continuous Flow
~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/100215FB000034EB000034EB41F823505A27F258.svg
   :width: 60
   :align: left

With this function you can start a previously configured
continuous flow or change an already running continuous flow. To execute
this function without errors, you must either have previously configured
a continuous flow for two pumps or have executed the 
`Continuous Flow Function`_ script function.

.. image:: ./Pictures/100002010000021900000072852784EDF6312364.png

In the configuration area, select the pump :guinum:`❶` whose continuous flow you want to
change. In the Flow field :guinum:`❷` enter the flow rate. The unit corresponds to
the unit configured in the Continuous Flow Wizard when configuring the
continuous flow.

.. tip::
   You can use script variables to set the flow rate.

Stop Dosage
~~~~~~~~~~~

.. image:: ./Pictures/1000783B000034EB000034EB057FAC65A6CE5D99.svg
   :width: 60
   :align: left

You can stop an active dosing process of a module with this
function.

|

.. tip::
   You can use script variables with device references in the pump drop-down box.  

Stop All Pumps
~~~~~~~~~~~~~~

.. image:: ./Pictures/1000783B000034EB000034EB057FAC65A6CE5D99.svg
   :width: 60
   :align: left

Stops the dosing of all pumps simultaneously.

|

Execute Reference Move
~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/10003A6B000034EB000034EB7D405E638826AD8C.svg
   :width: 60
   :align: left

This function allows you to start a reference move from the
script. With the parameter :guilabel:`Run To Completion` you can specify whether
the function is terminated after starting the reference move or after
completion of reference move.
