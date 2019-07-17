import csv
import argparse
import numpy as np


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--filename', type=str, help='tn93 filename')
args = parser.parse_args()

fn = args.filename

with open(fn) as csvfile:
    rows = list(csv.DictReader(csvfile))

def histogram(dists):
    hist = np.histogram(dists)
    print("Histogram")
    print(hist)

def scale(dists):
    ''' Scales distances to between 0 and the threshold '''
    dists *= (0.015/dists.max())
    return dists

dists = np.array([float(r['Distance']) for r in rows])
dists = scale(dists)
histogram(dists)


