import matplotlib.pyplot as plt
import csv


def generate_plot(filename):
    with open(filename, 'r') as csv_readings:
        reader = csv.reader(csv_readings)
        data = []
        for row in reader:
            data += row
        plt.plot([x for x in range(len(data))], data)
        plt.show()


if __name__ == "__main__":
    generate_plot(filename='readings.csv')
