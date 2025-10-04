from expyriment import design, control, stimuli
import random

radius = 150       
low_ISI = 50       
high_ISI = 300     
display_dur = 200  
bg_color = (0, 0, 0)
circle_color = (255, 255, 255)
tag_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


def present_for(stims, t=display_dur):
    t0 = exp.clock.time
    for s in stims:
        s.present(clear=False)
    exp.screen.update()
    exp.clock.wait(max(0, t - (exp.clock.time - t0)))

def make_circles(with_tags=False):
    frames = []
    colors = tag_colors if with_tags else [circle_color]*3
    # left frame
    left_circles = [stimuli.Circle(40, colour=colors[i],
                   position=(-radius + i*radius, 0)) for i in range(3)]
    # right frame
    right_circles = [stimuli.Circle(40, colour=colors[i],
                    position=(-radius + i*radius + radius, 0)) for i in range(3)]
    frames.append(left_circles)
    frames.append(right_circles)
    return frames

def run_ternus(frames, isi, label):
    exp.screen.clear()
    exp.screen.update()
    exp.textline.present()
    exp.clock.wait(1000)
    for _ in range(6):   
        present_for(frames[0])
        exp.screen.clear(); exp.screen.update()
        exp.clock.wait(isi)
        present_for(frames[1])
        exp.screen.clear(); exp.screen.update()
        exp.clock.wait(isi)


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