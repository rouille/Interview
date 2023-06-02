import numpy as np
from sklearn.datasets import make_blobs
from sklearn.metrics import adjusted_rand_score

from interview.algorithm.kmeans import KMeans


def test_kmeans():
    n = 5
    x_train, labels_true, centers = make_blobs(
        n_samples=1000,
        centers=n,
        return_centers=True,
    )
    km = KMeans(n)
    km.fit(x_train)

    # For each centroid get closest cluster center
    centroid2center = {
        i: np.argmin(
            [km.euclidean_distance(km.centroid[i], centers[j]) for j in range(n)]
        )
        for i in range(n)
    }

    labels_pred = km.predict(x_train)

    # Measure similarity of the two assignments, ignoring permutations:
    similarity = adjusted_rand_score(labels_true, labels_pred)

    # Back to the envelope estimate of score for well separated clusters
    # One centroid per cluster. Possibly 100% correct assignment
    if len(set(centroid2center.values())) == 5:
        assert 0.45 <= similarity <= 1
    # 1 cluster has no centroid. Around 20% wrong assignments.
    elif len(set(centroid2center.values())) == 4:
        assert 0.35 <= similarity <= 0.95
    # 2 clusters have no centroid. Around 40% wrong assignments.
    elif len(set(centroid2center.values())) == 3:
        assert 0.25 <= similarity <= 0.9
    # 3 clusters have no centroid. Around 60% wrong assignments.
    elif len(set(centroid2center.values())) == 2:
        assert 0.15 <= similarity <= 0.85
