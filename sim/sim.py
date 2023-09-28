import pygame
from pygame.locals import *
import math
import random
import copy
# Initialize pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Over Under Simulator")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()
# Initialize the gamepad
pygame.joystick.init()

# Create a Turtle
obj_x = 0
obj_y = 750
velocity = 0.3

background_image = pygame.image.load("assets/over_under_field.png").convert()  # Replace with the path to your image

# Scale the background image to fit the screen size
background_image = pygame.transform.smoothscale(background_image, screen.get_size())

logo = pygame.image.load("assets/robot.jpeg").convert_alpha()
logo = pygame.transform.smoothscale(logo, (50, 50))
# Create a list to store the trailing points
trail_points = []
circle_locs = []

# Function to handle gamepad input and control the Turtle
if pygame.joystick.get_count() == 0:
    print("No gamepad detected.")
    pass
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

def sim_loop(obj_x, obj_y):
    '''
    Runs the pygame window and event loop that contains the logic for the simulation.
    
    '''
    running = True
    while running:
        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            
            
            pygame.event.clear()
            screen.fill(WHITE)
            screen.blit(background_image, (0, 0))
            
            if event.type == JOYAXISMOTION:
                axis_x = joystick.get_axis(0)
                axis_y = -1 * joystick.get_axis(1)
                    
                
                
                obj_x += 3 * axis_x
                obj_y += -1 * (3 * axis_y)
                
                trail_points.append((obj_x, obj_y))
            
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                
                # C key used for clearing the screen, d key used to draw points onto the screen
                if event.key == pygame.K_c:
                    trail_points.clear()
                    circle_locs.clear()
                    trail_points.append((obj_x, obj_y))

                if event.key == pygame.K_d:
                    red = random.randint(0, 255)
                    green = random.randint(0, 255)
                    blue = random.randint(0, 255)
                    
                    clr = (red, green, blue)
                    
                    x = copy.copy(obj_x)
                    y = copy.copy(obj_y)
                    
                    circle_loc = (x, y, clr)
                    
                    
                    circle_locs.append(circle_loc)


                # Arrow key control -> Very basic, does not check held down keys
                if keys[pygame.K_RIGHT]:
                    obj_x += 3 * 10
                    trail_points.append((obj_x, obj_y))

                if keys[pygame.K_LEFT]:
                    obj_x += 3 * -10
                    trail_points.append((obj_x, obj_y))

                if keys[pygame.K_UP]:
                    obj_y += 3 * -10
                    trail_points.append((obj_x, obj_y))

                if keys[pygame.K_DOWN]:
                    obj_y += 3 * 10
                    trail_points.append((obj_x, obj_y))
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Checks location of mouse click on screen, moves the robot there.
                # The right click button adds waypoints.
                if event.button == 1:
                    obj_x, obj_y = pygame.mouse.get_pos()
                    trail_points.append((obj_x, obj_y))
                if event.button == 3:
                    red = random.randint(0, 255)
                    green = random.randint(0, 255)
                    blue = random.randint(0, 255)
                    
                    clr = (red, green, blue)
                    
                    x = copy.copy(obj_x)
                    y = copy.copy(obj_y)
                    
                    circle_loc = (x, y, clr)
                    
                    
                    circle_locs.append(circle_loc)

            if event.type == pygame.JOYBUTTONDOWN:
                # The left button for the gamepad on the xyab pad is assigned to place waypoints
                # The up button on the pad is assigned to clear the screen.
                if event.button == 2:
                    trail_points.clear()
                    circle_locs.clear()
                    trail_points.append((obj_x, obj_y))
                if event.button == 3:
                    red = random.randint(0, 255)
                    green = random.randint(0, 255)
                    blue = random.randint(0, 255)
                    
                    clr = (red, green, blue)
                    
                    x = copy.copy(obj_x)
                    y = copy.copy(obj_y)
                    
                    circle_loc = (x, y, clr)
                    
                    
                    circle_locs.append(circle_loc)
                
            
            # Draws the trail as a graph, draws locations of waypoints, and updates logo with x,y positions. 
            for i in range(1, len(trail_points)):
                pygame.draw.line(screen, RED, trail_points[i - 1], trail_points[i], 3)

            for circle in circle_locs:
                pygame.draw.circle(screen, circle[2], (circle[0], circle[1]), 10)
                
            
            screen.blit(logo, (int(obj_x) - 25, int(obj_y) - 25))
            
            
           
            pygame.event.pump()
        pygame.display.flip()
            
            # Exit the program on gamepad button press (e.g., 'A' button)
            

# Start the gamepad control function

sim_loop(obj_x, obj_y)
