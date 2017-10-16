import turtle as t
import random as r
import time
import pygame

def PosSet(WhatNum): # 사각형 기준 왼쪽 위 모서리로 거북이를 옮기는 함수
    if WhatNum <= 4:
        t.goto(t.xcor(), 500)
    elif WhatNum <= 8:
        t.goto(t.xcor(), 250)
    elif WhatNum <= 12:
        t.goto(t.xcor(), 0)
    elif WhatNum <= 16:
        t.goto(t.xcor(), -250)

    if WhatNum % 4 == 1:
        t.goto(-900, t.ycor())
    elif WhatNum % 4 == 2:
        t.goto(-450, t.ycor())
    elif WhatNum % 4 == 3:
        t.goto(0, t.ycor())
    elif WhatNum % 4 == 0:
        t.goto(450, t.ycor())

while 1:
    T = t.clone()
    t.reset()
    T.reset()
    T.ht()
    T.up()
    T.color("red")
    pygame.init()
    music = pygame.mixer.music
    music.load("Darara_5sec.mp3")
    t.title("거북왕을 찾아라")
    t.shape("turtle")
    t.fillcolor("#FACC2E")
    t.setup(width = 1920, height = 1070, startx = 0, starty = 0)

    RunningTime = int(t.numinput("숫자 입력", "몇 초동안 움직이실건가요?"))
    a = r.randint(1, 360)

    # 거북이가 판 그리는 부분 ㅇㅈ?
    music.play()
    t.speed(10)
    t.pensize(10) # 거북이 똥 사이즈 10
    t.up()
    t.setpos(-900, 500)
    t.down()
    for i in range(2):
        t.fd(1800)
        t.rt(90)
        t.fd(250)
        t.rt(90)
        t.fd(1800)
        t.lt(90)
        t.fd(250)
        t.lt(90)
    t.fd(1800) # 이 부분까지 가로선 그리는 부분

    t.lt(90)
    t.fd(1000)
    for i in range(2):
        t.lt(90)
        t.fd(450)
        t.lt(90)
        t.fd(1000)
        t.rt(90)
        t.fd(450)
        t.rt(90)
        t.fd(1000) # 이 부분까지 세로선 그리는 부분

    Text_X = - 675
    Text_Y = 360
    PlaceNum = 1
    t.up()
    for x in range(4):
        for y in range(4):
            t.goto(Text_X, Text_Y)
            t.write(PlaceNum, False, "center", ("Consolas", 30))
            PlaceNum += 1
            Text_X += 450
        Text_X = -675
        Text_Y -= 250

    Square_X = (-450, 0, 450, 900)
    Square_Y = (-250, 0, 250, 500)

    t.setpos(0, 0)
    WhatNum = int(t.numinput("숫자 입력", "거북이가 몇 번 구역으로 갈 것 같으세요?"))

    PosSet(WhatNum)
    t.setheading(0)
    t.begin_fill()
    for i in range(2):
        t.fd(450)
        t.rt(90)
        t.fd(250)
        t.rt(90)
    t.end_fill()

    t.setheading(0)
    t.fd(225)
    t.setheading(-90)
    t.fd(140)
    t.write(WhatNum, False, "center", ("Consolas", 30))

    PosSet(WhatNum)
    t.setheading(0)
    t.down()
    for i in range(2): # 색칠한 후 가려진 선 다시 그리기
        t.fd(450)
        t.rt(90)
        t.fd(250)
        t.rt(90)
    t.up()

    t.setpos(0, 0)
    t.down()

    t.pensize(1)
    t.speed(100)
    StartTime = time.time()
    music.load("Koong_Long.mp3")
    MusicStart = time.time()
    music.play()
    Timer = int(time.time() - StartTime)
    while 1:
        if RunningTime <= time.time() - StartTime:
            T.clear()
            EndPosition = t.pos()
            for x in Square_X:
                if EndPosition[0] < x: # 가로 경계선을 기준으로 어디서 끝났는지 구하기 위함
                    Answer_X = x       # 참고로 조건에 '=' 가 안 붙어있어서 선에 겹치면
                    break              # 선 기준 오른쪽 칸으로 인정될거임 (세로선은 위쪽)
            for y in Square_Y:
                if EndPosition[1] < y: # 이것도 마찬가지로 세로 경계선
                    Answer_Y = y
                    break
            music.stop()
            music.load("Ending.mp3")
            music.play()
            break
        T.write(Timer, False, "center", ("Consolas", 20))
        angle = r.randint(-30, 30)
        t.fd(5)
        a += angle
        t.setheading(a)
        if Timer != int(time.time() - StartTime):
            T.clear()
            Timer = int(time.time() - StartTime)
            T.write(Timer, False, "center", ("Consolas", 20))


        # 거북이가 가장자리에 닿았을 때
        # 튕기게 하는 부분 ㅇㅈ? ㅇ ㅇㅈ
        if(t.pos()[0] > 900 or t.pos()[0] < -900): # 왼쪽에 닿았을 때
            t.up()
            t.setx(t.pos()[0] * -1)
            t.down()

        if(t.pos()[1] > 500 or t.pos()[1] < -500): # 위쪽
            t.up()
            t.sety(t.pos()[1] * -1)
            t.down()

    if Answer_Y == 500:
        if Answer_X == -450:
            Answer = 1
        elif Answer_X == 0:
            Answer = 2
        elif Answer_X == 450:
            Answer = 3
        elif Answer_X == 900:
            Answer = 4

    elif Answer_Y == 250:
        if Answer_X == -450:
            Answer = 5
        elif Answer_X == 0:
            Answer = 6
        elif Answer_X == 450:
            Answer = 7
        elif Answer_X == 900:
            Answer = 8

    elif Answer_Y == 0:
        if Answer_X == -450:
            Answer = 9
        elif Answer_X == 0:
            Answer = 10
        elif Answer_X == 450:
            Answer = 11
        elif Answer_X == 900:
            Answer = 12

    elif Answer_Y == -250:
        if Answer_X == -450:
            Answer = 13
        elif Answer_X == 0:
            Answer = 14
        elif Answer_X == 450:
            Answer = 15
        elif Answer_X == 900:
            Answer = 16

    EndHeading = t.heading()
    t.goto(EndPosition[0], EndPosition[1])
    t.setheading(EndHeading)

    print("정답은", Answer, "입니다!")
    if WhatNum == Answer:
        music.load("Chuka_Faster.mp3")
        music.play()
        t.up()
        t.speed(10)
        i = 30
        c = 1
        for j in range(1,50):
            c += 0.1
            t.left(t.heading() + i)
            t.shapesize(c, c)
        print("ㅗㅜㅑ 맞추셨네요! 축하합니다 짝짝짝!")
    else:
        t.up()
        t.speed(10)
        i = 30
        c = 1
        time.sleep(1)
        t.fillcolor("red")
        t.shapesize(5, 5)
        print("꽝!")

        quit = t.textinput("확인", "종료하실거면 Q 계속하실거면 아무거나 넣어주세요")
        if quit == 'q' or quit == 'Q':
            break
