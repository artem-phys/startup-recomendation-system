import pandas as pd
import numpy as np
import math

services_filename = 'dataset/services_for_startups.xlsx'
services = pd.read_excel(services_filename, sheet_name=None)
