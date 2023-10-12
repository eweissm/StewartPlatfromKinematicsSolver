import numpy as np

# define constants for  the platform
BaseDiameter = 105  # mm
platformDiameter = 45  # mm
h = 15  # mm

# target position and orientation
PlatformTranslation = [0, 0, 90]  # [x_p, y_p, z_p]
PlatformAngles_deg = [0, 0, 0]  # [psi, theta, phi]

# convert PlatformAngles_deg to radians
PlatformAngles = PlatformAngles_deg*(np.pi/180)

# calculate full rotation matrix
BaseToPlatformRotationMatrix = []