from sklearn.cross_validation import KFold
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.linear_model import LassoCV, RidgeCV
from sklearn.cross_validation import train_test_split
import numpy as np
import pylab as pl
import pandas as pd

from dateutil.parser import parse
import datetime
import seaborn as sb

machine_header_descrip = pd.read_csv("./data/dictionary.csv")
machine_data = pd.read_csv("./data/data.csv", parse_dates=['saledate'],  
                           date_parser=lambda d: parse(d))
appdx = pd.read_csv("./data/machine_appendix.csv")

# Create columns for sale year, month and age for year minus year made
machine_data['Sale_Year'] = machine_data["saledate"].apply(lambda x: x.year)
machine_data['Sale_Month'] = machine_data["saledate"].apply(lambda x: x.month)
machine_data['Age'] = machine_data["Sale_Year"] - machine_data["YearMade"]

machine_data_sub = machine_data[["SalePrice", "ModelID", "YearMade", "Sale_Year", "Sale_Month", "Age"]]
machine_data_sub = machine_data_sub[machine_data_sub["Age"] >= 0]
machine_data_sub = machine_data_sub[machine_data_sub["Age"] <= 50]