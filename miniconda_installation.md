## Installation Miniconda ##
-Download miniconda: 
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
-run the installation script:
```
bash Miniconda3-latest-Linux-x86_64.sh
```
-Accept Licence and provide installation path (or default) (eg. below):
```
/home/xyx/Anindya/miniconda3
```
-Restart your terminal to reload the environment variables, then check the installed conda version:
```
conda --version
```
-Update conda to latest version
```
conda update conda
```
## Virtual Environment ##
-Create new virtual environments ( here env name py37, version 3.7 or whatever version you like)
```
conda create --name py37 python=3.7
``
-Delete a virtual environment:
```
conda remove --name p37 --all
```
-List all virtual environments:
```
conda info -e
```
-Activate a virtual environment:
```
conda activate py37
```
-Deactivate current virtual environment
```
conda deactivate
```
-Install Python packages:
```
conda install {package_name}
```
-Uninstall Python packages
```
conda uninstall {package_name}
```
or ```
conda remove {package_name}
```
-Update Python packages
```
conda update {package_name}
```
-Search for a package
```
conda search {package_name}*
```
