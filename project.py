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
    ml = []
    for i in range(0, 100):
        # taking 30 samples
        samples = takeNSample(rt, 30)
        # calculating mean from samples
        smean = stats.mean(samples)
        # printing result
        # print(f'Sample No.{i}\nTotal - ({len(samples)} Samples) \nMean: {smean}')
        # add mean to list
        ml.append(smean)
    return ml


l = setup()
std_deviation = stats.stdev(l)
# findig the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean - \
    std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean - \
    (2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - \
    (3*std_deviation), mean+(3*std_deviation)
print("std1", first_std_deviation_start, first_std_deviation_end)
print("std2", second_std_deviation_start, second_std_deviation_end)
print("std3", third_std_deviation_start, third_std_deviation_end)
# plotting graph


def plotGraph(list: Iterable):
    fig = ff.create_distplot([list], ["mean"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17],
                             mode="lines", name="Mean"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[
                  0, 0.17], mode="lines", name="first_std_deviation_start"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[
                  0, 0.17], mode="lines", name="first_std_deviation_end"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[
                  0, 0.17], mode="lines", name="second_std_deviation_start"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[
                  0, 0.17], mode="lines", name="second_std_deviation_end"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[
                  0, 0.17], mode="lines", name="third_std_deviation_start"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[
                  0, 0.17], mode="lines", name="third_std_deviation_end"))
    fig.show()


plotGraph(l)
