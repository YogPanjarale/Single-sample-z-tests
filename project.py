import statistics as stats
from typing import Iterable
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random

# reading file
file = pd.read_csv("./data/medium_data.csv")

# converting to list
rt = file['reading_time'].to_list()

# calculating mean
mean = stats.mean(rt)
print(f'Total - ({len(rt)} Samples) \nMean: {mean}')

# taking n samples from dataset


def takeNSample(list: Iterable, n: int):
    l = []
    for i in range(0, n):
        l.append(list[random.randrange(0, len(list))])
    return l


def setup():
    ml=[]
    for i in range(0, 100):
        # taking 30 samples
        samples = takeNSample(rt, 30)
        # calculating mean from samples
        smean = stats.mean(samples)
        # printing result
        # print(f'Sample No.{i}\nTotal - ({len(samples)} Samples) \nMean: {smean}')
        #add mean to list
        ml.append(smean)
    return ml

#plotting graph
def plotGraph(list:Iterable):
    fig = ff.create_distplot([list],["mean"],show_hist=False)
    fig.show()
l=setup()
plotGraph(l)
