# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 18:16:31 2019

@author: Mattis
"""

# Assignment 2: Which airline to choose?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read and examoine the first 10 rows
flights = pd.read_csv('formatted_flights.csv')
flights.head(10)

# =============================================================================
# # matplotlib histogram
#  plt.hist(flights['arr_delay'], color = 'blue', edgecolor = 'black', bins = int(180/5))
# 
# # seaborn histogram
# sns.distplot(flights['arr_delay'], hist=True, kde=False, bins = int(180/5), norm_hist = True, color = 'blue', hist_kws={'edgecolor':'black'})
# 
# # add labels
# plt.title('Histogram of Arrival Times')
# plt.xlabel('Delay (min)')
# plt.ylabel('Flights')
# =============================================================================

# =============================================================================
# # sepreate table into different airlines
# # Make a separate list for each airline
# x1 = list(flights[flights['name'] == 'United Air Lines Inc.']['arr_delay'])
# x2 = list(flights[flights['name'] == 'JetBlue Airways']['arr_delay'])
# x3 = list(flights[flights['name'] == 'ExpressJet Airlines Inc.']['arr_delay'])
# x4 = list(flights[flights['name'] == 'Delta Air Lines Inc.']['arr_delay'])
# x5 = list(flights[flights['name'] == 'American Airlines Inc.']['arr_delay'])
# 
# # Assign colors for each airline and the names
# colors = ['#E69F00', '#56B4E9', '#F0E442', '#009E73', '#D55E00']
# names = ['United Air Lines Inc.', 'JetBlue Airways', 'ExpressJet Airlines Inc.',
#          'Delta Air Lines Inc.', 'American Airlines Inc.']
#          
# # Make the histogram using a list of lists
# 
# # =============================================================================
# # # Normalize the flights and assign colors and names // solution1: side-by-side
# # plt.hist([x1, x2, x3, x4, x5], bins = int(180/15), normed=True,
# #          color = colors, label=names)
# # =============================================================================
# 
# # =============================================================================
# # # Stacked histogram with multiple airlines // solution2: stacked bars
# # plt.hist([x1, x2, x3, x4, x5], bins = int(180/15), stacked=True,
# #          normed=True, color = colors, label=names)
# # =============================================================================
# 
# # Plot formatting
# plt.legend()
# plt.xlabel('Delay (min)')
# plt.ylabel('Normalized Flights')
# plt.title('Side-by-Side Histogram with Multiple Airlines')
# =============================================================================

# solution3: density plots (smooth, continuous version of the histogram)
# List of five airlines to plot
airlines = ['United Air Lines Inc.', 'JetBlue Airways', 'ExpressJet Airlines Inc.',
         'Delta Air Lines Inc.', 'American Airlines Inc.']

# Iterate through the five airlines
for airline in airlines:
    # Subset to the airline
    subset = flights[flights['name'] == airline]
    
    # Draw the density plot
    sns.distplot(subset['arr_delay'], hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = airline)
    
# Plot formatting
plt.legend(prop={'size': 16}, title = 'Airline')
plt.title('Density Plot with Multiple Airlines')
plt.xlabel('Delay (min)')
plt.ylabel('Density')

# possible extensions: shade (shade = True), rug plot(rug = True)


