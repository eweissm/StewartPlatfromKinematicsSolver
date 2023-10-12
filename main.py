import numpy as np

# define constants for  the platform
BaseRadius = 105/2  # mm
platformRadius = 45/2  # mm
h = 15  # mm
FixedArmLength = 70  # mm

# target position and orientation
PlatformTranslation = np.transpose(np.array([0, 0, 90]))  # [x_p, y_p, z_p]
psi_deg = 0
theta_deg = 0
phi_deg = 0

# convert PlatformAngles_deg to radians
psi = psi_deg*(np.pi/180)
theta = theta_deg*(np.pi/180)
phi = phi_deg*(np.pi/180)

# calculate full rotation matrix
BaseToPlatformRotationMatrix = np.array([[np.cos(psi)*np.cos(theta), -np.sin(psi)*np.cos(phi)+np.cos(psi)*np.sin(theta)*np.sin(phi), np.sin(psi)*np.sin(phi)+np.cos(psi)*np.sin(theta)*np.cos(phi)],
                                [np.sin(psi)*np.cos(theta), np.cos(psi)*np.cos(phi)+np.sin(psi)*np.sin(theta)*np.sin(phi), -np.cos(psi)*np.sin(phi)+np.sin(psi)*np.sin(theta)*np.cos(phi)],
                                [-np.sin(theta), np.cos(theta)*np.sin(phi), np.cos(theta)*np.cos(phi)]])

# Calculate the arm lengths
l_i = np.zeros((6,3))
for i in range(6):
      b_i = np.transpose(np.array([BaseRadius*np.cos(i*np.pi/3), BaseRadius*np.sin(i*np.pi/3), 0]))  # Base anchor points [x_b, y_b, z_b]
      p_i = np.transpose(np.array([platformRadius*np.cos(i*np.pi/3), platformRadius*np.sin(i*np.pi/3), 0])) # platform anchor points [x_p, y_p, z_p]
      l_i[i] = PlatformTranslation + np.matmul(BaseToPlatformRotationMatrix, p_i) - b_i

print(l_i)