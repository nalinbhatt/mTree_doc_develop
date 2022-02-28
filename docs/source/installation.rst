============
Installation
============
.. 
    is mTree a software or a python library ?

In order to run **mTree** we need to install `Docker Desktop <https://www.docker.com>`_  first.  

.. _install-docker-desk:

Installing Docker Desktop
-------------------------

The links for **Docker Desktop** installation for different **os** can be found below. 

    - `Download Docker Desktop <https://www.docker.com/products/docker-desktop>`_

After completing the **Docker Desktop** installation, we can start installing **mTree**

.. _install-mTree:

Installing mTree
----------------

You can install **mTree** by pasting the following code in your command prompt, power shell or terminal.
However, make sure to check for the latest version of **mTree** `here <https://hub.docker.com/r/mtree/mtree/tags>`_,
in case the one below is out of date. 

.. code-block:: console

     docker pull mtree/mtree:1.0.11a

.. note:: 

    The command prompt should be based in the same virtual environment where you
    have **Docker Desktop** installed. 

After pasting and running the command in your command prompt, your screen should look
like something like this 

.. figure:: _static/terminal.png
        :align: center


.. _mTree-container-setup:

mTree Container Setup
----------------------

.. tip:: 

        If you don't have an **mTree** simulation that is ready to run or you are new to **mTree**, visit
        the :doc:`quick_start` before you do this next step. 

Open **Docker Desktop** app on your computer and click
**Images** on the sidebar. 

.. figure:: _static/mTree_image.png
        :align: center

     
You should see the **mTree** image we just downloaded through docker hub in the previous step.
In the next step, we are going to run this image within a small virtualization of the **os** called a 
**container**. We can create our docker **container** by clicking **RUN** on the **mTree** image. 

After that you should see the following window. Follow all the steps, in the image below, before moving 
on to the next step. 

.. figure:: _static/mTree_container_setup.png
        :align: center

Once all the instructions in the above image are completed, you should click **Containers/Apps**
on the sidebar. After hitting **Containers/Apps**, you should see the following container -

.. figure:: _static/installation_unstarted_container.png
        :align: center


.. _mTree-container-options:

Container Options
^^^^^^^^^^^^^^^^^
Your container comes with several options that can be executed to change its 
state. 

.. _mTree-container-start:

Start
*****

Click ``START`` to start your container. 

.. figure:: _static/start_button.png
        :align: center

A running docker container should have a green symbol on the left side. 

.. figure:: _static/started_container.png
        :align: center

.. _mTree-container-stop:

Stop
****
You can stop running your container by pressing ``STOP`` button

.. figure:: _static/stop_button.png
        :align: center

.. _mTree-container-restart:

Restart
*******

You can restart your container by pressing the ``RESTART`` button 

.. figure:: _static/restart_button.png
        :align: center

.. _mTree-container-delete:

Delete
******
If you want to delete the image, you can press the ``DELETE`` button

.. figure:: _static/delete_button.png
        :align: center

.. _mTree-container-cli:

Open Shell
**********

Once your container is running, you should click ``CLI`` button to open the command prompt/shell
linked to your container. 

.. figure:: _static/shell_button.png
        :align: center

The command prompt produced by Docker should look similar to the following -

.. figure:: _static/container_command_prompt.png
        :align: center









