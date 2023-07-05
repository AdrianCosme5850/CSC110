# Adrian Cosme-Halverson
# 3 JUL 23
# This program is a madlib style game. It takes an original story and asks the user for a variety of words. 
# It then replaces those words in the original story. The original story is as follows:
# Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. Rats make me crazy.

# Welcome message

print('Welcome to my madlib game!')

# Start of inputs

adjective = input('Give me an adjective. ')
place = input('Give me a place. ')
animal = input('Give me a plural animal. ')
material = input('Give me a material. ')
verb = input('Give me a past-tense verb. ')
pronoun = input('Give me a pronoun. ')

# Output

print(adjective +'? I was ' + adjective + ' once. They '+ verb +' me in a '+ place + '. A '+ material +' '+ place +'. A '+ material +' '+ place +' with '+ animal +'. '+ animal +' make me '+ adjective +'.')

# Report

# I started by whiteboarding out all of the requirements on a miro board. I then went through them one by one as I wrote the program.
# I heard this saying while I was at annual training for the National Guard just a week ago. It has been stuck in my head since then.
# I tested the program by just running it and seeing how the inputs and outputs looked. I realized during the testing that I needed to
# be more specific with how I asked for the verb tense and plural animal, or else the story did not come out right.
# I relearned the string concatonation is not fun. I will probably look to see if there is something like template notation for Python
# like there is for Javascript.