Getting Started
===============

This guide will help you get started with SagittalBrain.

Installation
------------

Prerequisites
~~~~~~~~~~~~~

Before installing SagittalBrain, make sure you have:

* Python 3.10 or higher
* pip (Python package installer)

Install from source
~~~~~~~~~~~~~~~~~~~

Clone the repository and install in development mode:

.. code-block:: bash

   git clone https://github.com/YOUR_USERNAME/sagittal_average.git
   cd sagittal_average
   pip install -e .

Verify installation
~~~~~~~~~~~~~~~~~~~

Test that the installation was successful:

.. code-block:: bash

   python -c "import sagittal_brain; print('Success!')"
   sagittal_average_run --help

Quick Start
-----------

Using the command-line tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The simplest way to use SagittalBrain is through the command-line interface:

.. code-block:: bash

   # Process a file with default output name
   sagittal_average_run brain_sample.csv

   # Specify custom output file
   sagittal_average_run brain_sample.csv -o results.csv

   # View help
   sagittal_average_run --help

Using the Python API
~~~~~~~~~~~~~~~~~~~~

You can also use SagittalBrain directly in your Python code:

.. code-block:: python

   from sagittal_brain import run_averages

   # Process a file
   run_averages('brain_sample.csv', 'brain_average.csv')

Input File Format
~~~~~~~~~~~~~~~~~

Your input CSV file should be organized as:

* **Rows**: Intersections of sagittal/horizontal planes
* **Columns**: Coronal planes  
* **Values**: Intensity measurements

Example input file:

.. code-block:: text

   0,0,0,1
   0,0,0,1
   1,1,1,2

Output File Format
~~~~~~~~~~~~~~~~~~

The output file contains one value per input row, representing the average:

.. code-block:: text

   0.3
   0.3
   1.3

Example Workflow
----------------

Complete example
~~~~~~~~~~~~~~~~

Here's a complete example from start to finish:

.. code-block:: python

   import numpy as np
   from sagittal_brain import run_averages

   # 1. Create sample data
   data = np.random.rand(20, 20)
   np.savetxt('sample_brain.csv', data, delimiter=',')

   # 2. Process the data
   run_averages('sample_brain.csv', 'sample_output.csv')

   # 3. Load and inspect results
   results = np.loadtxt('sample_output.csv', delimiter=',')
   print(f"Processed {len(results)} planes")
   print(f"Average value: {results.mean():.2f}")

Next Steps
----------

* Read the :doc:`../api/modules` for detailed API documentation
* Check out the `GitHub repository <https://github.com/YOUR_USERNAME/sagittal_average>`_
* Report issues or contribute on GitHub

Troubleshooting
---------------

Command not found
~~~~~~~~~~~~~~~~~

If ``sagittal_average_run`` is not found, make sure:

1. You've installed the package: ``pip install -e .``
2. Your PATH includes pip's bin directory
3. Try using the full path: ``~/.local/bin/sagittal_average_run``

Import errors
~~~~~~~~~~~~~

If you get import errors:

1. Verify installation: ``pip list | grep SagittalBrain``
2. Reinstall: ``pip install -e . --force-reinstall``
3. Check Python version: ``python --version`` (should be 3.10+)
