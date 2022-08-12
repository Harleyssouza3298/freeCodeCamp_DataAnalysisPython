import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
#print(df)
# Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height']/100)**2)).round(2)
df['overweight'] = np.where((df['overweight'] > 25), 1, 0)
#print(df)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] = np.where((df['cholesterol'] == 1), 0, 1)
df['gluc'] = np.where((df['gluc'] == 1), 0, 1)
    
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    ##df_cat_convert_data = df.melt(id_vars = 'cardio', value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    ##df_cat_convert_data = df_cat_convert_data.groupby(['cardio','variable']).value_counts().reset_index()
    ##df_cat_convert_data.rename(columns={0:'total'}, inplace=True)
    ##df_cat = df_cat_convert_data
    #df_cat.plot.bar(rot=0)
    #print(df_cat)
  df_cat = pd.melt(df, id_vars = 'cardio', var_name = 'variable', value_vars = ['alco', 'active','cholesterol', 'gluc', 'overweight','smoke'])

  df_cat = pd.melt(df, var_name = 'variable', value_vars = ['active','alco','cholesterol', 'gluc','overweight','smoke'], id_vars = 'cardio')

  fig = sns.catplot(data=df_cat, kind="count",  x="variable",hue="value", col="cardio").set_axis_labels("variable", "total")
  fig = fig.fig
  
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly. 
    
  #print(df_cat)
    #print(df_cat.loc[df_cat['variable']=='active'])

    # Draw the catplot with 'sns.catplot()'
    ##fig = sns.catplot(x='variable', y='total',data=df_cat, ci=None, hue='value',kind='bar', col = 'cardio')

    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo']<=df['ap_hi'])& 
  (df['height']>=df['height'].quantile(0.025))&   
  (df['height']<=df['height'].quantile(0.975))& 
  (df['weight']>=df['weight'].quantile(0.025))&
  (df['weight']<=df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()
    #print(corr['weight'])
    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(7,5))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,mask=mask, fmt='.1f',vmax=.3, linewidths=.5,square=True, cbar_kws = {'shrink':0.5},annot=True, center=0)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
