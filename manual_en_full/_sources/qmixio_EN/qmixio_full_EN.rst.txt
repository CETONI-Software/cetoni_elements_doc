.. include:: qmixio_common_EN.inc.rst


I/O Script Functions
------------------------------------------------------------

Introduction to I/O Script Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The I/O plugin contains script functions for switching digital
outputs and setting the values of analogue outputs.

|Figure 21: I/O script functions|

Set Digital Out
~~~~~~~~~~~~~~~~

.. image:: Pictures/1000064300003505000035054FDB6D797453998C.svg
   :width: 60
   :align: left

You use this function to set/delete a digital output from a
script. Select the digital channel in the configuration area of the
function and then set the desired output value.

|

Set Analog Out
~~~~~~~~~~~~~~

.. image:: Pictures/10000F0E00003505000035054CE4E2663723FE52.svg
   :width: 60
   :align: left

With this function, you can write a value from a script to an
analogue output channel. Select the analogue channel in the
configuration area, and then configure the analogue initial value that
is to be set during the subsequent execution of the function.

This function supports the use of variables. This means that, instead of
a numeric value, you can insert a name of a variable into the field
:guilabel:`Value`. This variable will then be set to the analog output value when
the script is run (figure below). This variable may then subsequently be
used for calculations or to carry out value-specific functions.

.. image:: Pictures/1000020100000218000000BA59FD4FDF9E3D6F7B.png


.. |Figure 21: I/O script functions| image:: Pictures/1000020100000123000000778D7426E56265EAC3.png


.. include:: qmixio_beckhoff_EN.inc.rst
