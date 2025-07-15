import math
from scipy.stats import norm

EXTEND_AREA = 10.0  # grid map extension length [m]

def calc_grid_map_config(ox, oy, xyreso):
    minx = round(min(ox) - EXTEND_AREA / 2.0)
    miny = round(min(oy) - EXTEND_AREA / 2.0)
    maxx = round(max(ox) + EXTEND_AREA / 2.0)
    maxy = round(max(oy) + EXTEND_AREA / 2.0)
    xw = int(round((maxx - minx) / xyreso))
    yw = int(round((maxy - miny) / xyreso))
    return minx, miny, maxx, maxy, xw, yw

def generate_gaussian_grid_map(ox, oy, xyreso, std):
    minx, miny, maxx, maxy, xw, yw = calc_grid_map_config(ox, oy, xyreso)
    gmap = [[0.0 for _ in range(yw)] for _ in range(xw)]

    for ix in range(xw):
        for iy in range(yw):
            x = ix * xyreso + minx
            y = iy * xyreso + miny
            mindis = min(math.hypot(iox - x, ioy - y) for iox, ioy in zip(ox, oy))
            gmap[ix][iy] = 1.0 - norm.cdf(mindis, 0.0, std)
    return gmap, minx, maxx, miny, maxy
