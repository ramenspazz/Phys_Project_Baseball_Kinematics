# Baseball simulation
This is a repository for academic purposes that contains the tools requred to simulate general nonrelatevistic kinematics using the pytorch framework for multiprocessing and sympy and numpy for the symbolic function representations and number crunching respectivly.

# High level description
This is a simulation of a baseball thrown at 44.7m/s at an angle of pi on 4 with both the xy and xz axis. This model uses a first order non-linear quadratic drag model in velocity to simulate air resistance as well, with a link to the page I found regulation baseball-ball stats on. 

# Running instructions

Included with this repo at the top level is a YML file that can be used to clone my anaconda enviroment used to run this project. You can use jupyter notebooks, but it is much faster to use MicrosoftÂ© Visual Studio Code and install the jupyter notebook tools (it should automatically prompt you to install them when you open an ipynb file). The YML file can be installed by running the command:

```BASH
conda env create -f enviroment.yml
```
Next, cd (set your current working directoy) to the location you would like to place the project files, then clone the github enviroment with the command (requires the git toolchain):

```BASH
git clone https://github.com/ramenspazz/Phys_Project_Baseball_Kinematics
```

The file that actually runs the simulation is located in <project directory>/ipynb_files/baseball.ipynb
  
The files under Py_files are where all the magic happens! For the most part, it is just levraging multiprocessing to speed up multibody simulations or simulations with a large number of independant variables (high dimensionality). These files are mostly commented, and contain no "special sauce magic code." All relavent code is contained in these files for review.
  
If you encounter any bugs, please let me know! Thank you and cheers!
