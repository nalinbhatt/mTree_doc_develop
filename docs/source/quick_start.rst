=================
Quick Start Guide
=================

In this **Quick Start Guide**, we are going to run a simple **mTree** simulation 
while giving an overview of key components that are necessary for **mTree** to execute 
without error. The goal of this guide is to show you how to run an mTree simulation from 
start to finish and point out the vital indicators that convey a simulation has run properly. 

Cloning mTree_auction_examples
==============================


We are going to clone the **mTree_auction_examples** repository, which can
be found `here <https://github.com/gmucsn/mTree_learning_exercises>`_, and run one 
of the examples to  **mTree** is running properly. 


Open your command prompt and navigate to an apporpriate place using  within your 
file system where you want to clone the repository and run the following code - 

.. code-block:: console

    $ git clone https://github.com/gmucsn/mTree_auction_examples.git

This will create a **mTree_auction_examples** folder at your specified 
location.


Running mTree_auction_examples 
==============================

In order to run this simulation we need to create a **docker container** using 
the **Docker Desktop** app that we downloaded in  :doc:`installation` section. 

Follow all the steps highlighted in the :ref:`mTree-container-setup` section 
and set the **Host Path** to the mTree_auction_examples folder (which you cloned in the previous step)

If you setup the container correctly, click "Container/Apps" on the sidebar of 
**Docker Desktop**. There should be a container by the name **mTree_auction_examples**
present. 

.. figure:: _static/mTree_auction_examples_comp_setup.png
        :align: center

Start the container and open the shell. More details on how to do this are 
covered in :ref:`mTree-container-options` under :ref:`mTree-container-start`
and :ref:`mTree-container-cli`. 

Your shell should look some version of this - 

.. figure:: _static/mTree_auction_examples_shell.png
        :align: center

Run the following commands to view the underlying files in the folder.  

| **Mac** 

.. code-block:: console

    $ ls 

| **Windows**

.. code-block:: console

    $ dir

You should see the following subfolders in your command prompt -

.. figure:: _static/quick_start_ls.png
        :align: center

Tatonnement
-----------

One of the subfolders present should have the name **tatonnement** which refers to 
the famous :ref:`learning_path_tatonnement`  auction. Further information about the 
auction style and description can be found in the :doc:`learning_paths`.

In your **mTree_auction_examples** container shell type in the following command to set 
the current directory to **tatonnement**.

.. code-block:: console
    
    $ cd tatonnement

File Structure
--------------

After setting tatonnement as the current directory, run **ls** or **dir** and 
you should see the following folders. 

1. **config**
2. **mes**
3. **logs**

.. note::
    In order to properly run an mTree simulation you need to set the current 
    directory to the folder which contains a **config**, **mes**, and a **logs** folder.
    **mTree** looks for these particular folders to run the simulation. For our example, this is the **tatonnement**
    folder inside **mTree_auction_examples**.

.. tip:: 
    In the future, when designing your own container, you can set the **Host Path**
    directly to the folder containing the **config** and **mes** folder. That way 
    you don't have to navigate to the desired directory within the docker shell. 

config
^^^^^^
The :ref:`config` folder contains your **json config files** which are used to instantiate mTree actors defined in 
the **mes** folder. 

mes
^^^
The **mes** folder (short for Microeconomic System) containes the python files where you define the different 
Actor classes, namely - the :ref:`environment` , :ref:`institution` and :ref:`agent`. 

.. warning:: 

    It is critical that your **simulation folder** contain a **config** folder with a **json config file** inside it 
    and a separate **mes** folder with python files inside, which contain :ref:`environment` , :ref:`institution` and :ref:`agent` code.
    In the absence of **any** of these your mTree simulation **will not run**. 


Inside the **config** folder in the **tatonnement** auction example, you should see a **basic_simulation.json** file. 
This is the config file which we will run. 

For the next step we want to make sure that our current directory is **tatonnement** so if you used the **cd** command to 
change the directory to **config** and view its contents, we want to go up a directory using the following command to make sure 
we are in the right directory.

.. code-block:: console 

    $ cd .. 

.. _run_config:

Running simulation
------------------

We can type the following command into the shell to start mTree.  

.. code-block:: console 

    $ mTree_runner 

You should see something similar to this in your shell 

.. figure:: _static/quick_start_mTree_runner.png
        :align: center

Type the following in your shell to start the selection process for a config file 

.. code-block:: console 

    $ run_simulation


You should see something similar to this in your shell

.. figure:: _static/quick_start_run_simulation.png
        :align: center

Click **<enter>** to select and run the **basic_simulation.json** file. 
Your output should look something similar to this. 

.. figure:: _static/quick_start_run_config.png
        :align: center


What to expect?
---------------

(Under progress)
We should see 
Ideally when a simulation is run, you should setup Actors in such a way that they constantly **log** their states 
to :ref:`log_file` s and  :ref:`data_log` for gaining insights regarding actor behavior. 

logs
^^^^
The **logs** folder is where the output from your simulation gets stored. Under  

Quitting
--------


























