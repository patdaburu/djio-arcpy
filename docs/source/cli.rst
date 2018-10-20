.. _cli:

.. image:: _static/images/logo.svg
   :width: 100px
   :alt: djio_arcpy
   :align: right

Using the Command Line Application
==================================

This project contains a command line application (`djio_arcpy`) based on
`Click <http://click.pocoo.org/5/>`_.

Installation
------------

The command line application is installed automatically when the package is installed.

Running the CLI in the Development Environment
----------------------------------------------

If you need to run the application from within the project's own development environment, you can
use the `make build` target.

.. code-block:: bash

   make build

Getting Help
------------

The command line application has a help function which you can access with the `--help` flag.

.. code-block:: bash

   djio_arcpy --help
