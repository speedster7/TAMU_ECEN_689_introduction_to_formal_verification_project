# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 01:33:46 2021

@author: Gokul
"""

import car


class mock:
    car_list = []
    AN1 = [0]*2
    N1A = [0]*2

    N1N2 = [0]*30
    N2N1 = [0]*30

    N2D = [0]*30
    DN2 = [0]*30

    DN5 = [0]*30
    N5D = [0]*30

    N5C = [0]*30
    CN5 = [0]*30

    CN6 = [0]*30
    N6C = [0]*30

    N5N4 = [0]*30
    N4N5 = [0]*30

    N4N2 = [0]*30
    N2N4 = [0]*30

    N4N6 = [0]*30
    N6N4 = [0]*30

    N4N3 = [0]*30
    N3N4 = [0]*30

    N6B = [0]*30
    BN6 = [0]*30

    BN3 = [0]*30
    N3B = [0]*30

    N3N1 = [0]*30
    N1N3 = [0]*30

    #traffic signals
    TN2N1 = 0
    TN3N1 = 0

    TN1N2 = 0
    TDN2 = 0
    TN4N2 = 0

    TN1N3 = 0
    TN4N3 = 0
    TBN3 = 0

    TN5N4 = 0
    TN2N4 = 0
    TN6N4 = 0
    TN3N4 = 0

    TDN5 = 0
    TCN5 = 0
    TN4N5 = 0

    TCN6 = 0
    TBN6 = 0
    TN4N6 = 0

    TN6B = 0
    TN3B = 0

    TN5C = 0
    TN6C = 0

    TN2D = 0
    TN5D = 0

    def reset(self):
        self.car_list = []
        self.AN1 = [0]*2
        self.N1A = [0]*2

        self.N1N2 = [0]*30
        self.N2N1 = [0]*30

        self.N2D = [0]*30
        self.DN2 = [0]*30

        self.DN5 = [0]*30
        self.N5D = [0]*30

        self.N5C = [0]*30
        self.CN5 = [0]*30

        self.CN6 = [0]*30
        self.N6C = [0]*30

        self.N5N4 = [0]*30
        self.N4N5 = [0]*30

        self.N4N2 = [0]*30
        self.N2N4 = [0]*30

        self.N4N6 = [0]*30
        self.N6N4 = [0]*30

        self.N4N3 = [0]*30
        self.N3N4 = [0]*30

        self.N6B = [0]*30
        self.BN6 = [0]*30

        self.BN3 = [0]*30
        self.N3B = [0]*30

        self.N3N1 = [0]*30
        self.N1N3 = [0]*30

        #traffic signals
        self.TN2N1 = 0
        self.TN3N1 = 0

        self.TN1N2 = 0
        self.TDN2 = 0
        self.TN4N2 = 0

        self.TN1N3 = 0
        self.TN4N3 = 0
        self.TBN3 = 0

        self.TN5N4 = 0
        self.TN2N4 = 0
        self.TN6N4 = 0
        self.TN3N4 = 0

        self.TDN5 = 0
        self.TCN5 = 0
        self.TN4N5 = 0

        self.TCN6 = 0
        self.TBN6 = 0
        self.TN4N6 = 0

        self.TN6B = 0
        self.TN3B = 0

        self.TN5C = 0
        self.TN6C = 0

        self.TN2D = 0
        self.TN5D = 0

    #possible nodes
    possible_routes = {}
    possible_routes["AN1"] = ["N1N2", "N1N3"]
    possible_routes["N1N2"] = ["N2D", "N2N4"]
    possible_routes["N2N1"] = ["N1N3"]
    possible_routes["N2D"] = ["DN5"]
    possible_routes["DN2"] = ["N2N1", "N2N4"]
    possible_routes["DN5"] = ["N5N4", "N5C"]
    possible_routes["N5D"] = ["DN2"]
    possible_routes["N5C"] = ["CN6"]
    possible_routes["CN5"] = ["N5N4", "N5D"]  # check
    possible_routes["CN6"] = ["N6N4", "N6B"]
    possible_routes["N6C"] = ["CN5"]
    possible_routes["N5N4"] = ["N4N2", "N4N6", "N4N3"]
    possible_routes["N4N5"] = ["N5D", "N5C"]
    possible_routes["N4N2"] = ["N2N1", "N2D"]
    possible_routes["N2N4"] = ["N4N5", "N4N6", "N4N3"]
    possible_routes["N4N6"] = ["N6C", "N6B"]
    possible_routes["N6N4"] = ["N4N5", "N4N2", "N4N3"]
    possible_routes["N4N3"] = ["N3N1", "N3B"]
    possible_routes["N3N4"] = ["N4N2", "N4N5", "N4N6"]
    possible_routes["N6B"] = ["BN3"]
    possible_routes["BN6"] = ["N6N4", "N6C"]
    possible_routes["BN3"] = ["N3N1", "N3N4"]
    possible_routes["N3B"] = ["BN6"]
    possible_routes["N3N1"] = ["N1N2"]
    possible_routes["N1N3"] = ["N3N4", "N3B"]

    def getRoadWithName(self, name):
        if(name == "AN1"):
            return self.AN1
        elif(name == "N1A"):
            return self.N1A
        elif(name == "N1N2"):
            return self.N1N2
        elif(name == "N2N1"):
            return self.N2N1
        elif(name == "N2D"):
            return self.N2D
        elif(name == "DN2"):
            return self.DN2
        elif(name == "DN5"):
            return self.DN5
        elif(name == "N5D"):
            return self.N5D
        elif(name == "N5C"):
            return self.N5C
        elif(name == "CN5"):
            return self.CN5
        elif(name == "CN6"):
            return self.CN6
        elif(name == "N6C"):
            return self.N6C
        elif(name == "N5N4"):
            return self.N5N4
        elif(name == "N4N5"):
            return self.N4N5
        elif(name == "N4N2"):
            return self.N4N2
        elif(name == "N2N4"):
            return self.N2N4
        elif(name == "N4N6"):
            return self.N4N6
        elif(name == "N6N4"):
            return self.N6N4
        elif(name == "N4N3"):
            return self.N4N3
        elif(name == "N3N4"):
            return self.N3N4
        elif(name == "N6B"):
            return self.N6B
        elif(name == "BN6"):
            return self.BN6
        elif(name == "BN3"):
            return self.BN3
        elif(name == "N3B"):
            return self.N3B
        elif(name == "N3N1"):
            return self.N3N1
        elif(name == "N1N3"):
            return self.N1N3


total_cars_count = 0
#test 1:  Create a car
print("-------------- Test Case 1 Starts ------------------")
if(mock.AN1[0] == 0):  # check if first slot dont have car
    total_cars_count += 1
    c = car.car(total_cars_count, mock)
    print("init:", c.carno, c.segment_name, c.segment_slot)
    mock.car_list = mock.car_list + [c]
    print("car_number", c.carno, "location",
          c.segment_name, "", c.segment_slot)
    if(mock.AN1[0] == 1):
        print("Test 1 Passed:", "Car Created")
    del mock.car_list[0]
mock.reset(mock)
print("-------------- Test Case 1 Ends ------------------")

#test 2:  Create 5 cars and Move each car 20 steps
print("-------------- Test Case 2 Starts ------------------")
t = 0
total_cars_count = 0
for i in range(0, 40):
    for k in range(len(mock.car_list)):
        mock.car_list[k].move(mock)
    if(mock.AN1[0] == 0 and len(mock.car_list) < 5):  # check if first slot dont have car
        total_cars_count += 1
        c = car.car(total_cars_count, mock)
        print("time_stamp:", t, "init car:", c.carno,
              c.segment_name, c.segment_slot)
        mock.car_list = mock.car_list + [c]
    for j in mock.car_list:
        print("time_stamp:", t, "====>carNo:", j.carno,
              "====>Location:", j.segment_name, "", j.segment_slot)
    t = t+2
print("-------------- Test Case 2 Ends ------------------")


#test case 3 : Check if the car stops for signal
print("-------------- Test Case 3 Starts ------------------")
print("current_location_of_car1:",
      mock.car_list[0].segment_name, mock.car_list[0].segment_slot)
print("current_signal:", mock.TN1N2)
#try moving during red, car wont move
mock.car_list[0].move(mock)
print("current_location_of_car1 with red signal and move:",
      mock.car_list[0].segment_name, mock.car_list[0].segment_slot)
mock.TN1N2 = 1  # set the signal to green
mock.car_list[0].move(mock)
print("Move after signal is green")
print("current_location_of_car1 with green signal and move:",
      mock.car_list[0].segment_name, mock.car_list[0].segment_slot)
print("-------------- Test Case 3 Ends ------------------")

#reset infra
mock.reset(mock)

#test 4:assume all signal to be green and initialise few cars and check if cars return to A
print("-------------- Test Case 4 Starts ------------------")
t = 0
total_cars_count = 0
#all signal set to one
mock.TN2N1 = 1
mock.TN3N1 = 1
mock.TN1N2 = 1
mock.TDN2 = 1
mock.TN4N2 = 1
mock.TN1N3 = 1
mock.TN4N3 = 1
mock.TBN3 = 1
mock.TN5N4 = 1
mock.TN2N4 = 1
mock.TN6N4 = 1
mock.TN3N4 = 1
mock.TDN5 = 1
mock.TCN5 = 1
mock.TN4N5 = 1
mock.TCN6 = 1
mock.TBN6 = 1
mock.TN4N6 = 1
mock.TN6B = 1
mock.TN3B = 1
mock.TN5C = 1
mock.TN6C = 1
mock.TN2D = 1
mock.TN5D = 1

t = 0
total_cars_count = 0
del_car_list = []
while(1):
    success_cars = []
    for k in range(len(mock.car_list)):
        mock.car_list[k].move(mock)
        #print("time_stamp:", t, "====>carNo:", mock.car_list[k].carno, "====>Location:", mock.car_list[k].segment_name ,"", mock.car_list[k].segment_slot)
        if(mock.car_list[k].check_visited_all()):
            print("time_stamp:", t, "carNo:", mock.car_list[k].carno, " reached back through ==>", ', '.join(
                mock.car_list[k].route))
            success_cars = success_cars + [mock.car_list[k]]
    for j in success_cars:
        del_car_list = del_car_list + [j.carno]
        #update in main road - remove from road
        mock.getRoadWithName(mock, j.segment_name)[j.segment_slot] = mock.getRoadWithName(
            mock, j.segment_name)[j.segment_slot] - 1
        mock.car_list.remove(j)
    if(mock.AN1[0] == 0 and total_cars_count < 5):  # check if first slot dont have car
        total_cars_count += 1
        c = car.car(total_cars_count, mock)
        print("time_stamp:", t, "init car:", c.carno,
              c.segment_name, c.segment_slot)
        mock.car_list = mock.car_list + [c]
    if(len(mock.car_list) == 0):
        break
    t = t+2


print("-------------- Test Case 4 Starts ------------------")
