#Taken from https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
# Just added plotting for 3-k cases

import numpy as np
import random
import matplotlib.pyplot as plt

def init_board(N):
    X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
    return X

def cluster_points(X, mu):
    clusters = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    # count = 0
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
        show_change = (mu, clusters)
        # if count == 0:
        #     show_change1 = (oldmu, clusters)
        #     parse_output(show_change1)
        #     count += 1
        # parse_output(show_change)

    return(mu, clusters)

def change_coords(array):
    return list(map(list, zip(*array)))

def parse_output(data):
    clusters = data[1]
    points1 = change_coords(clusters[0])
    plt.plot(points1[0], points1[1], 'ro')
    points2 = change_coords(clusters[1])
    plt.plot(points2[0], points2[1], 'g^')
    points3 = change_coords(clusters[2])
    plt.plot(points3[0], points3[1], 'ys')
    # points4 = change_coords(clusters[3])
    # plt.plot(points4[0], points4[1], 'bs')
    # points5 = change_coords(clusters[4])
    # plt.plot(points5[0], points5[1], 'k^')
    # points6 = change_coords(clusters[5])
    # plt.plot(points6[0], points6[1], 'ko')
    centroids = change_coords(data[0])
    plt.plot(centroids[0], centroids[1], 'kx')
    plt.axis([-1.0, 1, -1.0, 1])
    plt.show()

data = init_board(15)

# data = np.array([[-0.5,-0.5], [-0.6,-0.6],[-0.4,-0.4], [-0.3,-0.3],[-0.5,-0.5],
#                  [0.5,0.5],[0.6,0.6],[0.55,0.55],[0.65,0.65],[0.5,0.45],
#                  [0.124,0.124], [0.135,0.135],[0.120,0.120], [0.130,0.130],[0.140,0.140]])
#
# data = np.array([[-0.1, 0.75], [0.1,0.75],[-0.1,0.6], [0.1,0.6],[0.0, 0.7],
#                  [-0.1, -0.15], [0.1, -0.15], [-0.1, 0.15], [0.1, 0.15], [0.0, -0.0],
#                  [-0.1, -0.75], [0.1, -0.75], [-0.1, -0.6], [0.1, -0.6], [0.0, -0.7]])
#
# data = np.array([[-0.1, 0.75], [0.1,0.75],[-0.1,0.6], [0.1,0.6],[0.0, 0.7],
#                  [-0.1, -0.15], [0.1, -0.15], [-0.1, 0.15], [0.1, 0.15], [0.0, -0.0],
#                  [-0.1, -0.75], [0.1, -0.75], [-0.1, -0.6], [0.1, -0.6], [0.0, -0.7]])

# #Four
# data = np.array([[-0.75,0.75], [-0.7,0.6], [-0.60,0.75],
#                  [0.75, -0.75], [0.7, -0.6], [0.60, -0.75],
#                  [-0.75, -0.75], [-0.7, -0.6], [-0.60, -0.75],
#                  [0.75, 0.75], [0.7, 0.6], [0.60, 0.75]])
#
# #Six
# data = np.array([[-0.75,0.75], [-0.7,0.6],
#                  [-0.10,0.5], [0.10,0.5],
#                  [0.75, -0.75], [0.7, -0.6],
#                  [-0.10, -0.25],[0.10, -0.25],
#                  [-0.75, -0.75], [-0.7, -0.6],
#                  [0.75, 0.75], [0.7, 0.6]])
data = np.array([[-0.25, 0.96], [-0.4,0.6], [-0.52,0.28], [-0.54,-0.25], [-0.75, 0.1],
                 [-0.79, -0.4], [-0.85, 0.3], [-0.95, 0.35], [0, 0.27], [0.2, 0.1],
                 [0.19, -0.48], [0.27, 0.9], [0.65, 0.15], [0.68, 0.7], [0.82, -0.8]])

print(data)
print(type(data))
out = find_centers(list(data), 3)
parse_output(out)