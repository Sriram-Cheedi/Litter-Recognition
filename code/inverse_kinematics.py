
# REFER TO README.MD IN CODE FOLDER FOR DIAGRAMS AND EXPLANATIONS OF THE CALCULATIONS


import math
import numpy as np


#length of each part of arm (mm)
l0=74
l1=125 
l2=125
l3=165


#phase 1 imaginary arm
k = math.sqrt(l2**2 + l3**2)

#start distance for phase 1
d0 = math.sqrt(k**2 - l1**2)

#start distance for phase 2
dp = math.sqrt((l1 + l2)**2 + l3**2)

#calculate dmax
a1 = math.degrees(math.asin(((l1+l2)*(math.sin(math.radians(15))))/(l3)))
a2 = 180 - a1 - 15
dmax = (math.sin(math.radians(a2)) * l3)/(math.sin(math.radians(15)))
dmin = math.sqrt(k**2 - l1**2)



# Phase one of movement
def phase_one(d):
  x = math.degrees(math.atan(l3/l2))
  w = math.degrees(math.acos((l1**2 + k**2 - d**2)/(2*l1*k)))
  v = math.degrees(math.acos((l1**2 + d**2 - k**2)/(2*l1*d)))

  # Calculate angles relative to the straight up position
  theta = 90 - v
  gamma = 180 - w - x
  delta = 90

  return (theta, gamma, delta)

# Phase two of movement
def phase_two(d):

  # Calculate angles relative to the straight up position
  theta = 90 - math.degrees(math.acos(((l1 + l2)**2 + d**2 - l3**2 )/(2*(l1 + l2)*d)))
  gamma = 0
  delta = 180 - math.degrees(math.acos(((l1 + l2)**2 + l3**2 - d**2)/(2*(l1 + l2)*l3)))

  return (theta, gamma, delta)


# Calculates angles of joints required to move arm along straight line
def move_line(d):
  out = (0, 0, 0)

  # Between d and dplus do phase one
  if(d < dp):
    out = phase_one(d)
  
  # Greater than dplus do phase two
  else:
    out = phase_two(d)
    

  return out


def boundVector(oldVector):
  vector = oldVector

  # Make sure z value is no greater than 
  vector[2] = max(vector[2], -50)

  # Get the magnitude of the vector
  mag = np.linalg.norm(vector)

  # Make sure dist does not go out of bounds
  dist = max(dmin, min(dmax, mag))

  # Ensure that if 0,0,0 is entered somehow, we force the vector to have some magnitude
  # as 0 < dmin
  if mag == 0:
    vector = np.array([0,1,0])
    mag = 1   
  if dist == dmax:
      vector = (vector / mag) * dmax      # Normalise the vector and then multiply it by dmax

  if dist == dmin:
      vector = (vector / mag) * dmin


  return vector

def move(vector):
  
  vector = boundVector(vector)

  # Get projection of vector horizontally
  floor_projection = math.sqrt(vector[0]**2 + vector[1]**2)

  #Calculate rotation of the base
  base = math.degrees(math.atan(vector[0]/vector[1]))

  #Calculate additional degrees for the shoulder
  shoulder = math.degrees(math.atan2(vector[2] / floor_projection))

  # Get degrees required to move arm by the magnitude of the vector
  degrees = move_line(np.linalg.norm(vector))

  #Add the degrees required for the direction of the vector
  return (base, degrees[0] - shoulder, degrees[1], degrees[2], vector)
