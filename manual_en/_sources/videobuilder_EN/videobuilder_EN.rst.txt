Video Builder Plugin
====================

Introduction to Video Builder Plugin
---------------------------------------

The Video Builder plug-in allows you to quickly compose videos from
individual images taken by timing or scripting via the :ref:`camera <camera add-on>` 
or the microscope plug-ins. This is useful, for instance, for time laps
recordings of slow microfluidic processes or for long-exposure
microscope pictures.

To open the Video Builder dialog, select the relevant item from the
main menu via :menuselection:`Edit --> Video Builder`.

.. image:: ./Pictures/10000201000001310000008F0C4519C7.png

The Video Builder dialog contains the following elements
(see figure below):

.. rst-class:: guinums

1. Tool bar,
2. List of image folder(s),
3. Video parameter settings,
4. Thumbnail of the currently processed picture,
5. Progress bar of the processing step.

.. image:: ./Pictures/1000000000000283000001972BF3C6F7.png


Video Assembly
-----------------------------------------------------

The following description shows you how to assemble a video from
individual images.

Step 1 – Select Image Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/folder.svg
   :width: 60
   :align: left

To select the image files that you want to process, first
locate the relevant folder and open it via :guilabel:`Select Image Folder` button 
in the tool bar. This opens a dialog box (see figure below) that allows you to 
navigate to the folder containing your image files :guinum:`❶`. Open the folder 
by clicking on :guilabel:`Choose` :guinum:`❷`.

.. image:: ./Pictures/10000000000002B8000001D0ABD946FD.png

Step 2 – Video Assembly Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The section *Video Parameters* is to configure the parameter settings for
the image assembly process.

.. image:: ./Pictures/100002010000016E0000008139FB0D6A.png

You can set the following parameters:

.. rst-class:: guinums

1. **Frames/s** – configures the frame rate, i.e., how many images are
   to be shown per second.
2. **Skip Frames** – set the number of images that are excluded from the
   video. If this value is set to zero, all image files will be used; if
   set to one, for instance, every other image will be skipped and thus
   only every second image will be used to assemble the video.

Based on the number of available images and the two parameters just set,
the third box :guilabel:`Duration (s)` :guinum:`❸` will show the length of the final
video.

.. image:: Pictures/deshaker.svg
   :width: 60
   :align: left

In addition, the software offers the possibility to de-shake (stabilize)
the video sequence using the built-in video stabilizer / deshaker. Just check
the :guilabel:`Activate Deshaker` button to enable video stabilization.

|

.. tip::
   Video sequences (e.g. of images captured from  
   microscope camera) can be stabilized using the de-shaker 
   function. 

.. admonition:: Important
   :class: note

   The de-shaking step will increase the     
   time for building a video.  

Step 3 – Start Video Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: Pictures/movie_run.svg
   :width: 60
   :align: left

Start the assembly process by clicking on the :guilabel:`Build Video` button.
This will open a dialog box that is to define the target directory and
the name of the video file. Processing will start immediately
thereafter.

|

.. image:: Pictures/background.svg
   :width: 60
   :align: left

The assembly process may take several minutes, in particular
when a large number of images is to be processed. Processing may be
continued as a background task by activating the :guilabel:`Move to background` 
feature. This will close the *Video Builder* dialog and allows you to continue
to work with the application.

If a process is being carried in the background, this will be indicated
in the status bar :guinum:`❶` of the main application window and in the 
*Progress View*  :guinum:`❷` (see figure below).

.. image:: ./Pictures/1000000000000268000001692F31C313.png

You will be notified via the application's :ref:`Event Log <event log>` as
soon as the video assembly process has been completed(see figure below).

.. image:: ./Pictures/100002010000027F000000853E1FBCAB.png

Now you may start the process with a new set of pictures or with
different settings.
