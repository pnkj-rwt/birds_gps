## 1. LONGITUDE AND LATITUDE OF BIRDS

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv("bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)

# storing the indices of the bird 'Eric'
ix = birddata.bird_name == "Eric"
x,y = birddata.longitude[ix], birddata.latitude[ix]
plt.figure(figsize = (7,7))
plt.plot(x,y,"b.")

# To look at all the birds trajectories,plot each bird in the same plot
plt.figure(figsize = (7,7))

for bird_name in bird_names:
	ix = birddata.bird_name == bird_name
	x,y = birddata.longitude[ix], birddata.latitude[ix]
	plt.plot(x,y,".", label=bird_name)

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.show()

## 2. 2D SPEED AND FREQUENCY OF 'ERIC'

bird_names2 = pd.unique(birddata.bird_name)

# storing the indices of the bird Eric
speed = birddata.speed_2d[ix]

plt.figure(figsize = (8,4))
ind = np.isnan(speed)
plt.hist(speed[~ind], bins = np.linspace(0,30,20), normed=True)
plt.xlabel(" 2D speed (m/s) ")
plt.ylabel(" Frequency ")
plt.show()

## 3. DATE AND TIME TO COVER DISTANCES

import datetime

bird_names3 = pd.unique(birddata.bird_name)

timestamps = []
for k in range(len(birddata)):
	timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))

birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)

times = birddata.timestamp[birddata.bird_name == "Eric"]
elapsed_time = [time-times[0] for time in times]

plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1))
plt.xlabel(" Observation ")
plt.ylabel(" Elapsed time (days) ")
plt.show()

## 4. TRACK BIRDS (Eric, Nico & Sanne) OVER A MAP FOR A CARTOGRAPHIC VIEW

import cartopy.crs as ccrs
import cartopy.feature as cfeature

bird_names4 = pd.unique(birddata.bird_name)

# specifying projections
proj = ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
for name in bird_names:
	ix = birddata['bird_name'] == name
	x,y = birddata.longitude[ix], birddata.latitude[ix]
	ax.plot(x,y,'.', transform=ccrs.Geodetic(), label=name)
plt.legend(loc="upper left")
plt.show()