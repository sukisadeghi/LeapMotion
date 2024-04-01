from threading import Thread,Lock
import pygame
import sys
sys.path.insert(0 ,"C:/Users/suki/PycharmProjects/Leap_motion")
import Leap
from Leap import SwipeGesture
import random



shape_posi=[]

from time import sleep

class shape:

    color_index=0

    def __init__(self):
        self.color_index = random.randint(0, 6)


        #print(self.color_index)

move_R = False
move_L = False

class Graphic():
    move_right = False
    move_left = False

    poses = []
    x = 0
    y = 0
    count = 0
    while count < 88:
        posi = [x, y, 'empty']
        poses.append(posi)
        if y < 600:
            y += 60
        elif x < 400:
            y = 0
            x += 60
        count = count + 1
    x_pos = 0
    y_pos = 0
    print(poses)
    squares = []


    back_img = pygame.image.load(r"grass.jpg")
    #start_img= pygame.image.load(r"start.jpg")
    menu = pygame.image.load(r"menu.jpg")
    red = pygame.image.load(r"red.jpg")
    purple = pygame.image.load(r"purple.jpg")
    green = pygame.image.load(r"green.jpg")
    blue = pygame.image.load(r"blue.jpg")
    orange = pygame.image.load(r"orange.jpg")
    pink = pygame.image.load(r"pink.jpg")
    yellow = pygame.image.load(r"yellow.jpg")

    color_list = [red,purple, blue, green, orange, pink, yellow]

    def __init__(self):
        pygame.init()
        pygame.mixer.music.load('play.mp3')



    def set_pos(self, position):
        tmp = self.poses[position]
        self.x_pos = tmp[0]
        self.y_pos = tmp[1]

    def draw(self):
        pygame.mixer.music.play(-1)
        global move_L
        global move_R
        start_flag=True
        global lose_flag
        # Create a sample listener and controller
        listener = SampleListener()
        controller = Leap.Controller()
        # Have the sample listener receive events from the controller
        controller.add_listener(listener)
        # drawing screen
        button = pygame.image.load(r"button.jpg")
        start = pygame.image.load(r"start.jpg")
        start_screen = pygame.display.set_mode((450, 800))
        start_screen.fill(0)

        while start_flag:
            m = 660 // start.get_width() + 1
            for x in range(420 // start.get_width() + 1):
                for y in range(660 // start.get_height() + 1):
                    start_screen.blit(start, (x * 100, y * 100))

            #pygame.draw.rect(start_screen, (255,0,0), (140,580,180,60))
            start_screen.blit(button,(160,580))
            font = pygame.font.Font(None, 30)
            scoretext = font.render("Start", 1, (255, 255, 255))
            start_screen.blit(scoretext, (200,600))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x, y = event.pos
                    #if button.get_rect().collidepoint(x, y):
                    print(pos)
                    if x<270 and x>160:
                        if y<653 and y>580:
                            print("image clicked")
                            start_flag=False

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update()


        screen = pygame.display.set_mode((420, 660))
        screen.fill(0)
        flag_next = True

        # self.red=pygame.Surface((40,40))
        position = self.red.get_rect()
        # print(position)
        count=1
        lose_flag=False
        c=1
        while True:

            if lose_flag:
                print("scaping!!")
                break
            # new rect
            m = 660 // self.back_img.get_width() + 1
            for x in range(420 // self.back_img.get_width() + 1):
                for y in range(660 // self.back_img.get_height() + 3):
                    screen.blit(self.back_img, (x * 100, y * 100))

            if flag_next == True:
                shape_posi.append(22)
                self.set_pos(22)
                sq = shape()
                self.squares.append(sq)
                position.x = self.x_pos
                position.y = self.y_pos
                # print(position)
                screen.blit(self.color_list[sq.color_index], position)
                # print(sq.color_index)
                flag_next = False

            i = 0
            for rect in self.squares:
                temp = shape_posi[i]
                self.set_pos(temp)
                position.x = self.x_pos
                position.y = self.y_pos
                screen.blit(self.color_list[rect.color_index], position)
                # print ("x-pos{}  y_pos{}".format(self.x_pos,self.y_pos))
                i = i + 1
                # print(i)
            pygame.display.flip()
            # pygame.time.delay(200)
            pygame.display.update()
            flag_move = True
            size = shape_posi.__len__()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)


            while (flag_move and not lose_flag):

                # print(position)
                iter2 = self.poses[shape_posi[size - 1] + 1]
                iter1 = self.poses[shape_posi[size - 1]]

                size=self.squares.__len__()
                #print(flag)
                if iter2[2] == "empty" and self.y_pos < 600:

                    screen.blit(self.back_img, position, position)  # erase
                    position = position.move(0, 60)
                    self.y_pos = position.y
                    screen.blit(self.color_list[self.squares[size - 1].color_index], position)
                    shape_posi[size - 1] = shape_posi[size - 1] + 1

                    iter2[2] = "full"
                    iter1[2] = "empty"


                    #if self.move_right=="True" and self.x_pos!=360:
                    if move_R == True and self.x_pos != 360:
                        move_R=False
                        iter3 = self.poses[shape_posi[size - 1] + 11]
                        screen.blit(self.back_img, position, position)
                        position = position.move(60, 0)
                        self.x_pos = position.x
                        screen.blit(self.color_list[self.squares[size - 1].color_index], position)
                        shape_posi[size - 1] = shape_posi[size - 1] + 11
                        iter3[2] = "full"
                        iter2[2] = "empty"
                        self.move_right=False

                    if move_L ==True and self.x_pos != 0:
                        move_L=False
                        iter4 = self.poses[shape_posi[size - 1] - 11]
                        screen.blit(self.back_img, position, position)
                        position = position.move(-60, 0)
                        self.x_pos = position.x
                        screen.blit(self.color_list[self.squares[size - 1].color_index], position)
                        shape_posi[size - 1] = shape_posi[size - 1] - 11
                        iter4[2] = "full"
                        iter2[2] = "empty"
                        self.move_left=False

                    # print("after {} ".format(move_right))
                    # screen.blit(back_img,(self.x_pos, self.y_pos))


                elif self.y_pos == 0:
                    print("YOU LOST")
                    lose_flag=True



                else:
                    flag_next = True
                    flag_move = False

                # quit
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit(0)
                pygame.display.update()
                pygame.time.delay(200)
            if self.y_pos <= 480:
                size=shape_posi.__len__()
                print("square size {}".format(size))
                pl = shape_posi[size - 1]
                p2 = shape_posi[size - 1] + 1
                p3 = shape_posi[size - 1] + 2
                counter1 = 0
                for sq in shape_posi:
                    if sq == p2:
                        break
                    counter1 = counter1 + 1
                print("counter1 {}".format(counter1))
                #print("len: {}".format(self.squares.__len__()))

                counter2 = 0
                for sq in shape_posi:
                    if sq == p3:
                        break
                    counter2 = counter2 + 1
                if counter1!=size and counter2 !=size:
                    print(size-1)
                    print("finish1")
                    print(counter1)
                    print(counter2)
                    if self.squares[counter2].color_index == self.squares[counter1].color_index and self.squares[
                        counter1].color_index == self.squares[size - 1].color_index:
                        print("inside")
                        tmp = self.poses[p2]
                        tmp[2] = "empty"
                        tmp = self.poses[p3]
                        tmp[2] = "empty"
                        tmp = self.poses[pl]
                        tmp[2] = "empty"

                        # print(self.squares.__len__())
                        del self.squares[counter1]
                        del self.squares[counter2]
                        del self.squares[self.squares.__len__() - 1]

                        del shape_posi[counter1]
                        del shape_posi[counter2]
                        del shape_posi[shape_posi.__len__() - 1]

                                                            #delete row array
        print("get rid of")
        #lose = pygame.image.load(r"button.jpg") x
        lose = pygame.image.load(r"lose.jpg")
        lose_screen = pygame.display.set_mode((300, 517))
        lose_screen.fill(0)

        while lose_flag:

            for x in range(300 // lose.get_width() + 1):
                for y in range(517 // lose.get_height() + 1):
                    start_screen.blit(lose, (x*10,y*10))
            font1 = pygame.font.Font(None,50)
            scoretext1 = font1.render("you lose ", 1, (0,255,0))
            lose_screen.blit(scoretext1, (80,400))

            # pygame.draw.rect(start_screen, (255,0,0), (140,580,180,60))
            #start_screen.blit(button, (160, 580))
            #font = pygame.font.Font(None, 30)
            #scoretext = font.render("Start", 1, (255, 255, 255))
            #lose_screen.blit(scoretext, (200, 600))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        break
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update()


class SampleListener(Leap.Listener , Thread):
     finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
     bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
     state_names = ['STATE_Invlid', 'STATE_Start', 'STATE_Update', 'STATE_End']
     direction_flag = "inval"

     def on_init(self, controller):
        print ("Initialized")

     def on_connect(self, controller):
        print ("Connected")
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

     def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print ("Disconnected")

     def on_exit(self, controller):
        print ("Exited")

     def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        for gesture in frame.gestures():

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swip = SwipeGesture(gesture)
                swipDir = swip.direction
                if swipDir.y > 0:
                     #print self.state_names[gesture.state]
                     call(self, "right", gesture.state)
                elif swipDir.y < 0:
                     #print self.state_names[gesture.state]
                     call(self, "left", gesture.state)

def call(self, conditon, state_flag):
    global move_R
    global move_L

    if state_flag == 1:
        if conditon == "right":
            print(" right")
            Graphic.move_right=True
            move_R = True
        elif conditon == "left":
            #Drag_Left(self)
            Graphic.move_left=True
            print("left")
            move_L = True
        else:
            pass
'''def Drag_Right(self):

    print " Drag Right called"
    buf = Graphic()
    buf.buffer()

def Drag_Left(self):
    print " Drag Left called"'''

def main():
    grf=Graphic()
    grf.draw()

    # Keep this process running until Enter is pressed

if __name__ == "__main__":
    main()


