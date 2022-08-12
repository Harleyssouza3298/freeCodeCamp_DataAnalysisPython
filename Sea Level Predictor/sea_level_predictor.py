import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  #print(df)
    # Create scatter plot
  df.plot.scatter(x = 'Year', y = 'CSIRO Adjusted Sea Level', s = 2)

    # Create first line of best fit
  line_a = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  xA = pd.Series(i for i in range(1880, 2051))
  yA = xA * line_a.slope + line_a.intercept
  #print(yA)

  plt.plot(xA, yA)

    # Create second line of best fit
  df_tmp = df[df['Year'] >= 2000]
  #print (df_tmp)

  line_b = linregress(df_tmp['Year'], df_tmp['CSIRO Adjusted Sea Level'])
  #print(line_b)
  xB = pd.Series(i for i in range(2000, 2051))
  yB = xB * line_b.slope + line_b.intercept

  #print(yB)
  #print(yA)

  #print(xA)
  #print(xB)

  plt.plot(xB,yB)
    # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()