import csv
import matplotlib.pyplot as plt


def read_csv(path):
    with open(path, "r", newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

def get_world_population(data):
    data = list(filter(lambda item : item['Continent'] == 'South America',data))

    labels = list(map(lambda x: x["Country/Territory"], data))
    values = list(map(lambda x: x['World Population Percentage'], data))
    return labels, values

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    plt.show()







if __name__ == '__main__':
  data = read_csv('data.csv')
  labels, values = get_world_population(data)
  generate_pie_chart(labels, values)

