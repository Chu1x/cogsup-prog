from expyriment import design, control, stimuli
import random

def load(stims):
    for stim in stims:
        stim.preload()
    pass

radius = 150       
low_ISI = 50
high_ISI = 500
display_dur = 500
bg_color = (0, 0, 0)
circle_color = (255, 255, 255)
tag_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

def timed_draw(stims):
    t0 = exp.clock.time
    for stim in stims:
        stim.present(clear=False, update=False)
    t1 = exp.clock.time
    return t1 - t0


def present_for(stims, t=1000):
    dt = timed_draw(stims)
    # for stim in stims:
    #     stim.present(clear=True, update=False)
    exp.clock.wait(max(0, t - dt))


def make_circles(with_tags=False):
    """Create frames for Ternus illusion: frame1 = left+center, frame2 = center+right"""
    colors = tag_colors if with_tags else [circle_color]*3

    # positions
    left = -radius
    center = 0
    right = radius

    # frame1: left + center
    frame1 = [stimuli.Circle(40, colour=colors[0], position=(left,0)),
              stimuli.Circle(40, colour=colors[1], position=(center,0))]

    # frame2: center + right
    frame2 = [stimuli.Circle(40, colour=colors[1], position=(center,0)),
              stimuli.Circle(40, colour=colors[2], position=(right,0))]

    return [frame1, frame2]

def run_ternus(frames, isi, label):

    label_stim = stimuli.TextLine(text=label, text_size=40)
    label_stim.present()
    # exp.screen.update()
    exp.clock.wait(1000)

    exp.screen.clear()
    for _ in range(6): 
        present_for(frames[0])
        exp.screen.update()
        exp.clock.wait(isi)
        exp.screen.clear()
        present_for(frames[1])
        exp.screen.update()
        exp.clock.wait(isi)
        exp.screen.clear()


exp = design.Experiment("Ternus Illusion")
control.set_develop_mode(True)
control.initialize(exp)

# Fixation cross
exp.textline = stimuli.TextLine(text="+", text_size=40, text_colour=(180,180,180))

# Generate stimuli
frames_no_tag = make_circles(with_tags=False)
frames_tagged = make_circles(with_tags=True)

control.start()
run_ternus(frames_no_tag, low_ISI, "1. Element motion (low ISI)")
run_ternus(frames_no_tag, high_ISI, "2. Group motion (high ISI)")
run_ternus(frames_tagged, high_ISI, "3. Element motion with color tags")
stimuli.TextLine("End of demo", text_size=40).present()
exp.clock.wait(1500)
control.end()