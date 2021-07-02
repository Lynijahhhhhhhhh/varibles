# author: Lynijah
# date: 07-02-2021
#
# description: doing zeee variables

# Choose a song that you enjoy listening to. For this song you should pull up the lyrics.
# I suggest using Genius since it breaks down the song's structure into its individual parts.

# --------------- Section 3 --------------- #
def blank():
    return print(" ")
# 3.1
# Variables
#   1) Create a variable to represent each part of the song. By parts, I mean the verses, chorus, bridges, etc. Each
#   part should exist as a string. You may need to use string combination to combine longer verses and choruses.
#
#   Use the newline or \n escape character at the end of every line.
#
# Hint: When combining long strings, it may be nicer to utilize individual lines for each line in a verse or chorus.
# See below for an example. Surround the combination with a (), and then hit enter when the cursor is in between. It
# should make the form you see below of:
#
# variable = (
#    'lyrics go here'
# )
#
# Anything between these () are included in the operation.

example_verse = (
    'round your city, round the clock\n' +
    'everybody needs you\n' +
    'no, you can\'t make everybody equal\n'
)

# WRITE CODE BELOW
chorus="Maybe I’m not pretty,\nmaybe I’m just fun\n‘Cause I got a belly and I got a bum\nAnd I’m f*cking jelly of all the other ones\nWith their itty bitty bellies\nand their rump-ump-ump-ums"

verse1="I know that I should love myself\nBut it’s getting kinda hard when you’re constantly feeling like garbage\nKnow I shouldn’t hurt myself\nBut I can’t find a way to lose weight without literally starving"

preChorus="Every other song says I’m beautiful\nBut what if I don’t feel like I’m beautiful?\nI wish my body image didn’t say\nThat I should be another kinda way"

newChorus="Maybe I’m not pretty, maybe I’m just fun\n'Cause I got a belly and I got a bum\nBut I can’t be jelly of all the other ones\nSo I’m falling in lovе with my rump-ump-ump-um"

verse2="I’m not gonna ask for help\n‘Cause all you’re gonna say is\n“You’rе perfect and oh, you’re so worth it”\nBut sometimes I hate myself\nI get inside my head and I think that I somehow deserve this"

outro="I’m not pretty\nI’m not pretty\nSo I’m falling in love with my rump-ump-ump-um"
# 3.2
# Print
#   1) Print the variables out so that they form the song in correct order when outputted to the terminal.
#   2) Insert blank print statements so that there is a blank line in between different verses / choruses.
#
#   Remember you can re-use variables (like the chorus) if it's the same.
#
# WRITE CODE BELOW

print(chorus)
blank
print(verse1)
blank()
print(preChorus)
blank()
print(newChorus)
blank()
print(verse2)
blank()
print(preChorus)
blank()
print(newChorus)
blank()
print(outro)