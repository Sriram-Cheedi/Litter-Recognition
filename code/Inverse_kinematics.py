
# REFER TO README.MD IN CODE FOLDER FOR DIAGRAMS AND EXPLANATIONS OF THE CALCULATIONS


import math


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

  # Arbitrily set to 10 as minimum distance for now but improvements can be made to this
  if (d > 10):

    # Between d and dplus do phase one
    if(d < dp):
      out = phase_one(d)
    
    # Greater than dplus do phase two
    else:
      out = phase_two(d)
    

  return out

def move(x, y, z):

  # Get the magnitude of the vector
  dist = math.sqrt(x**2 + y**2 + z**2)

  # BAD CODE ALERT:
  # This section causes strange behaviour when distance is not within bounds of robot
  # The value of dist is capped at the max possible distance but x,y,z are not adjusted accordingly
  # 
  # 
  if dist > math.floor(dmax):
    dist = math.floor(dmax)

  # Get projection of vector horizontally
  floor_projection = math.sqrt(x**2 + y**2)

  #Calculate rotation of the base
  base = math.degrees(math.atan(x/y))

  #Calculate additional degrees for the shoulder
  shoulder = math.degrees(math.atan(z / floor_projection))

  #Get degrees required to move arm by the magnitude of the vectore
  degrees = move_line(dist)

  #Add the degrees required for the direction of the vector
  return (base, degrees[0] - shoulder, degrees[1], degrees[2])
