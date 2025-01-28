import math

#After receiving the coordinate
#Calculate degrees of each part of arm to reach

#length of each part of arm (mm)
l0=74
l1=125
l2=125
l3=165
k = math.sqrt(l2**2 + l3**2)

dp = math.sqrt((l1 + l2)**2 + l3**2)

print(dp)

def phase_one(d):
  x = math.degrees(math.atan(l3/l2))
  w = math.degrees(math.acos((l1**2 + k**2 - d**2)/(2*l1*k)))
  v = math.degrees(math.acos((l1**2 + d**2 - k**2)/(2*l1*d)))

  theta = 90 - v
  gamma = 180 - w - x
  delta = 90

  return (theta, gamma, delta)

def phase_two(d):
  theta = 90 - math.degrees(math.acos(((l1 + l2)**2 + d**2 - l3**2 )/(2*(l1 + l2)*d)))
  gamma = 0
  delta = 180 - math.degrees(math.acos(((l1 + l2)**2 + l3**2 - d**2)/(2*(l1 + l2)*l3)))

  return (theta, gamma, delta)

print(k)
print(phase_one(200))

# print(phase_two(350))

def move_to_anywhere(x, y, z):
#Base degree
  if y == 0:
    if x <= 0:
      theta_base = 180

    else:
      theta_base = 0

  else:
    theta_base = 90 - degrees(atan(x/y))

#Shoulder/Elbow/Wrist

#Compensation

