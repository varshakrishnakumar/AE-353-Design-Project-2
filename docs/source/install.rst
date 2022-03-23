Install
=====

.. _installation:

Installation
------------
The main file, *RunSegbot.ipynb*, runs on an *ae353* anaconda environment. The instructions given below will set up the user's system for project compilation.

.. code-block:: console
      conda create -n ae353
    
After creating the environment, if Jupyter and Git are not enabled on Anaconda's system, follow the instructions below

.. code-block:: console
      conda activate ae353
      conda config --env --add channels conda-forge
      conda config --env --set channel_priority strict
      conda install python=3 numpy scipy sympy matplotlib
      conda install notebook ipywidgets imageio imageio-ffmpeg pybullet
      conda install git
    

Next, clone this repository.

.. code-block:: console
      git clone https://github.com/varshakrishnakumar/AE-353-Design-Project-2.git
 

On an Anaconda Powershell terminal, locate the cloned repository and open Jupyter

.. code-block:: console  
      conda activate ae353
      cd *location of cloned repository*
      jupyter notebook
 

Upon completion of the instructions, a new Jupyter notebook will be opened. Navigate to *RunSegbot.ipynb* to compile the project.


