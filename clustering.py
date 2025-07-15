import math
import random

class Clusters:
    def __init__(self, x, y, n_label):
        self.x = x
        self.y = y
        self.n_data = len(self.x)
        self.n_label = n_label
        self.labels = [random.randint(0, n_label - 1) for _ in range(self.n_data)]
        self.center_x = [0.0 for _ in range(n_label)]
        self.center_y = [0.0 for _ in range(n_label)]

    def get_centroids(self):
        return list(zip(self.center_x, self.center_y))

    def plot_cluster(self, plt):
        for label in set(self.labels):
            x, y = self._get_labeled_x_y(label)
            plt.plot(x, y, ".", alpha=0.5)

    def calc_centroid(self):
        for label in set(self.labels):
            x, y = self._get_labeled_x_y(label)
            n_data = len(x)
            if n_data > 0:
                self.center_x[label] = sum(x) / n_data
                self.center_y[label] = sum(y) / n_data

    def update_clusters(self):
        cost = 0.0
        for ip in range(self.n_data):
            px = self.x[ip]
            py = self.y[ip]

            dx = [icx - px for icx in self.center_x]
            dy = [icy - py for icy in self.center_y]

            dist_list = [math.hypot(dx_, dy_) for dx_, dy_ in zip(dx, dy)]
            min_dist = min(dist_list)
            min_id = dist_list.index(min_dist)
            self.labels[ip] = min_id
            cost += min_dist
        return cost

    def _get_labeled_x_y(self, target_label):
        x = [self.x[i] for i, label in enumerate(self.labels) if label == target_label]
        y = [self.y[i] for i, label in enumerate(self.labels) if label == target_label]
        return x, y

def kmeans_clustering(rx, ry, nc, max_loop=10, dcost_th=0.1):
    clusters = Clusters(rx, ry, nc)
    clusters.calc_centroid()

    pre_cost = float("inf")
    for _ in range(max_loop):
        cost = clusters.update_clusters()
        clusters.calc_centroid()
        if abs(cost - pre_cost) < dcost_th:
            break
        pre_cost = cost
    return clusters
