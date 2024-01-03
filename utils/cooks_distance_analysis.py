import plotly.graph_objs as go
import statsmodels.api as sm
import numpy as np

def cooks_distance_analysis(df, dependent_var, independent_vars):
    """
    Perform Cook's distance analysis to identify influential outliers in regression.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the dataset.
    dependent_var (str): The name of the dependent variable.
    independent_vars (list): A list of independent variable names.

    Returns:
    Plotly figure object showing Cook's distance for each observation.
    """
    
    # Prepare the data for regression model
    X = df[independent_vars]
    y = df[dependent_var]

    # Adding a constant for the regression model
    X = sm.add_constant(X)

    # Fitting the model
    model = sm.OLS(y, X).fit()

    # Calculate Cook's distance
    influ = model.get_influence()
    cooks_d = influ.cooks_distance[0]

    # Identifying outliers
    threshold = 4 / len(X)
    outlier_indices = np.where(cooks_d > threshold)[0]
    outliers = df.iloc[outlier_indices]

    # Plotting
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(len(cooks_d)), y=cooks_d, mode='markers',
                             name='Cook\'s Distance',
                             marker=dict(color='lightblue', size=10)))
    
    # Highlighting outliers
    fig.add_trace(go.Scatter(x=outlier_indices, y=cooks_d[outlier_indices], mode='markers',
                             name='Outliers',
                             marker=dict(color='red', size=12)))

    # Adding threshold line
    fig.add_hline(y=threshold, line_dash="dash", line_color="green", 
                  annotation_text="Threshold")

    # Update layout
    fig.update_layout(title='Cook\'s Distance Outlier Detection',
                      xaxis_title='Observation Index',
                      yaxis_title='Cook\'s Distance',
                      hovermode="x unified")

    return fig
