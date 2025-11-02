from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_j, K_f, K_SPACE
import random

""" Constants """
KEYS = [K_j, K_f] 
COLORS = ["red", "blue", "green", "orange"]
TRIAL_TYPES = ["congruent", "incongruent"]

N_BLOCKS = 8
N_TRIALS_PER_BLOCK = 16
TOTAL_TRIALS = N_BLOCKS * N_TRIALS_PER_BLOCK  # 128 trials total

# Instructions
INSTR_START = """
You will see color words written in different colors.

Your task is to indicate the COLOR the word is printed in, 
not the word meaning.

Press J if the color is RED or ORANGE.
Press F if the color is BLUE or GREEN.

Try to respond as quickly and accurately as possible.
Press SPACE to start.
"""

INSTR_MID = """Take a short break.\nPress SPACE to continue."""
INSTR_END = """You have completed the experiment.\nPress SPACE to quit."""

FEEDBACK_CORRECT = ""
FEEDBACK_INCORRECT = ""


""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def present_for(*stims, t=1000):
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    exp.clock.wait(t)

def present_instructions(text):
    screen = stimuli.TextScreen(heading="Instructions", text=text)
    screen.present()
    exp.keyboard.wait(K_SPACE)

""" Global settings """
exp = design.Experiment(name="Stroop Balanced", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block', 'trial', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
fixation.preload()

stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

# Create all possible (word, color) pairs
pairs = []
for word in COLORS:
    for color in COLORS:
        trial_type = "congruent" if word == color else "incongruent"
        pairs.append((trial_type, word, color))

# To balance: equal number of congruent and incongruent trials
congruent_pairs = [p for p in pairs if p[0] == "congruent"]
incongruent_pairs = [p for p in pairs if p[0] == "incongruent"]

congruent_trials = congruent_pairs * 16 
incongruent_trials = incongruent_pairs * 6 
random.shuffle(incongruent_trials)
incongruent_trials = incongruent_trials[:64]

# Replicate and trim to 64 of each
all_trials = congruent_trials + incongruent_trials
random.shuffle(all_trials)

""" Experiment """
def run_trial(block_id, trial_id, trial_type, word, color):
    stim = stims[word][color]

    # Fixation
    present_for(fixation, t=500)

    # Stimulus presentation and response
    stim.present()
    key, rt = exp.keyboard.wait(KEYS)

    # Determine correct response based on COLOR
    if color in ["red", "orange"]:
        correct_key = K_j
    else:  # blue, green
        correct_key = K_f

    correct = (key == correct_key)
    exp.data.add([block_id, trial_id, trial_type, word, color, rt, correct])

    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=500)

# ---------------- Run Experiment ---------------- 
control.start()

present_instructions(INSTR_START)

for block_id in range(1, N_BLOCKS + 1):
    start_idx = (block_id - 1) * N_TRIALS_PER_BLOCK
    end_idx = start_idx + N_TRIALS_PER_BLOCK
    block_trials = all_trials[start_idx:end_idx]

    for trial_id, (trial_type, word, color) in enumerate(block_trials, start=1):
        run_trial(block_id, trial_id, trial_type, word, color)

    if block_id < N_BLOCKS:
        present_instructions(INSTR_MID)

present_instructions(INSTR_END)
control.end()