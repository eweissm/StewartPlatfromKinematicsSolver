import numpy as np

# define constants for  the platform
BaseDiameter = 105  # mm
platformDiameter = 45  # mm
h = 15  # mm

# target position and orientation
PlatformTranslation = [0, 0, 90]  # [x_p, y_p, z_p]
psi_deg = 0
theta_deg = 0
phi_deg = 0

# convert PlatformAngles_deg to radians
psi = psi_deg*(np.pi/180)
theta = theta_deg*(np.pi/180)
phi = phi_deg*(np.pi/180)

# calculate full rotation matrix
BaseToPlatformRotationMatrix = [[np.cos(psi)*np.cos(theta), -np.sin(psi)*np.cos(phi)+np.cos(psi)*np.sin(theta)*np.sin(phi), np.sin(psi)*np.sin(phi)+np.cos(psi)*np.sin(theta)*np.cos(phi)],
                                [np.sin(psi)*np.cos(theta), np.cos(psi)*np.cos(phi)+np.sin(psi)*np.sin(theta)*np.sin(phi), -np.cos(psi)*np.sin(phi)+np.sin(psi)*np.sin(theta)*np.cos(phi)],
                                [-np.cos(theta), np.cos(theta)*np.sin(phi), np.cos(theta)*np.cos(phi)]]