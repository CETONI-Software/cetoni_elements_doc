DAQ Add-on
==========

Installation
------------

The DAQ Add-on is not part of the standard installation package and must
be installed as add-on. The versions of the DAQ Add-on and the installed
CETONI Elements software should match. For example, if you want to
install the DAQ Add-on version 20190721, you need to have CETONI
Elements version 20190721 installed.

.. admonition:: Important
   :class: note

   The version number of CETONI Elements and 
   the DAQ Add-on should match. 

Please close all other programs before launching the installation.

.. admonition:: Important
   :class: note

   Install the DAQ plugin and the device     
   driver before connecting your DAQ devices to your PC     
   through USB for the first time.

Launch :file:`CETONI_Elements_DAQ_Setup_64bit.exe` to begin the
installation. The installation assistant will guide you through the
installation of the software and hardware drivers.

.. admonition:: Important
   :class: note

   If you want to install the hardware       
   drivers on a windows system, you need to be logged in as 
   an administrator.

Introduction
------------

The DAQ Plugin serves data logging and evaluation at high sample rates
(> 1000 samples per second). Devices with a high data acquisition rate
are supported (i.e. . National Instruments USB 600x multi-function I/O
devices). But the DAQ Plugin supports usage of devices with low data
acquisition rate, too. Data are written into a process graph and into a
CSV-log-file simultaneously. There is no separate configuration
required. Use the push button :guilabel:`DAQ` :guinum:`❶` (see figure below) in the
sidebar to display the process data graphs.

.. image:: ./Pictures/100002010000036C00000297163E6666C1D280B6.png

.. rst-class:: guinums

#. **DAQ selector button** – Click this to show the process data
   graphs and the workbench for the results analysis of pattern
   recognition. The former is explained in detail in section
   `Diagram Navigation & Use`_, the latter in section
   1.10.4.Result Analysis for Pattern Recognition
#. **Graph canvas** – This displays the curves of all process data sets
   that are being recorded.
#. **Legend** – The legend lists all data sets that are displayed with
   their respective colors. Here you can toggle between whether or not a
   curve is being displayed.
#. **Toolbar** – Here you find buttons to configure the data logging, to
   start and stop the recording and to navigate the display.

Toolbar
-------

+-----------+---------------------------------------------------------+
| |image34| | Opens the configuration dialog of the graphic process   |
|           | data logger.                                            |
+-----------+---------------------------------------------------------+
| |image35| | Toggles the recording of process data.                  |
+-----------+---------------------------------------------------------+
| |image36| | Panning tool to move the currently displayed section of |
|           | the graph.                                              |
+-----------+---------------------------------------------------------+
| |image37| | Draws a zoom-in frame to enlarge a desired area of the  |
|           | graph.                                                  |
+-----------+---------------------------------------------------------+
| |image38| | Auto-scales the X axis to fit all process data on the   |
|           | screen.                                                 |
+-----------+---------------------------------------------------------+
| |image39| | Auto-scales the Y axis to fit all process data on the   |
|           | screen.                                                 |
+-----------+---------------------------------------------------------+
| |image40| | Auto-scales both X and Y axes to fit all process data   |
|           | on the screen.                                          |
+-----------+---------------------------------------------------------+
| |image41| | Activates auto-scaling: during a recording, both x- and |
|           | y-axes are continuously rescaled to fit all process     |
|           | data on the screen.                                     |
+-----------+---------------------------------------------------------+
| |image42| | Show all curves. If curves are hidden, they are         |
|           | displayed again.                                        |
+-----------+---------------------------------------------------------+
| |image43| | Clear plot data. Deletes all data from the diagram.     |
+-----------+---------------------------------------------------------+
| |image44| | Toggle X-axis scale. This switches the scaling of the   |
|           | X-axis between absolute date/time stamp and relative    |
|           | time in seconds and milliseconds since the start of     |
|           | recording.                                              |
+-----------+---------------------------------------------------------+
| |image45| | Export plot image. Exports an image of the currently    |
|           | displayed section.                                      |
+-----------+---------------------------------------------------------+

Configuration Dialog
--------------------

Overview
~~~~~~~~

.. image:: ./Pictures/10004180000034EB000034EB6DA9ACE22B65C020.svg
   :width: 60
   :align: left

Click on the button *Configure data acquisition* in the
toolbar to open the configuration dialog.

|

.. image:: ./Pictures/1000020100000371000001D48D6E763E7F12EB56.png

The configuration dialog consists
of the following sections:

.. rst-class:: guinums

#. **Device List** – shows all devices that return data that may be
   logged. The filter selection box allows to pre-select a specific
   device type (e.g., I/O channels).
#. **DAQ Channels** – lists all data series or curves that are being
   recorded and displayed in the diagram.
#. **DAQ Configuration** – in this section you can adapt the sample rate
   and enter the path of the log file that is written simultaneously to
   the process data graph.

DAQ Channels Table
~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/10000201000002340000009A60C2C459DC16C006.png

The table :guilabel:`DAQ Channels` shows the
configured data acquisition channels in tabular form. Each row in the
table corresponds exactly to one curve in the graphical plot. The
following columns are available:

-  **Channel** – returns the channel number.
-  **Device** – lists the device name for each respective channel
   including its icon.
-  **Property** – shows the property of the respective device that is to
   be recorded. The data type is identified via a data-type specific
   icon.

   ========= ===============
   |image47| Numerical value
   |image48| Boolean value
   |image49| Text value
   ========= ===============

-  **Label** – allows you to define a user-specific name for each channel.
   This label will also be used in the legend of the plotted graph.

To add and configure channels, please proceed as detailed in the
following sections.

Configure data acquistion
-------------------------

Step 1 – Adding Channels
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/10000000000002CC00000188EAF4D5DCF6382AA7.png

To add a channel you :guilabel:`Logger Channels`
table. To do this, move the relevant item from the
:guilabel:`Device List` to the :guilabel:`Logger Channels` table using Drag-&-Drop.
The new channel will be added at the position where you release the mouse button
(see figure above).

.. tip::
   To simplify the device selection process, the 
   device list may be filtered for a relevant device type.

Step 2 – Selecting the Device Property
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the device property that you want to record by double clicking
into the :guilabel:`Property` field of the respective channel from
:guilabel:`DAQ Channels` table. This will display a drop-down list with all available
device properties from which you may select the desired item (see figure
below).

.. image:: ./Pictures/10000000000002CC0000016B456742182C113BB4.png

Step 3 – Changing the Channel Label
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the Label column you can assign a label to each channel. This label
will later be displayed in the legend of the graph as the curve label.
To change the label, double-click in the :guilabel:`Label` table cell 
(see figure below) and then enter the new label.

.. image:: ./Pictures/100000000000025F000000BE2048E5FE978F309A.png

.. admonition:: Important
   :class: note

   When a different device property is      
   being selected, a new channel label will be assigned    
   automatically. Therefore, the channel label should be   
   changed **after** the device property has been selected.

Deleting Channels
~~~~~~~~~~~~~~~~~

In order to delete one or multiple channels from the :guilabel:`DAQ Channels`
list, first you have to mark the respective channels using
the computer mouse. Now you may use either the keyboard's :kbd:`Delete` key
or select the relevant item :menuselection:`Delete Selection` from the right-click
context menu.

|image56| |image57|

You may also delete the entire list in a single step by using the 
:menuselection:`Clear Logger` item of the context menu.

Step 4 – Defining the Sample Rate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the field :guilabel:`Sample Rate (Hz)` you can define the frequency measurement
values are written into the plot and the log file at. The maximum sample
rate depends on the measurement frequency of the hardware in use.

.. image:: ./Pictures/10000201000002030000006E8920DC98A24B4880.png

.. admonition:: Important
   :class: note

   Always select a sample rate that is only 
   as high as necessary. High sample rates produce a lot   
   of data. Drawing large amounts of data requires more    
   computer power and may slow down the usability of the   
   application.  

.. admonition:: Important
   :class: note

   Use a low sample rate to record data     
   over several days or use the graphical logger instead.

The configuration will be saved and reloaded automatically upon exiting
the *Logger Configuration* dialog.

Step 5 – Configuring the Log File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this section you can enter the log file :guinum:`❶` the measurement values
are written into in addition to the graphical plot. Furthermore you can
define the separator character the measurement values of the different
channels are separated from each other with :guinum:`❷`.

.. image:: ./Pictures/10000201000002A1000000B9F4DB74E960861B0F.png

Start/Stop Data Logging
-----------------------

.. image:: ./Pictures/10002C2B000034EB000034EB03167AF23B475C0B.svg
   :width: 60
   :align: left

The data logging process may be started/stopped via the
relevant button in the toolbar.

|

Diagram Navigation & Use
------------------------

Overview
~~~~~~~~

The DAQ plug-in offers a number of possibilities to customize the way
data are displayed. This includes resizing parts of a curve and showing
or hiding individual curves. The diagram consists of a plot area :guinum:`❶` plus
both an X-axis (time) :guinum:`❸` and a Y-axis (process data) :guinum:`❹`.

.. image:: ./Pictures/10000201000002C60000018E72664BA750C67A4C.png

The time axis shows date
and time as absolute values. The process-data axis shows the respective
measurement data; it is without units as it potentially represents a
variety of very different values and measurement units.

A right mouse click within the plot area will open a context menu :guinum:`❷` with
a number of additional functions.

Changing the Displayed Section
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/100005C7000035050000350518807CBDF5FF2BAE.svg
   :width: 60
   :align: left

The *Pan Tool* provides you with a simple way to move the
displayed section of the plot area. It may be activated via its toolbar
button and the displayed section may then be moved around using the
mouse whilst keeping the left button pressed.

.. admonition:: Important
   :class: note

   Panning of the displayed plot section    
   will deactivate the auto-scaling of the diagram axes. 

Display Curve Values
~~~~~~~~~~~~~~~~~~~~

When the *Pan Tool* is active, you can move the mouse pointer over a
curve to display the value at that specific position.

.. image:: ./Pictures/1000020100000255000000C02731E793C603A163.png

Zooming via the Mouse Wheel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Turning the mouse wheel whilst the pointer is within the plot area will
allow you to adjust the displayed section of a graph by increasing
(zooming in) or decreasing (zooming out) its zoom level.

========= ==============================
|image69| Increase zoom level (zoom in)
|image70| Decrease zoom level (zoom out)
========= ==============================

Defining a Display Section
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/1000100A000034EB000034EBFC7CEEC6D6B20A4B.svg
   :width: 60
   :align: left

The *Zoom Tool* allows you to directly select a specific area
of the plot and increase its resolution. To do this, please proceed as
follows (see figure below):

.. rst-class:: guinums

#. Using the mouse, left-click-and-hold into the plot area to set the
   first corner of the zoom frame.
#. Move the mouse pointer to define the size of the frame as desired.
#. Releasing the mouse button will finalize the size of the frame. The
   selected area will be scaled to the current graph size (zoom in).

.. image:: ./Pictures/10000000000001FA0000015E46DAC1CBDA6E2854.png

Auto-Fit & Auto-Scale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The toolbar and the context menu both contain a number of tools to
adjust what is displayed in the diagram, in particular to ensure that
all or specific data are visible.

The following possibilities exist:

+-----------+---------------------------------------------------------+
| |image80| | Rescales the X axis to display all current time data    |
|           | values for a given process data resolution.             |
+-----------+---------------------------------------------------------+
| |image81| | Rescales the Y axis to display all current process data |
|           | values within a given time period.                      |
+-----------+---------------------------------------------------------+
| |image82| | Rescales both X and Y axes to display all currently     |
|           | available data.                                         |
+-----------+---------------------------------------------------------+
| |image83| | (Re-)activates auto-scaling: as long as data are being  |
|           | recorded, both X and Y axes will be adjusted            |
|           | dynamically to ensure all data are being displayed.     |
+-----------+---------------------------------------------------------+

You may also activate auto-scaling for X and Y axes individually via the
context menu:

.. image:: ./Pictures/1000000000000109000001040CF9729CD97C9A4D.png

.. admonition:: Important
   :class: note

   Zooming or panning within the displayed  
   plot section will deactivate auto-scaling. 

Show/Hide Individual Curves
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To improve scaling and visibility, you may show or hide individual
curves. To do this, right-click the desired item in the plot legend and
select the desired function to either hide the corresponding curve only
:menuselection:`Hide Curve` or all other but the corresponding curve 
:menuselection:`Show only this curve` as indicated in the figure below.

.. image:: ./Pictures/10000000000001A40000005CD26CCB4A8D0DF1F9.png

To revert to displaying all
curves, activate the context menu from within the plot area and select
the menu item :menuselection:`Show all curves` (see figure below).

.. image:: ./Pictures/1000000000000109000001041C877E8A24D5AB94.png

Select Curve Color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To choose a different curve color, right click an item in the plot
legend. From the context menu select the menu item :menuselection:`Select Color` 
(see figure below).

.. image:: ./Pictures/10000000000002100000007CF77B5C49CD7E0D88.png

In the color
selection dialog which is now shown (figure below), you can choose any
color.

.. image:: ./Pictures/1000000000000222000001B58F8CFB4F56DCF4FD.png

Exporting Plot Image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/10001855000034EB000034EBA6C6DA993124AA4C.svg
   :width: 60
   :align: left

You may export a picture
of the current diagram using the toolbar or the right-click context menu and selecting
:menuselection:`Export plot image`. This will open a dialog box (see figure below) to
define the location (folder) where the image is to be saved:

.. image:: ./Pictures/100002010000010C000000E1260A96B6F1A86108.png

Please enter a name for the
image file :guinum:`❶` and select the desired file type :guinum:`❷`. The export function
supports standard image file formats (:file:`png, jpg...`) as well as scalable
vector graphic formats (:file:`.pdf, svg...`).

.. image:: ./Pictures/100002010000026300000143DB4B32F0CF0E84B4.png

To close the dialog and to start the image export, click :guilabel:`Save`:guinum:`❸`.

Deletion of Diagram Data
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/100019CB000035050000350509AD2B23340F765E.svg
   :width: 60
   :align: left

You may clear the plot area and delete all data recorded
since the start of the present recording using the context menu item
:menuselection:`Clear plot data`. Recording will resume from this point.

.. image:: ./Pictures/100002010000010D000000D1835EC0ADB6A09475.png

Switching the scaling of the X-axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/100018130000350500003505CADD59D81E3150FD.svg
   :width: 60
   :align: left

You can switch the scaling of the X-axis between two
different modes. By default, the X axis displays an absolute date/time
stamp.

.. image:: ./Pictures/100002010000022B0000006E35B772A9B9B293D2.png

You can switch the
X-axis to display the relative time in seconds and milliseconds. This
means that the event t\ :sub:`0` marks the point in time at which the
recording was started.

To toggle the axis, right-click in the diagram and select
:menuselection:`Toggle X-axis scale` from the context menu.

.. image:: ./Pictures/100002010000010D000000C7FB8978837EA08B41.png

Script Functions
----------------

.. image:: ./Pictures/10000201000000FB0000005C7BE945F338BAE398.png

To automate the capture of data or
to synchronize data capture with other processes, the data acquisition
can be started and stopped using QmixElements script functions. The
corresponding functions can be found in the :guilabel:`DAQ` category in the list
of the available script functions.

Start Data Acquisition
~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/10002C2B000034EB000034EB03167AF23B475C0B.svg
   :width: 60
   :align: left

This function is used to start the data acquisition with the
currently configured settings and channels. The current content of the
plot is not deleted.

|

Stop Data Acquisition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: ./Pictures/10002BC8000034EB000034EB9AA7EDFD557960B7.svg
   :width: 60
   :align: left

This function stops data acquisition.

|

Importing Log Files
-------------------

The DAQ add-on offers the functionality to read recorded log-files into
the plot. The tool for importing log files is able to recognize related
log files of a long-term recording and import all related log files in
chronological order. For large amounts of data, individual data points
are omitted so that a maximum of one million data points per log curve
are displayed in the plot.

.. admonition:: Important
   :class: note

   The import tool recognizes log files     
   that belong together and reads them in chronological    
   order.   

To read in a single log file or a series of log files proceed as
follows:

.. rst-class:: steps

#. From the toolbar select the tool for importing log files.

#. Select an arbitrary file from the log file series you want to read
   in. In the example shown, the tool recognizes from the file
   numbering that the log files belong together.

   .. image:: ./Pictures/1000020100000278000001D0E39D30D1CC066F05.png

#. The log files are then read in. The progress window
   displays the progress of the import process. You can continue
   working with the software during the import.

   .. image:: ./Pictures/10000201000002FC00000282E7401BFC642FC493.png

#. After completion
   of the import process, the log curves are displayed in the graphical
   plot together with the file name.

   .. image:: ./Pictures/100002010000025C00000201E71E54E4AEA77F6D.png

Pattern Scan
------------

The DAQ add-on offers the possibility to search plot curves for patterns
and mark them in the graphical plot.

Configuring and Running the Pattern Scan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following simple example explains pattern recognition based on the
recognition of square wave signals.

.. rst-class:: steps
   
#. A plot curve is given, which contains square wave signals with a
   width between 5 and 8 seconds and a peak value of 5V.

   .. image:: ./Pictures/10000201000004EF000001D3F48FD363154B3642.png

#. To configure
   the pattern scan, right-click the curve you want to scan :guinum:`❶` and
   select :menuselection:`Configure Pattern Scan` :guinum:`❷`.

   .. image:: ./Pictures/10000201000002BC0000019435E84DFC0044B4A8.png

#. In the dialog
   that opens afterwards, you must first create a new pattern
   scanner. To do this, click the :guilabel:`Add New Time Value Pattern Scanner`
   button :guinum:`❶`. Then you can give the pattern scanner a
   meaningful name :guinum:`❷`. In the example, *Rectangle Pattern Scanner* is
   selected. With the button :guinum:`❸` you can delete the selected pattern
   scanner and with :guinum:`❹` you can delete all pattern scanners.

   .. image:: ./Pictures/100002010000023C0000025250C7943D7A04C238.png

#. A report file is generated
   during pattern recognition. This file contains the measured values
   around the median of the recognized pattern. How many values around
   the median should be contained in the report file can be configured
   via the input field :guilabel:`Number of Median Values` :guinum:`❶`. 
   If you want all
   measurement values within the detected pattern to be included in the
   report file, select the check box :guilabel:`Use All` :guinum:`❷`.

   .. image:: ./Pictures/10000201000002240000013BA4342E81413037EB.png

#. The next step is to configure the patterns
   to be recognized by the pattern scanner. To do this, you must select
   the pattern scanner :guinum:`❶` whose pattern you want to configure. You can
   then create a new pattern using the :guilabel:`Create Item` button :guinum:`❷`. 
   You can now give the created pattern a meaningful name :guinum:`❸`.

   .. image:: ./Pictures/100002010000023C00000252E671EDC37054DC8E.png

#. The next step is to describe the
   pattern to be recognized. Since square wave signals with a duration
   of 5 - 8 seconds and a height of 5V are to be recognized, a section
   with a minimum duration of 5 seconds and a maximum duration of 8
   seconds, as well as a minimum value of 4.8 and a maximum value of
   5.2 is created. The value range is selected between 4.8 and 5.2 to
   tolerate a certain noise of the measurement signal. To do this,
   enter the above values in the first sample line that was
   automatically generated.

   .. image:: ./Pictures/10000201000002270000012D0A91CE9C8E182551.png

#. Then the end of the
   rectangular pattern must be detected. The measuring signal must drop
   back to approximately 0V for a certain time. Thus a new section is
   inserted with a duration of 0.2 to 0.5 seconds, in which the
   measurement signal must remain between -0.2 and +0.2. To do this,
   click on the point after which the new section is to be inserted :guinum:`❶`,
   and then click on :guilabel:`Add Item` :guinum:`❷`. Then enter the specified values in
   the newly created line.

   .. image:: ./Pictures/10000201000002310000012F01CDDA082C5126D6.png

   .. tip::
      A single pattern scanner can detect multiple  
      patterns. Repeat steps **(5)** - **(7)** to add another     
      pattern to your pattern scanner.  

#. In the penultimate step, you can specify a file path where the
   report file is stored. To do this, click on the :guilabel:`Report File` button
   and enter the file path and name in the file dialog that opens.
   Finally, click on the :guilabel:`OK` button to complete the configuration of
   the pattern scanner.

   .. admonition:: Important
      :class: note

      The pattern recognition settings for a   
      plot curve are saved. When the plot curve is reloaded,  
      the corresponding pattern scanner is automatically      
      assigned to it.  

#. In the last step the pattern scan is executed. To do this, click the
   :guilabel:`Run Pattern Scan` button :guinum:`❶`. The start :guinum:`❷` and 
   end :guinum:`❸` points of the recognized patterns are then marked in the plot. 
   A message :guinum:`❹` will show you how many patterns have been detected in 
   the plot curves being examined. The report file is also written.

   .. image:: ./Pictures/10000201000004E40000026C5BCC6D58152989B2.png

Using an Existing Pattern Scanner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you have configured a pattern scanner, you can assign it to a
variety of other plot curves. Proceed as follows:

.. rst-class:: steps

#. Right-click on the curve you want to scan and select
   :guilabel:`Configure Pattern Scan`.

   .. image:: ./Pictures/10000201000002BC0000019435E84DFC0044B4A8.png

#. In the dialog
   that opens, select the pattern scanner you want to use and then
   click :guilabel:`OK`.

   .. image:: ./Pictures/100002010000023C00000252776076AF95048BA6.png

Enabling / Disabling Pattern Recognition for a Plot Curve
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable or disable the pattern recognition for a plot curve,
right-click on the plot curve :guinum:`❶` and select 
:menuselection:`Enable / Disable Pattern Scan` :guinum:`❷`.

.. image:: ./Pictures/100002010000013C000000F65410305BA939F782.png

Result Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
^^^^^^^^

Using the result analysis for pattern recognition, you can compare the
individual results of a pattern recognition within a measured value
curve. The individual results are superimposed in a separate analysis
plot. This allows you to assess how they have changed during the course
of the measurement. You can access the result analysis of pattern
recognition by clicking the :guilabel:`Pattern Analysis` button :guinum:`❶` in the 
:guilabel:`DAQ` group (see figure below).

.. image:: ./Pictures/10000201000003B700000297E47C9D294ED8BE10.png

.. rst-class:: guinums

#. **Pattern Analysis** selector button – This button takes you to the
   result analysis of the pattern recognition.
#. **Diagram** – In the diagram, the measured values of each individual
   pattern recognition result are displayed one above the other. Here
   you can compare the individual results with each other.
#. **Legend** – The legend contains the designation of all curves that
   are displayed in the diagram with the corresponding color. The curve
   designation contains the relative time at which the result occurred
   in the original trace.
#. **Toolbar** – Here you will find buttons for navigating within the
   display, as well as for selecting the plot curve in the process data
   diagram whose pattern recognition results are to be displayed in the
   result analysis. The operating elements of the navigation work in the
   same way as the operating elements in the process data diagram (see
   section `Diagram Navigation & Use`_) and are therefore not
   explained again.

Carrying Out a Results Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Section `Configuring and Running the Pattern Scan`_
describes how to perform pattern recognition. Assume that after
performing pattern recognition there are two plot curves with results
(see figure below).

.. image:: ./Pictures/10000201000003B7000002978124C09E73F81507.png

.. rst-class:: steps

#. In the first step, select the :guilabel:`Pattern Analysis` button from the
   :guilabel:`DAQ` group to access the results analysis.

   .. image:: ./Pictures/10000201000001CA0000011B98CA543B7F823990.png

#. In the second step, select the
   plot curve whose results you would like to have displayed from the
   drop-down field in the toolbar. In the example shown, "Channel 2
   Extinction" is selected.

   .. image:: ./Pictures/10000201000002D2000000AAF371EF2EC38EC678.png

#. The
   diagram now shows the individual pattern recognition results for
   "Channel 2 Extinction". For this plot curve, two matches were found
   with the configured pattern. You can see that both results have the
   same amplitude. However, the result which occurred after 30.7
   seconds takes about 1.6 seconds longer than the result which
   occurred after 12.9 seconds.

   .. image:: ./Pictures/10000201000003B700000297B9603A75211E898D.png


.. |image34| image:: ./Pictures/10004180000034EB000034EB6DA9ACE22B65C020.svg
   :width: 60
.. |image35| image:: ./Pictures/10002C2B000034EB000034EB03167AF23B475C0B.svg
   :width: 60
.. |image36| image:: ./Pictures/100005C7000035050000350518807CBDF5FF2BAE.svg
   :width: 60
.. |image37| image:: ./Pictures/1000100A000034EB000034EBFC7CEEC6D6B20A4B.svg
   :width: 60
.. |image38| image:: ./Pictures/10000AAD0000350500003505B065E97D3266EBF3.svg
   :width: 60
.. |image39| image:: ./Pictures/10000AA70000350500003505B68BB28A6EC24106.svg
   :width: 60
.. |image40| image:: ./Pictures/10000D410000350500003505737D2F8FEABFA448.svg
   :width: 60
.. |image41| image:: ./Pictures/10001744000034EB000034EBD90F77816321BB6E.svg
   :width: 60
.. |image42| image:: ./Pictures/1000032600003505000035052A2D87EA9B64D7C0.svg
   :width: 60
.. |image43| image:: ./Pictures/100019CB000035050000350509AD2B23340F765E.svg
   :width: 60
.. |image44| image:: ./Pictures/100018130000350500003505CADD59D81E3150FD.svg
   :width: 60
.. |image45| image:: ./Pictures/10001855000034EB000034EBA6C6DA993124AA4C.svg
   :width: 60
.. |image47| image:: ./Pictures/100004EA000035050000350581CFD983D12D425F.svg
   :width: 40
.. |image48| image:: ./Pictures/1000034B000035050000350585C9BEED447C4FB8.svg
   :width: 40
.. |image49| image:: ./Pictures/10000B740000350500003505221106A05ED7DC85.svg
   :width: 40

.. |image56| image:: ./Pictures/100000000000012100000091DA9FF37806721579.png
.. |image57| image:: ./Pictures/10000000000001220000008F22C1F8D0316FE153.png
.. |image69| image:: ./Pictures/10000000000001EC000002E9E123686A038FFB99.png
   :width: 80
.. |image70| image:: ./Pictures/10000000000001EC000002E9C869BC0EE323BD20.png
   :width: 80
.. |image80| image:: ./Pictures/10000AAD0000350500003505B065E97D3266EBF3.svg
   :width: 60
.. |image81| image:: ./Pictures/10000AA70000350500003505B68BB28A6EC24106.svg
   :width: 60
.. |image82| image:: ./Pictures/10000D410000350500003505737D2F8FEABFA448.svg
   :width: 60
.. |image83| image:: ./Pictures/10001744000034EB000034EBD90F77816321BB6E.svg
   :width: 60
