# Copyright 2022 Autarky.ai LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Automated imports for IPython and Jupyter Notebook.

This script automatically imports a set of widely used modules at the
start of every IPython or Jupyter Notebook session.
"""

import math
import os
import warnings

try:
    import numpy as np
except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
except ImportError:
    pass
try:
    import pandas as pd
except ImportError:
    pass
try:
    import sklearn as sk
except ImportError:
    pass
try:
    import statsmodels.api as sm
except ImportError:
    pass
try:
    import yfinance as yf
except ImportError:
    pass
try:
    from tqdm import tqdm, trange
except ImportError:
    pass


warnings.filterwarnings('ignore')
try:
    np.random.seed(0)
except NameError:
    pass
try:
    plt.style.use('autarkydotai')
except NameError:
    pass
