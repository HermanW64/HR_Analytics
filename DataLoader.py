# read the csv file and show the info
import pandas as pd
import numpy as np
from IPython.display import display


class DataLoader():
    def __init__(self, fileName):
        path = "./Dataset/" + str(fileName)
        self.dataset = pd.read_csv(path)
        self.dataset_height = self.dataset.shape[0]
        self.dataset_width = self.dataset.shape[1]
        self.dataset_varlist = self.dataset.columns.to_list()

    def show_head(self, num_rows):
        # show the first num_rows rows
        display(self.dataset.head(num_rows))
        
    def show_variable_info(self):
        # show variable (column) information
        display(self.dataset.iloc[:, 0:int(self.dataset_width/2)].info())
        display(self.dataset.iloc[:, int(self.dataset_width/2): self.dataset_width].info())

    def show_description(self):
        # show summaries of the columns
        display(self.dataset.iloc[:,0: int(self.dataset_width/2)].describe())
        display(self.dataset.iloc[:,int(self.dataset_width/2):self.dataset_width].describe())

    # ---------------------------data manipulation-------------------------

    def delete_column(self, col_name):
        # delete the particular column
        # You should work on the dataset_output (deep copy of original one), not the original one
        if col_name in self.dataset_varlist:
            self.dataset = self.dataset.drop(columns=str(col_name), axis=1)
            self.dataset_varlist = self.dataset.columns.to_list()

        else:
            print("Already deleted!")

    def change_var_type(self, col_name, new_type):
        # change the column type to int, float, string, boolean
        if new_type not in [int, float, str, bool]:
            print("Only int, float, str, bool are acceptable!")
            return
        
        self.dataset[col_name] = self.dataset[col_name].astype(new_type)

    def replace_values(self, col_name, mapping_dict):
        # repalce the values in the column, from old to new
        # mapping_dict should be a dictionary
        self.dataset[col_name] = self.dataset[col_name].replace(mapping_dict)

    def check_missingValues(self):
        # show number of missing values in each column
        missing_values = self.dataset.iloc[:, 0: int(self.dataset_width/2)].isnull().sum()
        display(missing_values)
        missing_values = self.dataset.iloc[:, int(self.dataset_width/2): self.dataset_width].isnull().sum()
        display(missing_values)

    def save_dataset(self):
        # save current dataset as cleaned data
        output_path = "./Dataset/cleaned_Employee_Attrition.csv"
        self.dataset.to_csv(output_path, index=False)
        print("Dataset saved!")

    # ---------------------------Interactive Pipeline Process-------------------------
    def run_pipeline(self):
        # Read the data, and show basic info
        print("Data loaded! The basic info is displayed below:")
        print("The first 3 rows: \n")
        self.show_head(3)

        print("The descriptive info of each variable: \n")
        self.show_description()

        # Remove redundant/meaningful variables (EmployeeCount, StandardHours)
        while True:
            del_col = str(input("Which variable need to be deleted?(Enter the variable name, or enter 'skip' to skip)"))
            if del_col.lower() == 'skip':
                print("As you wish! The step is skipped!")
                break
            
            elif del_col in self.dataset_varlist:
                self.delete_column(del_col)
                print("{0} is deleted!".format(del_col))
                continue

            else:
                print("Varibale not found in the dataset. Available variables are: /n", self.dataset_varlist)
                continue

        # Replace values in certain varibales
        while True:
            col_name = str(input("Which variable's value need to be replaced?(Enter the variable name first, or enter 'skip' to skip the step)"))
            if col_name.lower() == 'skip':
                print("As you wish! The step is skipped!")
                break
            
            elif col_name in self.dataset_varlist:
                # show unique values
                unique_values = self.dataset[col_name].unique()
                print("You are focusing on varibale {0}. The unique values are: \n{1}".format(col_name, unique_values))
                dict_string = input("Please enter dictionary-like string for replacement (i.e., {'Yes': 1, 'No': 0}).")
                dict_string = eval(dict_string)

                if isinstance(dict_string, dict):
                    # replace the value
                    self.replace_values(col_name, dict_string)
                    print("Changed!")
                else:
                    print("Invalid input. Please enter a dictionary-like string.")

                continue

            else:
                print("Varibale not found in the dataset. Available variables are: \n", self.dataset_varlist)
                continue
        # data_loader.replace_values("Attrition", {"Yes": 1, "No": 0})

        # Change variable type
        print("The variable information: \n")
        self.show_variable_info()

        while True:
            col_name = input("Which varibale's data type needs to be changed? (Enter the varibale name first, or enter 'skip' to skip the step)")

            if col_name.lower() == "skip":
                print("As you wish! The step is skipped!")
                break

            elif col_name in self.dataset_varlist:
                print("You are focuing on ", col_name)

                while True:
                    new_type = input("Which type it should be?(int, float, str, bool)")

                    if str(new_type) in ['int', 'float', 'str', 'bool']:
                        self.change_var_type(col_name, eval(new_type))
                        print("Changed!")
                        break

                    else: 
                        print("only the 4 types are acceptable!")
                        continue

                continue

            else:
                print("Varibale not found in the dataset. Available variables are: \n", self.dataset_varlist)
                continue

        # Check Missing values
        print("Missing value checking: \n")
        self.check_missingValues()
        while True: 
            miss_val = input("How to deal with the missing values? (Enter skip to skip the step)")
            
            if miss_val.lower() == 'skip':
                print("As you wish! The step is skipped!")
                break

            else:
                print("You can only enter skip now!")
                continue
        
        # Export the cleaned data
        self.save_dataset()