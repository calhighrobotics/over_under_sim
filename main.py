import pygame
import math
# Initialize pygame
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gamepad Control")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()
# Initialize the gamepad
pygame.joystick.init()

# Create a Turtle
obj_x = 0
obj_y = 750
velocity = 0.3

background_image = pygame.image.load("over_under_field.png").convert()  # Replace with the path to your image

# Scale the background image to fit the screen size
background_image = pygame.transform.smoothscale(background_image, screen.get_size())


# Create a list to store the trailing points
trail_points = []

# Function to handle gamepad input and control the Turtle
if pygame.joystick.get_count() == 0:
    print("No gamepad detected.")
    pygame.quit()

joystick = pygame.joystick.Joystick(0)
joystick.init()


while True:
    
    
    for event in pygame.event.get():
    
        if event.type == pygame.JOYBUTTONDOWN and event.button == 0 or event.type == pygame.QUIT:
            pygame.quit()
            break
        
        
        pygame.event.clear()
        screen.fill(WHITE)
        screen.blit(background_image, (0, 0))
        # Get the joystick axes values
        axis_x = joystick.get_axis(0)
        axis_y = -1 * joystick.get_axis(1)

        # Adjust speed and angles based on joystick input# Adjust the angle increment as needed

        # Control Turtle movement
        
        '''  
        hypot = math.hypot(axis_x, axis_y)
            
            
        angle = math.degrees(math.asin(axis_y / hypot))
        
        if axis_x > 0 and axis_y > 0:
            pass
           
           
        if axis_x < 0 and axis_y > 0:
            temp = 90 + (90 - angle)
            angle = temp
            
        if axis_x < 0 and axis_y < 0:
            temp = 180 + (-1 * angle)
            angle = temp
            
        if axis_x > 0 and axis_y < 0:
            temp = 270 + (90 - (-1 * angle))
            angle = temp
        
        print(f'x: {axis_x}, y: {axis_y}, a: {angle}, hyp: {hypot}')
        print(trail_points)
        
        '''
            # Invert y-axis for more intuitive control
        
        obj_x += 3 * axis_x
        obj_y += -1 * (3 * axis_y)
        
        print(f'x: {axis_x}, y: {axis_y}')
        
        trail_points.append((obj_x, obj_y))
        
            
        
        
        
        for i in range(1, len(trail_points)):
            pygame.draw.line(screen, RED, trail_points[i - 1], trail_points[i], 3)

        pygame.draw.circle(screen, RED, (int(obj_x), int(obj_y)), 10)
        
        pygame.display.flip()
        pygame.event.pump()
        
        # Exit the program on gamepad button press (e.g., 'A' button)
        if event.type == pygame.JOYBUTTONDOWN and event.button == 0 or event.type == pygame.QUIT:
            pygame.quit()
            break

# Start the gamepad control function