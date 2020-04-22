import  numpy as np
import matplotlib.pyplot as plt
import csv
from pdf_reader import  *

#getting country population from CSV file
population_data=[];
with open('C:\\Users\\Asus\\Desktop\\COVID_19\\wolrd_population_data.csv') as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader:
        population_data.append(line)

def get_population(country_name):
    for data in population_data:
        if data[0]==country_name:
            return float(data[1])

    print("Data Not Found For "+country_name)
    return 0

#finishing code for gatting population data










country_name=convert_file_to_list('C:\\Users\\Asus\\Desktop\\COVID_19\\python_files\\country_names.txt')

csv_file_location='C:\\Users\\Asus\\Desktop\\COVID_19\\data.csv'

fig, ax = plt.subplots()

maximum_day=1
for names in country_name:
    with open(csv_file_location) as file:
        reader=csv.DictReader(file)
        print(names)
        values = []
        for row in reader:
            values.append(row[names])


        numpy_values=np.array(values)
        numpy_values=numpy_values.astype(np.int)
        for i in range(0,numpy_values.size):
            if numpy_values[i]!=0:
                break
        for x in range(i,numpy_values.size):
            if numpy_values[x]==0:
                numpy_values[x]=numpy_values[x-1]
        maximum_day=max(maximum_day,numpy_values.size-i+1)
        line,=ax.plot(np.arange(1,numpy_values.size-i+1),numpy_values[i:numpy_values.size]/(get_population(names)/100),'-o',label=names)



ax.grid(which='major', color='#CCCCCC', linestyle='--')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')
ax.set_xlabel('Day counted after first COVID-19 case is reported',fontsize=14)
ax.set_ylabel('Percentage of population infected in a country',fontsize=14)
ax.set_xlim(1,maximum_day)
legend = ax.legend(loc='upper left', shadow=True, fontsize='x-large')
plt.show()
