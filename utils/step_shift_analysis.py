import plotly.graph_objs as go

def detect_step_shifts(df, column, method='rolling_mean', window_size=10, threshold=1.0):
    """
    Detect potential step-shifts in a given column of a DataFrame using various methods.

    :param df: DataFrame containing the data.
    :param column: The column to analyze for step-shifts.
    :param method: Method to use for detecting step-shifts ('rolling_mean', 'rolling_median', 'cusum').
    :param window_size: The size of the rolling window to calculate the mean/median.
    :param threshold: The threshold for change in mean/median to detect a shift.
    :return: A list of indices where step-shifts are detected.
    """
    shifts = []

    if method == 'rolling_mean':
        rolling_stat = df[column].rolling(window=window_size, min_periods=1).mean()

    elif method == 'rolling_median':
        rolling_stat = df[column].rolling(window=window_size, min_periods=1).median()

    elif method == 'cusum':
        rolling_stat = cusum(df[column], threshold)

    else:
        raise ValueError(f"Method {method} not recognized.")

    if method in ['rolling_mean', 'rolling_median', 'cusum']:
        shifts = detect_shifts_from_rolling_statistic(rolling_stat, threshold)

    return shifts

def detect_shifts_from_rolling_statistic(rolling_statistic, threshold):
    """
    Helper function to detect shifts from a rolling statistic.

    :param rolling_statistic: Pandas Series with the rolling statistic.
    :param threshold: The threshold for detecting a shift.
    :return: A list of indices where step-shifts are detected.
    """
    shifts = []
    for i in range(1, len(rolling_statistic)):
        if abs(rolling_statistic.iloc[i] - rolling_statistic.iloc[i - 1]) > threshold:
            shifts.append(i)
    return shifts

def cusum(series, threshold):
    """
    CUSUM algorithm for change detection.

    :param series: Pandas Series to analyze.
    :param threshold: The threshold for detecting a shift.
    :return: Cumulative sum of changes in the series.
    """
    shifted_series = series - series.shift(1).fillna(0)
    return shifted_series.cumsum()

def plot_data_with_shifts(df, column, shifts):
    """
    Create a plot of the data with detected step-shifts highlighted.

    :param df: DataFrame containing the data.
    :param column: The column to plot.
    :param shifts: List of indices where shifts are detected.
    :return: Plotly figure object.
    """
    fig = go.Figure()

    # Add the main line plot for the data
    fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=column))

    # Add markers or lines for detected shifts
    for shift in shifts:
        fig.add_vline(x=df.index[shift], line_width=2, line_dash="dash", line_color="red")

    # Update layout
    fig.update_layout(title=f"Step-Shift Detection in {column}",
                      xaxis_title="Index",
                      yaxis_title=column,
                      hovermode="x unified")

    return fig

