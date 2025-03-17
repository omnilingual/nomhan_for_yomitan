# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:20:47 2024

@author: Omnis
"""

hanDict = {}

raw = open("han_raw.txt", "r", encoding="utf-8")
rawLines = raw.readlines()
raw.close()

code = 0x4e00
for rawLine in rawLines:
    if rawLine.strip() == "":
        code += 1
        continue
    pronunciations = rawLine.split(",");
    for pronunciation in pronunciations:
        if finePronunciation := pronunciation.strip() in hanDict:
            hanDict[pronunciation.strip()] += " | " + chr(code)
        else:
            hanDict[pronunciation.strip()] = chr(code)
    code += 1

with open("han_bank.json", "w", encoding="utf-8") as f:
    seq = 1
    f.write("[\n")
    for entry in hanDict:
        f.write("\t[\"" + entry + "\",\"\",\"Hán\",\"\",0,[\"" + hanDict[entry] + "\"]," + str(seq) + ",\"\"],\n")
        seq += 1

with open("han_bank.json", "rb+") as f:
    f.seek(-3, 2)
    f.write(bytes("\n]", "utf-8"))
