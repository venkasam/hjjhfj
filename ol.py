import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics 

data=pd.read_csv("m.csv")
height=data["Height(Inches)"].to_list()
weight=data["Weight(Pounds)"].to_list()

h_mean=statistics.mean(height)
w_mean=statistics.mean(weight)
h_median=statistics.median(height)
w_median=statistics.median(weight)
h_mo=statistics.mode(height)
w_mo=statistics.mode(weight)

print("mean,median,mode of height",(h_mean,h_median,h_mo))
print("mean,median,mode of weight",(w_mean,w_median,w_mo))

h_sd=statistics.stdev(height)
w_sd=statistics.stdev(weight)
#sd 123 for height
h_first_stdev_start,h_first_stdev_end=h_mean-h_sd,h_mean+h_sd
h_second_stdev_start,h_second_stdev_end=h_mean-(2*h_sd),h_mean+(2*h_sd)
h_th_stdev_start,h_th_stdev_end=h_mean-(3*h_sd),h_mean+(3*h_sd)
#sd 123 for weight
w_first_stdev_start,w_first_stdev_end=w_mean-w_sd,w_mean+w_sd
w_second_stdev_start,w_second_stdev_end=w_mean-(2*w_sd),w_mean+(2*w_sd)
w_th_stdev_start,w_th_stdev_end=w_mean-(3*w_sd),w_mean+(3*w_sd)

#percentage of data with 123 sd for hwight

h1=[result for result in height if result>h_first_stdev_start and result<h_first_stdev_end]
h2=[result for result in height if result>h_second_stdev_start and result<h_second_stdev_end]
h3=[result for result in height if result>h_th_stdev_start and result<h_th_stdev_end]
#percentage of data with 123 sd for width
w1=[result for result in weight if result>w_first_stdev_start and result<w_first_stdev_end]
w2=[result for result in weight if result>w_second_stdev_start and result<w_second_stdev_end]
w3=[result for result in weight if result>w_th_stdev_start and result<w_th_stdev_end]

#printing data for height and weight

print("{}% of data for height lies with 1st sd".format(len(h1)*100.0/len(height)))
print("{}% of data for height lies with 2st sd".format(len(h2)*100.0/len(height)))
print("{}% of data for height lies with 3st sd".format(len(h3)*100.0/len(height)))
print("{}% of data for weight lies with 1st sd".format(len(w1)*100.0/len(weight)))
print("{}% of data for weight lies with 2st sd".format(len(w2)*100.0/len(weight)))
print("{}% of data for weight lies with 3st sd".format(len(w3)*100.0/len(weight)))