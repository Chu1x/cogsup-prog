from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")


control.initialize(exp)
control.start(subject_id=1)

fixation = stimuli.FixCross()


square = stimuli.Rectangle(size = (50, 50), color = (0, 0, 255))

square.present(clear=True, update=False)



fixation.present(clear=True, update=True)


exp.clock.wait(500)


square.present(clear=True, update=True)


exp.keyboard.wait()


control.end()