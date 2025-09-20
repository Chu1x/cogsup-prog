from expyriment import design, control, stimuli, misc
from expyriment.stimuli import extras
import expyriment

expyriment.control.defaults.initialise_delay = 0 # No countdown
expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message

exp = design.Experiment(name = "two_squares")
control.initialize(exp)

left_vertices = misc.geometry.vertices_triangle(angle=-60, length1=50, length2=50)
left_square = stimuli.Shape(
    vertex_list=left_vertices,colour=(128, 0, 128), position=(-100, 0)
)

right_vertices = misc.geometry.vertices_regular_polygon(n_edges=6, length=25.5)
right_square = stimuli.Shape(
    vertex_list=right_vertices, colour=(255, 255, 0), position=(100, 0)
)

line_length = 50
line_left = stimuli.Line(start_point=(-101, 22), end_point=(-101, 22+line_length), line_width=3)
line_right = stimuli.Line(start_point=(100, 22), end_point=(100, 22+line_length), line_width=3)

text_dist = 20
text_left = stimuli.TextLine("triangle", position=(-101, 22+line_length+text_dist))
text_right = stimuli.TextLine("hexagon", position=(100, 22+line_length+text_dist))

control.start(subject_id=1)

left_square.present(clear=True, update=False)
right_square.present(clear=False, update=False)
line_left.present(clear=False, update=False)
line_right.present(clear=False, update=False)
text_left.present(clear=False, update=False)
text_right.present(clear=False, update=True)


exp.keyboard.wait()

control.end()

