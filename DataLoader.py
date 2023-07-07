# read the csv file and show the info
import pandas as pd
import numpy as np
from IPython.display import display


class DataLoader():
    def __init__(self, fileName):
        path = "./Dataset/" + str(fileName)
        self.dataset = pd.read_csv(path)

    def show_head(self, num_rows):
        # show the first num_rows rows
        display(self.dataset.head(num_rows))
        
    def show_variable_info(self):
        # show variable (column) information
        display(self.dataset.info())