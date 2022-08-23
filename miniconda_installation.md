## Installation Miniconda ##
- Download miniconda: 
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```
- run the installation script:
```
bash Miniconda3-latest-Linux-x86_64.sh
```
- Accept Licence and provide installation path (or default) (eg. below):
```
/home/xyx/Anindya/miniconda3
```
- Restart your terminal to reload the environment variables, then check the installed conda version:
```
conda --version
```
- Update conda to latest version
```
conda update conda
```
- conda: not found
```
export PATH="/home01/anindya.sundardas/miniconda3/bin:$PATH"
```
## Virtual Environment ##
- Create new virtual environments ( here env name py37, version 3.7 or whatever version you like)
```
conda create --name py37 python=3.7
```
- Delete a virtual environment:
```
conda remove --name p37 --all
```
- List all virtual environments:
```
conda info -e
```
### Names and prefixes ###
- For a Conda env to have a name it must be installed in one of the envs_dirs directories
  ```
  conda config --show envs_dirs
  ```
- Creating an env outside of one of those forfeits its "name-ability". Instead, one must use the path (called its prefix) to activate it, e.g.
  ```
  conda activate /home/name/anaconda3/envs/my_env_name
  ```
- Adding Other Env Locations
  ```
  conda config --prepend envs_dirs /home/name/anaconda3/envs
  ```
 ### Activate Virtual Environment
- Activate a virtual environment:
```
conda activate py37
```
- Deactivate current virtual environment
```
conda deactivate
```
- Install Python packages:
```
conda install {package_name}
```
- Uninstall Python packages
```
conda uninstall {package_name}
```
or 
```
conda remove {package_name}
```
- Update Python packages
```
conda update {package_name}
```
- Search for a package
```
conda search {package_name}*
```
-  To use explicit specification files to build an identical conda environment
-- Specification files looks like :
```
# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
# platform: osx-64
@EXPLICIT
https://repo.anaconda.com/pkgs/free/osx-64/mkl-11.3.3-0.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/numpy-1.11.1-py35_0.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/openssl-1.0.2h-1.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/pip-8.1.2-py35_0.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/python-3.5.2-0.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/readline-6.2-2.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/setuptools-25.1.6-py35_0.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/sqlite-3.13.0-0.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/tk-8.5.18-0.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/wheel-0.29.0-py35_0.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/xz-5.2.2-0.tar.bz2
https://repo.anaconda.com/pkgs/free/osx-64/zlib-1.2.8-3.tar.bz2
```
1. To create an environment and install the dependencies in the same environment:
```
conda create --name <env> --file <this file>
```
2. To install in the current working environment
```
conda install --file <this file>
```
3. Export conda env into a new yml file
```
conda env export > environment_extract.yml
```
4. Create conda env from yaml file (before that change the conda environment name)
```
conda env create -f environment_extract.yml
```
