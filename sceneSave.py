import re
import maya.cmds as cmds
import os

def savePrimary():
    scenefile = cmds.file(query=True, sn=True, shn=False)
    path, currentFile = os.path.split(scenefile)

    newFile = os.path.join(path, incrementHard(currentFile))
    newFileName = cmds.file(rename=newFile)
    cmds.file(save=True, force=True)
    print "Saved scene as: \n{}".format(newFileName)

def saveSecondary():
    scenefile = cmds.file(query=True, sn=True, shn=False)
    path, currentFile = os.path.split(scenefile)
    # lastNum = re.compile(r'(?:[^\d]*(\d+)[^\d]*)+')
    newFile = os.path.join(path, increment(currentFile))
    newFileName = cmds.file(rename=newFile)
    cmds.file(save=True, force=True)
    print "Saved scene as: \n{}".format(newFileName)

def increment(s):
    """ look for the last sequence of number(s) in a string and increment """
    lastNum = re.compile(r'(?:[^\d]*(\d+)[^\d]*)+')
    m = lastNum.search(s)
    if m:
        next = str(int(m.group(1))+1)
        start, end = m.span(1)
        s = s[:max(end-len(next), start)] + next + s[end:]
    return s

def incrementHard(s):
    """ look for the first sequence of number(s) in the file and increment. Also reset the next group of numbers to 001."""
    lastNum = re.compile(r'(?:(\d+)[^\d]*(\d+)[^\d]*)+')
    m = lastNum.search(s)
    if m:
        next = str(int(m.group(1))+1)
        start, end = m.span(1)
        s = s[:max(end-len(next), start)] + next + s[end:]
        reset = "1"
        resetStart, resetEnd = m.span(2)
        endSpan = len(m.group(2))
        s = s[:max(resetEnd-endSpan, resetStart)] + reset.rjust(endSpan,'0') + s[resetEnd:]
    return s


