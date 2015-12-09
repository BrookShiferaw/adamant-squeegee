   #!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), Mon Nov 30 07:57:42 2015
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'task'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess
    
  # Initialize components for Routine "instruct"
instructClock = core.Clock()
instruction = visual.TextStim(win=win, ori=0, name='instruction',
    text= "Four coloured squares will appear inside a display box and disappear. Remember the location of each colour everytime they appear as a group.  After a brief delay, one of them will reappear in the center. \n\nYour task is to indicate the direction it has moved from its most recent location to the centre by pressing either 'up', 'down', 'left', or 'right' arrow keys on the keyboard as fast as you can. \n\n Press 'enter' to begin.",    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "centralTask"
centralTaskClock = core.Clock()
targetcontainer = visual.Rect(win=win, name='targetcontainer',units='deg', 
    width=[7, 7][0], height=[7, 7][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=u'black', lineColorSpace='rgb',
    fillColor=u'grey', fillColorSpace='rgb',
    opacity=1,depth=0.0, 
interpolate=True)
upcue = visual.Rect(win=win, name='upcue',units='deg', 
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0, 3],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
downcue = visual.Rect(win=win, name='downcue',units='deg', 
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0, -3],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)
leftcue = visual.Rect(win=win, name='leftcue',units='deg', 
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[-3, 0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-3.0, 
interpolate=True)
rightcue = visual.Rect(win=win, name='rightcue',units='deg', 
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[3, 0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
targetbox = visual.Rect(win=win, name='targetbox',units='deg', 
    width=[0.5, 0.5][0], height=[0.5, 0.5][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1,depth=-5.0, 
interpolate=True)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instruct"-------
t = 0
instructClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
start = event.BuilderKeyResponse()  # create an object of type KeyResponse
start.status = NOT_STARTED
# keep track of which components have finished
instructComponents = []
instructComponents.append(instruction)
instructComponents.append(start)
for thisComponent in instructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instruct"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction* updates
    if t >= 0.0 and instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction.tStart = t  # underestimates by a little under one frame
        instruction.frameNStart = frameN  # exact frame index
        instruction.setAutoDraw(True)
    
    # *start* updates
    if t >= 0.0 and start.status == NOT_STARTED:
        # keep track of start time/frame for later
        start.tStart = t  # underestimates by a little under one frame
        start.frameNStart = frameN  # exact frame index
        start.status = STARTED
        # keyboard checking is just starting
        start.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if start.status == STARTED:
        theseKeys = event.getKeys(keyList=['return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            start.keys = theseKeys[-1]  # just the last key pressed
            start.rt = start.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if start.keys in ['', [], None]:  # No response was made
   start.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('start.keys',start.keys)
if start.keys != None:  # we had a response
    thisExp.addData('start.rt', start.rt)
thisExp.nextEntry()
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#########start of task1########

# set up handler to look after randomisation of conditions etc
task1 = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'practisetrail.xlsx'),
    seed=None, name='task1')
thisExp.addLoop(task1)  # add the loop to the experiment
thisTask1 = task1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTask1.rgb)
if thisTask1 != None:
    for paramName in thisTask1.keys():
        exec(paramName + '= thisTask1.' + paramName)

for thisTask1 in task1:
    currentLoop = task1
    # abbreviate parameter names if possible (e.g. rgb = thisTask1.rgb)
    if thisTask1 != None:
        for paramName in thisTask1.keys():
            exec(paramName + '= thisTask1.' + paramName)
    
    #------Prepare to start Routine "centralTask"-------
    t = 0
    centralTaskClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    upcue.setLineColor(upbox)
    upcue.setFillColor(upbox)
    downcue.setLineColor(downbox)
    downcue.setFillColor(downbox)
    leftcue.setLineColor(leftbox)
    leftcue.setFillColor(leftbox)
    rightcue.setLineColor(rightbox)
    rightcue.setFillColor(rightbox)
    targetbox.setLineColor(targettest)
    targetbox.setFillColor(targettest)
    answer1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    answer1.status = NOT_STARTED
    # keep track of which components have finished
    centralTaskComponents = []
    centralTaskComponents.append(targetcontainer)
    centralTaskComponents.append(upcue)
    centralTaskComponents.append(downcue)
    centralTaskComponents.append(leftcue)
    centralTaskComponents.append(rightcue)
    centralTaskComponents.append(targetbox)
    centralTaskComponents.append(answer1)
    centralTaskComponents.append(ISI)
    for thisComponent in centralTaskComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "centralTask"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = centralTaskClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *targetcontainer* updates
        if t >= 0.0 and targetcontainer.status == NOT_STARTED:
            # keep track of start time/frame for later
            targetcontainer.tStart = t  # underestimates by a little under one frame
            targetcontainer.frameNStart = frameN  # exact frame index
            targetcontainer.setAutoDraw(True)
        
        # *upcue* updates
        if t >= .5 and upcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            upcue.tStart = t  # underestimates by a little under one frame
            upcue.frameNStart = frameN  # exact frame index
            upcue.setAutoDraw(True)
        if upcue.status == STARTED and t >= (.5 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            upcue.setAutoDraw(False)
        
        # *downcue* updates
        if t >= 0.5 and downcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            downcue.tStart = t  # underestimates by a little under one frame
            downcue.frameNStart = frameN  # exact frame index
            downcue.setAutoDraw(True)
        if downcue.status == STARTED and t >= (0.5 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            downcue.setAutoDraw(False)
        
        # *leftcue* updates
        if t >= 0.5 and leftcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftcue.tStart = t  # underestimates by a little under one frame
            leftcue.frameNStart = frameN  # exact frame index
            leftcue.setAutoDraw(True)
        if leftcue.status == STARTED and t >= (0.5 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            leftcue.setAutoDraw(False)
        
        # *rightcue* updates
        if t >= .5 and rightcue.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightcue.tStart = t  # underestimates by a little under one frame
            rightcue.frameNStart = frameN  # exact frame index
            rightcue.setAutoDraw(True)
        if rightcue.status == STARTED and t >= (.5 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
            rightcue.setAutoDraw(False)
        
        # *targetbox* updates
        if t >= 3.5 and targetbox.status == NOT_STARTED:
            # keep track of start time/frame for later
            targetbox.tStart = t  # underestimates by a little under one frame
            targetbox.frameNStart = frameN  # exact frame index
            targetbox.setAutoDraw(True)
        
        # *answer1* updates
        if t >= 3.5 and answer1.status == NOT_STARTED:
            # keep track of start time/frame for later
            answer1.tStart = t  # underestimates by a little under one frame
            answer1.frameNStart = frameN  # exact frame index
            answer1.status = STARTED
            # keyboard checking is just starting
            answer1.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if answer1.status == STARTED:
            theseKeys = event.getKeys(keyList=['up', 'down', 'left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                answer1.keys = theseKeys[-1]  # just the last key pressed
                answer1.rt = answer1.clock.getTime()
                # was this 'correct'?
                if (answer1.keys == str(corrAns)) or (answer1.keys == corrAns):
                    answer1.corr = 1
                else:
                    answer1.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if t >= 1.5 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(2)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in centralTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "centralTask"-------
    for thisComponent in centralTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if answer1.keys in ['', [], None]:  # No response was made
       answer1.keys=None
       # was no response the correct answer?!
       if str(corrAns).lower() == 'none': answer1.corr = 1  # correct non-response
       else: answer1.corr = 0  # failed to respond (incorrectly)
    # store data for task1 (TrialHandler)
    task1.addData('answer1.keys',answer1.keys)
    task1.addData('answer1.corr', answer1.corr)
    if answer1.keys != None:  # we had a response
        task1.addData('answer1.rt', answer1.rt)
    # the Routine "centralTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'task1'



win.close()
core.quit()
