#!/bin/bash
set -e

# install all dependencies
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip

virtualenv pandas/py-pandas --python=/usr/bin/python3.6
source pandas/py-pandas/bin/activate

# install binaries
python -m pip install --upgrade psutil
python -m pip install --upgrade pandas
python -m pip install --upgrade pyarrow

# check
python
import pandas as pd
pd.__version__
quit()

deactivate
