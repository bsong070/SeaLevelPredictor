import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',float_precision='legacy')
    # Create scatter plot
    fig,ax = plt.subplots(figsize=(11,9))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope1, intercept1, rvalue1, pvalue1, stderr1 = linregress(x,y)
    m1 = slope1
    b1 = intercept1
    x_fit1 = pd.Series([i for i in range(1880,2050)])
    y_fit1 = m1*x_fit1+b1
    line_fit1=plt.plot(x_fit1,y_fit1,'red')

    # Create second line of best fit
    df_modified = df[df['Year']>=2000]
    x=df_modified['Year']
    y=df_modified['CSIRO Adjusted Sea Level']
    slope2, intercept2, rvalue2, pvalue2, stderr2 = linregress(x,y)
    m2=slope2
    b2=intercept2
    x_fit2 = pd.Series([i for i in range(2000,2050)])
    y_fit2 = m2*x_fit2+b2
    line_fit_2=plt.plot(x_fit2,y_fit2,'black')

    # Add labels and title
    plt.title('Rise in Sea Level',fontsize=15)
    plt.xlabel('Year',fontsize=12)
    plt.ylabel('Sea Level (inches)',fontsize=12)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()