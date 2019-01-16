import csv
import pandas as pd
import xml.etree.ElementTree as ET
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as dt
df = pd.read_csv('15-nov.csv')

def xml_to_df(file_name,save_to_csv=False,csv_name=''):
  tree = ET.parse(file_name)
  root = tree.getroot()
  bk = root[0]
  day_col = []
  month_col = []
  hour_col = []
  year_col = []
  coin_col = []
  for item in bk:
    item_dict = item.attrib
    date = dt.datetime(int(item_dict['Year']),1,1) + dt.timedelta(int(item_dict['Day'])-1)
    month_col.append(date.month)
    day_col.append(item_dict['Day'])
    hour_col.append(item_dict['Hour'])
    year_col.append(item_dict['Year'])
    coin_col.append(item.text)
  data_dict = {'hour':hour_col,'day':day_col,'month':month_col,'year':year_col,'coin_num':coin_col}
  df = pd.DataFrame(data_dict)
  if save_to_csv:
    df.to_csv(csv_name)
  return df

def generic_line_plot(data,xlabel,ylabel,xaxis,yaxis,title):
  sb.set(style='darkgrid')
  ax = sb.lineplot(x=xaxis,y=yaxis,data=data)
  ax.set(xlabel=xlabel,ylabel=ylabel,title=title)
  plt.show()

def get_hour_data(df):
  hour_map = {hour : 0 for hour in range(25)}
  for index,row in df.iterrows():
    hour = row['hour']
    num_coins = row['coin_num']
    hour_map[hour]+=num_coins
  return hour_map

def get_month_data(df):
  months = set()
  for index,row in df.iterrows():
    months.add(row['month'])
  months = list(months)
  month_map = {month : 0 for month in months}
  for index,row in df.iterrows():
    month_map[row['month']]+=row['coin_num']
  return month_map

def get_day_data(df):
  days = set()
  for index,row in df.iterrows():
    days.add(row['day'])
  days = list(days)
  day_map = {day : 0 for day in days}
  for index,row in df.iterrows():
    day_map[row['day']]+=row['coin_num']
  return day_map

def lineplot_with_lists(xy_map,xlabel,ylabel,title):
  sb.set(style='darkgrid')
  ax = sb.lineplot(x=list(xy_map.keys()),y=list(xy_map.values()))
  ax.set(xlabel=xlabel,ylabel=ylabel,title=title)
  plt.show()

def hour_coins_plot(df):
  lineplot_with_lists(get_hour_data(df),'Hour','# of Coins','Coins by Hour')

def day_coins_plot(df):
  lineplot_with_lists(get_day_data(df),'Day','# of Coins','Coins by Day')

def month_coins_plot(df):
  lineplot_with_lists(get_month_data(df),'Month','# of Coins','Coins by Month')
  
month_coins_plot(df)