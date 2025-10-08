from expyriment import design, control, stimuli
# from expyriment.misc.constants import C_WHITE, C_BLACK
from expyriment.misc.constants import *


""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(side):
    instructions = f"""This is the blind spot test for your {side.upper()} eye.
    
    Please:
    Cover your {'right' if side.lower() == 'l' else 'left'} eye.
    Fixate on the + symbol.
    Use arrow keys to move the circle.
    Press 1 to make it smaller, 2 to make it larger.
    When the circle disappears (in your blind spot), press SPACE to continue.
    
    """
    stimuli.TextScreen("Instructions", instructions).present()
    exp.keyboard.wait(keys=[K_SPACE])

#------------------left or right fixation------------------

    fixation_pos = [300, 0] if side.lower() == 'l' else [-300, 0]
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=fixation_pos)
    fixation.preload()
    
    # side = {"left"}

    radius = 75
    circle_pos = [-300, 0] if side.lower() == 'l' else [300, 0]
    circle = make_circle(radius, circle_pos)

    # fixation.present(True, False)
    # circle.present(False, True)

    # exp.keyboard.wait(keys=[K_SPACE])

    while True:
        exp.screen.clear()

        fixation.present(True, False)
        circle.present(False, True)

        key = exp.keyboard.check(keys=[K_LEFT, K_RIGHT, K_UP, K_DOWN, K_1, K_2, K_SPACE])
        if key is None:
            continue

        x, y = circle.position

        if key == K_LEFT:
            x -= 10
        elif key == K_RIGHT:
            x += 10
        elif key == K_UP:
            y += 10
        elif key == K_DOWN:
            y -= 10
        elif key == K_1:
            radius = max(5, radius - 5)
            circle = make_circle(radius, (x, y))
        elif key == K_2:
            radius += 5
            circle = make_circle(radius, (x, y))
        elif key == K_SPACE:
            break

        circle.position = (x, y)







control.start(subject_id=1)

# text_screen.present(clear=True, update=True)
run_trial('L')
run_trial('R')


# exp.keyboard.wait(keys=[K_DOWN, K_UP, K_LEFT, K_RIGHT])


    
control.end()