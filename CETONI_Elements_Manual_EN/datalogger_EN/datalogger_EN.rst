CSV Data Logger Plugin
======================

Introduction
------------

The data logger plug-in provides the user with a powerful tool to record
any of the data provided by connected devices in a user-defined time
interval. Data are written into a CSV file (CSV:
comma/character-separated values). This text file format is commonly
used to save and exchange simply-structured data.

.. tip::
   CSV files can be opened and worked with in     
   spreadsheet applications, such as Microsoft Excel if the 
   correct value-separating and decimal sign has been used.

Configuration Dialogue
----------------------

Open the Configuration Dialogue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/10000201000001B600000043E638CC3BBADD620A.png

When the data logging plug-in has
been loaded, the toolbar will display two additional buttons for the
configuration of the logging of data :guinum:`❶` and to start/stop the logging
process :guinum:`❷`.

Overview CSV-Logger Configuration Dialogue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the data logging configuration has been activated, the following
configuration dialogue will be displayed:

.. image:: ../../img/datalogger/configuration_dialog_overview.png

The configuration dialogue contains the following elements:

.. rst-class:: guinums

1. **Object Tree** - The Object Tree contains a tree of all objects and their
   properties that are present in the application. You can use various filters
   to filter the object tree for specific objects. By default, only devices and
   device properties are displayed.
   
2. **Logger Channels** - lists all channels that may be recorded by the
   logger.
   
3. **CSV File Configuration** - allows the user to set various settings
   for the data logging file.


Object Tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the Object Tree you will find a hierarchical list of all objects
(e.g. devices) and their child objects (such as child devices):

.. image:: ../../img/datalogger/object_tree.png

.. rst-class:: guinums

1. **Object** - An object can be, for example, a device (here **Nemesys_M_1**) or 
   another application object. You will find the two elements **Children** and 
   **Properties** in each object after expanding it in the next level.

2. **Children** - The Children element groups all child objects of the parent
   object. In our example, these are all objects or devices that are
   subordinate to the device **Nemesys_M_1** or belong to this device.

3. **Properties** - The Properties element groups all properties of the parent
   object. In our example, these are all the properties of the **Nemesys_M_1**
   device that can be recorded in the logger.

4. **Child Object** - All child objects can be found in the **Children** group. 
   In the example **Nemesys_M_1**, these are, for example, the digital and
   analogue inputs and outputs of the device, such as **Nemesys_M_1_DigOUT1**. 
   These objects can in turn be expanded to display their child objects and
   properties.

5. **Property** - In the **Properties** group you will find all properties of
   the parent object. In the example of **Nemesys_M_1**, these are, for example, 
   the properties **SyringeFillLevel** or **ActualFlow**. You can simply
   drag and drop these properties into the channel list to record their values.


Filtering the Object Tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Above the object tree you will find various filters with which you can filter 
the object tree according to certain criteria. The :guilabel:`Devices Only` :guinum:`❶`
checkbox is activated by default. This means that only devices that are managed
by the internal device manager (:guilabel:`Core.DeviceManager`) are displayed in
the object tree. If you deactivate this checkbox, other application objects are
displayed in the object tree.

If the :guilabel:`Devices Only`:guinum:`❶` checkbox is activated, a selection 
box :guinum:`❷` is displayed with which you can filter the device tree according
to a specific device type. In the illustration below, for example, the tree was 
filtered for syringe pumps:

.. image:: ../../img/datalogger/object_tree_filter.png

In addition, you will find an input field :guinum:`❸` directly above the object tree,
with which you can filter the object tree according to a specific term, e.g. a 
device name or a device property. In the image below, for example, a filter has
been set for the device property **ActualFlow**. This means that only objects
or devices with this property are displayed in the object tree:

.. image:: ../../img/datalogger/object_tree_filter_text.png


Overview Table Logger-Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ../../img/datalogger/logger_channels_view.png

The table :guilabel:`Logger Channels` shows the configuration of the logger. 
Each row in that table corresponds to one column in the recorded
CSV file. The following columns may be recorded:

-  **Object** - contains the name of the object from which the value of a
   certain property is to be recorded and the icon of the object.
-  **Property** - this is the name of the object property/process data
   value that will be recorded. Its type (numeric or boolean) can be
   identified by the displayed icon.

   ============ =================
   |icon-num|   Numeric value
   |icon-bool|  Boolean value
   |icon-text|  Text value
   ============ =================

-  **Label** - allows you to define a customized description for the
   selected channel. This description will be used as the column header
   in the CSV file.

In order to add a channel to the data logging process, simply follow the
steps below.

Logger Configuration
------------------------------------

Add Logger Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:step:`Step 1- Adding of Channels`

Drag-and-Drop the object property you want to record from the
:guilabel:`Device List`Object Tree` into the :guilabel:`Logger Channels` list. 
The new channel is inserted in the line where you release the mouse button 
(see figure below).

.. image:: ../../img/datalogger/csv_logger_drag_and_drop.png

.. tip::
   To simplify the selection of an object property, you can filter the object
   tree according to various criteria.

:step:`Step 2 - Setting the Channel Label`

In the column :guilabel:`Label` you can customize the description for each
channel. This label will be used as the column header of the csv file
for the selected channel.

.. image:: Pictures/10000201000002670000009030B373AFA6AF1077.png

To do this, double-click
into the respective table cell that is to be changed and insert the new
description (see figure above).

.. admonition:: Important
   :class: note

   Upon choosing a new device property, a   
   new channel description will be assigned automatically. 
   That is, you should change the channel label only once  
   the correct device property has been selected. 

Deleting Channels
~~~~~~~~~~~~~~~~~

Highlight the desired channels using the mouse to delete one or more
channels from the list, and then use either the :kbd:`Delete` key or the
:menuselection:`Delecte Selection` item of the right-click context menu:


|image14| |image15|


To delete the entire channel list, use the context menu item 
:menuselection:`Clear Logger`.

Configuration of CSV Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the :guilabel:`CSV File Configuration` section you can set the global
properties of the CSV logger as well as the format of the recorded data
(see figure below).

.. image:: Pictures/10000201000002740000005D7814BAB01380FB40.png

Select File Name and Folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the file name and location of the log file via :guilabel:`Log Filename` 
:guinum:`❶`. For this, click on the folder symbol on the right, select the target
folder and give a file name.

.. image:: Pictures/100000000000028F000001D742CE00F60CA536D2.png

Setting the Recording Interval
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the time interval at which the data of all channels is to be
recorded via the field :guilabel:`Log Interval` :guinum:`❷`. The time unit for the interval
is seconds and you may set it in 0.1 second increments.

.. admonition:: Important
   :class: note

   Choose the recording interval as large   
   as possible and as small as necessary. This will        
   minimize amount of data that will be recorded.

Set the Separating Character
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The character that will be used to separate individual data (columns)
needs to be set via the selection field :guilabel:`CSV Separator` 
:guinum:`❸`. Depending on the software that is to be used for data 
evaluation, the character that needs to be used may change.

.. tip::
   To obtain a CSV file that can be imported     
   into Microsoft Excel, the semicolon (;) should be used.

.. admonition:: Important
   :class: note

   All configuration settings of the        
   process data logger will be saved upon closing the      
   configuration dialogue and are available when the       
   application will be restarted. 

Start/Stop of the Logging Process
---------------------------------

.. image:: Pictures/1000106B000034EB000034EBCD48AF0AC896EFC6.svg
   :width: 60
   :height: 60
   :align: left

Use the relevant toolbar button to start and stop the data
logging process.

A new data file will be created each time the logging process is
started. A time stamp with date and time will be added as a suffix to
file name :file:`_YYYYMMDD_hhmmss`. That means, if the file name
:file:`ProcessDataLog.csv` has been assigned by the user, starting the logging
process on November 05, 2012 at 10:32 am and 9 secondswill create a
logging file with the name :file:`ProcessDataLog_20121105_103209.csv.` 
This ensures, that a new logging file with a unique time stamp will be
created each time the logging process is started.

Log File Data Format
--------------------

The recorded CSV files have the following structure:

-  Each CSV file consists of multiple data sets organized in rows and
   separated by line breaks.
-  Each data set consists of a number of data fields (columns) that are
   separated by a specific character (e.g., semicolon).
-  The first column always contains the relative time point (in seconds)
   of the corresponding data set.
-  The first row shows the channel labels as configured by the user.

.. image:: Pictures/10000000000002EF000000E6889ECE76397F99EB.png

To obtain the
absolute time stamp for a data set, you may simply add an extra column
to the spreadsheet and calculate the time by adding the data set's
relative time to the absolute time given in the file names time stamp.

.. tip::
   The absolute time stamp at which logging      
   started is given in the file name of the log file. 

Script Functions
----------------

To automate the capture of data or to synchronize data capture with
other processes, the CSV data logger can be started and stopped using
script functions. The corresponding functions can be found
in the :guilabel:`Logging` category in the list of the available script
functions.

.. image:: Pictures/10000201000001060000008EE8252D88C2E8FBC7.png

Start CSV Logger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/1000106B000034EB000034EBCD48AF0AC896EFC6.svg
   :width: 60
   :height: 60
   :align: left

This function is used to start the CSV logger with the
currently configured settings and channels. A new log file is created
with the current time stamp.

|

Stop CSV Logger
~~~~~~~~~~~~~~~

.. image:: Pictures/1000101A000034EB000034EB2614684FE9CC8E2D.svg
   :width: 60
   :height: 60
   :align: left

This function stops the current logging and closes the open
log file.

.. |image14| image:: Pictures/100000000000012100000091D7BFE42C03BA6ECE.png

.. |image15| image:: Pictures/10000000000001220000008F424E5926A933056B.png

.. |icon-num| image:: ../../img/datalogger/property_number.svg
   :width: 40
.. |icon-bool| image:: ../../img/datalogger/property_bool.svg
   :width: 40
.. |icon-text| image:: ../../img/datalogger/property_text.svg
   :width: 40