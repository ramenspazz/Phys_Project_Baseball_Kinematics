# Baseball simulation
This is a repository for academic purposes that contains the tools requred to simulate general nonrelatevistic kinematics using the pytorch framework for multiprocessing and sympy and numpy for the symbolic function representations and number crunching respectivly.

Included with this repo at the top level is a YML file that can be used to clone my anaconda enviroment used to run this project. You can use jupyter notebooks, but it is much faster to use Microsoft© Visual Studio Code and install the jupyter notebook tools (it should automatically prompt you to install them when you open an ipynb file). The YML file can be installed by running the command:

```BASH
conda env create -f enviroment.yml
```

The file that actually runs the simulation is located in <project directory>/ipynb_files/baseball.ipynb
  
The files under Py_files are where all the magic happens! For the most part, it is just levraging multiprocessing to speed up multibody simulations or simulations with a large number of independant variables (high dimensionality). These files are mostly commented, and contain no "special sauce magic code." All relavent code is contained in these files for review.

Cheers!
