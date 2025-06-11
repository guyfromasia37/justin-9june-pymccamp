# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER


def teleport():
    agent.teleport_to_player()
player.on_chat("tp", teleport)

def turnleft():
    agent.turn(LEFT)
player.on_chat("tl", turnleft)

def turnright():
    agent.turn(RIGHT)
    
player.on_chat("tr", turnright)

def moveit(steps):
    agent.move(FORWARD, 1)
player.on_chat("fwd", moveit)


def moveUp(steps):
    agent.move(UP, steps)
player.on_chat("jump", moveUp)


def mvdown(steps):
    agent.move(DOWN,steps)
player.on_chat("DOWN", mvdown)


def obby1():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 3)
    agent.move(FORWARD, 7)
    agent.move(DOWN, 3)


player.on_chat("move", obby1)



def obby2():
    agent.move(UP, 3)
    agent.move(FORWARD, 7)
    agent.move(DOWN, 3)
    agent.move(FORWARD, 3)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 4)


player.on_chat("move2", obby2)

def treegulp(height):
    for i in range(height):
        agent.move(UP, 1)
        agent.destroy(FORWARD)
        agent.collect_all()
player.on_chat("t", treegulp)


def getout():
    agent.destroy(FORWARD)
    agent.destroy(LEFT)
    agent.destroy(RIGHT)
    agent.destroy(UP)
    agent.destroy(DOWN)
    agent.collect_all()
    agent.move(FORWARD, 1)
player.on_chat("m", getout)