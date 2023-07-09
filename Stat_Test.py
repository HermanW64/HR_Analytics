# the file conducts chi-square test and correspendance analysis
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
import prince
from IPython.display import display

class Stat_Tester():

    def __init__(self, fileName):
        pathName = "./Dataset/" + str(fileName)
        self.dataset = pd.read_csv(pathName)
        self.varlist = self.dataset.columns.tolist()

    def show_rows(self, num_rows):
        # show the first num_rows rows
        display(self.dataset.head(num_rows))

    def generate_crosstable(self, col_1, col_2, chi_sq_test=False, ca=False):
        # generate a crosstable of two variables
        if (col_1 in self.varlist) and (col_2 in self.varlist):
            print("\n------Association between {0} and {1}------".format(str(col_1), str(col_2)))
            crosstable = pd.crosstab(self.dataset[str(col_1)], self.dataset[str(col_2)])
            display(crosstable)

            if chi_sq_test == True:
                # Perform the chi-square test
                chi2, p_value, dof, expected = chi2_contingency(crosstable)
                print("Chi-square statistic:", round(chi2, 4))
                print("P-value:", round(p_value, 4))
                print("Degrees of freedom:", dof)
                # print("Expected frequencies:\n", expected)

                if round(p_value) < 0.05:
                    print("Conclusion: there is a SIGNIFICANT relationship between {0} and {1}".format(str(col_1), str(col_2)))
                      
                else:
                    print("Conclusion: there is an insignificant relationship between {0} and {1}".format(str(col_1), str(col_2)))

        else:
            print("Invalid variable name(s), all available variables: \n", self.varlist)


