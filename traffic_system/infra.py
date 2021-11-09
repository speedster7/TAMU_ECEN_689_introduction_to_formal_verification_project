import random ## used to generate random no of vehicles in each lane
import pandas ## used to format printing for visibility to user

class infra:                    ## MAIN infrastructure class that holds all the sub-blocks needed for transport
    
    car_list=[];                ##List of all cars in the traffic system
    


#Constructor to initialize all road arrays with zero initial values ie no cars are present initially
    def __init__(self):         
    
    ## Roads are contructed as list of integers
        self.AN1 = [0]*2;   
        self.N1A = [0]*2;
        
        #forward lane in the direction N1N2        
        self.N1N2 = [0]*30;  

        #backward lane in the direction N2N1 Similarly for all other lanes        
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
        

        
#### Traffic Light singnals ##  

#Signal TN2N1 controls all cars moving from node N2 to N1     
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
        
        
 ##Function to get road integer array from road Name    
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


    #List of all possible routes at junctions - for each paths
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
        
    #traffic lights - at each of the nodes
    traffic_lights ={}
    traffic_lights["N1"] = ["TN2N1","TN3N1"]
    traffic_lights["N2"] = ["TN1N2","TDN2", "TN4N2"]
    traffic_lights["D"] = ["TN2D","TN5D"]
    traffic_lights["N3"] = ["TN4N3","TBN3","TN1N3"]
    traffic_lights["N4"] = ["TN5N4","TN2N4", "TN3N4", "TN6N4"]
    traffic_lights["N5"] = ["TDN5","TCN5","TN4N5",]
    traffic_lights["B"] = ["TN6B","TN3B"]
    traffic_lights["N6"] = ["TBN6","TN4N6","TCN6"]
    traffic_lights["C"] = ["TN5C","TN6C"]
    
    
    #all route nodes - All possible routes at each node - used in checking_for_Violations function
    all_routes_node = {};
    all_routes_node["N1"] = ["N2N1","N3N1","N1N2","N1N3"];
    all_routes_node["N2"] = ["N1N2","DN2", "N4N2","N2N1","N2N4","N2D"];
    all_routes_node["D"] = ["N2D","N5D","DN2","DN5"]
    all_routes_node["N3"] = ["N4N3","BN3","N1N3","N3N4","N3B","N3N1"]
    all_routes_node["N4"] = ["N5N4","N2N4", "N3N4", "N6N4","N4N5","N4N2","N4N3","N4N6"]
    all_routes_node["N5"] = ["DN5","CN5","N4N5","N5D","N5C","N5N4"]
    all_routes_node["B"] = ["N3B","N6B","BN6","BN3"]
    all_routes_node["N6"] = ["BN6","N4N6","CN6","N6C","N6N4","N6B"]
    all_routes_node["C"] = ["N5C","N6C","CN6","CN5"]
    
    
    # Temporary dictionary mapping used to find if a node is incoming or outgoing 
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
    # find if a node is incoming or outgoing : eg N2N1 at node N1 is incoming since last char is 'N1'

        for i in range(len(self.all_routes_node[node])):
           
            if(s_path == self.all_routes_node[node][i]):
                path_map=self.tmp_all_routes_node[node][i]
                path_split=path_map.split(",");
                
                if(path_split[0]==node):
                    return("out");
                else:
                    return("in");
                    
                
 # get congestion at each of the nodes - returns sumed up values in each path - no of cars basically   
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
        

            
            
## Gets the map of car in each path,slot -> carno -used in violations checking            
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
        
        for c in self.car_list:
            car_map[c.segment_name][c.segment_slot] =c.carno;
        
        return car_map;
            
            
## Get the list of traffic lights at node_name passed
    def get_node_traffic_lights(self, node_name):
        return self.traffic_lights[node_name]


## Get the corresponding path(integer array/road) which is controlled by traffic light name passed    
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
        
        
## Get the traffic light value at the specified Traffic light name       
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


## SET the traffic light value at the specified Traffic light name           
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



## Main Function which updates the traffic values at all nodes
    def update_traffic_lights(self):
        star=str('/'*68);

        
        print(star + " BEFORE UPDATE " +star);
        print("");
        
        # Print Traffic lights before updating for post analysis
        self.print_traffic_lights(); 
    

        # Loop through each node 
        for key in self.traffic_lights:      
            
            # Get Traffic lights at the node 'Key'
            lights = self.get_node_traffic_lights(key)
            
            #Get the congestion information at that node and find maximum congested path index
            t_index=self.get_node_congestion(key).index(max(self.get_node_congestion(key)));
            
            #Loop through the traffic lights in that node
            for i in lights:
            
            #if index is NOT same as max_index -> signal 0
                if(lights.index(i)!=t_index):
                    self.set_traffic_light_value(i,0)
            
            #if index is EQUAL to max_index -> signal 1 to decongest the max_congested path
                else:
                    self.set_traffic_light_value(i,1)
                    
        print("");                       
        print(star + " AFTER UPDATE " +star);
        print("");          

        #Print the traffic lights after update
        self.print_traffic_lights();                


# Check for Collisions
    def get_collision(self):
    
    #Initial Collision set to 0
        new_collision = 0
        
        #Loop through all possible routes
        for key in self.possible_routes:

            #Get array with that route
            arr = self.getRoadWithName(key)

        #Check if any element in that array is >1 which signifies that a collision has occured
            for i in arr:

                if(i>1):
                    new_collision = new_collision + 1;
  
        return new_collision;
                 
        
        #Check only one traffic light is enabled at each node
    def chk_unique_traffic_signal_at_junction(self):
        
        #arrange traffic signal values according to each node
        traffic_check = [[self.TN2N1,self.TN3N1],	
        	[self.TN1N2,self.TDN2,self.TN4N2],  
        	[self.TBN3,self.TN1N3,self.TN4N3],	
        	[self.TN3N4,self.TN2N4,self.TN5N4,self.TN6N4],	
        	[self.TDN5,self.TCN5,self.TN4N5],
        	[self.TBN6,self.TCN6,self.TN4N6],
        	[self.TN3B,self.TN6B],
        	[self.TN5C,	self.TN6C],	
        	[self.TN5D,self.TN2D]];
        
        #if sum of any individual list is >1 
        #for eg [1,1] in first row then it means both TN2N1 AND TN3N1 is ON, so signal ERROR
        for t in range(len(traffic_check)):
            if(sum(traffic_check[t])>1):
                print("chk_unique_traffic_signal_at_junction CONSTARINT FAILED:index:",t,"traffic_check",traffic_check[t]); 
                break;
        return True;
    
 #Check for all vehicle violations 
 # parameter :pre_road -> has the road topology before move function is applied on all cars
 # parameter : pre_car_map -> has the car_number information in each of the slots before move function is applied
    def check_vehicle_violations(self,pre_road,pre_car_map):
        

        curr_car_map=self.get_car_map();
        
        print("prev_car_map",pre_car_map);
        print("curr_car_map",curr_car_map);  
        print(pre_road.get_traffic_details());
    
        #Loop through each node
        for node in self.traffic_lights:
            lights = self.get_node_traffic_lights(node);
            
            
          #Loop through each traffic lights
            for tl in lights:
                l = tl.replace("T","");
                print("CHECK ENTRY segment=",l);
                
                #Get Current car mapping - (path,slotno) -> (carno)
                curr_car_map=self.get_car_map();
                
                #Check if GREEN signal has occured
                if(pre_road.get_traffic_light_value(tl)==1 and (curr_car_map.get(l)!=None and pre_car_map.get(l) !=None)):
                    
                    print("Entering TRAFFIC GREEN")    
               
                    
                    curr_car_map=self.get_car_map();

                    #Get current car number at path 'small L' at '29th' slot            
                    curr_car_no=curr_car_map.get(l).get(29,0);
                    
                    #Get previous car number at path 'small L' at '29th' slot  
                    pre_car_no=pre_car_map.get(l).get(29,0);
                    
                    print("TGreen:curr_car_no,precar_no",curr_car_no,pre_car_no);
                    
                    #Check if a change has occurred - meaning car has moved from there - comparing prev_carno and curr_car_no
                    if(pre_car_no>0 and curr_car_no==0):
                        
                        #Loop through all possible routes at node to check if car is present  in wrong paths or not
                        for p in self.all_routes_node[node]:
                            if(p not in self.possible_routes[l] and p!=l): #exclude possible routes and current route
                                print("route p",p);
                                print("chk route p");
                                print(self.get_car_map());
                                print(self.get_car_map().get(p));
                                print(self.get_car_map().get(p).get(0,0));
                                car_no_in_p0 = self.get_car_map().get(p).get(0,0);  #get slot 0 of  lane p
                                car_no_in_p29 =self.get_car_map().get(p).get(29,0); #get slot 29 of lane p 
                                print("route p",p);
                                print("car no :p0,p29",car_no_in_p0,car_no_in_p29);
                                print("NODE TYPE:",self.chk_node_in_out(p,node));

                                if(self.chk_node_in_out(p,node)=='in'):            # Check if its incoming or outgoing node
                        
                                    if(curr_car_no == car_no_in_p29 and curr_car_no!=0): # if incoming then check slot 29
                                        print("ERROR : Car Crossing lane");
                                        exit();

                                elif(self.chk_node_in_out(p,node)=='out'):              # if outgoing then check slot 0
                                    if(curr_car_no == car_no_in_p0 and curr_car_no!=0):
                                        print("ERROR : Car making U turn");
                                        exit();
                                
                elif((curr_car_map.get(l)!=None and pre_car_map.get(l) !=None)): # if no GREEN signal then come here
                        print("TL=0 loop")
                        curr_car_map=self.get_car_map();
                        curr_car_no=curr_car_map.get(l).get(29,0);
                        pre_car_no=pre_car_map.get(l).get(29,0);
                        print("precar,currcar",pre_car_no,curr_car_no);
                        if(pre_car_no >0 and curr_car_no==0 ):          # if no GREEN but car moves from that 29th slot signal ERROR
                            print("ERROR : No Respect to traffic : crossing when Traffic light is not green",l);
                            exit();
 
    ##Print status of all paths in each node
    def print_status_node(self,node):
        star=str('*'*67);
        tl_array = [];
        tl_index = [];
        for tl in self.traffic_lights[node]:
            tl_array = tl_array + [self.get_traffic_to_array(tl)];
            tl_index = tl_index + [tl.replace("T","")];
        #print(tl_array,tl_index);
        df1 = pandas.DataFrame(data=tl_array,
                               columns=["S1","S2","S3","S4","S5","S6","S7","S8","S9","S10",
                                        "S11","S12","S13","S14","S15","S16","S17","S18","S19","S20",
                                        "S21","S22","S23","S24","S25","S26","S27","S28","S29","S30"],
                               index=tl_index);
        df2=pandas.DataFrame(df1).astype(int).to_string();  
        print(star+" JUNCTION "+ node +" "+star)    ;               
        print(df2); 

        
    ## Print traffic lights status
    def print_traffic_lights(self):
        star=str('*'*68);
        tl_array = [];
        tl_index = [];
        for node in self.traffic_lights:
            for tl in self.traffic_lights[node]:
                tl_array = tl_array + [self.get_traffic_light_value(tl)];
                tl_index = tl_index + [tl];
            #print(tl_array,tl_index);
        df1 = pandas.DataFrame(data=tl_array,columns=["Red/Green"],
                               index=tl_index);
        
        df2 = df1.T;
        df3=df2.astype(int).to_string();  
        print(star+" TRAFFIC SIGNAL : START " +star)    ;  
        print("");             
        print(df3); 
        print("");
        print(star+" TRAFFIC SIGNAL : END " +star)    ;               
        
                   

## Create a new infra object
#automatically initilizes all Traffic signals to zero and road slots to 0
road = infra();


hashchar=str('#'*67);

## Take 5 samples of traffic distribution - Randomized traffic
for i in range(1,6):
    
    print("");
    print(hashchar+" Iteration Randomize "+str(i)+" "+hashchar);
    
    
    ## Randomize each of the slots in each path to get a random traffic distribution

    road.N1N2 = [random.randint(0,1) for i in range(0,30)];
    road.N2N1 = [random.randint(0,1) for i in range(0,30)];
    
    road.N2D = [random.randint(0,1) for i in range(0,30)];
    road.DN2 = [random.randint(0,1) for i in range(0,30)];
    
    road.DN5 = [random.randint(0,1) for i in range(0,30)];
    road.N5D = [random.randint(0,1) for i in range(0,30)];
    
    road.N5C = [random.randint(0,1) for i in range(0,30)];
    road.CN5 = [random.randint(0,1) for i in range(0,30)];
    
    road.CN6 = [random.randint(0,1) for i in range(0,30)];
    road.N6C = [random.randint(0,1) for i in range(0,30)];
    
    road.N5N4 = [random.randint(0,1) for i in range(0,30)];
    road.N4N5 = [random.randint(0,1) for i in range(0,30)];
    
    road.N4N2 = [random.randint(0,1) for i in range(0,30)];
    road.N2N4 = [random.randint(0,1) for i in range(0,30)];
    
    road.N4N6 = [random.randint(0,1) for i in range(0,30)];
    road.N6N4 = [random.randint(0,1) for i in range(0,30)];
    
    road.N4N3 = [random.randint(0,1) for i in range(0,30)];
    road.N3N4 = [random.randint(0,1) for i in range(0,30)];
    
    road.N6B = [random.randint(0,1) for i in range(0,30)];
    road.BN6 = [random.randint(0,1) for i in range(0,30)];
    
    road.BN3 = [random.randint(0,1) for i in range(0,30)];
    road.N3B = [random.randint(0,1) for i in range(0,30)];
    
    road.N3N1 = [random.randint(0,1) for i in range(0,30)];
    road.N1N3 = [random.randint(0,1) for i in range(0,30)];   
    
    
    ##print status of traffic lights BEFORE update
    for key in road.traffic_lights:
        road.print_status_node(key);
    
    
    ##print status of traffic lights AFTER update 
    road.update_traffic_lights();
    
    ##Validate if the changes are logically consistent
