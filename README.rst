================================================================================
pyexcel-gantt - Let you focus on presentation with gantt
================================================================================

.. image:: https://raw.githubusercontent.com/pyexcel/pyexcel.github.io/master/images/patreon.png
   :target: https://www.patreon.com/pyexcel

.. image:: https://api.travis-ci.org/pyexcel/pyexcel-gantt.svg?branch=master
   :target: http://travis-ci.org/pyexcel/pyexcel-gantt

.. image:: https://codecov.io/github/pyexcel/pyexcel-gantt/coverage.png
   :target: https://codecov.io/github/pyexcel/pyexcel-gantt

.. image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :target: https://gitter.im/pyexcel/Lobby

.. image:: https://readthedocs.org/projects/pyexcel-gantt/badge/?version=latest
   :target: http://pyexcel-gantt.readthedocs.org/en/latest/

Support the project
================================================================================

If your company has embedded pyexcel and its components into a revenue generating
product, please `support me on patreon <https://www.patreon.com/bePatron?u=5537627>`_ to
maintain the project and develop it further.

If you are an individual, you are welcome to support me too on patreon and for however long
you feel like to. As a patreon, you will receive
`early access to pyexcel related contents <https://www.patreon.com/pyexcel/posts>`_.

With your financial support, I will be able to invest
a little bit more time in coding, documentation and writing interesting posts.



Introduction
================================================================================
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



Installation
================================================================================
You can install it via pip:

.. code-block:: bash

    $ pip install pyexcel-gantt


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/pyexcel/pyexcel-gantt.git
    $ cd pyexcel-gantt
    $ python setup.py install



Development guide
================================================================================

Development steps for code changes

#. git clone https://github.com/pyexcel/pyexcel-gantt.git
#. cd pyexcel-gantt

Upgrade your setup tools and pip. They are needed for development and testing only:

#. pip install --upgrade setuptools pip

Then install relevant development requirements:

#. pip install -r rnd_requirements.txt # if such a file exists
#. pip install -r requirements.txt
#. pip install -r tests/requirements.txt

Once you have finished your changes, please provide test case(s), relevant documentation
and update CHANGELOG.rst.

.. note::

    As to rnd_requirements.txt, usually, it is created when a dependent
	library is not released. Once the dependecy is installed
	(will be released), the future
	version of the dependency in the requirements.txt will be valid.


How to test your contribution
------------------------------

Although `nose` and `doctest` are both used in code testing, it is adviable that unit tests are put in tests. `doctest` is incorporated only to make sure the code examples in documentation remain valid across different development releases.

On Linux/Unix systems, please launch your tests like this::

    $ make

On Windows systems, please issue this command::

    > test.bat

How to update test environment and update documentation
---------------------------------------------------------

Additional steps are required:

#. pip install moban
#. git clone https://github.com/pyexcel/pyexcel-commons.git commons
#. make your changes in `.moban.d` directory, then issue command `moban`

What is pyexcel-commons
---------------------------------

Many information that are shared across pyexcel projects, such as: this developer guide, license info, etc. are stored in `pyexcel-commons` project.

What is .moban.d
---------------------------------

`.moban.d` stores the specific meta data for the library.

Acceptance criteria
-------------------

#. Has Test cases written
#. Has all code lines tested
#. Passes all Travis CI builds
#. Has fair amount of documentation if your change is complex
#. Agree on NEW BSD License for your contribution




License
================================================================================

New BSD License
