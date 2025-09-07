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