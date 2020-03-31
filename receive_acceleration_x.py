#import create_serial
import pygame
from create_serial import CreateSerial

# return the acc_x value, separated from list
def unPackSerialAcc(acc_x):
    acc_x_value = 0
    item_to_find = "acc_x"
    for item in acc_x:
        if item_to_find in item:
            string_acc_x_value = item.split(": ")[1]
            acc_x_value = float(string_acc_x_value)
            print(acc_x_value)

pygame.init()

DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 400
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
display = pygame.display.set_mode(DISPLAY_SIZE)

grey = (50, 50, 50)
clock = pygame.time.Clock()


# ----------------- serial connection --------------------
serial_1 = CreateSerial("/dev/cu.usbmodem142301") # change this to the name of your serial port
serial_1.openPort() # open the serial port
line = ""
msg_filtered = ""

# ----------------- game loop ----------------------------
run_game = True
while run_game:
    display.fill((grey))
    line = serial_1.read()
    if line != None:
        msg_filtered = line

    unPackSerialAcc(msg_filtered)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                serial_1.write("score_up")
            elif event.key == pygame.K_DOWN:
                serial_1.write("score_down")

    pygame.display.update()
    clock.tick(45)

serial_1.close()
pygame.quit()
quit()
