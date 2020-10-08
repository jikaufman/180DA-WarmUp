# Resources used:
# https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
# Changed the code from the above link to work with live video feed.

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

def main():

    cap = cv2.VideoCapture(0)
    plt.show()
    clt = KMeans(n_clusters=3) #cluster number

    while(True):
        # Capture frame-by-frame
        _, frame = cap.read()

        img = frame.copy()

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        left_edge = 500
        right_edge = 600

        cv2.rectangle(frame,(left_edge,left_edge),(right_edge,right_edge),(255,0,0),3)

        img = frame[left_edge:right_edge,left_edge:right_edge]

        img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number
        clt.fit(img)

        hist = find_histogram(clt)
        bar = plot_colors2(hist, clt.cluster_centers_)

        plt.clf()
        plt.axis("off")
        plt.imshow(bar)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        plt.pause(1)


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
