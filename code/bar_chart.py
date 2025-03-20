import matplotlib.pyplot as plt
from collections import Counter
import os
import datetime
def bar_chart():

    """

    Import txt
    Get all the lines of data
    Create bar chart
    save image

    """

    txt_path = os.path.join("Data", "litters.txt")
    f = open(txt_path, "r")
    #Remove \n
    lines = [line.strip() for line in f.readlines()]

    counts = Counter(lines)

    litters = list(counts.keys())
    counter = list(counts.values())

    plt.bar(litters, counter)

    x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    plt.title(x)
    plt.xlabel("Types")
    plt.ylabel("Count")

    image_path = os.path.join("Data", f'bar_chart-{x.replace(" ", "_").replace(":", "-")}.png') 
    plt.savefig(image_path)

    plt.show()

bar_chart()