#!/usr/bin/env python3

import matplotlib.pyplot as plt
import json5
import argparse


class StravaParser:
    def __init__(self, dotsize=10, savefiles=True, file='ride.json'):
        self.dotsize = dotsize
        self.savefiles = savefiles
        with open(file) as f:
            js = json5.load(f)
            rideData = js['data']
            self.locitems = rideData[0]['values']
            self.hritems = rideData[1]['values']

        self.speeds = []
        self.lats = []
        self.longs = []
        self.hrs = []
        self.elevations = []
        self.distances = []
 

    def appendEntry(self, lat=0, long=0, hr=0):
        self.lats.append(lat)
        self.longs.append(long)
        self.hrs.append(hr)


    def findHR(self, timein=0):
        for i in self.hritems:
            if i[0] >= timein:
                return i[1]
        return self.hritems[-1][1]


    def parse(self):
        # JSON structure
        # ['Meta data'] Metadata

        # GPS data
        # ['data'][0]['values']
        # =["time","latlng","elevation","h_accuracy","v_accuracy","speed","course","device_time","distance"]

        # HR logging
        #['data'][1]['values'] = ["time",'HR']

        for i in self.locitems:
            hr = self.findHR(i[0])
            self.appendEntry(i[1][0], i[1][1], hr)

        for s in self.locitems:
            self.speeds.append(s[5]*2.24)
        for l in self.locitems:
            self.elevations.append(l[2]*3.28084)
        for d in self.locitems:
            self.distances.append(d[8]*0.000621371)

        # %matplotlib notebook
        plt.close()
        plt.title("Heart Rate (BPM)")
        plt.xticks([])
        plt.yticks([])
        plt.style.use('seaborn-notebook')
        plt.scatter(self.longs, self.lats, c=self.hrs, cmap='jet', s=self.dotsize)
        plt.colorbar()
        plt.show()
        if self.savefiles:
            plt.savefig('hr.png', dpi=250)

        plt.close()
        plt.title('Heart Rate Histogram')
        plt.xlabel('Heart Rate (bpm)')
        plt.hist(self.hrs, bins=30)
        plt.show()
        if self.savefiles:
            plt.savefig('hrhist.png', dpi=250)

        plt.close()
        plt.xticks([])
        plt.yticks([])
        plt.title("Speed (MPH)")
        plt.scatter(self.longs, self.lats, c=self.speeds, cmap='jet', s=self.dotsize)
        plt.colorbar()
        plt.show()
        if self.savefiles:
            plt.savefig('speed.png', dpi=250)

        plt.close()
        plt.hist(self.speeds, bins=30)
        plt.title('Speed Histogram')
        plt.xlabel('Speed (mph)')
        plt.show()
        if self.savefiles:
            plt.savefig('speedhist.png', dpi=250)

        plt.close()
        plt.plot(self.distances, self.elevations, lw=1, color='b')
        plt.ylabel('Elevation (Feet)')
        plt.xlabel('Miles Traveled')
        plt.title('Elevation over distance')
        plt.show()
        if self.savefiles:
            plt.savefig('ele.png', dpi=250)

        plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse args for stravaparser')

    parser.add_argument('--nosave', '-n', dest='savefiles',
                        action='store_false', default=True)
    parser.add_argument('--file', '-f', default='ride.json')
    parser.add_argument('--dotsize', '-d', type=int, default=10)

    args = parser.parse_args()

    sp = StravaParser(dotsize=args.dotsize,
                      savefiles=args.savefiles, file=args.file)
    sp.parse()

