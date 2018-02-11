matrixAr = []

with open("generated_data_with_errors.txt") as file:   #read from txt file "generated_data_with errors.txt"
    text = file.read()
    b = text.replace("[[","").replace("]]","") # to remove head [[ and tail ]]
print b
sensor_data_array = b.split('], [')

# print type(b) # string
# type(text) # string
#type(sensor_data_array) # list
# len(sensor_data_array) # 32
faulty_sensors = " "
error_log = "the errors are"
counter = 1
for sensor in sensor_data_array:
    dataset = sensor.replace("[[","").replace("]]","")
    dataset_array = dataset.split(',')


    for data in dataset_array:

         if "err" == data.strip():
            faulty_sensors += str(counter) +","


    counter = counter +1
    if counter == 33:
        counter = 1
import datetime  #add time
curtime = str(datetime.datetime.now())
print (faulty_sensors)
error_log = "the faulty sensors are; " + faulty_sensors + "  ;  " + curtime  + "\n\n"
print error_log
f = open('error-log2.txt', 'a') #append to error log
f.write(error_log)
f.close()
