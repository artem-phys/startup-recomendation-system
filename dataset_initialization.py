import pandas as pd
import numpy as np
import math

services_filename = 'https://raw.githubusercontent.com/artem-phys/startup-recomendation-system/main/dataset/services_for_startups.xlsx'
services = pd.read_excel(services_filename, sheet_name=None)

services_sheets = list(services.keys())

print(services_sheets)
print(services[services_sheets[0]].head(1))

