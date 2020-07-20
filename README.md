
# Apple-Watch-Strava-Parse-Viz
This jupyter notebook script uses matplotlib to generate interesting visualizations of Bike/Run/Whatever data recorded by the Strava Apple Watch App. Map visualizations within jupyter notebook are zoomable 

# Graphics generated
<p align="center">
  <img src="images/hr.png" width="450" title="Interactive Heart Rate Map">
  <img src="images/speed.png" width="450" title="Interactive Speed Map">
</p>
<p align="center">
  <img src="images/hrhist.png" width="450" title="Heart rate Histogram">
  <img src="images/speedhist.png" width="450" title="Speed Histogram">
</p>


<p align="center">
  <img src="images/ele.png" width="450" title="elevation change over distance">
</p>


# Packages used

- [Matplotlib](https://matplotlib.org/)

- [Json5](https://json5.org/)

# Compatible Files

Json Files generated by the Apple Watch Strava App. Can be found by going to your own Strava activity and clicking [Export Original](images/howto.PNG)

# How to Run

<b> Option 1: Easiest method </b>

1. Install [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/install/)
2. Open stravaparse.ipynb with jupyter notebook
3. Drop ride file into the same folder as stravaparse.ipynb
4. Rename ride file to ride.json
5. Run cell by cell using Shift + Enter

Parameters: 

dotsize = number  Change size of points on speed and heart rate map

savefiles = True / False Save images of each graph

<b> Option 2: Run through cmd </b>

1. Use pip to install matplotlib and json5

```
pip install matplotlib
```

2. Run stravaparse.py using optional parameters listed below

--file or -f filename.json

--nosave or -n to disable image save

--dotsize or -d number to set dot plot size (default 10)

ex:
```shel
python stravaparse.py -f cyclelog.json -n
```

# Future work

-Investigate & support other strava generated file formats 

-Support Apple Fitness data

-Incorporate more visualizations 

-Add a map tile background (Looking for a solid free api, matplotlib supports backgrounds)

~-Add support for running through a python command line~ 
 Thanks Zach, can now be run as .py python3
