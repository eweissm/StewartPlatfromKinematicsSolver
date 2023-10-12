import numpy as np

# define constants for  the platform
BaseRadius = 105/2  # mm
platformRadius = 45/2  # mm
h = 15  # mm
FixedArmLength = 70  # mm

# target position and orientation
PlatformTranslation = np.transpose(np.array([0, 10, 70]))  # [x_p, y_p, z_p]
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



alpha = np.zeros(6)
for i in range(6):
      b_i = np.transpose(np.array([BaseRadius*np.cos(i*np.pi/3), BaseRadius*np.sin(i*np.pi/3), 0]))  # Base anchor points [x_b, y_b, z_b]
      p_i = np.transpose(np.array([platformRadius*np.cos(i*np.pi/3), platformRadius*np.sin(i*np.pi/3), 0])) # platform anchor points [x_p, y_p, z_p]

      # Calculate the arm lengths
      l_i = PlatformTranslation + np.matmul(BaseToPlatformRotationMatrix, p_i) - b_i

      beta_i = i*np.pi/3

      e_i = 2*h*l_i[2]
      f_i = 2*h*(np.cos(beta_i)*l_i[0]+np.sin(beta_i)*l_i[1])
      g_i = np.linalg.norm(l_i)**2-(FixedArmLength**2-h**2)

      alpha[i] = np.arcsin(g_i/np.sqrt(e_i**2+f_i**2)) - np.arctan2(f_i, e_i)

alpha_deg = np.ceil(alpha*180/np.pi+90)
print(alpha_deg)