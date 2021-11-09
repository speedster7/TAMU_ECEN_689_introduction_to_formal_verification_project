# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 00:43:49 2021

@author: Gokul, Balaji
"""


class car:

    route = []  # to track route
    visited = []  # to add visited nodes
    id = None
    all_visited = None

    #constructor
    def __init__(self, carno, road):
       self.carno = carno
       self.segment_name = "AN1"
       self.segment_slot = 0
       road.AN1[0] = 1

    #defining move function

    def move(self, road):

        #Add the road name to route
        if(self.segment_name and self.segment_slot == 0):
            self.route = self.route + [self.segment_name]
        if(self.segment_slot == 29 and (self.segment_name == "N2N1" or self.segment_name == "N3N1") and ('B' in self.visited and 'C' in self.visited and 'D' in self.visited)):
            if(road.N1A[0] == 0):
                road.N1A[0] = road.N1A[0] + 1
                road.getRoadWithName(road, self.segment_name)[self.segment_slot] = road.getRoadWithName(
                    road, self.segment_name)[self.segment_slot] - 1
                self.segment_name = "N1A"
                self.segment_slot = 0
        elif(self.segment_name == "N1A" and self.segment_slot == 1):
            self.visited = self.visited + ["A"]
        #end of each road move to first slot of next road
        elif((self.segment_slot == 29) or ((self.segment_name == "AN1") and self.segment_slot == 1)):
            # get the congestion info:
            congestion_info = self.get_junction_info(road)
            # congestion info is of the format [[available routes], current_signal, current road]
            if(congestion_info[1] == 1):  # check if traffic signal is green
                cong_tmp = congestion_info[0]  # gets the available routes
                seg_tmp = []
                for seg in cong_tmp:
                    #check if the first slots of next road is free
                    if(seg[0] == 0):
                        #if the first slot is free, calculate the congestion to compare with other routes
                        seg_tmp = seg_tmp + [sum(seg)]
                    else:
                        #if the road is not free to take, not required to calculate congestion, give a highvalue
                        seg_tmp = seg_tmp + [1000]
                #print(self.segment_name,self.segment_slot);
                #print("cong_tmp",cong_tmp);
                #print("seg_tmp",seg_tmp);
               # if((seg_tmp.count(seg_tmp[0])== len(seg_tmp))):
                """" if the congestion of available routes are equal,
                   then check if there a path to unvisited node.
                   If there is a path to unvisited node, prioritise that"""
                if((seg_tmp.count(seg_tmp[0]) == len(seg_tmp)) and seg_tmp[0] != 1000):
                    path_to_take = []
                    available_path = road.possible_routes[self.segment_name]
                    if("B" not in self.visited):
                        for value in available_path:
                            if("B" in value):
                                path_to_take = path_to_take + [value]
                        #print("path to take_4", path_to_take)
                    if("C" not in self.visited):
                        for value in available_path:
                            if("C" in value):
                                path_to_take = path_to_take + [value]
                        #print("path to take_5", path_to_take)
                    if("D" not in self.visited):
                        for value in available_path:
                            if("D" in value):
                                path_to_take = path_to_take + [value]
                        #print("path to take_6", path_to_take)
                    if(len(path_to_take)):
                        #print("entry2");
                        road.getRoadWithName(road, path_to_take[0])[
                            0] = road.getRoadWithName(road, path_to_take[0])[0] + 1
                        if(self.segment_name == "AN1"):
                            congestion_info[-1][1] = congestion_info[-1][1] - 1
                        else:
                            congestion_info[-1][29] = 0
                        self.segment_name = path_to_take[0]
                        self.segment_slot = 0
                    else:
                        #print("entry3");
                        """"else take first of the availabe route"""
                        seg_min_index = seg_tmp.index(min(seg_tmp))
                        #update new segment

                        cong_tmp[seg_min_index][0] = cong_tmp[seg_min_index][0] + 1
                        #print("seg_min_index: ", seg_min_index);
                        #update old segment
                        if(self.segment_name == "AN1"):
                            congestion_info[-1][1] = congestion_info[-1][1] - 1
                        else:
                            congestion_info[-1][29] = congestion_info[-1][29] - 1
                        #self.segment_name = road.possible_routes[seg_min_index];
                        self.segment_name = road.possible_routes[self.segment_name][seg_min_index]
                        self.segment_slot = 0

                else:
                    """"if congestion is not equal, take the route with minimal congestion"""
                    if(min(seg_tmp) != 1000):
                        # print("cong_tmp", cong_tmp)
                        # print("seg_tmp", seg_tmp)
                        seg_min_index = seg_tmp.index(min(seg_tmp))

                        #update new segment
                        cong_tmp[seg_min_index][0] = cong_tmp[seg_min_index][0] + 1
                        #print("seg_min_index: ", seg_min_index);

                        #update old segment
                        if(self.segment_name == "AN1"):
                            congestion_info[-1][1] = congestion_info[-1][1]-1
                        else:
                            congestion_info[-1][29] = congestion_info[-1][29] - 1

                        #self.segment_name = road.possible_routes[seg_min_index];
                        #print("segment_name",self.segment_name)
                        #print("seg_min_index", seg_min_index)
                        self.segment_name = road.possible_routes[self.segment_name][seg_min_index]

                        self.segment_slot = 0

                #update the visited nodes
                if(self.segment_name.count("A") > 0):
                    self.visited = self.visited + ["A"]

                if(self.segment_name.count("B") > 0):
                    self.visited = self.visited + ["B"]

                if(self.segment_name.count("C") > 0):
                    self.visited = self.visited + ["C"]

                if(self.segment_name.count("D") > 0):
                    self.visited = self.visited + ["D"]
        #if the car is in any other slot other than last slot of segment, then update the location
        else:
            congestion_info = self.get_junction_info(road)
            #checking if next slot is free
            if(congestion_info[2][self.segment_slot+1] == 0):
                #update the new slot
                congestion_info[2][self.segment_slot+1] = 1

                #update the old slot
                congestion_info[2][self.segment_slot] = 0
                self.segment_slot = self.segment_slot + 1

    #get the congestion at the junction

    def get_junction_info(self, road):

        if(self.segment_name == 'AN1'):
            tmp = [[road.N1N2, road.N1N3], 1, road.AN1]
            return(tmp)

        if(self.segment_name == 'N1A'):
            tmp = [[], 0, road.N1A]
            return(tmp)

        if(self.segment_name == 'N1N2'):
            tmp = [[road.N2D, road.N2N4], road.TN1N2, road.N1N2]
            return(tmp)

        if(self.segment_name == 'N2N1'):
            tmp = [[road.N1N3], road.TN2N1, road.N2N1]  # v3
            return(tmp)

        if(self.segment_name == 'N2D'):
            tmp = [[road.DN5], road.TN2D, road.N2D]
            return(tmp)

        if(self.segment_name == 'DN2'):
            tmp = [[road.N2N1, road.N2N4], road.TDN2, road.DN2]
            return(tmp)

        if(self.segment_name == 'DN5'):
            tmp = [[road.N5N4, road.N5C], road.TDN5, road.DN5]
            return(tmp)

        if(self.segment_name == 'N5D'):
            tmp = [[road.DN2], road.TN5D, road.N5D]
            return(tmp)

        if(self.segment_name == 'N5C'):
            tmp = [[road.CN6], road.TN5C, road.N5C]
            return(tmp)

        if(self.segment_name == 'CN5'):
            tmp = [[road.N5N4, road.N5D], road.TCN5, road.CN5]
            return(tmp)

        if(self.segment_name == 'CN6'):
            tmp = [[road.N6N4, road.N6B], road.TCN6, road.CN6]
            return(tmp)

        if(self.segment_name == 'N6C'):
            tmp = [[road.CN5], road.TN6C, road.N6C]
            return(tmp)

        if(self.segment_name == 'N5N4'):
            tmp = [[road.N4N2, road.N4N6, road.N4N3], road.TN5N4, road.N5N4]
            return(tmp)

        if(self.segment_name == 'N4N5'):
            tmp = [[road.N5D, road.N5C], road.TN4N5, road.N4N5]
            return(tmp)

        if(self.segment_name == 'N4N2'):
            tmp = [[road.N2N1, road.N2D], road.TN4N2, road.N4N2]
            return(tmp)

        if(self.segment_name == 'N2N4'):
            tmp = [[road.N4N5, road.N4N6, road.N4N3], road.TN2N4, road.N2N4]
            return(tmp)

        if(self.segment_name == 'N4N6'):
            tmp = [[road.N6C, road.N6B], road.TN4N6, road.N4N6]
            return(tmp)

        if(self.segment_name == 'N6N4'):
            tmp = [[road.N4N3, road.N4N2, road.N4N5], road.TN6N4, road.N6N4]
            return(tmp)

        if(self.segment_name == 'N4N3'):
            tmp = [[road.N3N1, road.N3B], road.TN4N3, road.N4N3]
            return(tmp)

        if(self.segment_name == 'N3N4'):
            tmp = [[road.N4N2, road.N4N5, road.N4N6], road.TN3N4, road.N3N4]
            return(tmp)

        if(self.segment_name == 'N6B'):
            tmp = [[road.BN3], road.TN6B, road.N6B]
            return(tmp)

        if(self.segment_name == 'BN6'):
            tmp = [[road.N6N4, road.N6C], road.TBN6, road.BN6]
            return(tmp)

        if(self.segment_name == 'BN3'):
            tmp = [[road.N3N1, road.N3N4], road.TBN3, road.BN3]
            return(tmp)

        if(self.segment_name == 'N3B'):
            tmp = [[road.BN6], road.TN3B, road.N3B]
            return(tmp)

        if(self.segment_name == 'N3N1'):
            tmp = [[road.N1N2], road.TN3N1, road.N3N1]  # v3
            return(tmp)

        if(self.segment_name == 'N1N3'):
            tmp = [[road.N3N4, road.N3B], road.TN1N3, road.N1N3]
            return(tmp)

    #function to check if all nodes are visited

    def check_visited_all(self):
        if('A' in self.visited and 'B' in self.visited and 'C' in self.visited and 'D' in self.visited):
            self.all_visited = True
            return True
        else:
            return False
