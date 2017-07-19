`pyexcel-gantt` - Let you focus on data, instead of file formats
================================================================================

:Author: C.W.
:Source code: http://github.com/pyexcel/pyexcel-gantt.git
:Issues: http://github.com/pyexcel/pyexcel-gantt/issues
:License: New BSD License
:Released: |version|
:Generated: |today|

Introduction
--------------------------------------------------------------------------------

**pyexcel-gantt** draws gantt chart using frappe-gantt.js for pyexcel data. Credit goes to `frappe's gantt chart`_

Here is `a sample csv`_ file::

    id,name,start,end,progress,dependencies,custom_class
    Task 1,Writing pyexcel-gantt,2017-07-17,2017-07-18,80,,
    Task 2,Test pyexcel-gantt,2017-07-19,2017-07-20,10,Task 1,,
    Task 3,Write up the documentation,2017-07-21,2017-07-22,0,Task 1,,
    Task 4,Release pyexcel-gantt,2017-07-23,2017-07-23,0,"Task 2, Task 3",,bar-milestone


What you can do is to view it with pyexcel's `command line interface`_:

    pyexcel view --in-browser --output-file-type gantt.html demo/tasks.csv

.. image:: https://github.com/pyexcel/pyexcel-gantt/raw/master/pyexcel-gantt.gif


Programmatically, you can do the following:

.. code-block:: python

    import pyexcel as p
    
    
    p.save_as(file_name='tasks.csv',
              dest_file_name='tasks.gantt.html')


Alternatively, you can save the file as:

.. code-block:: bash

   $ pyexcel transcode tasks.csv tasks.gantt.html 


.. _a sample csv: https://github.com/pyexcel/pyexcel-gantt/raw/master/demo/tasks.csv
.. _command line interface: https://github.com/pyexcel/pyexcel-cli
.. _frappe's gantt chart: https://github.com/frappe/gantt

Known constraints
==================

Fonts, colors and charts are not supported.

Installation
--------------------------------------------------------------------------------

You can install it via pip:

.. code-block:: bash

    $ pip install pyexcel-gantt


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/pyexcel-gantt.git
    $ cd pyexcel-gantt
    $ python setup.py install


Rendering Options
--------------------------------------------------------------------------------

You can pass the following options to :meth:`pyexcel.Sheet.save_as`.
The same options are applicable to
pyexcel's signature functions, but please remember to add 'dest_' prefix.

**embed** If it is set true, the resulting html will only contain a portion
of HTML without the HTML header. And it is expected that you, as the
developer to provide the necessary HTML header in your web page.


Embed Setup
--------------------------------------------------------------------------------


Please copy the hightlighted lines into the head section of each of your web pages:

.. code-block:: html
   :linenos:
   :emphasize-lines: 2-21

   <html><head>
    <style>
        body {
            font-family: sans-serif;
            background: #ccc;
        }
        .container {
            width: 80%;
            margin: 0 auto;
        }
        .gantt-container {
            overflow: scroll;
        }
        /* custom class */
        .gantt .bar-milestone .bar-progress {
            fill: tomato;
        }
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/snap.svg/0.5.1/snap.svg-min.js"></script>
    <script src="https://github.com/frappe/gantt/raw/master/dist/frappe-gantt.min.js"></script>
     </head><body>
    <!-- here is the embedded gatt -->
     </body>
   </html>


Then pass on `embed=True` to pyexcel signature functions. It is as simple as that.

License
================================================================================

New BSD License
