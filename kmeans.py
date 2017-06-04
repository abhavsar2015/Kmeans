from scipy.spatial import distance
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def cost(centroids, clusters):
    return sum(distance.cdist([centroid], cluster, 'sqeuclidean').sum()
            for centroid, cluster in (centroids, clusters))


def compute_centroids(clusters):
    return [np.mean(cluster,  dtype=np.float64) for cluster in clusters]


def kmeans(k, centroids, points, method):
    clusters = [[] for _ in range(k)]

    for point in points:
        clusters[closest_centroid(point, centroids)].append(point)

    new_centroids = compute_centroids(clusters)

    if not equals(centroids, new_centroids):
        print("cost [k={}, {}] = {}".format(k, method, cost(new_centroids, clusters)))

        clusters = kmeans(k, new_centroids, points, method)

    return clusters


def closest_centroid(point, centroids):
    min_distance = float('inf')
    belongs_to_cluster = None
    dist1=0
    for j, centroid in enumerate(centroids):
        dist = distance.sqeuclidean(point, centroid)
        if dist < min_distance:
            min_distance = dist
            belongs_to_cluster = j

    return belongs_to_cluster


def contains(point1, points):
    for point2 in points:
        if point1[0] == point2[0] and point1[1] == point2[1]:
        # if all(x == y for x, y in izip(points1, points2)):
            return True

    return False


def equals(points1, points2):
    if len(points1) != len(points2):
        return False

    y=0
    t=(points1, points2)[0];
    for point1 in (points1, points2)[0]:
        point2=t[y]
        if point1[0] != point2[0] or point1[1] != point2[1]:
        # if any(x != y for x, y in izip(points1, points2)):
            y = y + 1
            return False
        y=y+1
    return True


if __name__ == "__main__":
    data = [[-19.0748,     -8.536       ],
            [ 22.0108,      -10.9737    ],
            [ 12.6597,      19.2601     ],
            [ 11.26884087,  19.90132146 ],
            [ 15.44640731,  21.13121676 ],
            [-20.03865146,  -8.820872829],
            [-19.65417726,  -8.211477352],
            [-15.97295894,  -9.648002534],
            [-18.74359696,  -5.383551586],
            [-19.453215,   -8.146120006],
            [-16.43074088,  -7.524968005],
            [-19.75512437,  -8.533215751],
            [-19.56237082,  -8.798668569],
            [-19.47135573,  -8.057217004],
            [-18.60946986,  -4.475888949],
            [-21.59368337,  -10.38712463],
            [-15.39158057,  -3.8336522  ],
            [-40.0,          40.0       ]]
    k = 4
    x=[]
    y=[]
    # k-means picking the first k points as centroids
    centroids = data[:k]
    clusters = kmeans(k, centroids, data, "second")
    o=0
    for cluster in clusters:
      for clust in cluster:
          x.append(clust[0])
          y.append(clust[1])
    colors = iter(cm.rainbow(np.linspace(0, 1, len(x))))
    plt.scatter(x, y, color=['red','green'])
    plt.show()
    print(clusters)