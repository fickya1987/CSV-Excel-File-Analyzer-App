import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def perform_comparative_linear_regression(df, dependent_var, independent_vars, group_var):
    """
    Perform Comparative Linear Regression and generate visualization.
    
    :param df: Pandas DataFrame with the data.
    :param dependent_var: The dependent variable.
    :param independent_vars: List of independent variables.
    :param group_var: The variable used for grouping data.
    :return: Plotly figure object.
    """
    # Initialize a list to store results
    results = []
    fig = px.scatter(df, x=independent_vars[0], y=dependent_var, color=group_var, title="Comparative Linear Regression")

    # Loop over each group
    for group in df[group_var].unique():
        subset = df[df[group_var] == group]
        X = subset[independent_vars]
        y = subset[dependent_var]

        # Linear regression model
        model = LinearRegression().fit(X, y)
        y_pred = model.predict(X)
        r2 = r2_score(y, y_pred)

        # Store results
        results.append({'Group': group, 'Coefficients': model.coef_, 'R²': r2})

        # Add regression line to the plot
        fig.add_scatter(x=subset[independent_vars[0]], y=y_pred, mode='lines', name=f'{group} Fit')

    return fig, results

