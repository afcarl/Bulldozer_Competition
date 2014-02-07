imimport pandas as pd
import numpy as np
from scipy.stats.kde import gaussian_kde
from scipy.stats import norm as stats_norm
from scipy import stats
import statsmodels.api as sm
import statsmodels.stats.api as sms

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.linear_model import LassoCV, RidgeCV
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import scale

# first we ingest the data from the source on the web
# this contains a reduced version of the data set from Lending Club
loansData = pd.read_csv('machine _appendix.csv')

print loansData.head()