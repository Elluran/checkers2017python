import pygame, sys




def render(desk):
    surface = pygame.display.get_surface()
    surface.fill(pygame.Color("white"))

    for i in range(0,8,2):
        for e in range(1,8,2):
            pygame.draw.rect(surface, pygame.Color("#45362E"), (i*100, e*100, 100, 100))
            pygame.draw.rect(surface, pygame.Color("#45362E"), ((i+1) * 100, (e-1) * 100, 100, 100))


    for i in range(8):
        for e in range(8):
            desk[i][e].render()

    pygame.draw.line(surface, pygame.Color("black"), (800,0), (800,800), 1)
    pygame.display.flip()

def dia(coords1, coords2, desk):
    x1, y1 = int(coords1[0]), int(coords1[1])
    x2, y2 = int(coords2[0]), int(coords2[1])
    print(coords2,coords1)

    while x1 != x2:
        if x1 < x2:
            x1 += 1
        if y1 < y2:
            y1 += 1
        if x2 < x1:
             x1 -= 1
        if y2 < y1:
             y1 -= 1
        desk[y1][x1].color = "null"

class checker():

    def __init__(self, color, x, y):
        self.color = color
        self.texture = pygame.transform.smoothscale(pygame.image.load("res/pieces2.png").convert_alpha(),(300,200))
            # self.render()
        self.x = x
        self.y = y
        self.surface = pygame.display.get_surface()
        self.selected = 0
        self.turn = 0
        self.last = (0,0)
        self.d = 0

    def render(self):
        if self.color == "black":
            if self.d == 0:
                self.rect = pygame.Rect(0, 0, 100, 100)
            else:
                self.rect = pygame.Rect(0, 100, 100, 100)
        elif self.color == "white":
            if self.d == 0:
                self.rect = pygame.Rect(100, 0, 100, 100)
            else:
                self.rect = pygame.Rect(100, 100, 100, 100)

        if self.color != "null":
            self.surface.blit(self.texture, (self.x*100,self.y*100), self.rect)
        if self.selected == 1:
            self.select()

    def select(self):
        self.surface.blit(self.texture, (self.x * 100, self.y * 100), pygame.Rect(200,0,100,100))

    def onclick(self, desk, obj):


        def clear():
            for i in range(8):
                for e in range(8):
                    desk[i][e].selected = 0
                    desk[i][e].turn = 0

        if self.turn == 0:
            clear()

        if obj.lock == 0:

            if obj.player == self.color:
                self.selected = 1
                if self.d == 0:
                    if self.color == "white":
                        if self.x > 0:
                            if desk[self.y - 1][self.x - 1].color == "null":
                                desk[self.y - 1][self.x - 1].selected = 1
                                desk[self.y - 1][self.x - 1].turn = 1
                                desk[self.y - 1][self.x - 1].last = (self.x, self.y)
                        if self.x < 7:
                            if desk[self.y - 1][self.x + 1].color == "null":
                                desk[self.y - 1][self.x + 1].selected = 1
                                desk[self.y - 1][self.x + 1].turn = 1
                                desk[self.y - 1][self.x + 1].last = (self.x, self.y)
                    if self.color == "black":
                        if self.x > 0:
                            if desk[self.y + 1][self.x - 1].color == "null":
                                desk[self.y + 1][self.x - 1].selected = 1
                                desk[self.y + 1][self.x - 1].turn = 1
                                desk[self.y + 1][self.x - 1].last = (self.x, self.y)
                        if self.x < 7:
                            if desk[self.y + 1][self.x + 1].color == "null":
                                desk[self.y + 1][self.x + 1].selected = 1
                                desk[self.y + 1][self.x + 1].turn = 1
                                desk[self.y + 1][self.x + 1].last = (self.x, self.y)
                else:
                    def dunnofunc():
                        desk[tmpy][tmpx].selected = 1
                        desk[tmpy][tmpx].turn = 1
                        desk[tmpy][tmpx].last = (self.x, self.y)

                    tmpx, tmpy = self.x + 1, self.y - 1
                    while tmpy >= 0 and tmpx <= 7 and desk[tmpy][tmpx].color == "null":
                        dunnofunc()
                        tmpx, tmpy = tmpx + 1, tmpy - 1

                    tmpx, tmpy = self.x - 1, self.y - 1
                    while tmpy >= 0 and tmpx >= 0 and desk[tmpy][tmpx].color == "null":
                        dunnofunc()
                        tmpx, tmpy = tmpx - 1, tmpy - 1

                    tmpx, tmpy = self.x + 1, self.y + 1
                    while tmpy <= 7 and tmpx <= 7 and desk[tmpy][tmpx].color == "null":
                        dunnofunc()
                        tmpx, tmpy = tmpx + 1, tmpy + 1

                    tmpx, tmpy = self.x - 1, self.y + 1
                    while tmpy <= 7 and tmpx >= 0 and desk[tmpy][tmpx].color == "null":
                        dunnofunc()
                        tmpx, tmpy = tmpx - 1, tmpy + 1

            if self.color == "null" and self.turn and self.selected:
                self.color = obj.player
                x, y = self.last
                desk[y][x].color = "null"
                self.d = desk[y][x].d
                desk[y][x].d = 0
                clear()
                obj.nextturn()
                return obj.player
        else:
            if (str(self.x) + str(self.y)) in obj.moves.keys():
                self.selected = 1
                obj.latest = (str(self.x) + str(self.y))
                for i in obj.moves[str(self.x) + str(self.y)]:
                    x,y = int(i[0]), int(i[1])
                    desk[y][x].selected = 1


            elif obj.latest != "null" and (str(self.x) + str(self.y)) in obj.moves[obj.latest]:
                x, y = int(obj.latest[0]), int(obj.latest[1])

                obj.lock = 0
                desk[self.y][self.x].color = obj.player
                desk[self.y][self.x].d = desk[y][x].d
                desk[y][x].d = 0
                dia((str(self.x) + str(self.y)), obj.latest, desk)
                desk[self.y][self.x].check(desk,obj)
                if obj.lock == 0:
                    obj.nextturn()
                    obj.moves.clear()
                    obj.latest = "null"
                    print("unclocked")
                return obj.player

            else:
                obj.latest = "null"
                return obj.player

        return obj.player

    def check(self, desk, obj):
        if self.d == 0:
            if self.x <= 5 and self.color == obj.player and self.y >= 2:
                if self.color != desk[self.y - 1][self.x + 1].color and desk[self.y - 1][self.x + 1].color != "null":
                    if desk[self.y - 2][self.x + 2].color =="null":
                        desk[self.y][self.x].selected = 1
                        obj.mov(str(self.x)+str(self.y), str(self.x+2) + str(self.y-2))
                        obj.lock = 1
            if self.x >= 2 and self.color == obj.player and self.y >= 2:
                if self.color != desk[self.y - 1][self.x - 1].color and desk[self.y - 1][self.x - 1].color != "null":
                    if desk[self.y - 2][self.x - 2].color =="null":
                        desk[self.y][self.x].selected = 1
                        obj.mov(str(self.x)+str(self.y), str(self.x-2) + str(self.y-2))
                        obj.lock = 1
            if self.x <= 5 and self.color == obj.player and self.y <= 5:
                if self.color != desk[self.y + 1][self.x + 1].color and desk[self.y + 1][self.x + 1].color != "null":
                    if desk[self.y + 2][self.x + 2].color =="null":
                        desk[self.y][self.x].selected = 1
                        obj.mov(str(self.x)+str(self.y), str(self.x + 2) + str(self.y + 2))
                        obj.lock = 1
            if self.x >= 2 and self.color == obj.player and self.y <= 5:
                if self.color != desk[self.y + 1][self.x - 1].color and desk[self.y + 1][self.x - 1].color != "null":
                    if desk[self.y + 2][self.x - 2].color =="null":
                        desk[self.y][self.x].selected = 1
                        obj.mov(str(self.x)+str(self.y), str(self.x-2) + str(self.y + 2))
                        obj.lock = 1
        else:
            if self.x <= 5 and self.color == obj.player and self.y >= 2:
                tmpx, tmpy = self.x + 1, self.y - 1
                while tmpx <= 6 and tmpy >= 1 and desk[tmpy][tmpx].color == "null":
                    tmpx, tmpy = tmpx + 1, tmpy - 1
                if desk[tmpy][tmpx].color != self.color and desk[tmpy][tmpx].color != "null":
                    tmpx, tmpy = tmpx + 1, tmpy - 1
                    while tmpx <= 7 and tmpy >= 0 and desk[tmpy][tmpx].color == "null":
                        desk[self.y][self.x].selected = 1
                        obj.lock = 1
                        obj.mov(str(self.x) + str(self.y), str(tmpx) + str(tmpy))
                        tmpx, tmpy = tmpx + 1, tmpy - 1

            if self.x >= 2 and self.color == obj.player and self.y >= 2:
                tmpx, tmpy = self.x - 1, self.y - 1
                while tmpx >= 1 and tmpy >= 1 and desk[tmpy][tmpx].color == "null":
                    tmpx, tmpy = tmpx - 1, tmpy - 1
                if desk[tmpy][tmpx].color != self.color and desk[tmpy][tmpx].color != "null":
                    tmpx, tmpy = tmpx - 1, tmpy - 1
                    while tmpx >=0 and tmpy >= 0 and desk[tmpy][tmpx].color == "null":
                        desk[self.y][self.x].selected = 1
                        obj.lock = 1
                        obj.mov(str(self.x) + str(self.y), str(tmpx) + str(tmpy))
                        tmpx, tmpy = tmpx - 1, tmpy - 1

            if self.x <= 5 and self.color == obj.player and self.y <= 5:
                tmpx, tmpy = self.x + 1, self.y + 1
                while tmpx <= 6 and tmpy <= 6 and desk[tmpy][tmpx].color == "null":
                    tmpx, tmpy = tmpx + 1, tmpy + 1
                if desk[tmpy][tmpx].color != self.color and desk[tmpy][tmpx].color != "null":
                    tmpx, tmpy = tmpx + 1, tmpy + 1
                    while tmpx <= 7 and tmpy <= 7 and desk[tmpy][tmpx].color == "null":
                        desk[self.y][self.x].selected = 1
                        obj.lock = 1
                        obj.mov(str(self.x) + str(self.y), str(tmpx) + str(tmpy))
                        tmpx, tmpy = tmpx + 1, tmpy + 1

            if self.x >= 2 and self.color == obj.player and self.y <= 5:
                tmpx, tmpy = self.x - 1, self.y + 1
                while tmpx >= 1 and tmpy <= 6 and desk[tmpy][tmpx].color == "null":
                    tmpx, tmpy = tmpx - 1, tmpy + 1
                if desk[tmpy][tmpx].color != self.color and desk[tmpy][tmpx].color != "null":
                    tmpx, tmpy = tmpx - 1, tmpy + 1
                    while tmpx >=0 and tmpy <= 7 and desk[tmpy][tmpx].color == "null":
                        desk[self.y][self.x].selected = 1
                        obj.lock = 1
                        obj.mov(str(self.x) + str(self.y), str(tmpx) + str(tmpy))
                        tmpx, tmpy = tmpx - 1, tmpy + 1

class gamedata():
    lock = 0
    player = "white"
    moves = {}
    latest = "null"

    def mov(self, id, info):
        if id not in self.moves.keys():
            self.moves[id] = [info]
        else:
            self.moves[id].append(info)

    def nextturn(self):
        self.player = "white" if self.player == "black" else "black"

def game():

    gamedataobj = gamedata()
    desk = [[checker("null", i, e) for i in range(0, 8)] for e in range(0, 8)]

    for i in range (0,8,2):
        desk[7][i] = checker("white", i, 7)
        desk[5][i] = checker("white", i, 5)
        desk[6][i+1] = checker("white", i+1, 6)
    for i in range (0,8,2):
        desk[0][i+1] = checker("black", i+1, 0)
        desk[1][i] = checker("black", i, 1)
        desk[2][i+1] = checker("black", i+1, 2)


    render(desk)

    def vdamke():
        for i in desk[0]:
            if i.color == "white":
                i.d = 1
        for i in desk[7]:
            if i.color == "black":
                i.d = 1

    def cleardeskinfo():
        for i in range(8):
            for e in range(8):
                desk[i][e].check(desk, gamedataobj)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                if mousex <= 800:
                    turn = gamedataobj.player
                    desk[mousey//100][mousex//100].onclick(desk, gamedataobj)
                    if turn != gamedataobj.player:
                        cleardeskinfo()
                    vdamke()
                    print(gamedataobj.moves, gamedataobj.latest)


                render(desk)
            elif event.type == pygame.QUIT: sys.exit()
