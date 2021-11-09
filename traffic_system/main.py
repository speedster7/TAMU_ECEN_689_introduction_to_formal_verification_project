import infra

import  car

import copy


count = 0;
step_count=0;
del_cars_count=0;
total_cars_count=0;
del_car_list=[];
collision = 0
road = infra.infra();
#pre_move_status
pre_road = infra.infra();
pre_car_map={};

while(1):

    print("entering while ...");
    
    pre_road = copy.deepcopy(road); #road status before all car moves
    
    pre_car_map= road.get_car_map();
    
 

    cars_to_be_deleted = [];
    for i in range(len(road.car_list)):
        
    
        road.car_list[i].move(road);  #car movement  



        
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
    
    
    if(road.AN1[0]==0 and len(road.car_list)<10): #check if first slot dont have car
        total_cars_count +=1;
        c = car.car(total_cars_count, road);
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
        road.getRoadWithName(j.segment_name)[j.segment_slot] = road.getRoadWithName(j.segment_name)[j.segment_slot] - 1 ;
        
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
