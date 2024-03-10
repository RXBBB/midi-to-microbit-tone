import sys
import pretty_midi

#-------------------------------------
# Made by RXB
# This loads midis into microbit
# 
# Enter The microbit website and then
# go into python mode and paste it in
#
# THIS ONLY SUPPORTS SINGLE VOICE MIDIS!
#-------------------------------------


# Load Midis
if len(sys.argv) < 2:
    print("Usage: python script.py <midi_file>")
    sys.exit(1)
midi_file = sys.argv[1]
# Load into prettymidi
midi_data = pretty_midi.PrettyMIDI(midi_file)

# convert midi note number to hertz
def midi_to_hz(note):
    return 440 * (2 ** ((note - 69) / 12))


# process notes
for instrument in midi_data.instruments:
    prev_end = 0
    for note in instrument.notes:
        # handle pause before note
        pause_duration = (note.start - prev_end) * 1000  # Convert to ms
        if pause_duration > 0:
            print(f"music.play(music.tone_playable(0, {pause_duration}), music.PlaybackMode.UNTIL_DONE)")
        # play the playing notes
        note_name = note.pitch
        note_hz = midi_to_hz(note_name)
        note_duration = (note.end - note.start) * 1000  # Convert to ms
        print(f"music.play(music.tone_playable({note_hz}, {note_duration}), music.PlaybackMode.UNTIL_DONE)")
        prev_end = note.end

    # handle potential pause after the last note
    if prev_end < midi_data.get_end_time():
        pause_duration = (midi_data.get_end_time() - prev_end) * 1000  # Convert to ms
        print(f"music.play(music.tone_playable(0, {pause_duration}), music.PlaybackMode.UNTIL_DONE)")
