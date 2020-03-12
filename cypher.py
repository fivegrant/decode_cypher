#!/usr/bin/env python3

phrase = "Quazszuejmddkqemdufmtyeaybvbyogkjjmxwmtquazoazbutbyqkxfezbxwtbxyus" +\
         "jkqquazbxhmxybhmvkoajybmtkxfbvquatujhmbyeqquazuixdmkxtquadkqmlsmzb" +\
         "mxomygmymxtbuxkxfmxnuqygmyzbadsguvfbtouhmzq"

# Frequency of characters
freq = {}

# Cypher
cypher = {
    "a": "e",
    "b": " ",
    "c": " ",
    "d": " ",
    "e": " ",
    "f": " ",
    "g": " ",
    "h": " ",
    "i": " ",
    "j": " ",
    "k": " ",
    "l": " ",
    "m": "i",
    "n": " ",
    "o": " ",
    "p": " ",
    "q": "t",
    "r": " ", 
    "s": "s",    
    "t": " ",
    "u": "h",
    "v": " ",
    "w": " ",
    "x": "u",
    "y": " ",
    "z": "e",
}

phrase = phrase.lower()

# Calculate frequency of characters
for c in phrase:
  if c in freq:
    freq[c] += 1
  else:
    freq[c] = 1

# Print
output = ""

for c in phrase:
    output += cypher[c]

print(freq)
print("\n\n")
print(output)
