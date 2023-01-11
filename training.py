#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sklearn as sk


# In[2]:


pricing_requests = pd.read_csv("AVN_Data.csv",index_col =0)


# In[3]:


from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from category_encoders import TargetEncoder


# In[4]:


hotels = pd.read_csv('features_hotels.csv', index_col=['hotel_id', 'city'])


# In[5]:


y = pricing_requests["price"]
X = pricing_requests.loc[ : , pricing_requests.columns != 'price']


# In[6]:


X


# In[7]:


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import QuantileTransformer, StandardScaler


numeric_features = ["hotel_id", "stock","date"]
numeric_transformer = Pipeline(
    steps=[("scaler", StandardScaler())]
)

categorical_features = ["city","language","mobile","avatar_id","group","brand","parking","pool","children_policy"]
categorical_transformer = TargetEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)


# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 500, num = 3)]
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 50, num = 3)]
max_depth.append(None)
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Create the random grid
random_grid = {'randomforestregressor__n_estimators': n_estimators,
               'randomforestregressor__max_depth': max_depth,
               'randomforestregressor__min_samples_leaf': min_samples_leaf}

# Create the pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('randomforestregressor', RandomForestRegressor())
])

# Create the randomized search object
random_search = RandomizedSearchCV(estimator=pipeline, param_distributions=random_grid, n_iter=100, cv=3, verbose=2, random_state=42, n_jobs=-1)

# Fit the randomized search object to the training data
random_search.fit(X, y)

# Get the best combination of hyperparameters
best_params = random_search.best_params_


# In[8]:


best_params


# In[9]:


#get_ipython().run_line_magic('pinfo', 'RandomForestRegressor')


# In[10]:


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import QuantileTransformer, StandardScaler


numeric_features = ["hotel_id", "stock","date"]
numeric_transformer = Pipeline(
    steps=[("scaler", StandardScaler())]
)

categorical_features = ["city","language","mobile","group","brand","parking","pool","children_policy"]
categorical_transformer = TargetEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)



# Create the pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('randomforestregressor', RandomForestRegressor(n_estimators = 300))
])

pipeline.fit(X, y)

import pickle

with open('random_forest.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

# In[11]:


test = pd.read_csv("test_set.csv",index_col =0)

test = test.join(hotels, on=['hotel_id', 'city'])
test = test.drop(["order_requests"],axis =1)


# In[20]:


X.columns


# In[21]:


test=test[['hotel_id', 'stock', 'city', 'date', 'language', 'mobile', 'avatar_id','group', 'brand', 'parking', 'pool', 'children_policy']]


# In[22]:


A = random_search.predict(test)


# In[23]:


Submission = pd.DataFrame(A)

Submission.to_csv("submission2023.csv",header = ["price"],index_label="index")


# In[24]:


print(Submission)


# 
