import expyriment
from expyriment import design, control, stimuli

exp = design.Experiment(name="display-edges")

control.set_develop_mode()
control.initialise(exp)

# w = exp.screen.size[0]
# h = exp.screen.size[1]

w, h = exp.screen.size
stim_length = w // 10

edges = []
for x in (-w, w):
    for y in (-h, h):
        edges.append((x//2, y//2))



square_length=0.05*w
line_width=1
size = (square_length, square_length)

rectangle_ls = stimuli.Rectangle(size, colour=(255, 0, 0), position=(-w//2, h//2))
rectangle_li = stimuli.Rectangle(size, colour=(255, 0, 0), position=(-w//2, -h//2))
rectangle_rs = stimuli.Rectangle(size, colour=(255, 0, 0), position=(w//2, h//2))
rectangle_ri = stimuli.Rectangle(size, colour=(255, 0, 0), position=(w//2, -h//2))

control.start(subject_id=1)
rectangle_ls.present(clear=True, update=False)
rectangle_li.present(clear=False, update=False)
rectangle_rs.present(clear=False, update=False)
rectangle_ri.present(clear=False, update=True)

exp.clock.wait(1000)

control.end()

