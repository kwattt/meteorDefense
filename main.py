import pygame as p
import numpy as np
import meteors as m
import visuals as v
#from pypresence import Presence
#client_id = '702792332201820251'
#   RPC = Presence(client_id)  # Initialize the client class
#    RPC.connect()
#    print(RPC.update(state="Test", \
#        details="Test2!"))  # Set the presence

class Settings:
    #default Settings

    screenX = 400
    screenY = 600
    gameStatus = 0

    win = None
    clock = None

    currentFrame = 0

    maxFrames = 60
    Vel = 0
    spawnFrame = 0
    frameResult = 0

    meteor_spawnRate = 0.55 # Meteors / seg
    meteor_spawnDif = 0.15 # Meteor random spawn delay

    healthPoints = 100

def initial_config():
    p.init()

    game.spawnFrame = 0
    game.meteor_spawnRate = 0.55
    game.meteor_spawnDif = 0.12

    # Inicio de partida se establecen los frames % spawn < También al cambiar FPS.
    game.spawnFrame = int(game.meteor_spawnRate*game.maxFrames)

    game.win = p.display.set_mode((game.screenX, game.screenY))
    game.clock = p.time.Clock()

def Generate():
    if game.gameStatus == 200:
        return

    cFrames = game.clock.get_fps()
    if cFrames == 0:
        game.Vel = 1/(120*2.0/120)
    else:
        game.Vel = 1/(cFrames*2.0/120)


    game.frameResult = game.maxFrames*game.meteor_spawnRate
    if game.currentFrame == game.frameResult:
        game.spawnFrame = game.frameResult + \
            int(np.random.uniform(0.0, game.meteor_spawnDif)*game.maxFrames)

    if game.spawnFrame == game.currentFrame:
        game.currentFrame = 0
        sel = 0
        bspeed = 0
        if game.gameStatus == 1:
            if np.random.randint(0, 3) == 0:
                sel = 1
                bspeed = np.random.uniform(-0.2, 0.8)
            else:
                sel = 0

        allMeteors.append(m.Meteor(sel, \
            game.Vel*(np.random.uniform(2.0, 4.4-bspeed)), game.screenX))

    game.currentFrame += 1

def checkHealth():

    if game.healthPoints <= 0:
        game.gameStatus = 200

def gameMode1():

    cannonDegrees = 0
    Cannon = v.Cannon(game.screenY)
    bg = v.bg()
    mt = v.Mountain(game.screenX, game.screenY)
    game.healthPoints = 100

    while game.gameStatus == 1:
        mousePos = (0, 0)

        for e in p.event.get():
            if e.type == p.QUIT:
                game.gameStatus = -1

            elif e.type == p.MOUSEBUTTONDOWN:
                mousePos = p.mouse.get_pos()

        # Assets generales.

        bg.Draw(game.win)
        mt.Draw(game.win)
        Cannon.Draw(game.win, cannonDegrees)

        # Control de FPS
        game.clock.tick(game.maxFrames)

        # Generar meteoros
        Generate()

        # Loop Projectiles.

        for pr in v.Proyectile.getProjectiles():
            pr.Draw(game.win, cannonDegrees)
            pr.UpdatePos()
            if pr.kme:
                allProjectiles.remove(pr)
                del pr

        # Loop meteoros.
        for met in m.Meteor.getMeteors():
            met.UpdatePos()
            met.Draw(game.win, hitbox=False)

            if mousePos[0] > 0:
                mx, my = mousePos
                x, y = met.pos
                if mx < x + met.hitbox[2]/2 and mx > x - met.hitbox[2]/2:
                    if my < y + met.hitbox[3]/2 and my > y - met.hitbox[3]/2:

                        shootPos = (Cannon.xpos-(float(Cannon.size[1]/2 + 1.0) \
                            * np.cos(np.radians(-1.0 * cannonDegrees -90))), \
                            Cannon.ypos-(float(Cannon.size[1]/2 + 1.0) \
                            * np.sin(np.radians(-1.0* cannonDegrees - 90))))

                        cannonDegrees = Cannon.AngleToMouse(game.screenY)
                        allProjectiles.append(v.Proyectile(shootPos[0], shootPos[1], \
                            met.pos[0], met.pos[1], cannonDegrees))

                        allMeteors.remove(met)
                        del met
                        continue

            #coll mountain
            if met.pos[1]+met.hitbox[3]/2 > mt.hitbox[1]:
                game.healthPoints -= met.damage
                allMeteors.remove(met)
                del met

                checkHealth()

        v.showFps(game.win, game.clock)

        p.display.flip()

        if game.gameStatus == 200:
            print("Perdiste!")

def game_menu():
    mousePos = (0, 0)

    while game.gameStatus != -1:
        game.gameStatus = 0

        # Menú improvisado

        for e in p.event.get():
            if e.type == p.QUIT:
                game.gameStatus = -1

            elif e.type == p.MOUSEBUTTONDOWN:
                mousePos = p.mouse.get_pos()

        game.win.fill((0,0,0))
        playText = p.font.SysFont("Ubuntu", 15).render(str("Jugar"), \
            True, p.Color("goldenrod"))

        rectHb = (game.screenX/2 - 50, game.screenY/2, 100, 100)
        p.draw.rect(game.win, (255, 255, 255), rectHb)
        game.win.blit(playText, ((game.screenX/2 - 50), game.screenY/2))

        if mousePos[0] < rectHb[0] + rectHb[2]/2 and mousePos[0] > rectHb[0] - rectHb[2]/2:
            if mousePos[1] < rectHb[1] + rectHb[3]/2 and mousePos[1] > rectHb[1] - rectHb[3]/2:

                game.gameStatus = 1

        mousePos = (0, 0)

        p.display.flip()

        if game.gameStatus == 1:
            # ir a func del modo
            gameMode1()


#gameInit

# Load Settings
game = Settings()

allMeteors = []
allProjectiles = []

# Establecer configuración

initial_config()

# Ir al menú

game_menu()
