
# Robot Progress Timeline

## Introduction

In this markdown we have attempted to document all the progress we have made on the most physical aspect of our project - the Braccio Arm.
It will be an attempt to collate all the progress and activities we undertook throughout the project. We will categorise the milestones by
the release period they took place in.

To see documentation for the time we spent on the Raspberry Pi and camera system, please look for another folder in our docs.

### MVP


### Beta Release

Towards the tail end of our release to the client, we ran a few tests with the arm to see how precisely it could target a specific vector. To our horror
and utter dismay, there is a huge precision issue in the servos of the arm. 

When it comes to vertical movement (ie every servo excluding the base), this is a very minor issue in our current iteration of the project. Picking 
an object up ± 1cm from the centre of it won't be a huge issue until we try to pick up more complex (top-heavy) objects. On the other hand, when it
comes to horizontal movement, a few degrees of error in the base servo translate to huge margains of error at the farthest end of the robot's pickup
range (the most we measured was a horrific 15cm or so). The arm behaved strangely after completing its movement. We could physically twist it to the 
correct location, at which point it would lock up and stop moving. This tipped us off to suspect that the resistance the servos were facing while moving
was a likely culprit. It seems they had a tendency to stop just shy of the correct angle they were supposed to be targeting.

We didn't have time to fix this issue before our Beta Release to our client, but this suspicion had given us a few ideas ofpotential fixes.

### Final Release

In our first session after our beta release to the client, we set about tinkering with the base of the robot. We first had to test two things:

1) Was the base on too loose? Was there a lack of grip between the servo and the plastic connections causing it to lag behind the correct position?

2) Was the base on too tight? Was a high amount of tension between the base and servo causing it to not be able to turn as freely as it should?

While testing the former, we screwed on the base far too tight and caused the arm to almost tear itself in two. While testing the latter, we found that
there was no real change in the error. This left us to take to forums to look into what could be causing it. We spent a couple of hours just messing
around with different configurations of how tight to screw the base in and testing the starting angle of the base servo - to no avail.

In reality, the issue was quite simple. Servos are not precision devices. Being from a more theoretical field, we had simply sort of expected the
hardware to be theoretically flawless. However, the servos in the Braccio arm are fairly-budget friendly when compared to precision devices.
It would seem that just before reaching the target degree, the power in the servo dips slightly. This causes the servo to be unable to overcome
anymore resistance and stop just short of the target. So - we took to a software solution for this. We programmed the base servo to overshoot the
target by some number of degrees and then slowly "wiggle" its way back to the target.







  
