from sklearn import tree
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier,\
    GradientBoostingRegressor, AdaBoostRegressor, StackingRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, ElasticNet, LassoLars, Lasso, RidgeCV
import xgboost as xgb
from sklearn.svm import SVR


models = {
    'DTGC': tree.DecisionTreeClassifier(criterion='gini', random_state=42),
    'DTEC': tree.DecisionTreeClassifier(criterion='entropy', random_state=42),
    "RF": RandomForestClassifier(random_state=42),
    "XGB": xgb.XGBClassifier(random_state=42),

}
