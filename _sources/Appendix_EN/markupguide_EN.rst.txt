:orphan:

Heading Level 1
================

Heading Level 2
----------------

Heading Level 3
~~~~~~~~~~~~~~~~

Heading Level 4
^^^^^^^^^^^^^^^^

Admonitions
----------------

.. tip::
   Describes practical tips and useful information to facilitate the handling 
   of the software.

.. admonition:: Important
   :class: note

   Describes important information and other especially useful notes, in which 
   no dangerous or damaging situations can arise.  

.. admonition:: Attention
   :class: caution

   Indicates a potentially damaging situation. Failure to avoid this situation 
   may result in damage to the product or anything nearby.      

.. admonition:: Caution
   :class: error
  
   Describes a situation that may be dangerous. If this aspect is not avoided, 
   light or minor injuries as well as damage to property could result. 


Lists
----------------

Steps
~~~~~~~~~~~~~~~~

Use the :code:`.. rst-class:: steps` directive for a list of steps

.. rst-class:: steps

#. Use the steps class to create a numbered list of steps. This is the first
   step.
#. This is the scond step
#. This is the third step
#. And now follows the fourth step

GUI Elements Numbering
~~~~~~~~~~~~~~~~~~~~~~~~

Use the :code:`.. rst-class:: guinums` to create a list with big red numbers
for numbering elements in a GUI screenshot.

.. rst-class:: guinums

#. This is the first numbered UI element in the screenshot
#. This is the second numbered UI element in the screenshot
#. This is the third numbered UI element in the screenshot
#. This is the fourth numbered UI element in the screenshot

Inline Markup
----------------

GUI Elements Numbering
~~~~~~~~~~~~~~~~~~~~~~~~

For inline text numbering, you can use the following markup. This is the
first element :guinum:`❶`, followd by the second element :guinum:`❷`, then
comes the third :guinum:`❸` and fourth elment :guinum:`❹` and the last element
is the :guinum:`❺`.