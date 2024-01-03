import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit

def linear_regression(x, y):
    model = LinearRegression().fit(x, y)
    y_pred = model.predict(x)
    r2 = r2_score(y, y_pred)
    return y_pred, r2

def polynomial_regression(x, y, degree):
    polynomial_features = PolynomialFeatures(degree=degree)
    x_poly = polynomial_features.fit_transform(x)
    model = LinearRegression().fit(x_poly, y)
    y_pred = model.predict(x_poly)
    r2 = r2_score(y, y_pred)
    return y_pred, r2

def exponential_fit(x, y):
    def exp_func(x, a, b, c):
        return a * np.exp(b * x) + c
    params, _ = curve_fit(exp_func, x.flatten(), y)
    y_pred = exp_func(x, *params)
    r2 = r2_score(y, y_pred)
    return y_pred, r2

def perform_curve_fitting_analysis(df, independent_var, dependent_var, relationship_type, degree=None):
    x = df[[independent_var]].values
    y = df[dependent_var].values

    if relationship_type == 'linear':
        y_pred, r2 = linear_regression(x, y)
    elif relationship_type == 'polynomial' and degree is not None:
        y_pred, r2 = polynomial_regression(x, y, degree)
    elif relationship_type == 'exponential':
        y_pred, r2 = exponential_fit(x, y)
    else:
        raise ValueError("Invalid relationship type or missing degree for polynomial.")

    # Plotting
    fig = px.scatter(df, x=independent_var, y=dependent_var, title=f'{relationship_type.title()} Curve Fitting')
    fig.add_scatter(x=df[independent_var], y=y_pred, mode='lines', name='Fitted Curve')
    
    return fig, r2
