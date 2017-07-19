**{{name}}** {{description}}. Credit goes to `frappe's gantt chart`_

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
