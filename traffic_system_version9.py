# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 22:53:24 2021

@author: Gokul
"""


        
#global variables
import copy


class infra:
    car_list=[];
    

    def __init__(self):
        self.AN1 = [0]*2;
        self.N1A = [0]*2;
        
        self.N1N2 = [0]*30;
        self.N2N1 = [0]*30;
        
        self.N2D = [0]*30;
        self.DN2 = [0]*30;
    
        self.DN5 = [0]*30;
        self.N5D = [0]*30;
        
        self.N5C = [0]*30;
        self.CN5 = [0]*30;
    
        self.CN6 = [0]*30;
        self.N6C = [0]*30;
        
        self.N5N4 = [0]*30;
        self.N4N5 = [0]*30;
    
        self.N4N2 = [0]*30;
        self.N2N4 = [0]*30;
    
        self.N4N6 = [0]*30;
        self.N6N4 = [0]*30;
    
        self.N4N3 = [0]*30;
        self.N3N4 = [0]*30;
    
        self.N6B = [0]*30;
        self.BN6 = [0]*30;
    
        self.BN3 = [0]*30;
        self.N3B = [0]*30;
        
        self.N3N1 = [0]*30;
        self.N1N3 = [0]*30;    
        
        #traffic signals
        #self.TAN1  = 0; #removed
        
        
        self.TN2N1 = 0;  
        self.TN3N1 = 0;
        
        self.TN1N2 = 0;
        self.TDN2  = 0;
        self.TN4N2 = 0;
        
        self.TN1N3 = 0;   
        self.TN4N3 = 0;    
        self.TBN3  = 0;
        
        
        self.TN5N4 = 0;    
        self.TN2N4 = 0;   
        self.TN6N4 = 0;
        self.TN3N4 = 0;
        
        self.TDN5  = 0;
        self.TCN5  = 0;
        self.TN4N5 = 0;
        
        self.TCN6  = 0;
        self.TBN6  = 0;
        self.TN4N6 = 0;
        
        self.TN6B  = 0;
        self.TN3B  = 0;
        
        self.TN5C  = 0;
        self.TN6C  = 0;
        
        self.TN2D  = 0;
        self.TN5D  = 0;
    
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
        elif(name=="DN2"):
            return self.DN2
        elif(name=="DN5"):
            return self.DN5
        elif(name=="N5D"):
            return self.N5D
        elif(name=="N5C"):
            return self.N5C
        elif(name=="CN5"):
            return self.CN5
        elif(name=="CN6"):
            return self.CN6
        elif(name=="N6C"):
            return self.N6C
        elif(name=="N5N4"):
            return self.N5N4
        elif(name=="N4N5"):
            return self.N4N5
        elif(name=="N4N2"):
            return self.N4N2
        elif(name=="N2N4"):
            return self.N2N4
        elif(name=="N4N6"):
            return self.N4N6
        elif(name=="N6N4"):
            return self.N6N4
        elif(name=="N4N3"):
            return self.N4N3
        elif(name=="N3N4"):
            return self.N3N4
        elif(name=="N6B"):
            return self.N6B
        elif(name=="BN6"):
            return self.BN6
        elif(name=="BN3"):
            return self.BN3
        elif(name=="N3B"):
            return self.N3B
        elif(name=="N3N1"):
            return self.N3N1
        elif(name=="N1N3"):
            return self.N1N3


    #possible nodes
    possible_routes ={}
    possible_routes["AN1"]  = ["N1N2", "N1N3"]
    possible_routes["N1N2"] = ["N2D", "N2N4"]
    possible_routes["N2N1"] = ["N1N3"] 
    possible_routes["N2D"]  = ["DN5"]
    possible_routes["DN2"]  = ["N2N1", "N2N4"]
    possible_routes["DN5"]  = ["N5N4", "N5C"]
    possible_routes["N5D"]  = ["DN2"]
    possible_routes["N5C"]  = ["CN6"]
    possible_routes["CN5"]  = ["N5N4", "N5D"] #check
    possible_routes["CN6"]  = ["N6N4", "N6B"]
    possible_routes["N6C"]  = ["CN5"]
    possible_routes["N5N4"] = ["N4N2", "N4N6", "N4N3"]
    possible_routes["N4N5"] = ["N5D", "N5C"]
    possible_routes["N4N2"] = ["N2N1", "N2D"]
    possible_routes["N2N4"] = ["N4N5", "N4N6", "N4N3"]
    possible_routes["N4N6"] = ["N6C", "N6B"]
    possible_routes["N6N4"] = ["N4N5", "N4N2","N4N3"]
    possible_routes["N4N3"] = ["N3N1", "N3B"]
    possible_routes["N3N4"] = ["N4N2", "N4N5","N4N6"]
    possible_routes["N6B"]  = ["BN3"]
    possible_routes["BN6"]  = ["N6N4", "N6C"]
    possible_routes["BN3"]  = ["N3N1", "N3N4"]
    possible_routes["N3B"]  = ["BN6"]
    possible_routes["N3N1"] = ["N1N2"]    
    possible_routes["N1N3"] = ["N3N4", "N3B"]
        
    #traffic lights
    traffic_lights ={}
    traffic_lights["N1"] = ["TN2N1","TN3N1"]
    traffic_lights["N2"] = ["TN1N2","TDN2", "TN4N2"]
    traffic_lights["D"] = ["TN2D","TN5D"]
    traffic_lights["N3"] = ["TN4N3","TBN3","TN1N3"]
    traffic_lights["N4"] = ["TN5N4","TN2N4", "TN3N4", "TN6N4"]
    traffic_lights["N5"] = ["TDN5","TCN5","TN4N5",]
    traffic_lights["B"] = ["TN3B","TN6B"]
    traffic_lights["N6"] = ["TBN6","TN4N6","TCN6"]
    traffic_lights["C"] = ["TN5C","TN6C"]
    
    
    #all route nodes
    all_routes_node = {};
    all_routes_node["N1"] = ["N2N1","N3N1","N1N2","N1N3"];
    all_routes_node["N2"] = ["N1N2","DN2", "N4N2","N2N1","N2N4","N2D"];
    all_routes_node["D"] = ["N2D","N5D","DN2","DN5"]
    all_routes_node["N3"] = ["N4N3","BN3","N1N3","N3N4","N3B","N3N1"]
    all_routes_node["N4"] = ["TN5N4","TN2N4", "TN3N4", "TN6N4","N4N5","N4N2","N4N3","N4N6"]
    all_routes_node["N5"] = ["TDN5","TCN5","TN4N5","N5D","N5C","N5N4"]
    all_routes_node["B"] = ["TN3B","TN6B","BN6","BN3"]
    all_routes_node["N6"] = ["TBN6","TN4N6","TCN6","N6C","N6N4","N6B"]
    all_routes_node["C"] = ["TN5C","TN6C","CN6","CN5"]
    
    tmp_all_routes_node={};
    tmp_all_routes_node["N1"] = ["N2,N1","N3,N1","N1,N2","N1,N3"];
    tmp_all_routes_node["N2"] = ["N1,N2","DN2", "N4,N2","N2,N1","N2,N4","N2D"];
    tmp_all_routes_node["D"] = ["N2,D","N5,D","D,N2","D,N5"]
    tmp_all_routes_node["N3"] = ["N4,N3","B,N3","N1,N3","N3,N4","N3,B","N3,N1"]
    tmp_all_routes_node["N4"] = ["N5,N4","N2,N4", "N3,N4", "N6,N4","N4,N5","N4,N2","N4,N3","N4,N6"]
    tmp_all_routes_node["N5"] = ["D,N5","C,N5","N4,N5","N5,D","N5,C","N5,N4"]
    tmp_all_routes_node["B"] = ["N3,B","N6,B","B,N6","B,N3"]
    tmp_all_routes_node["N6"] = ["B,N6","N4,N6","C,N6","N6,C","N6,N4","N6,B"]
    tmp_all_routes_node["C"] = ["N5,C","N6,C","C,N6","C,N5"]
    

    def chk_node_in_out(self,s_path,node):

        for i in range(len(self.all_routes_node[node])):
           
            if(s_path == self.all_routes_node[node][i]):
                path_map=self.tmp_all_routes_node[node][i]
                path_split=path_map.split(",");
                
                if(path_split[0]==node):
                    return("out");
                else:
                    return("in");
                    
                
    
    def get_node_congestion(self, name):
        if(name=="N1"):
            return [sum(self.N2N1),sum(self.N3N1)]
        if(name=="N2"):
            return [sum(self.N1N2),sum(self.DN2),sum(self.N4N2)]
        if(name=="N3"):
            return [sum(self.N4N3),sum(self.BN3),sum(self.N1N3)]
        if(name == "N4"):
            return [sum(self.N5N4),sum(self.N2N4),sum(self.N3N4),sum(self.N6N4)]
        if(name=="N5"):
            return [sum(self.DN5),sum(self.CN5),sum(self.N4N5)]
        if(name=="N6"):
            return [sum(self.BN6),sum(self.N4N6),sum(self.CN6)]
        if(name=="B"):
            return [sum(self.N6B),sum(self.N3B)]
        if(name=="C"):
            return [sum(self.N5C),sum(self.N6C)]
        if(name=="D"):
            return [sum(self.N2D),sum(self.N5D)]
        

            
            
            
    def get_car_map(self):
        car_map={};
        car_map["AN1"]  = {};
        car_map["N1N2"] = {};
        car_map["N2N1"] = {};
        car_map["N2D"]  = {};
        car_map["DN2"]  = {};
        car_map["DN5"]  = {};
        car_map["N5D"]  = {};
        car_map["N5C"]  = {};
        car_map["CN5"]  = {};
        car_map["CN6"]  = {};
        car_map["N6C"]  = {};
        car_map["N5N4"] = {};
        car_map["N4N5"] = {};
        car_map["N4N2"] = {};
        car_map["N2N4"] = {};
        car_map["N4N6"] = {};
        car_map["N6N4"] = {};
        car_map["N4N3"] = {};
        car_map["N3N4"] = {};
        car_map["N6B"]  = {};
        car_map["BN6"]  = {};
        car_map["BN3"]  = {};
        car_map["N3B"]  = {};
        car_map["N3N1"] = {};
        car_map["N1N3"] = {};        
        
        for c in road.car_list:
            car_map[c.segment_name][c.segment_slot] =c.carno;
        
        return car_map;
            
            

    def get_node_traffic_lights(self, node_name):
        return self.traffic_lights[node_name]
    
    def get_traffic_to_array(self, traffic_light_name):
        if(traffic_light_name == "TN1N2"):
            return self.N1N2
        elif(traffic_light_name == "TN2N1"):
            return self.N2N1
        elif(traffic_light_name == "TN2D"):
            return self.N2D
        elif(traffic_light_name=="TDN2"):
            return self.DN2
        elif(traffic_light_name=="TDN5"):
            return self.DN5
        elif(traffic_light_name=="TN5D"):
            return self.N5D
        elif(traffic_light_name=="TN5C"):
            return self.N5C
        elif(traffic_light_name=="TCN5"):
            return self.CN5
        elif(traffic_light_name=="TCN6"):
            return self.CN6
        elif(traffic_light_name=="TN6C"):
            return self.N6C
        elif(traffic_light_name=="TN5N4"):
            return self.N5N4
        elif(traffic_light_name=="TN4N5"):
            return self.N4N5
        elif(traffic_light_name=="TN4N2"):
            return self.N4N2
        elif(traffic_light_name=="TN2N4"):
            return self.N2N4
        elif(traffic_light_name=="TN4N6"):
            return self.N4N6
        elif(traffic_light_name=="TN6N4"):
            return self.N6N4
        elif(traffic_light_name=="TN4N3"):
            return self.N4N3
        elif(traffic_light_name=="TN3N4"):
            return self.N3N4
        elif(traffic_light_name=="TN6B"):
            return self.N6B
        elif(traffic_light_name=="TBN6"):
            return self.BN6
        elif(traffic_light_name=="TBN3"):
            return self.BN3
        elif(traffic_light_name=="TN3B"):
            return self.N3B
        elif(traffic_light_name=="TN3N1"):
            return self.N3N1
        elif(traffic_light_name=="TN1N3"):
            return self.N1N3     
        
        
        
    def get_traffic_light_value (self, traffic_light_name):
        if(traffic_light_name == "TN1N2"):
            return self.TN1N2
        elif(traffic_light_name == "TN2N1"):
            return self.TN2N1
        elif(traffic_light_name == "TN2D"):
            return self.TN2D
        elif(traffic_light_name=="TDN2"):
            return self.TDN2
        elif(traffic_light_name=="TDN5"):
            return self.TDN5
        elif(traffic_light_name=="TN5D"):
            return self.TN5D
        elif(traffic_light_name=="TN5C"):
            return self.TN5C
        elif(traffic_light_name=="TCN5"):
            return self.TCN5
        elif(traffic_light_name=="TCN6"):
            return self.TCN6
        elif(traffic_light_name=="TN6C"):
            return self.TN6C
        elif(traffic_light_name=="TN5N4"):
            return self.TN5N4
        elif(traffic_light_name=="TN4N5"):
            return self.TN4N5
        elif(traffic_light_name=="TN4N2"):
            return self.TN4N2
        elif(traffic_light_name=="TN2N4"):
            return self.TN2N4
        elif(traffic_light_name=="TN4N6"):
            return self.TN4N6
        elif(traffic_light_name=="TN6N4"):
            return self.TN6N4
        elif(traffic_light_name=="TN4N3"):
            return self.TN4N3
        elif(traffic_light_name=="TN3N4"):
            return self.TN3N4
        elif(traffic_light_name=="TN6B"):
            return self.TN6B
        elif(traffic_light_name=="TBN6"):
            return self.TBN6
        elif(traffic_light_name=="TBN3"):
            return self.TBN3
        elif(traffic_light_name=="TN3B"):
            return self.TN3B
        elif(traffic_light_name=="TN3N1"):
            return self.TN3N1
        elif(traffic_light_name=="TN1N3"):
            return self.TN1N3

    
    def set_traffic_light_value (self, traffic_light_name, value):
        if(traffic_light_name == "TN1N2"):
            self.TN1N2 = value
        elif(traffic_light_name == "TN2N1"):
            self.TN2N1 = value
        elif(traffic_light_name == "TN2D"):
            self.TN2D= value
        elif(traffic_light_name=="TDN2"):
            self.TDN2 = value
        elif(traffic_light_name=="TDN5"):
            self.TDN5 = value
        elif(traffic_light_name=="TN5D"):
            self.TN5D = value
        elif(traffic_light_name=="TN5C"):
            self.TN5C = value
        elif(traffic_light_name=="TCN5"):
            self.TCN5 = value
        elif(traffic_light_name=="TCN6"):
            self.TCN6 = value
        elif(traffic_light_name=="TN6C"):
            self.TN6C = value
        elif(traffic_light_name=="TN5N4"):
            self.TN5N4 = value
        elif(traffic_light_name=="TN4N5"):
            self.TN4N5 = value
        elif(traffic_light_name=="TN4N2"):
            self.TN4N2 = value
        elif(traffic_light_name=="TN2N4"):
            self.TN2N4 = value
        elif(traffic_light_name=="TN4N6"):
            self.TN4N6 = value
        elif(traffic_light_name=="TN6N4"):
            self.TN6N4 = value
        elif(traffic_light_name=="TN4N3"):
            self.TN4N3 = value
        elif(traffic_light_name=="TN3N4"):
            self.TN3N4 = value
        elif(traffic_light_name=="TN6B"):
            self.TN6B = value
        elif(traffic_light_name=="TBN6"):
            self.TBN6 = value
        elif(traffic_light_name=="TBN3"):
            self.TBN3 = value
        elif(traffic_light_name=="TN3B"):
            self.TN3B = value
        elif(traffic_light_name=="TN3N1"):
            self.TN3N1 = value
        elif(traffic_light_name=="TN1N3"):
            self.TN1N3 = value



    
    
    #declare rest traffic lights    
    def update_traffic_lights(self):

          #traffic AN1
        print("before Update");
        print([	[self.TN2N1,self.TN3N1],	
        	[self.TN1N2,self.TDN2,self.TN4N2],  
        	[self.TBN3,self.TN1N3,self.TN4N3],	
        	[self.TN3N4,self.TN2N4,self.TN5N4,self.TN6N4],	
        	[self.TDN5,self.TCN5,self.TN4N5],
        	[self.TBN6,self.TCN6,self.TN4N6],
        	[self.TN3B,self.TN6B],
        	[self.TN5C,	self.TN6C],	
        	[self.TN5D,self.TN2D]
        ]);
          
    
    #TAN1 removed
#        if(self.AN1[1]==1):
#            self.TAN1  = 1;
#        else:
#            self.TAN1 = 0;
 
        for key in road.traffic_lights:      
            lights = self.get_node_traffic_lights(key)
            t_index=self.get_node_congestion(key).index(max(self.get_node_congestion(key)));
            for i in lights:
                if(lights.index(i)!=t_index):
                    self.set_traffic_light_value(i,0)
                else:
                    self.set_traffic_light_value(i,1)
                    
                    
        print("After Update");
        print([	[self.TN2N1,self.TN3N1],	
        	[self.TN1N2,self.TDN2,self.TN4N2],  
        	[self.TBN3,self.TN1N3,self.TN4N3],	
        	[self.TN3N4,self.TN2N4,self.TN5N4,self.TN6N4],	
        	[self.TDN5,self.TCN5,self.TN4N5],
        	[self.TBN6,self.TCN6,self.TN4N6],
        	[self.TN3B,self.TN6B],
        	[self.TN5C,	self.TN6C],	
        	[self.TN5D,self.TN2D]
        ]);
                

    def get_collision(self):
        new_collision = 0
        for key in self.possible_routes:
            #print("route", key)
            arr = self.getRoadWithName(key)
            #print("arr", arr)
            for i in arr:
                #print("i",i)
                if(i>1):
                    new_collision = new_collision + 1;
            #print("road", key, "collision", new_collision)       
        return new_collision;
                 
        
        #modify traffic lights based on AN1 congestion
    def chk_unique_traffic_signal_at_junction(self):
        
        traffic_check = [[road.TN2N1,road.TN3N1],	
        	[road.TN1N2,road.TDN2,road.TN4N2],  
        	[road.TBN3,road.TN1N3,road.TN4N3],	
        	[road.TN3N4,road.TN2N4,road.TN5N4,road.TN6N4],	
        	[road.TDN5,road.TCN5,road.TN4N5],
        	[road.TBN6,road.TCN6,road.TN4N6],
        	[road.TN3B,road.TN6B],
        	[road.TN5C,	road.TN6C],	
        	[road.TN5D,road.TN2D]];
                 
        for t in range(len(traffic_check)):
            if(sum(traffic_check[t])>1):
                print("chk_unique_traffic_signal_at_junction CONSTARINT FAILED:index:",t,"traffic_check",traffic_check[t]); 
                break;
        return True;
    
    def get_traffic_details(self):
        
        traffic_check = [[road.TN2N1,road.TN3N1],	
        	[road.TN1N2,road.TDN2,road.TN4N2],  
        	[road.TBN3,road.TN1N3,road.TN4N3],	
        	[road.TN3N4,road.TN2N4,road.TN5N4,road.TN6N4],	
        	[road.TDN5,road.TCN5,road.TN4N5],
        	[road.TBN6,road.TCN6,road.TN4N6],
        	[road.TN3B,road.TN6B],
        	[road.TN5C,	road.TN6C],	
        	[road.TN5D,road.TN2D]];

        return traffic_check;    
    
    
    def check_vehicle_violations(self,pre_road,pre_car_map):
        
        
        #chk unique at junctin
#        pre_dic={};
#        pos_dic={};  
#        for node in self.traffic_lights:
#            lights = self.get_node_traffic_lights(node);
#            for l in lights:
#                pre_dic[node]={};
#                pos_dic[node]={};
#        
#                
#        for node in self.traffic_lights:
#            lights = self.get_node_traffic_lights(node);
#            for l in lights:
#                
#                pos_dic[node][l]=[self.car_map().get(l,29,0)]; #first element represent inflow
#                for pos_route in self.possible_routes(l):    
#                    pos_dic[node][l] = pos_dic[node][l] + [self.car_map().get(pos_route,0)];
#
#                pre_dic[l]=[pre_road.pre_car_map.get(l,29,0)];
#                for pos_route in pre_road.possible_routes(l):    
#                    pre_dic[node][l] = pre_dic[node][l] + [pre_road.pre_car_map.get(pos_route,0)];     
        curr_car_map=self.get_car_map();
        
        print("prev_car_map",pre_car_map);
        print("curr_car_map",curr_car_map);  
        print(pre_road.get_traffic_details());
    
        for node in self.traffic_lights:
            lights = self.get_node_traffic_lights(node);
            
            
          
            for tl in lights:
                l = tl.replace("T","");
                print("CHECK ENTRY segment=",l);
                
                curr_car_map=self.get_car_map();
                if(pre_road.get_traffic_light_value(tl)==1 and (curr_car_map.get(l)!=None and pre_car_map.get(l) !=None)):
                    
                    print("Entering TRAFFIC GREEN")    
                    #chk if pre and post of that is valid
                    
                    curr_car_map=self.get_car_map();
                    #print(curr_car_map,pre_car_map);
                    #print(curr_car_map.get(l),pre_car_map.get(l));
#                    if(curr_car_map.get(l) == None or  pre_car_map.get(l) ==None):
#                        continue;
                                
                    curr_car_no=curr_car_map.get(l).get(29,0);
                    pre_car_no=pre_car_map.get(l).get(29,0);
                    
                    print("TGreen:curr_car_no,precar_no",curr_car_no,pre_car_no);
                    
                    
                    if(pre_car_no>0 and curr_car_no==0):
                        
                        for p in self.all_routes_node[node]:
                            if(p not in self.possible_routes[l] and p!=l):
                                
                                car_no_in_p0 = self.get_car_map().get(p).get(0,0);
                                car_no_in_p29 =self.get_car_map().get(p).get(29,0);
                                print("route p",p);
                                print("car no :p0,p29",car_no_in_p0,car_no_in_p29);
                                print("NODE TYPE:",self.chk_node_in_out(p,node));
                                #if(p[-1]==node[-1]):
                                if(self.chk_node_in_out(p,node)=='in'):
                        
                                    if(curr_car_no == car_no_in_p29 and curr_car_no!=0):
                                        print("ERROR : Car Crossing lane");
                                        exit();
                                #elif(p[0]==node[0]):
                                elif(self.chk_node_in_out(p,node)=='out'):
                                    if(curr_car_no == car_no_in_p0 and curr_car_no!=0):
                                        print("ERROR : Car making U turn");
                                        exit();
                                
                elif((curr_car_map.get(l)!=None and pre_car_map.get(l) !=None)):
                        print("TL=0 loop")
                        curr_car_map=self.get_car_map();
                        curr_car_no=curr_car_map.get(l).get(29,0);
                        pre_car_no=pre_car_map.get(l).get(29,0);
                        print("precar,currcar",pre_car_no,curr_car_no);
                        if(pre_car_no >0 and curr_car_no==0 ):
                            print("ERROR : No Respect to traffic : crossing when Traffic light is not green",l);
                            exit();
                        
                    
                    
            
        
        
                
                
                

            
            
                            
                                
                    

                    
                
                
            
        

        
       
        
road = infra();
#pre_move_status
pre_road = infra();
pre_car_map={};


class car:
    
    #segment_name = None
    #segment_slot = None
    visited = [];
    id = None;
    all_visited = None;
    def __init__(self,carno):
       self.carno=carno;
       self.segment_name = "AN1"
       self.segment_slot = 0
       road.AN1[0]=1;
       self.all_visited = False


    def move(self):
        global road;
        
        #chck in nodes B,C,D reached update vseg list

        #consider only N1A for updating 'A' in vseg
        if(self.segment_slot==29 and (self.segment_name=="N2N1" or self.segment_name=="N3N1") and ('B' in self.visited and 'C' in self.visited and 'D' in self.visited)):
            self.visited = self.visited +["A"]
        elif((self.segment_slot == 29) or ((self.segment_name == "AN1") and self.segment_slot == 1)):
            congestion_info = self.get_junction_info();
            #print("visited array:", self.visited);
            #print("congestion info from start of move(): ", congestion_info[0], congestion_info[1] ,congestion_info[2])
            
            if(congestion_info[1] == 1 ): #traffic signal
                cong_tmp = congestion_info[0];
                seg_tmp = [];
                
                for seg in cong_tmp:
                    if(seg[0]==0):
                        seg_tmp = seg_tmp + [sum(seg)];
                    else:
                        seg_tmp = seg_tmp + [1000];
                #print(self.segment_name,self.segment_slot);
                #print("cong_tmp",cong_tmp);
                #print("seg_tmp",seg_tmp);     
               # if((seg_tmp.count(seg_tmp[0])== len(seg_tmp))):
                if((seg_tmp.count(seg_tmp[0])== len(seg_tmp)) and seg_tmp[0]!=1000): 
                    print("entry1");
                    path_to_take=[]
                    available_path = road.possible_routes[self.segment_name]
                    if("B" not in  self.visited):
                        for value in available_path:
                            if("B" in value):
                                path_to_take= path_to_take + [value]
                        print("path to take_4", path_to_take)
                    if("C" not in  self.visited):
                        for value in available_path:
                            if("C" in value):
                                path_to_take= path_to_take + [value]
                        print("path to take_5", path_to_take)
                    if("D" not in  self.visited):
                        for value in available_path:
                            if("D" in value):
                                path_to_take= path_to_take + [value]
                        print("path to take_6", path_to_take)  
                    if(len(path_to_take)):  
                        print("entry2");
                        road.getRoadWithName(path_to_take[0])[0]=road.getRoadWithName(path_to_take[0])[0] + 1
                        if(self.segment_name=="AN1"): 
                            congestion_info[-1][1] = congestion_info[-1][1] - 1;
                        else:
                            congestion_info[-1][29] = 0;
                        self.segment_name = path_to_take[0]
                        self.segment_slot = 0; 
                    else:
                        print("entry3");
                       
                        seg_min_index = seg_tmp.index(min(seg_tmp)); 
                        #update new segment
                        
                        cong_tmp[seg_min_index][0] = cong_tmp[seg_min_index][0] + 1;
                        #print("seg_min_index: ", seg_min_index);
                        #update old segment
                        if(self.segment_name=="AN1"): 
                            congestion_info[-1][1] =congestion_info[-1][1] -  1;
                        else:
                            congestion_info[-1][29] = congestion_info[-1][29] - 1;
                        #self.segment_name = road.possible_routes[seg_min_index];
                        self.segment_name = road.possible_routes[self.segment_name][seg_min_index];
                        self.segment_slot = 0;
                                                       
                else: 
                    if(min(seg_tmp)!=1000):
                        print("entry4");
                        # print("cong_tmp", cong_tmp)
                        # print("seg_tmp", seg_tmp)
                        seg_min_index = seg_tmp.index(min(seg_tmp))
                        #update new segment
                        cong_tmp[seg_min_index][0] = cong_tmp[seg_min_index][0] + 1;
                        #print("seg_min_index: ", seg_min_index);
                        #update old segment
                        if(self.segment_name=="AN1"): 
                            congestion_info[-1][1] = congestion_info[-1][1]-1;
                        else:
                            congestion_info[-1][29] = congestion_info[-1][29] - 1;
                        
                        #self.segment_name = road.possible_routes[seg_min_index];
                        print("segment_name",self.segment_name)
                        print("seg_min_index", seg_min_index)
                        self.segment_name = road.possible_routes[self.segment_name][seg_min_index];
                        
                        self.segment_slot = 0;
                
                if( self.segment_name.count("A") >0):
                    self.visited = self.visited + ["A"];
                
                if( self.segment_name.count("B") >0):
                    self.visited = self.visited + ["B"];
                    
                if( self.segment_name.count("C") >0):
                    self.visited = self.visited + ["C"];
                
                if( self.segment_name.count("D") >0):
                    self.visited = self.visited + ["D"];    
        
        else:
            print("entry5");
            congestion_info = self.get_junction_info();
            #print("congestion info from else of move(): ", congestion_info[0], congestion_info[1] ,congestion_info[2])
            if(congestion_info[2][self.segment_slot+1]==0):
                congestion_info[2][self.segment_slot+1]=1;
                congestion_info[2][self.segment_slot]=0;
                self.segment_slot = self.segment_slot + 1;
            
                
        #each junction also update vseg a.k.a visited segment
        
        #traffic rules - check in junction
        #if in junction speacial case
        
        #else common case
        #elif(A)            
        
    def get_junction_info(self):
        global road;
        
        if(self.segment_name == 'AN1'):
            tmp=[[road.N1N2,road.N1N3],1,road.AN1];
            return(tmp);
            
        if(self.segment_name == 'N1N2'):
            tmp=[[road.N2D,road.N2N4],road.TN1N2,road.N1N2];
            return(tmp);

        if(self.segment_name == 'N2N1'):
            tmp=[[road.N1N3],road.TN2N1,road.N2N1];   #v3
            return(tmp);
            
        if(self.segment_name == 'N2D'):
            tmp=[[road.DN5],road.TN2D,road.N2D];
            return(tmp);
            
        if(self.segment_name == 'DN2'):
            tmp=[[road.N2N1,road.N2N4],road.TDN2,road.DN2];
            return(tmp);
            
        if(self.segment_name == 'DN5'):
            tmp=[[road.N5N4,road.N5C],road.TDN5,road.DN5];
            return(tmp);        
            
        if(self.segment_name == 'N5D'):
            tmp=[[road.DN2],road.TN5D,road.N5D];
            return(tmp);

        if(self.segment_name == 'N5C'):
            tmp=[[road.CN6],road.TN5C,road.N5C];
            return(tmp);
            
        if(self.segment_name == 'CN5'):
            tmp=[[road.N5N4,road.N5D],road.TCN5,road.CN5];
            return(tmp);

        if(self.segment_name == 'CN6'):
            tmp=[[road.N6N4,road.N6B],road.TCN6,road.CN6];
            return(tmp);

        if(self.segment_name == 'N6C'):
            tmp=[[road.CN5],road.TN6C,road.N6C];
            return(tmp);
        
        if(self.segment_name == 'N5N4'):
            tmp=[[road.N4N2,road.N4N6,road.N4N3],road.TN5N4,road.N5N4];
            return(tmp);
    
        if(self.segment_name == 'N4N5'):
            tmp=[[road.N5D,road.N5C],road.TN4N5,road.N4N5];
            return(tmp);
            
        if(self.segment_name == 'N4N2'):
            tmp=[[road.N2N1,road.N2D],road.TN4N2,road.N4N2];
            return(tmp);
        
        if(self.segment_name == 'N2N4'):
            tmp=[[road.N4N5,road.N4N6,road.N4N3],road.TN2N4,road.N2N4];
            return(tmp);
            
        if(self.segment_name == 'N4N6'):
            tmp=[[road.N6C,road.N6B],road.TN4N6,road.N4N6];
            return(tmp);
            
        if(self.segment_name == 'N6N4'):
            tmp=[[road.N4N3,road.N4N2,road.N4N5],road.TN6N4,road.N6N4];
            return(tmp);
            
        if(self.segment_name == 'N4N3'):
            tmp=[[road.N3N1,road.N3B],road.TN4N3,road.N4N3];
            return(tmp);
            
        if(self.segment_name == 'N3N4'):
            tmp=[[road.N4N2,road.N4N5,road.N4N6],road.TN3N4,road.N3N4];
            return(tmp);
            
        if(self.segment_name == 'N6B'):
            tmp=[[road.BN3],road.TN6B,road.N6B];
            return(tmp);
            
        if(self.segment_name == 'BN6'):
            tmp=[[road.N6N4,road.N6C],road.TBN6,road.BN6];
            return(tmp);
            
        if(self.segment_name == 'BN3'):
            tmp=[[road.N3N1,road.N3N4],road.TBN3,road.BN3];
            return(tmp);
            
        if(self.segment_name == 'N3B'):
            tmp=[[road.BN6],road.TN3B,road.N3B];
            return(tmp);
            
        if(self.segment_name == 'N3N1'):
            tmp=[[road.N1N2],road.TN3N1,road.N3N1];#v3
            return(tmp);

        if(self.segment_name == 'N1N3'):
            tmp=[[road.N3N4,road.N3B],road.TN1N3,road.N1N3];
            return(tmp);
            


        
    def check_visited_all(self):
        if('A' in self.visited and 'B' in self.visited and 'C' in self.visited and 'D' in self.visited):
            self.all_visited = True
            return True;
        else:
            return False;
            
count = 0;
step_count=0;
del_cars_count=0;
total_cars_count=0;
del_car_list=[];
collision = 0


while(1):

    print("entering while ...");
    
    pre_road = copy.deepcopy(road); #road status before all car moves
    
    pre_car_map= road.get_car_map();
    
 

    cars_to_be_deleted = [];
    for i in range(len(road.car_list)):
        
    
        road.car_list[i].move();  #car movement  



        
        collision = collision + road.get_collision()
        print("Total number of collisions from the start:",  collision)
        if(road.car_list[i].check_visited_all()):
            cars_to_be_deleted = cars_to_be_deleted + [road.car_list[i]];
            print('\x1b[1;31;47m' + "I Reached!! "+"arr_index: ", i,"CarNo:",road.car_list[i].carno,"node: ",
                        road.car_list[i].segment_name, "slot: ", road.car_list[i].segment_slot,
                        "visited array: ", ''.join(set(road.car_list[i].visited)) + '\x1b[0m');
        else:
           print("arr_index: ", i,"CarNo:",road.car_list[i].carno,"node: ",
                 road.car_list[i].segment_name, "slot: ", road.car_list[i].segment_slot, 
                 "visited array: ", ''.join(set(road.car_list[i].visited)));
           
            
            #del road.car_list[i];       #del car if completed    
        # and 
    
    
    road.check_vehicle_violations(pre_road,pre_car_map);     
    
    
    if(road.AN1[0]==0): #check if first slot dont have car
        total_cars_count +=1;
        c = car(total_cars_count);
        print("init:",c.carno, c.segment_name, c.segment_slot);
        road.car_list = road.car_list + [c];
        
    road.update_traffic_lights();  
    
    
    
    traffic_check = [[road.TN2N1,road.TN3N1],	
    	[road.TN1N2,road.TDN2,road.TN4N2],  
    	[road.TBN3,road.TN1N3,road.TN4N3],	
    	[road.TN3N4,road.TN2N4,road.TN5N4,road.TN6N4],	
    	[road.TDN5,road.TCN5,road.TN4N5],
    	[road.TBN6,road.TCN6,road.TN4N6],
    	[road.TN3B,road.TN6B],
    	[road.TN5C,	road.TN6C],	
    	[road.TN5D,road.TN2D]];
             
    for t in range(len(traffic_check)):
        if(sum(traffic_check[t])>1):
            print("TRAFFIC CHECK CONSTARINT FAILED:index:",t,"traffic_check",traffic_check[t]); 
            break;

    
            
    #cars deleted in separate iteration
    for j in cars_to_be_deleted:
        del_car_list=del_car_list + [j.carno];
        print('\x1b[1;31;47m' +"DELETED Index: ", road.car_list.index(j),"CarNo:",
            j.carno,"node: ", j.segment_name, "slot: ", j.segment_slot, 
            "visited array: ", ''.join(set(j.visited)) + '\x1b[0m');
        
        #update in main road - remove from road
        road.getRoadWithName(j.segment_name)[j.segment_slot] = road.getArrayWithName(j.segment_name)[j.segment_slot] - 1 ;
        
        road.car_list.remove(j);   
        del_cars_count +=1;
        
    step_count = step_count +1;
    if(step_count%160==0):
        print('\x1b[1;31;47m'+"***********************30 steps after---DELTED CARS COUNT:*******************" + '\x1b[0m');
        print('\x1b[1;31;47m'+"Total Cars:",str(total_cars_count),"Completed Cars:",str(del_cars_count)  + '\x1b[0m');
        
        print('\x1b[1;31;47m'+"Del Car Nos:"+ '\x1b[0m',end="");
        for d in del_car_list:
            print('\x1b[1;31;47m'+ str(d)+ '\x1b[0m',end="");
            if(d!=del_car_list[-1]):
                print('\x1b[1;31;47m'+","+ '\x1b[0m',end="");
                
    p_ctrl=input("Press e to exit");
    if(p_ctrl == 'e'):
       break;