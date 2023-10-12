import numpy as np

# define constants for  the platform
BaseRadius = 105/2  # mm
platformRadius = 45/2  # mm
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
                                [-np.sin(theta), np.cos(theta)*np.sin(phi), np.cos(theta)*np.cos(phi)]]

B_i = [[BaseRadius*np.cos(0*np.pi()/3), BaseRadius*np.sin(0*np.pi()/3), 0],
      [BaseRadius*np.cos(1*np.pi()/3), BaseRadius*np.sin(1*np.pi()/3), 0],
      [BaseRadius*np.cos(2*np.pi()/3), BaseRadius*np.sin(2*np.pi()/3), 0],
      [BaseRadius*np.cos(3*np.pi()/3), BaseRadius*np.sin(3*np.pi()/3), 0],
      [BaseRadius*np.cos(4*np.pi()/3), BaseRadius*np.sin(4*np.pi()/3), 0],
      [BaseRadius*np.cos(5*np.pi()/3), BaseRadius*np.sin(5*np.pi()/3), 0]]  # Base anchor points [x_b, y_b, z_b]

P_i = [[platformRadius*np.cos(0*np.pi()/3), platformRadius*np.sin(0*np.pi()/3), 0],
      [platformRadius*np.cos(1*np.pi()/3), platformRadius*np.sin(1*np.pi()/3), 0],
      [platformRadius*np.cos(2*np.pi()/3), platformRadius*np.sin(2*np.pi()/3), 0],
      [platformRadius*np.cos(3*np.pi()/3), platformRadius*np.sin(3*np.pi()/3), 0],
      [platformRadius*np.cos(4*np.pi()/3), platformRadius*np.sin(4*np.pi()/3), 0],
      [platformRadius*np.cos(5*np.pi()/3), platformRadius*np.sin(5*np.pi()/3), 0]]  # platform anchor points [x_p, y_p, z_p]
