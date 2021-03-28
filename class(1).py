import pandas as pd
import statistics as stats
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
# data file
df = pd.read_csv("./data/10000.csv")
data = df["Math_score"].to_list()
Mean = stats.mean(data)
stdev = stats.stdev(data)

#printing values
print(
    f"All - ({len(data)} Entries) \nMean :{Mean} \nStandard Deviation :{stdev}")

# creating the figure
fig = ff.create_distplot([data], ["Math Score"], show_hist=False)
fig.add_trace(go.Scatter(data,mode="lines",name="Math Score"))
# calculating for random sample of 1000
dl = []
for i in range(0, 1000):
    t = random.randint(0, len(data)-1)
    dl.append(data[t])
Mean = stats.mean(dl)
stdev = stats.stdev(dl)

#printing values
print(
    f"Sample - ({len(dl)} Entries) \nMean :{Mean} \nStandard Deviation :{stdev}")
fig.add_trace(go.Scatter(x=[Mean, Mean],
                         mode="lines", name="1000 sample mean"))
# calculating for result sample of 100 each
for i in range(1, 4):
    df = pd.read_csv(f"./data/data{i}.csv")
    data :list= df["Math_score"].to_list()
    print(data)
    Mean = stats.mean(data)
    stdev = stats.stdev(data)
    fig.add_trace(go.Scatter(data,mode="lines",name=f"Sample {i}"))
    #printing values
    print(
        f"Sample {i} - ({len(data)} Entries) \nMean :{Mean} \nStandard Deviation :{stdev}")

    fig.add_trace(go.Scatter(x=[Mean, Mean],y=[0,1],
                             mode="lines", name=f"Result Sample {i}"))
fig.show()
