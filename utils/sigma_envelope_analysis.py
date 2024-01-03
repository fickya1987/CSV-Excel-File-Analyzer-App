import plotly.figure_factory as ff
import plotly.graph_objs as go

def calculate_sigma_bounds(df, column, sigma_level):
    mean = df[column].mean()
    std_dev = df[column].std()
    lower_bound = mean - sigma_level * std_dev
    upper_bound = mean + sigma_level * std_dev
    return lower_bound, upper_bound

def perform_sigma_envelope_analysis(df, column, sigma_level):
    lower_bound, upper_bound = calculate_sigma_bounds(df, column, sigma_level)
    std_dev = df[column].std()
    # Identifying outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

    # Creating normal distribution plot
    hist_data = [df[column].dropna()]
    group_labels = [column]
    dist_fig = ff.create_distplot(hist_data, group_labels, bin_size=[std_dev])

    # Add vertical lines for sigma bounds
    dist_fig.add_vline(x=lower_bound, line_dash="dash", line_color="red", annotation_text=f"{sigma_level}-Sigma Lower Bound")
    dist_fig.add_vline(x=upper_bound, line_dash="dash", line_color="green", annotation_text=f"{sigma_level}-Sigma Upper Bound")

    # Add scatter plot for outliers
    dist_fig.add_trace(go.Scatter(
        x=outliers[column],
        y=[0] * len(outliers),
        mode='markers',
        name='Outliers',
        marker=dict(color='orange', size=10)
    ))

    # Update layout with legend
    dist_fig.update_layout(
        title_text='Normal Distribution Plot',
        showlegend=True,
        legend=dict(
            orientation="h",
            y=5, yanchor="bottom",
            x=0.5, xanchor="center"
        )
    )

    return dist_fig
