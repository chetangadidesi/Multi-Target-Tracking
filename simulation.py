import random

def update_positions(cx, cy):
    DX1, DY1 = 0.4, 0.5
    DX2, DY2 = -0.3, -0.5
    cx[0] += DX1
    cy[0] += DY1
    cx[1] += DX2
    cy[1] += DY2
    return cx, cy

def calc_raw_data(cx, cy, n_points, rand_d):
    rx, ry = [], []
    for (icx, icy) in zip(cx, cy):
        for _ in range(n_points):
            rx.append(icx + rand_d * (random.random() - 0.5))
            ry.append(icy + rand_d * (random.random() - 0.5))
    return rx, ry
