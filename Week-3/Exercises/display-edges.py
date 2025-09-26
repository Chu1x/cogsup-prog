from expyriment import design, control, stimuli
import expyriment

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



s_length=0.05*w
line_width=1

size = (s_length, s_length)

rectangle_ls = stimuli.Rectangle(size, colour=(255, 0, 0), line_width=1, position=(-w//2 + s_length //2, h//2 - s_length//2))
rectangle_li = stimuli.Rectangle(size, colour=(255, 0, 0), line_width=1, position=(-w//2 + s_length //2, -h//2 + s_length //2))
rectangle_rs = stimuli.Rectangle(size, colour=(255, 0, 0), line_width=1, position=(w//2 - s_length //2, h//2 - s_length //2))
rectangle_ri = stimuli.Rectangle(size, colour=(255, 0, 0), line_width=1, position=(w//2 - s_length //2, -h//2 + s_length //2))

control.start(subject_id=1)
rectangle_ls.present(clear=True, update=False)
rectangle_li.present(clear=False, update=False)
rectangle_rs.present(clear=False, update=False)
rectangle_ri.present(clear=False, update=True)

exp.keyboard.wait()

control.end()

