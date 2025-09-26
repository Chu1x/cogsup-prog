from expyriment import design, control, stimuli
import expyriment

exp = design.Experiment(name="kanizsa-rectangle", 
                        background_colour=expyriment.misc.constants.C_GREY)

control.set_develop_mode()
control.initialise(exp)

width, height = exp.screen.size


def kanizsa_rec (aspect_ratio=1.0, scale_rect=0.25, scale_circle=0.05):
    rect_w = width * scale_rect
    rect_l = rect_w * aspect_ratio
    r_w_half = rect_w // 2
    r_l_half = rect_l // 2

    r_circle = width *scale_circle


    circle_ls = stimuli.Circle(radius=r_circle, colour=(0,0,0), position=(-r_w_half, r_l_half))
    circle_rs = stimuli.Circle(radius=r_circle, colour=(0,0,0), position=(r_w_half, r_l_half))
    circle_li = stimuli.Circle(radius=r_circle, colour=(255, 255, 255), position=(-r_w_half, -r_l_half))
    circle_ri = stimuli.Circle(radius=r_circle, colour=(255, 255, 255), position=(r_w_half, -r_l_half))

    rectangle = stimuli.Rectangle(size=(rect_w, rect_l), colour=expyriment.misc.constants.C_GREY, position=(0,0))

    circle_ls.present(clear = True, update = False)
    circle_rs.present(clear = False, update = False)
    circle_li.present(clear = False, update = False)
    circle_ri.present(clear = False, update = False)
    rectangle.present(clear = False, update = True)



control.start(subject_id=1)
kanizsa_rec(aspect_ratio=0.6, scale_rect=0.5, scale_circle=0.06)



# circle_ls.present(clear = True, update = False)
# circle_rs.present(clear = False, update = False)
# circle_li.present(clear = False, update = False)
# circle_ri.present(clear = False, update = False)
# rectangle.present(clear = False, update = True)


exp.keyboard.wait()
control.end()