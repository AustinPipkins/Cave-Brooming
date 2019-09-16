from graphics import *
import time
import random
import math

handle = open("msHighScore.txt")
"""
austin pipkins
6-9-19
3 day project
"""

def gameOver(mode, timeDur, win, flagedCords, bombCords, maxBomb):
    time.sleep(.5)

    f1 = Rectangle(Point(80, 150), Point(420, 350))
    f1.draw(win)
    f1.setFill("#666666")
    f2 = Rectangle(Point(85, 155), Point(415, 345))
    f2.draw(win)
    f2.setFill("#101010")

    f2 = Rectangle(Point(110, 305), Point(210, 330))
    f2.draw(win)
    f2.setFill("#009900")
    titl = Text(Point(160, 317.5), "Play Again")
    titl.draw(win)
    titl.setTextColor("#101010")
    titl.setSize(10)

    title = Text(Point(335, 180), "Leader Board")
    title.draw(win)
    title.setTextColor("#009900")
    title.setSize(15)

    title = Text(Point(250, 250), "|\n|\n|\n|\n|\n|\n|\n|\n|\n|")
    title.draw(win)
    title.setTextColor("#009900")
    title.setSize(12)

    title1 = Text(Point(165, 195), "")
    title1.draw(win)
    title1.setTextColor("#009900")
    title1.setSize(15)

    mint = math.floor((timeDur)/60)
    sect = math.floor((timeDur)-mint*60)
    handle = open("msHighScore.txt")

    recordList = []
    for line in handle:
        print("poop")
        line = line.replace("\n", "")
        recordList.append(line)

    place1 = Text(Point(335, 215), ("#1  " + recordList[0]))
    place1.draw(win)
    place1.setSize(14)
    place1.setTextColor("#009900")
    place2 = Text(Point(335, 243), ("#2  " + recordList[1]))
    place2.draw(win)
    place2.setSize(12)
    place2.setTextColor("#009900")
    place3 = Text(Point(335, 270), ("#3  " + recordList[2]))
    place3.draw(win)
    place3.setSize(12)
    place3.setTextColor("#009900")



    winner = False
    for i in recordList:
        recordTime = i.replace(":", " ").split()
        recordTime = int(recordTime[0])*60 + int(recordTime[1])
        if timeDur < int(recordTime):
            winner = True




    title = Text(Point(165, 235), ("Time Duration:               \n" + str(mint)+ " Minute(s) " + str(sect) + " Second(s)"))
    title.draw(win)
    title.setTextColor("#009900")
    title.setSize(10)

    correct = 0
    for flagCord in flagedCords:
        for bombCord in bombCords:
            if flagCord == bombCord:
                correct = correct+1
                


    title = Text(Point(165, 275), ("Correclty Placed Flags:   \n" + str(correct)+ " out of " + str(maxBomb)))
    title.draw(win)
    title.setTextColor("#009900")
    title.setSize(10)

    if mode == 3:
        title1.setText("You Set Off\nA Bomb!\n")


    else:
        title1.setText("You flagged\nAll The Bombs!")
        if winner == True:
            titl.setText("Enter Name >")

        Entry(Point(335, 285), 13)

        entry = Entry(Point(335, 300), 13).draw(win)
        
        mesg = Text(Point(335, 325), "Type name and <enter>")
        mesg.draw(win)
        mesg.setTextColor("#009900")
        mesg.setSize(9)
        
        rep = 0
        while rep == 0:
            key = win.getKey()
            if key == "Return":
                given = entry.getText()
                if len(given)>6:
                    mesg.setText("Name is too long")

                elif len(given)<2:
                    mesg.setText("Name is too short")

                else:

                    recordList = recordList[:len(recordList)-1]
                    placed = False
                    for i in recordList:
                        if placed == False:
                            recordTime = i.replace(":", " ").split()
                            recordTime = int(recordTime[0])*60 + int(recordTime[1])
                            if timeDur < int(recordTime):
                                placed = True
                                mint = math.floor((timeDur)/60)
                                sect = math.floor((timeDur)-mint*60)
                                if sect < 10:
                                    sect ="0"+ str(sect)
                                
                                recordList.insert(recordList.index(i), (str(str(mint) + ":" + str(sect)+" "+ str(given))))

                    place1.setText(("#1  " + recordList[0]))
                    place2.setText(("#2  " + recordList[1]))
                    place3.setText(("#3  " + recordList[2]))

                    rep = 1


        open('msHighScore.txt', 'w').close()
        for name in recordList:
            print("penis")
            with open("msHighScore.txt", "a") as f:
               f.write(name + "\n")

        titl.setText("Play Again")

    mouseCords = str(win.getMouse()).replace("Point(", "").replace(")", "").replace(",", "").split()
    mouseX = float(mouseCords[0])
    mouseY = float(mouseCords[1])
    
    Point(110, 305), Point(210, 330)
    if mouseX > 109 and mouseX < 211 and mouseY > 304 and mouseY < 331:
    
        win.close()
        main()
        quit()
        



def main():
    #make gui
    win = GraphWin("Cave Brooming", 600, 600)
    win.setBackground("#42a4d1")
    Rectangle(Point(50, 100), Point(450, 500)).draw(win).setFill("#999999")
    Rectangle(Point(48, 98), Point(452, 502)).draw(win).setFill("#101010")

    Rectangle(Point(50, 10), Point(450, 80)).draw(win).setFill("#999999")
    Rectangle(Point(55, 15), Point(445, 75)).draw(win).setFill("#101010")
    title = Text(Point(250, 45), "Cave Brooming")
    title.draw(win)
    title.setTextColor("#009900")
    title.setSize(36)
    
    for j in range(0, 20):
        for pointX in range(0, 20):
            pointY = j
            Rectangle(Point(50+20*pointX, 100+20*pointY), Point(70+20*pointX, 120+20*pointY)).draw(win).setFill("#999999")

    Rectangle(Point(470, 100), Point(570, 200)).draw(win).setFill("#999999")
    cir = Circle(Point(520, 150), 50)
    cir.draw(win)
    cir.setFill("#ef0000")
    title = Text(Point(520, 150), "Place\nFlag").draw(win).setSize(20)
    
    
    Rectangle(Point(470, 220), Point(570, 280)).draw(win).setFill("#999999")
    Rectangle(Point(475, 225), Point(565, 275)).draw(win).setFill("#101010")
    mesg = Text(Point(520, 250), "Click to Inspect")
    mesg.setTextColor("#009900")
    mesg.setSize(9)
    mesg.draw(win)

    Rectangle(Point(470, 300), Point(570, 380)).draw(win).setFill("#999999")
    Rectangle(Point(475, 305), Point(565, 375)).draw(win).setFill("#101010")
    boxMesg = Text(Point(520, 340), "Click Square\nTo Start")
    boxMesg.draw(win)
    boxMesg.setTextColor("#009900")
    boxMesg.setSize(10)
    

    Rectangle(Point(470, 400), Point(570, 500)).draw(win).setFill("#999999")
    Rectangle(Point(475, 405), Point(565, 495)).draw(win).setFill("#101010")
    text = Text(Point(520, 418), "High Scores:")
    recordList = []
    handle = open("msHighScore.txt")
    for line in handle:
        recordList.append(line)
    
    text.draw(win)
    text.setSize(10)
    text.setTextColor("#009900")
    text = Text(Point(520, 446), recordList[0])
    text.draw(win)
    text.setSize(10)
    text.setTextColor("#009900")
    text = Text(Point(520, 467), recordList[1])
    text.draw(win)
    text.setSize(10)
    text.setTextColor("#009900")
    text = Text(Point(520, 488), recordList[2])
    text.draw(win)
    text.setSize(10)
    text.setTextColor("#009900")

    Image(Point(520, 50), "msIcon.png").draw(win)

    Rectangle(Point(470, 520), Point(570, 580)).draw(win).setFill("#999999")
    Rectangle(Point(475, 525), Point(565, 575)).draw(win).setFill("#101010")
    statusText = Text(Point(520, 550), "STATUS\nSafe")
    statusText.draw(win)
    statusText.setTextColor("#009900")
    statusText.setSize(10)

    

    Rectangle(Point(50, 520), Point(450, 580)).draw(win).setFill("#999999")
    Rectangle(Point(55, 525), Point(445, 575)).draw(win).setFill("#101010")
    timeText = Text(Point(250, 550), "Time Recorder")
    timeText.draw(win)
    timeText.setSize(10)
    timeText.setTextColor("#009900")

    
    
 



    #initialization
    rep = 0
    while rep == 0:
        mouseCords = str(win.getMouse()).replace("Point(", "").replace(")", "").replace(",", "").split()
        mouseX = float(mouseCords[0])
        mouseY = float(mouseCords[1])

        if mouseX < 50:
            rep = 0

        elif mouseX >450:
            rep = 0

        elif mouseY <100:
            rep = 0

        elif mouseY >500:
            rep = 0

        else:
            rep = 1

    cordX = math.ceil((mouseX-50)/20)
    cordY = math.ceil((mouseY-100)/20)

    noBombZoneX = []
    noBombZoneY = []
    bombCordsX = []
    bombCordsY = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if cordX+i == 0 or cordX+i == 21 or cordY+j == 21 or cordY+j == 0:
                None
            else:
                noBombZoneX.append(cordX+i)
                noBombZoneY.append(cordY+j)


            

    maxBomb = 50# number of bombs
    numOfBomb = 0

    while numOfBomb < maxBomb:
        poop = 0
        randX = random.randint(1, 20)
        randY = random.randint(1, 20)
        for i in range(len(noBombZoneX)):
            if randX == noBombZoneX[i] and randY == noBombZoneY[i]:
                poop = 1
        
        for i in range(len(bombCordsX)):
            if randX == bombCordsX[i] and randY == bombCordsY[i]:
                poop = 1

        if poop == 0:
            numOfBomb = numOfBomb + 1
            bombCordsX.append(randX)
            bombCordsY.append(randY)


            

    
    for i in range(len(bombCordsX)):
        x = bombCordsX[i]
        y = bombCordsY[i]
        #Rectangle(Point(50+20*(x-1), 100+20*(y-1)), Point(70+20*(x-1), 120+20*(y-1))).draw(win).setFill("#900999")

    numberSpaces = dict()#key: cords, val: number
    
    for d in range(len(bombCordsX)):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                tempCords = tuple()
                poop = 0
                if i == 0 and j == 0:
                    poop = 1

                else:
                    for k in range(len(bombCordsX)):
                        if bombCordsX[d]+i == bombCordsX[k] and bombCordsY[d]+j == bombCordsY[k]:
                            poop = 1
                if poop == 0:
                    #Rectangle(Point(50+20*(bombCordsX[d]+i-1), 100+20*(bombCordsY[d]+j-1)), Point(70+20*(bombCordsX[d]+i-1), 120+20*(bombCordsY[d]+j-1))).draw(win).setFill("#90bb99")
                    
                    bombCounter = 0
                    for o in [-1, 0, 1]:
                        for p in [-1, 0, 1]:
                            for k in range(0, len(bombCordsX)):
                                if bombCordsX[d]+i+o == bombCordsX[k] and bombCordsY[d]+j+p == bombCordsY[k]:
                                    bombCounter = bombCounter+1

                    #Text((Point(60+20*(bombCordsX[d]+i-1), 110+20*(bombCordsY[d]+j-1))), str(bombCounter)).draw(win).setSize(10)
                    tempCords = ( bombCordsX[d]+i,bombCordsY[d]+j )
                    numberSpaces[tempCords] = bombCounter

    

    goodCords = dict()
    borderCords = dict()

    stuckCords = dict()

    tempCords = ( cordX, cordY )
    goodCords[tempCords] = 1
    Rectangle(Point(50+20*(cordX-1), 100+20*(cordY-1)), Point(70+20*(cordX-1), 120+20*(cordY-1))).draw(win).setFill("#FFFFFF")

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if cordX+i == 0 or cordX+i == 21 or cordY+j == 21 or cordY+j == 0:
                None
            else:
            
                if (i == 0 and j == 0)==False:
                    tempCords = ( cordX+i, cordY+j)
                    if tempCords in numberSpaces:
                        stuckCords[tempCords] = 1
                        Rectangle(Point(50+20*(cordX+i-1), 100+20*(cordY+j-1)), Point(70+20*(cordX+i-1), 120+20*(cordY+j-1))).draw(win).setFill("#444444")

                    else:
                        borderCords[tempCords] = 1
                        Rectangle(Point(50+20*(cordX+i-1), 100+20*(cordY+j-1)), Point(70+20*(cordX+i-1), 120+20*(cordY+j-1))).draw(win).setFill("#0000ff")

    while len(borderCords) > 0:
        
        BC = borderCords.copy()
        for d in BC:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if (i == 0 and j == 0)==False:
                        poop = 0#0 make it border
                        xCord = d[0]+i
                        yCord = d[1]+j
                        dCord = (xCord, yCord)
                        for k in goodCords:
                            if dCord == k:
                                poop = 1#1 do nothing
                        for k in borderCords:
                            if dCord == k:
                                poop = 1
                        for k in numberSpaces:
                            if dCord == k:
                                poop = 2#make stuck
                        for k in stuckCords:
                            if dCord == k:
                                poop = 1#do nothing

                        if xCord > 20 or xCord < 1 or yCord > 20 or yCord < 1:
                            poop = 1
                                
                        if poop == 0:
                            borderCords[dCord] = 1
                            Rectangle(Point(50+20*(xCord-1), 100+20*(yCord-1)), Point(70+20*(xCord-1), 120+20*(yCord-1))).draw(win).setFill("#0000ff")

                        if poop == 2:
                            stuckCords[dCord] = 1
                            Rectangle(Point(50+20*(xCord-1), 100+20*(yCord-1)), Point(70+20*(xCord-1), 120+20*(yCord-1))).draw(win).setFill("#444444")

            goodCords[d] = 1
            Rectangle(Point(50+20*(d[0]-1), 100+20*(d[1]-1)), Point(70+20*(d[0]-1), 120+20*(d[1]-1))).draw(win).setFill("#FFFFFF")
            del borderCords[d]

    for cords in stuckCords:
        x = cords[0]
        y = cords[1]
        Text((Point(60+20*(x-1), 110+20*(y-1))), str(numberSpaces[cords])).draw(win).setSize(10)



        
    mode = 0#chck bombs
    

    flagedCords = dict()
    bombCords = dict()
    numOfFlags = 0
    boxMesg.setText("Bombs:       \n             " + str(maxBomb) + "\nFlags:          \n              " + str(numOfFlags))
    startHour = int(str(str(time.ctime((time.time()))).replace(":", " ").split()[3:4]).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))
    startMin = str(str(time.ctime((time.time()))).replace(":", " ").split()[4:5]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
    startSec = str(str(time.ctime((time.time()))).replace(":", " ").split()[5:6]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
    clock = time.clock()
    amPm = 'am'
    if startHour>11:
        amPm = 'pm'
        if startHour == 12:
            None
        else:
            startHour = startHour-12

    timeText.setText(" ")

    startTimeText = Text(Point(100, 550), (str("Start Time:\n"+str(startHour)+ ":"+ startMin+ ":"+ startSec+" " +amPm)))
    startTimeText.draw(win)
    startTimeText.setSize(10)
    startTimeText.setTextColor("#009900")

    endTimeText = Text(Point(200, 550), "End Time:\nUnknown...")
    endTimeText.draw(win)
    endTimeText.setSize(10)
    endTimeText.setTextColor("#009900")

    durTimeText = Text(Point(350, 550), "Time Duration:\n00 Minutes : 00 Seconds")
    durTimeText.draw(win)
    durTimeText.setSize(10)
    durTimeText.setTextColor("#009900")










    for i in range(len(bombCordsX)):
        bombCords[(bombCordsX[i], bombCordsY[i])] = 1

    while True:
        correct = 0
        for flag in flagedCords:
            for bomb in bombCords:
                if bomb == flag:
                    correct = correct + 1
        if correct == maxBomb:
            mode = 4
                    
        
        mint = math.floor((time.clock()-clock)/60)
        sect = math.floor((time.clock()-clock)-mint*60)
        durTimeText.setText("Time Duration:\n" + str(mint)+" Minute(s) : "+str(sect)+" Second(s)")

        
        if mode == 0:
            mouseCords = str(win.getMouse()).replace("Point(", "").replace(")", "").replace(",", "").split()
            mouseX = float(mouseCords[0])
            mouseY = float(mouseCords[1])
            cordX = math.ceil((mouseX-50)/20)
            cordY = math.ceil((mouseY-100)/20)

            if cordY < 6 and cordY > 0 and cordX > 21 and cordX < 27:
                mode = 1#flag mode
                cir.setFill("#bb0000")
                mesg.setText("Click to place or\nremove Flag")

            if cordY < 21 and cordY > 0 and cordX > 0 and cordX < 21:
                peep = 1

                for i in bombCords:
                    if cordX == i[0] and cordY == i[1]:
                        Rectangle(Point(50+20*(cordX-1), 100+20*(cordY-1)), Point(70+20*(cordX-1), 120+20*(cordY-1))).draw(win).setFill("#ffff00")
                        mode = 3#game over
                        statusText.setText("STATUS\nDANGER")
                        mesg.setText("You hit\na bomb!")
                        peep = 0



                for i in numberSpaces:
                    if cordX == i[0] and cordY == i[1]:
                        Rectangle(Point(50+20*(cordX-1), 100+20*(cordY-1)), Point(70+20*(cordX-1), 120+20*(cordY-1))).draw(win).setFill("#444444")
                        Text((Point(60+20*(cordX-1), 110+20*(cordY-1))), str(numberSpaces[(cordX, cordY)])).draw(win).setSize(10)
                        peep = 0

                if peep == 1:

                    Rectangle(Point(50+20*(cordX-1), 100+20*(cordY-1)), Point(70+20*(cordX-1), 120+20*(cordY-1))).draw(win).setFill("#ffffff")

                    borderCords = dict()
                    borderCords[(cordX, cordY)] = 1
                    goodCords  = dict()
                    stuckCords  = dict()

                    while len(borderCords) > 0:
                        BC = borderCords.copy()
                        for d in BC:
                            for i in [-1, 0, 1]:
                                for j in [-1, 0, 1]:
                                    if (i == 0 and j == 0)==False:
                                        poop = 0#0 make it border
                                        xCord = d[0]+i
                                        yCord = d[1]+j
                                        dCord = (xCord, yCord)
                                        for k in goodCords:
                                            if dCord == k:
                                                poop = 1#1 do nothing
                                        for k in borderCords:
                                            if dCord == k:
                                                poop = 1
                                        for k in numberSpaces:
                                            if dCord == k:
                                                poop = 2#make stuck
                                        for k in stuckCords:
                                            if dCord == k:
                                                poop = 1#do nothing

                                        if xCord > 20 or xCord < 1 or yCord > 20 or yCord < 1:
                                            poop = 1
                                                
                                        if poop == 0:
                                            borderCords[dCord] = 1
                                            Rectangle(Point(50+20*(xCord-1), 100+20*(yCord-1)), Point(70+20*(xCord-1), 120+20*(yCord-1))).draw(win).setFill("#0000ff")

                                        if poop == 2:
                                            stuckCords[dCord] = 1
                                            Rectangle(Point(50+20*(xCord-1), 100+20*(yCord-1)), Point(70+20*(xCord-1), 120+20*(yCord-1))).draw(win).setFill("#444444")

                            goodCords[d] = 1
                            Rectangle(Point(50+20*(d[0]-1), 100+20*(d[1]-1)), Point(70+20*(d[0]-1), 120+20*(d[1]-1))).draw(win).setFill("#FFFFFF")
                            del borderCords[d]

                    for cords in stuckCords:
                        x = cords[0]
                        y = cords[1]
                        Text((Point(60+20*(x-1), 110+20*(y-1))), str(numberSpaces[cords])).draw(win).setSize(10)







                        
                        
                    

        elif mode == 1:
            mouseCords = str(win.getMouse()).replace("Point(", "").replace(")", "").replace(",", "").split()
            mouseX = float(mouseCords[0])
            mouseY = float(mouseCords[1])
            cordX = math.ceil((mouseX-50)/20)
            cordY = math.ceil((mouseY-100)/20)
            reject = 0
            for i in goodCords:
                if cordX == i[0] and cordY == i[1]:
                    reject = 1
            for i in stuckCords:
                if cordX == i[0] and cordY == i[1]:
                    reject = 1

            for i in flagedCords:
                if cordX == i[0] and cordY == i[1]:
                    reject = 2

                    
            if cordY < 6 and cordY > 0 and cordX > 21 and cordX < 27:
                reject = 1
                mode = 0
                cir.setFill("#ef0000")
                mesg.setText("Click to Inspect")

            if cordX > 20 or cordX < 1 or cordX > 20 or cordX < 1:
                mode = 0
                cir.setFill("#ef0000")
                mesg.setText("Click to Inspect")

                reject = 1

            if reject == 0:
                #flagging it
                numOfFlags = numOfFlags + 1
                boxMesg.setText("Bombs:       \n             " + str(maxBomb) + "\nFlags:          \n              " + str(numOfFlags))
                    
                Rectangle(Point(50+20*(cordX-1), 100+20*(cordY-1)), Point(70+20*(cordX-1), 120+20*(cordY-1))).draw(win).setFill("#ee0000")
                mode = 0
                cir.setFill("#ef0000")
                mesg.setText("Click to Inspect")
                flagedCords[(cordX,cordY)] = 1

            if reject == 2:
                #unflagging it
                numOfFlags = numOfFlags - 1
                boxMesg.setText("Bombs:       \n             " + str(maxBomb) + "\nFlags:          \n              " + str(numOfFlags))
                    
                Rectangle(Point(50+20*(cordX-1), 100+20*(cordY-1)), Point(70+20*(cordX-1), 120+20*(cordY-1))).draw(win).setFill("#999999")
                mode = 0
                cir.setFill("#ef0000")
                del flagedCords[(cordX,cordY)]
                mesg.setText("Click to Inspect")


        
 
            
        elif mode > 2:

            endHour = int(str(str(time.ctime((time.time()))).replace(":", " ").split()[3:4]).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))
            endMin = str(str(time.ctime((time.time()))).replace(":", " ").split()[4:5]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            endSec = str(str(time.ctime((time.time()))).replace(":", " ").split()[5:6]).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
            mint = math.floor((time.clock()-clock)/60)
            sect = math.floor((time.clock()-clock)-mint*60)


            amPm = 'am'
            if endHour>11:
                amPm = 'pm'
                if endHour == 12:
                    None
                else:
                    endHour = endHour-12
            endTimeText.setText((str("End Time:\n"+str(endHour)+ ":"+ endMin+ ":"+ endSec+" " +amPm)))
            gameOver(mode, (time.clock()-clock), win, flagedCords, bombCords, maxBomb)



    #end of main

main()
