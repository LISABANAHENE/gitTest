import random as rand

# generate dataset
generate_data = ""
def generate_data ():

    cluster_of_sensor_data = []
    number_of_sensors = 32
    each_sensor_data = 16

    for d in range(number_of_sensors): # do the below block 32 times

        cluster_of_sensor_data.append([])
        for f in range(each_sensor_data): # do the below block 16 times
            readings = rand.random()
            cluster_of_sensor_data[d].append(readings)


    return cluster_of_sensor_data

print generate_data()

#import datetime
#curtime = str(datetime.datetime.now())
t = str(generate_data())+ "\n\n"
f = open('generated_data.txt', 'a')   #write to a file "generated_data.txt"
f.write(t)

f.close()



