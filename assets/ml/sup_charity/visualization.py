__author__ = "Chris"
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dython.nominal import associations


def dist_vis(data: pd.core.frame.DataFrame,
             column: str = None,
             bars: int = None,
             separator: str = None,
             fig_title: str = None,
             x_title: str = None,
             legend: bool = False,
             h: int = 600,
             w: int = 750):
    """
    Function to create visuals of distributions with plotly

    Parameters
    ----------
    :param data: dataframe
    :param column: factor to view
    :param bars: number of bins
    :param separator: factor to differentiate the distribution by with color
    :param fig_title: title of figure
    :param x_title: title for x-axis
    :param legend: indicate to use a legend
    :param h: height
    :param w: width
    :return: plotly.graph_objs._figure.Figure
    """
    figure_0 = px.histogram(data, x=column, nbins=bars, color=separator, opacity=0.75)
    figure_0.update_layout(height=h, width=w,
                           title_text=fig_title,
                           showlegend=legend)
    figure_0.update_yaxes(title_text="Number of Records")
    figure_0.update_xaxes(title_text=x_title)

    return figure_0


def comp_dist(data: pd.core.frame.DataFrame,
              fac_1: dict = {},
              fac_2: dict = {}):
    """
    Function to compare distributions

    Parameters
    ----------
    :param data: Pandas Dataframe
    :param fac_1: information around the first factor to display
            {'column_name': None,
            'title': None,
            'x_axis': None}
    :param fac_2: information around the second factor to display
        {'column_name': None,
        'title': None,
        'x_axis': None}
    :return:
    """
    # Define space for figure
    figure_1 = make_subplots(rows=2, cols=1)

    # Define dimensions, title, and legend
    figure_1.update_layout(height=800, width=850,
                           title_text="Skewed Distributions of Continuous Census Data Features",
                           showlegend=False)

    # Create plots
    figure_1.add_trace(
        go.Histogram(x=data[fac_1['column_name']], nbinsx=25,
                     name=fac_1['title']),
        row=1, col=1)
    figure_1.add_trace(
        go.Histogram(x=data[fac_2['column_name']], nbinsx=25,
                     name=fac_2['title']),
        row=2, col=1)

    # Define x-axis titles for plots
    figure_1.update_xaxes(title_text=fac_1['x_axis'], row=1, col=1)
    figure_1.update_xaxes(title_text=fac_2['x_axis'], row=2, col=1)

    # Define y-axis for each plot
    for i in range(1, 3):
        figure_1.update_yaxes(title_text="Number of Records", range=[0, 2000],
                              patch=dict(tickmode='array',
                                         tickvals=[0, 500, 1000, 1500, 2000],
                                         ticktext=[0, 500, 1000, 1500, ">2000"]),
                              row=i, col=1)

    return figure_1
