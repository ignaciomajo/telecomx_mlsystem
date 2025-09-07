## EDA HELPER FUNCTIONS TELECOM X

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Callable, List, Dict, Tuple
from pathlib import Path

# BOXPLOT

def boxplot_churn(df: pd.DataFrame,
                  ycol: str,
                  ylabel: str=None,
                  path='.'):
    
    """    
    Generates and saves a boxplot with the distribution of a numerical feature ('ycol')
    diferentiated by Churn condition.
    --------------------------------------------------------------------------------------------------
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the data for plotting. Must include columns 'Churn' and <'ycol'>
    ycol : str
        Numerical column name to visualize.
    ylabel : str, optional
        Personalized label for Y axis. If not specified, 'ycol' name will be used.
    --------------------------------------------------------------------------------------------------
    Saving
    --------
    Saves chart as PNG image in path './<path>/' under the name 'boxplot_Churn_<ycol>.png' 
    --------------------------------------------------------------------------------------------------
    Retorna
    -------
    fig: matplotlib.figure.Figure
        Figure object from Matplotlib with generated plots.
    """
    churn_colors = ['#4682b4', '#e9611d']

    if ylabel is None:
        ylabel = ycol
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax = sns.boxplot(data=df, x='Churn', y=ycol, hue='Churn', palette=churn_colors)
    plt.title(f'{ycol} distribution by Churn', fontsize=18, pad=20)
    plt.xlabel('Churn', fontsize=15)
    plt.ylabel(ylabel, fontsize=15)
    plt.xticks(fontsize=13)
    plt.grid(True)
    
    fig.savefig(path/f'boxplot_Churn_{ycol}.png',
                transparent=False,
                dpi=300,
                bbox_inches='tight')
    plt.show()
    return fig

# HISTOGRAM

def histograma_churn(df, 
                     xcol, 
                     xlabel: str=None,
                     path: Path='.'):
    """
    Generates and saves a double histogram with numerical variable distribution ('xcol') diferentiated by
    churn condition ('Yes' and 'No')
    --------------------------------------------------------------------------------------------------
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the data to plot. Must inlcude 'Churn' feature and the numeric column <'xcol'>
    xcol : str
        Numerical column name to visualize.
    xlabel : str, optional
        Personalized label for X axis. If not specified, 'xcol' name will be used.
    --------------------------------------------------------------------------------------------------
    Saving
    --------
    Saves chart as PNG image in path './<path>/' under the name 'hist_Churn_<xcol>.png'
    --------------------------------------------------------------------------------------------------
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object from Matplotlib with generated plots.
    """

    churn_colors = ['#4682b4', '#e9611d']

    if xlabel is None:
        xlabel = xcol
        
    fig, axes = plt.subplots(2,1, figsize=(8,6))

    sns.histplot(data=df[df['Churn'] == 'No'], x=xcol, bins=30, color=churn_colors[0], kde=True, ax=axes[0])
    axes[0].set_title("Churn = 'No'", fontsize=15, fontweight='bold', loc='left', color='teal')
    axes[0].set_xlabel(xlabel, fontsize=13)
    axes[0].set_ylabel('Frequency', fontsize=13)
    
    sns.histplot(data=df[df['Churn'] == 'Yes'], x=xcol, bins=30,  color=churn_colors[1], kde=True, ax=axes[1])
    axes[1].set_title("Churn = 'Yes'", fontsize=15, fontweight='bold', loc='left', color='indianred')
    axes[1].set_xlabel(xlabel, fontsize=13)
    axes[1].set_ylabel('Frequency', fontsize=13)

    # Adjust axes limits
    ymax1 = axes[0].get_ylim()[1]
    ymax2 = axes[1].get_ylim()[1]

    ymax = max(ymax1, ymax2)

    axes[0].set_ylim(0, ymax)
    axes[1].set_ylim(0, ymax)

    # Figure configurations 

    sns.despine()
    plt.suptitle(f'{xlabel} distribution by Churn', fontsize=18, y=1.01)
    plt.subplots_adjust(hspace=2)
    plt.tight_layout()
    
    fig.savefig(f'{path}/hist_Churn_{xcol}.png',
                    transparent=False,
                    dpi=300,
                    bbox_inches='tight')
    
    plt.show()
    return fig


def bar_churn(df: pd.DataFrame,
              xcol: str,
              ycol: str='count',
              hue_col: str='Churn',
              figsize: Tuple=(6,4),
              xlabel: str=None,
              ylabel: str='Customer Count',
              path: Path='.'):
    
    """
    Generates and saves a grouped bar chart to compare a categorical feature classes ('xcol')
    diferentiated by Churn, using frequency or another metric as height.
    --------------------------------------------------------------------------------------------------
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the data to plot. Must inlcude 'Churn' feature and the categorical column <'xcol'>
    xcol : str
        Categorical column to represent in X axis.
    ycol : str, opcional
        Numerical column for Y axis. (By default: 'count').
    hue_col : str, optional
        Column used to group by. (By default: 'Churn').
    figsize : Tuple, optional
        Fig size in inches (width, height). (By default: (6, 4))
    xlabel : str, optional
        X axis label. If not specified, 'xcol' name will be used.
    ylabel : str, opcional
        Y axis label. (By default: 'Customer Count').
    --------------------------------------------------------------------------------------------------
    Saving
    --------
    Saves chart as PNG image in path './<path>/' under the name 'bar_Churn_<xcol>.png'
    --------------------------------------------------------------------------------------------------
    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure object from Matplotlib with the generated bar plot.
    """
    
    churn_colors = ['#4682b4', '#e9611d']

    fig, ax = plt.subplots(figsize=figsize)

    if title_translate is None:
        title_translate = xcol
        
    ax = sns.barplot(data=df, x=xcol, y=ycol, hue=hue_col, palette=churn_colors)
    ax.set_title(f'Churn by {xcol}', fontsize=18, pad=20)
    if xlabel is None:
        ax.set_xlabel('')
    else:
        ax.set_xlabel(xcol, fontsize=15)
        
    ax.set_ylabel(ylabel, fontsize=15)
    ax.tick_params(axis='y', labelsize=10)
    ax.tick_params(axis='x', labelsize=12)
    for bar in ax.patches:
        height = bar.get_height()
        if height == 0:
            continue
        else:
            ax.text(bar.get_x() + bar.get_width() / 2, 
                    height + 30,
                    f'{height:.0f}',
                    ha='center')
            
    sns.despine()
    #plt.tight_layout()

    fig.savefig(path/f'bar_Churn_{xcol}.png',
                transparent=False,
                dpi=300,
                bbox_inches='tight')

    plt.show()
    return fig