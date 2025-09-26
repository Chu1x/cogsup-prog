from expyriment import design, control, stimuli
# from expyriment.stimuli import extras
import expyriment

exp = design.Experiment(name="kanizsa-square", 
                        background_colour=expyriment.misc.constants.C_GREY)

control.set_develop_mode()
control.initialise(exp)

width, height = exp.screen.size
s_length = width // 4
r = width // 20

l = s_length / 2

circle_ls = stimuli.Circle(radius=r, colour=(0,0,0),position=(-l, l))
circle_rs= stimuli.Circle(radius=r, colour=(0,0,0), position=(l, l))
circle_li= stimuli.Circle(radius=r, colour=(255,255,255), position=(-l, -l))
circle_ri = stimuli.Circle(radius=r, colour=(255,255,255), position=(l, -l))
rectangle = stimuli.Rectangle(size=(s_length, s_length), colour=(192,192,192),position=(0,0))


control.start(subject_id=1)

circle_ls.present(clear = True, update = False)
circle_rs.present(clear = False, update = False)
circle_li.present(clear = False, update = False)
circle_ri.present(clear = False, update = False)
rectangle.present(clear = False, update = True)


exp.keyboard.wait()
control.end()