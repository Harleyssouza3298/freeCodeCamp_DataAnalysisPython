import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from datetime import datetime

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

def parse_date(x):
  return datetime.strptime(x, "%Y-%m-%d")

df = pd.read_csv('fcc-forum-pageviews.csv', index_col=['date'], parse_dates=['date'], date_parser=parse_date)

#print(df)

# Clean data

df = df.loc[(df['value'] >= df['value'].quantile(0.025)) &
(df['value']<= df['value'].quantile(0.975))]

#print(df)


def draw_line_plot():
    # Draw line plot
  #date_form = DateFormatter("%m-%d")
  fig ,ax = plt.subplots(figsize=(32, 10), dpi=100)
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')
  #ax.xaxis.set_major_formatter(date_form)
  sns.lineplot(data=df, legend = False)
  #print(teste)

    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['tmp'] = df.index

    #print(df)
    df_bar['tmp'] = pd.to_datetime(df_bar['tmp'])
    df_bar['month'] = pd.to_datetime(df_bar['tmp']).dt.month
    df_bar['year'] = pd.to_datetime(df_bar['tmp']).dt.year

    df_tmp = df_bar
  
    teste = df_tmp.pivot_table(index=['year','month'], values=['value'], aggfunc = 'mean').reset_index()
  
    #print(teste)
    
    # Draw bar plot
    fig ,ax = plt.subplots(figsize=(80, 20), dpi=50)

    #month_year = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    chart = sns.barplot(data = teste, x='year', y='value', hue = 'month')
    chart.set(xlabel='Years', ylabel = 'Average Page Views')
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    #print(df_box)
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize=(20,10))

    #Year
    sns.boxplot(ax=ax1, data = df_box, x=df_box['year'], y=df_box['value'] )
  
    ax1.set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")

    #Month
    sns.boxplot(ax=ax2, data = df_box, x=df_box['month'], y = df_box['value'], order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
  
  
    # Draw box plots (using Seaborn)
    

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
