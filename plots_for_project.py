import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.makedirs('project_plots',exist_ok=True)
data = pd.read_csv('books.csv',error_bad_lines=False)
data.rename(columns={'# num_pages': 'pages_number'},inplace=True)
# print(data.columns)
# print(data.dtypes)
# print(data.shape)
# print(data.describe())
# print(data.info())
# print(data.isnull().sum())
with pd.option_context('display.max_columns',8):
    print(data.corr())

#Line plot of the column 'bookID' and 'pages_number'
plt.plot(data['bookID'],data['pages_number'])
plt.xlabel('bookID')
plt.ylabel('pages_number')
plt.title('pages number x bookID')
plt.savefig(f'project_plots/line_plt.png')
plt.show()
plt.clf()

#Creating scatter
plt.scatter(data['average_rating'], data['text_reviews_count'],c='m', label='text review count', marker='^')
plt.scatter(data['average_rating'], data['pages_number'],label='page number')
plt.xlabel('average_rating')
plt.legend(loc='upper left')
plt.savefig(f'project_plots/scatter_plt.png')
plt.show()
plt.clf()

plt.scatter(data['text_reviews_count'],data['ratings_count'],marker='X')
plt.xlabel('text_reviews_count')
plt.ylabel('ratings_count')
plt.title('Text Review x Ratings Count')
plt.savefig(f'project_plots/count_scatter_plt.png')
plt.show()
plt.clf()

#Creating histogram
plt.hist(data['average_rating'],bins=30,label='average_rating', color='lime')
plt.xlabel('average_rating')
plt.title('Average Rating')
plt.savefig(f'project_plots/hist_average_rating.png')
plt.show()
plt.clf()


plt.hist(data['ratings_count'], bins=100, color='red', label= 'ratings_count')
plt.title('Ratings Count')
plt.xlabel('Ratings Count')
plt.legend()
plt.savefig(f'project_plots/hist_rating.png')
plt.show()
plt.clf()


data1 = data[['average_rating','isbn13','language_code','pages_number','ratings_count','text_reviews_count']]
f, axes = plt.subplots(len(data1.keys()), len(data1.keys()), figsize=(25, 25))
for i, column1 in enumerate(data1.keys()):
    for j, column2 in enumerate(data1.keys()):
        x = data1[column1]
        y = data1[column2]
        axes[i, j].scatter(x, y, c='pink')
        axes[i, j].set_xlabel(column1)
        axes[i, j].set_ylabel(column2)
        axes[i, j].set_title(f'{column1} x {column2}')
plt.legend(loc='upper left', fontsize='small')
plt.tight_layout()
plt.savefig(f'project_plots/general_plt.png')
plt.show()