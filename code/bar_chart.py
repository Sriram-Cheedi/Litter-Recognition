import matplotlib.pyplot as plt
from collections import Counter
import os
def bar_chart():

    """

    Import txt
    Get all the lines of data
    Create bar chart
    save image

    """


    litters = ['6 Clear plastic bottle']
    counter = [1]

    plt.bar(litters, counter)

    plt.title("Litters")
    plt.xlabel("Types")
    plt.ylabel("Count")

    image_path = os.path.join("Data", "bar_chart.png") 
    plt.savefig(image_path)

    plt.show()

bar_chart()