def shortest_path(M,start,goal):
    explored=set()
    frontier={}
    Node_objects={}
    path=graph_search(M,start,goal)
    print("shortest path called")
    path.remove(None)
    print(path)
    return path
def dist_bw_intersections(M,intersection1,intersection2):
    x=(M.intersections[intersection2][0]-M.intersections[intersection1][0])**2
    y=(M.intersections[intersection2][1]-M.intersections[intersection1][1])**2
    sqrt = (x+y)**(1/2.0)
    return sqrt
def cal_f(M,intersection1,intersection2,goal,total):
    g=dist_bw_intersections(M,intersection1,intersection2)
    g=g+total
    h=dist_bw_intersections(M,intersection2,goal)
    f=g+h
    return f

class Node(object):
    def __init__(self,state):
        self.total = 0
        self.state = state
        self.parent = None
        self.road = []
    def set_roads(self,roads):
        self.road = list(roads)
    def set_parent(self,parent):
        self.parent = parent
    def set_total(self,total):
        self.total = total
    def get_parent(self):
        return self.parent
        
def graph_search(M,start,goal):
    explored=set()
    frontier={}
    Node_objects={}
    frontier[start] = cal_f(M,start,start,goal,0)
    
    parent = None
    Node_objects[start]=Node(start)
    
    while bool(frontier) == True:
        if bool(frontier) == False:
            return False
            
        key_min = min(frontier.keys(),key=(lambda k: frontier[k]))
        explored.add(key_min)
        value=frontier[key_min]
        del frontier[key_min]
        
        Node_objects[key_min].set_roads(M.roads[key_min])
        for road in Node_objects[key_min].road:
            if road in explored:
                if road!=Node_objects[key_min].parent:
                    val=cal_f(M,road,key_min,goal,Node_objects[road].total)
                    if val<value:
                        Node_objects[key_min].set_parent(road)
                        
        
        if key_min == goal:
            parent = goal
            path=[]
            path.append(goal)
           
            while parent != None:
                
                parent = Node_objects[parent].parent
                
                path.append(parent)
                
            return path[::-1]
        for roads in Node_objects[key_min].road:
            if roads not in frontier and roads not in explored:
                frontier[roads] = cal_f(M,key_min,roads,goal,Node_objects[key_min].total)
                Node_objects[roads]=Node(roads)
                Node_objects[roads].set_parent(key_min)
                Node_objects[roads].set_total(dist_bw_intersections(M,key_min,roads)+Node_objects[key_min].total)
               
        
        
        
        
        
        
