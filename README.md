# FaultTreeAnalysis
Python module for reliability computation

### **Install with conda**

the recommendation is to use Anaconda/Miniconda with your own enviroment for nmarkv.
```
conda create -n relpy python=3.8.2 jupyter numpy scipy matplotlib pybind11
conda activate FaultTreeAnalysis
conda install python-graphviz
pip install git+https://github.com/wsinwsin/FaultTreeAnalysis.git
```
For Jupyter, make the kernel for the environment `FaultTreeAnalysis`
```
conda activate FaultTreeAnalysis
ipython kernel install --user --name FaultTreeAnalysis
```
### **Install with pip**
```
pip install git+https://github.com/wsinwsin/FaultTreeAnalysis.git
```
Requriements:
- IPython
- pybind11
- numpy
- scipy
- pytest==5.4.3
- pytest-cov==2.10.0
- graphviz==0.14
- pydotplus==2.0.2

[Reference](https://github.com/okamumu/relpy)
