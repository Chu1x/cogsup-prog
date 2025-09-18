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

step_size = 10

while right_square.position[0] - left_square.position[0] > 50:
    left_square.move((5, 0))
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)
    #exp.clock.wait(20)

exp.clock.wait(20)

while right_square.position[0] - left_square.position[0] < 400:

    right_square.move((5, 0))
    right_square.present(clear=True, update=False)
    left_square.present(clear=False, update=True)
    #exp.clock.wait(20)

exp.keyboard.wait()

control.end()

