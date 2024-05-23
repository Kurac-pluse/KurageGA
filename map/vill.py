#map
class tile:
    def __init__(self, facility="", area="", object="", penetrable=None):
        self.facility = facility
        self.area = area
        self.object = object
        # エージェントが通過可能なタイルか
        self.penetrable = penetrable

def set_bed_room(village, x,y,w,l):
    for i in range(w):
        for j in range(l):
            village[x+i][y+j].area = "bedroom"
    return village

def set_bath_room(village, x,y,w,l):
    for i in range(w):
        for j in range(l):
            village[x+i][y+j].area = "bathroom"
    return village

def set_kitchen(village, x,y,w,l):
    for i in range(w):
        for j in range(l):
            village[x+i][y+j].area = "kitchen"
    return village

def set_living_room(village, x,y,w,l):
    for i in range(w):
        for j in range(l):
            village[x+i][y+j].area = "livingroom"
    return village

def set_wall(village, x,y,w,l):
    wall = "wall"
    for i in range(20):
        village[x+i][y].object = wall
        village[x+i][y].penetrable = False
    for i in range(15):
        village[x+i][y+9].object = wall
        village[x+i][y+9].penetrable = False
    for i in range(10):
        village[x][y+i].object = wall
        village[x][y+i].penetrable = False
    for i in range(10):
        village[x+w-1][y+i].object = wall
        village[x+w-1][y+i].penetrable = False
    for i in range(6):
        village[x+5][y+i+1].object = wall
        village[x+5][y+i+1].penetrable = False
        village[x+10][y+i+1].object = wall
        village[x+10][y+i+1].penetrable = False
        village[x+11+i][y+4].object = wall
        village[x+11+i][y+4].penetrable = False
    village[x+8][y+6].object = wall
    village[x+8][y+6].penetrable = False
    village[x+9][y+6].object = wall
    village[x+9][y+6].penetrable = False
    return village

def set_house_object(village, x,y,w,l):
    for i in range(4):
        for j in range(2):
            village[x+1+i][y+1+j].object = "bed"
            village[x+1+i][y+1+j].penetrable = True
            village[x+15+i][y+1+j].object = "kitchen"
            village[x+15+i][y+1+j].penetrable = True
    
            village[x+8+j][y+1+i].object = "bath"
            village[x+8+j][y+1+i].penetrable = True
    for i in range(2):
        for j in range(2):
            village[x+1+i][y+4+j].object = "desk"
            village[x+1+i][y+4+j].penetrable = False
            village[x+1+i][y+6+j].object = "chair"
            village[x+6+i][y+6+j].penetrable = True
            village[x+6+i][y+1+j].object = "wc"
            village[x+6+i][y+1+j].penetrable = True
            village[x+11+i][y+1+j].object = "refrigerator"
            village[x+11+i][y+1+j].penetrable = False
            village[x+11+i][y+5+j].object = "chair"
            village[x+11+i][y+5+j].penetrable = True
            village[x+13+i][y+5+j].object = "desk"
            village[x+13+i][y+5+j].penetrable = False
            village[x+15+i][y+5+j].object = "chair"
            village[x+15+i][y+5+j].penetrable = True
    return village

def set_house(village, x,y,w=20,l=10):
    for i in range(w):
        for j in range(l):
            village[x+i][y+j].facility = "house"
    #ここからは拡張性なしで部屋の形を固定
    village = set_bed_room(village, x+1,y+1,4,8)
    village = set_bath_room(village, x+6,y+1,4,5)
    village = set_kitchen(village, x+11,y+1,8,3)
    village = set_living_room(village, x+11,y+5,8,4)
    for i in range(w):
        for j in range(l):
            if village[x+i][y+j].area == "":
                village[x+i][y+j].area = "corridor"
    village = set_wall(village, x,y,w,l)
    village = set_house_object(village, x,y,w,l)
    return village

def set_park(village, x,y,w,l):
    for i in range(w):
        for j in range(l):
            village[x+i][y+j].facility = "park"
            village[x+i][y+j].area = "park"
    for i in range(2):
        for j in range(2):
            village[x+8+i][y+1+j].object = "chair"
            village[x+8+i][y+1+j].penetrable = True
            village[x+12+i][y+1+j].object = "chair"
            village[x+12+i][y+1+j].penetrable = True
            village[x+10+i][y+1+j].object = "desk"
            village[x+10+i][y+1+j].penetrable = False
            village[x+4+i][y+3+j].object = "tree"
            village[x+4+i][y+3+j].penetrable = False
            village[x+16+i][y+3+j].object = "tree"
            village[x+16+i][y+3+j].penetrable = False
    for i in range(22):
        village[x+i][y].object = "fance"
        village[x+i][y].penetrable = False
        village[x+i][y+5].object = "fance"
        village[x+i][y+5].penetrable = False
    return village

# village = [[tile() for _ in range(20)] for _ in range(50)]
# village = set_house(village, x=1,y=1,w=20,l=10)
# village = set_house(village, x=29,y=1,w=20,l=10)
# village = set_park(village, x=14,y=13,w=22,l=6)

# for i in range(50):
#     for j in range(20):
#         print(village[i][j].area, " ", end="")    
#     print("a")

def get_village():
    village = [[tile() for _ in range(20)] for _ in range(50)]
    village = set_house(village, x=1,y=1,w=20,l=10)
    village = set_house(village, x=29,y=1,w=20,l=10)
    village = set_park(village, x=14,y=13,w=22,l=6)
    return village

# village = set_house(village, 1,1,20,10)

