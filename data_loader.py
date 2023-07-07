# read the csv file and show the info
import pandas as pd
import numpy as np
from IPython.display import display

def data_loader(fileName):
    
    # get the path name
    
    # read the data using pandas
    raw_data = pd.read_csv(fileName)
    
    # show variable (column) information
    display(raw_data.head(3))
    display(raw_data.info())