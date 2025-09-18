from expyriment import design, control, stimuli
import expyriment

expyriment.control.defaults.initialise_delay = 0 # No countdown
expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message

exp = design.Experiment(name = "two_squares")
control.initialize(exp)

left_square = stimuli.Rectangle(
    size=(50, 50),colour=(255, 0, 0), position=(-400, 0)
)
right_square = stimuli.Rectangle(
    size=(50, 50), colour=(0, 255, 0), position=(0, 0)
)


control.start(subject_id=1)

left_square.present(clear=True, update=False)
right_square.present(clear=False, update=True)
exp.clock.wait(1000)

gap = 3
speed = 1
step_size = 5

while right_square.position[0] - left_square.position[0] > 50 + gap:
    left_square.move((step_size, 0))
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)

exp.clock.wait(20)

while right_square.position[0] - left_square.position[0] < 400:

    right_square.move((step_size*speed, 0))
    right_square.present(clear=True, update=False)
    left_square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()

