"""
author:hanyunxuan
date:2018.3.29

K Means
Step 1 - Pick K random points as cluster centers called center points.
Step 2 - Assign each non-center point to nearest cluster by calculating its distance(flow,degree) to each center point.
Step 3 - Find new cluster center by taking the average of the assigned points.
Step 4 - Repeat Step 2 and 3 until none of the cluster assignments change.

Input:
Longitude Latitude of nodes,number of center nodes
Output:
coordinates and codes of center points,
coordinates and codes of non-center points

"""
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def k_means(data, number_center):
    # 假如我要构造一个聚类数为3的聚类器
    estimator = KMeans(n_clusters=number_center)  # 构造聚类器
    estimator.fit(data)  # 聚类
    label_pred = estimator.labels_  # 获取聚类标签
    centroids = estimator.cluster_centers_  # 获取聚类中心
    inertia = estimator.inertia_  # 获取聚类准则的总和

    plt.plot(data[:, 0].tolist(), data[:, 1].tolist(), 'b^')  # 画社区点
    plt.plot(centroids[:, 0].tolist(), centroids[:, 1].tolist(), 'ro')  # 画中心点
    plt.show()  #

    print(" 获取聚类标签","\n",label_pred,"\n","获取聚类中心","\n",centroids,"\n","获取聚类准则的总和","\n",inertia)

    return label_pred, centroids, inertia


if __name__ == '__main__':
    data = np.random.rand(12, 2)  # 生成一个随机数据，样本大小为100, 特征数为2
    number_center = 3
    [label_pred, centroids, inertia] = k_means(data, number_center)
