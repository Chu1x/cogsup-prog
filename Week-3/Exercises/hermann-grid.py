from expyriment import design, control, stimuli, misc
# import expyriment

exp = design.Experiment(name="hermann-grid",
                        background_colour=misc.constants.C_BLACK)

control.set_develop_mode()
control.initialise(exp)

control.start(subject_id=1)

screen_w, screen_h = exp.screen.size
step = 50           
line_width = 4     
dot_radius = 4     
line_colour = (200, 200, 200) 
dot_colour = (255, 255, 255)  

# drawing vertical lines
for x in range(-screen_w//2, screen_w//2, step):
    line = stimuli.Line(start_point=(x, -screen_h//2),
                        end_point=(x, screen_h//2),
                        colour=line_colour,
                        line_width=line_width)
    line.present(clear=False, update=False)

# drawing horizontal lines
for y in range(-screen_h//2, screen_h//2, step):
    line = stimuli.Line(start_point=(-screen_w//2, y),
                        end_point=(screen_w//2, y),
                        colour=line_colour,
                        line_width=line_width)
    line.present(clear=False, update=False)

# intersection dots
for x in range(-screen_w//2, screen_w//2, step):
    for y in range(-screen_h//2, screen_h//2, step):
        dot = stimuli.Circle(radius=dot_radius,
                             colour=dot_colour,
                             position=(x, y))
        dot.present(clear=False, update=False)

exp.screen.update()


exp.keyboard.wait()
control.end()
