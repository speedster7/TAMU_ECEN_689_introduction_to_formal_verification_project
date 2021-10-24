# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:03:14 2021

@author: Velz_Wiz
"""


        
#global variables



class infra:
    AN1 = [0]*1;
    N1A = [0]*1;
    
    N1N2 = [0]*30;
    N2N1 = [0]*30;
    
    N2D = [0]*30;
    DN2 = [0]*30;

    DN5 = [0]*30;
    N5D = [0]*30;
    
    N5C = [0]*30;
    CN5 = [0]*30;

    CN6 = [0]*30;
    N6C = [0]*30;
    
    N5N4 = [0]*30;
    N4N5 = [0]*30;

    N4N2 = [0]*30;
    N2N4 = [0]*30;

    N4N6 = [0]*30;
    N6N4 = [0]*30;

    N4N3 = [0]*30;
    N3N4 = [0]*30;

    N6B = [0]*30;
    BN6 = [0]*30;

    BN3 = [0]*30;
    N3B = [0]*30;

    N3N1 = [0]*30;
    N1N3 = [0]*30;

    car_list=[];
    collison=0;

    #possible nodes
    possible_routes ={}
    
    possible_routes["AN1"]  = ["N1N2", "N1N3"]
    possible_routes["N1N2"] = ["N2D", "N2N4"]
    possible_routes["N2N1"] = ["N1N3", "AN1"]
    possible_routes["N2D"]  = ["DN5"]
    possible_routes["DN2"]  = ["N2N1", "N2N4"]
    possible_routes["DN5"]  = ["N5N4", "N5C"]
    possible_routes["N5D"]  = ["DN2"]
    possible_routes["N5C"]  = ["CN6"]
    possible_routes["CN5"]  = ["N5N4", "N5D"] #check
    possible_routes["N5N4"] = ["N4N2", "N4N6, N4N3"]
    possible_routes["CN6"]  = ["N6N4", "N6B"]
    possible_routes["N6C"]  = ["CN5"]
    possible_routes["N5N4"] = ["N4N2", "N4N6"]
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
    possible_routes["N3N1"] = ["N1N2", "N1A"]
    possible_routes["N1N3"] = ["N3N4", "N3B"]
        
    #traffic lights
    TAN1  = 0;
    TN1N2 = 0;
    TN2N1 = 0;
    TN2D  = 0;
    TDN2  = 0;
    TDN5  = 0;
    TN5D  = 0;
    TN5C  = 0;
    TCN5  = 0;
    TCN6  = 0;
    TN6C  = 0;
    TN5N4 = 0;
    TN4N5 = 0;
    TN4N2 = 0;
    TN2N4 = 0;
    TN4N6 = 0;
    TN6N4 = 0;
    TN4N3 = 0;
    TN3N4 = 0;
    TN6B  = 0;
    TBN6  = 0;
    TBN3  = 0;
    TN3B  = 0;
    TN3N1 = 0;
    TN1N3 = 0;
    
    
    #declare rest traffic lights
    
    
    def update(self):
        
        self.TAN1  = 1;
        self.TN1N2 = 1;
        self.TN2N1 = 1;
        self.TN2D  = 1;
        self.TDN2  = 1;
        self.TDN5  = 1;
        self.TN5D  = 1;
        self.TN5C  = 1;
        self.TCN5  = 1;
        self.TCN6  = 1;
        self.TN6C  = 1;
        self.TN5N4 = 1;
        self.TN4N5 = 1;
        self.TN4N2 = 1;
        self.TN2N4 = 1;
        self.TN4N6 = 1;
        self.TN6N4 = 1;
        self.TN4N3 = 1;
        self.TN3N4 = 1;
        self.TN6B  = 1;
        self.TBN6  = 1;
        self.TBN3  = 1;
        self.TN3B  = 1;
        self.TN3N1 = 1;
        self.TN1N3 = 1;
        
        #modify traffic lights based on AN1 congestion
        
road = infra();

class car:
    
    #segment_name = None
    #segment_slot = None
    visited = [];
    
    def __init__(self):
        #self.carno=carno;
       self.segment_name = "AN1"
       self.segment_slot = 0


    def move(self):
        global road;
        
        #chck in nodes B,C,D reached update vseg list

                #consider only N1A for updating 'A' in vseg
        
        
        if((self.segment_slot == 29) or (self.segment_name == "AN1")):
            congestion_info = self.get_junction_info();
            #print("visited array:", self.visited);
            #print("congestion info from start of move(): ", congestion_info[0], congestion_info[1] ,congestion_info[2])
            
            if(congestion_info[1] == 1): #traffic signal
                cong_tmp = congestion_info[0];
                seg_tmp = [];
                
                for seg in cong_tmp:
                    if(seg[0]==0):
                        seg_tmp = seg_tmp + [sum(seg)];
                    else:
                        seg_tmp = seg_tmp + [1000];
                
                seg_min_index = seg_tmp.index(min(seg_tmp));
                
                #update new segment
                cong_tmp[seg_min_index][0] = 1;
                #print("seg_min_index: ", seg_min_index);
                #update old segment
                if(self.segment_name=="AN1"): 
                    congestion_info[-1][0] = 0;
                else:
                    congestion_info[-1][29] = 0;
                
                #self.segment_name = road.possible_routes[seg_min_index];
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
            tmp=[[road.N1N2,road.N1N3],road.TAN1,road.AN1];
            return(tmp);
            
        if(self.segment_name == 'N1N2'):
            tmp=[[road.N2D,road.N2N4],road.TN1N2,road.N1N2];
            return(tmp);

        if(self.segment_name == 'N2N1'):
            tmp=[[road.N1A,road.N1N3],road.TN2N1,road.N2N1];
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
            tmp=[[road.N1N2,road.N1A],road.TN3N1,road.N3N1];
            return(tmp);

        if(self.segment_name == 'N1N3'):
            tmp=[[road.N3N4,road.N3B],road.TN1N3,road.N1N3];
            return(tmp);
            


        
    def check_visited_all(self):
        if('A' in self.visited and 'B' in self.visited and 'C' in self.visited and 'D' in self.visited):
            return True;
        else:
            return False;
            

while(1):

    print("entering while ...");
    
    p_ctrl = input();
    if(p_ctrl == '$'):
        exit();
        
    ## car generate 
    if(len(road.car_list) < 20):
        c = car();
        print("init:", c.segment_name, c.segment_slot);
        road.car_list = road.car_list + [c];
        
    for i in range(len(road.car_list)):
        #road.getcongestion(carlist_i.getsegment())
        road.car_list[i].move();  #car movement

        print("numbner: ", i,"node: ", road.car_list[i].segment_name, "slot: ", road.car_list[i].segment_slot, "visited array: ", road.car_list[i].visited);

        if(road.car_list[i].check_visited_all()):
            del road.car_list[i];       #del car if completed
    
    road.update();
    
#segment,array
#traffic light