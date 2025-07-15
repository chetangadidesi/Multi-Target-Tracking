from clustering import kmeans_clustering
from tracking import assign_cluster_ids
from simulation import update_positions, calc_raw_data
from occupancy_map import generate_gaussian_grid_map
from visualization import draw_heatmap
import matplotlib.pyplot as plt

def main():
    cx = [0.0, 8.0]
    cy = [0.0, 8.0]
    n_points = 10
    rand_d = 3.0
    n_cluster = 2
    sim_time = 15.0
    dt = 1.0
    time = 0.0

    prev_centroids = []
    prev_ids = []
    next_id = 1

    while time <= sim_time:
        time += dt
        cx, cy = update_positions(cx, cy)
        raw_x, raw_y = calc_raw_data(cx, cy, n_points, rand_d)

        clusters = kmeans_clustering(raw_x, raw_y, n_cluster)
        current_centroids = clusters.get_centroids()

        if not prev_centroids:
            assigned_clusters = [(next_id + i, *c) for i, c in enumerate(current_centroids)]
            prev_ids = [id for id, _, _ in assigned_clusters]
            next_id += len(current_centroids)
        else:
            assigned_clusters = assign_cluster_ids(current_centroids, prev_centroids, prev_ids)
            prev_ids = [id for id, _, _ in assigned_clusters]

        prev_centroids = [(x, y) for _, x, y in assigned_clusters]
        ox = [x for _, x, _ in assigned_clusters]
        oy = [y for _, _, y in assigned_clusters]

        gmap, minx, maxx, miny, maxy = generate_gaussian_grid_map(ox, oy, 0.5, 2.0)

        plt.cla()
        draw_heatmap(gmap, minx, maxx, miny, maxy, 0.5)
        clusters.plot_cluster(plt)
        plt.plot(cx, cy, "or", label="True")
        for id, x, y in assigned_clusters:
            plt.plot(x, y, "xk")
            plt.text(x + 0.1, y + 0.1, f"ID {id}", fontsize=10)
        plt.title(f"Time {time:.1f}")
        plt.xlim(minx, maxx)
        plt.ylim(miny, maxy)
        plt.pause(dt)

if __name__ == '__main__':
    main()
