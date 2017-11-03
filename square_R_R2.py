import  numpy as np

def performance_metric2(y_true, y_predict):

    avey = np.mean(y_true)
    da2 = []
    for yt in y_true:
        tmp = np.square(yt - avey)
        da2.append(tmp)
    sstot = np.sum(da2)

    da3 = []

    for index in range(len(y_true)):
        yt = y_true [index]
        yp = y_predict[index]
        tmp = np.square(yt - yp)
        da3.append(tmp)

    ssres = np.sum(da3)

    score = 1 - ssres/sstot

    return score

score = performance_metric2([3, -0.5, 2, 7, 4.2], [2.5, 0.0, 2.1, 7.8, 5.3])

print score
