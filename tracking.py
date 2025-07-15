import numpy as np

def assign_cluster_ids(current_centroids, previous_centroids, previous_ids):
    assigned = []
    used_prev = set()

    for cx, cy in current_centroids:
        min_dist = float("inf")
        matched_id = None
        for i, (px, py) in enumerate(previous_centroids):
            if i in used_prev:
                continue
            dist = np.hypot(cx - px, cy - py)
            if dist < min_dist:
                min_dist = dist
                matched_id = previous_ids[i]
        if matched_id is None:
            matched_id = max(previous_ids, default=0) + 1
        assigned.append((matched_id, cx, cy))
        used_prev.add(previous_ids.index(matched_id))
    return assigned
