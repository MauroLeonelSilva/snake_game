import os
import random
import readchar


#INSTRUCTIONS
# FOR CREATE THE MAP, EACH LINE MUST BE THE SAME SIZE, IF YOU DONT

# IF YOU DON'T WRITE THE BLANK SPACES (" "), THE GAME IS BROKEN
# If it seems more practical to put another symbol instead of putting spaces, you can put any character except "#"

# THE HASH ("#") IS A OBSTACLE WALL, YOU CAN'T GO THROUGH IT 
# IF YOU PRESS "Q" EXIT GAME
# YOU CAN INDICATE HOW MANY FRUITS APPEAR ON THE MAP IN THE LINE(NUM_OF_MAP_FRUITS)



#Create the Map here:
obstacle_definition = """\
#############   ############
#                          #
#                          #
#                          #
                            
             ###            
#                          #
#                          #
#                          #
#                          #
#                          #
#                          #
#                          #
#############   ############\
"""

POS_X = 0
POS_Y = 1

# How many fruits (*) do you want to appear on the screen?
NUM_OF_MAP_FRUITS = 1

my_position = [1,1]
tail_length = 0 
tail = []
map_objects = []
num_of_objects = NUM_OF_MAP_FRUITS+ len(map_objects)

end_game = False
died = False

#create obstacle wall map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
print(obstacle_definition)

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

#number of objects on the map
total_objects = MAP_WIDTH * MAP_HEIGHT
for coordinate_y in range(MAP_HEIGHT):
    for coordinate_x in range(MAP_WIDTH):
        if obstacle_definition[coordinate_y][coordinate_x] == "#":
                total_objects -= 1

# Main loop
while not end_game:
    os.system("cls")

    #generate random objects in the map
    while len(map_objects) < NUM_OF_MAP_FRUITS:

        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#" and new_position not in tail:
            map_objects.append(new_position)
         

    #draw map
    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for coordinate_y in range(MAP_HEIGHT):

        print("|", end="")
    
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = " "
            object_in_cell = None
            tail_in_cell = None
            

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object
                    

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw ="O"
                    tail_in_cell = tail_piece
                    

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length += 1
                    num_of_objects +=1

                if tail_in_cell:
                    end_game = True
                    died = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "#"
                    
            print(" {}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 2 + "+")
    print("Need to eat " + str(total_objects - tail_length - NUM_OF_MAP_FRUITS + 1) + " ' * ' to win")
    
            

    #movimiento del jugador
    direction = str(readchar.readchar())
    new_position = None

    if direction == 'w':
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
        
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
        
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1 ) % MAP_WIDTH , my_position[POS_Y]]
        
    elif direction == 'd':
        new_position = [(my_position[POS_X] + 1 ) % MAP_WIDTH , my_position[POS_Y]]

    elif direction == "q":
        end_game = True
    
    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

    if num_of_objects == total_objects:
        print("You Won!")
        break
    os.system("cls")



if died:
    print("Game Over!")