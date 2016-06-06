# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:36:53 2016

@author: Yifei
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc
import pylab
from matplotlib.backends.backend_pdf import PdfPages



# Example data
two_D_Ux = -0.15045e-02
two_D_Uy = 0.011758
three_D_Ux = 9.47

Tri3_dofs = np.array([90, 292, 1038, 3898, 4170, 4698, 5298, 5842, 14322, 25634])
Tri3_Ux = np.array([-0.0873929e-02, -0.127231e-02, -0.143843e-02, -0.148735e-02, -0.148835e-02, -0.148919e-02, -0.149204e-02, -0.149269e-02, -0.149982e-02, -0.150168e-02])/two_D_Ux
Tri3_Uy = np.array([0.0068367, 0.00993406, 0.0112263, 0.0116063, 0.0116131, 0.0116189, 0.0116457, 0.0116505, 0.0117028, 0.0117171])/two_D_Uy

Tri6_dofs = np.array([62, 114, 138, 292, 1780, 4830, 8986, 12073, 15609, 19300])
Tri6_Ux = np.array([-0.00132675, -0.00149616, -0.00149623, -0.001504, -0.001504, -0.00150448, -0.00150449, -0.00150450, -0.00150451, -0.00150453])/two_D_Ux
Tri6_Uy = np.array([0.00847992, 0.011506, 0.011513, 0.0117277, 0.0117383, 0.0117391, 0.0117392, 0.0117392, 0.0117393, 0.0117393])/two_D_Uy

Quad4_dofs = np.array([48, 372, 1332, 3374, 4842, 6228, 8386, 10232, 15344, 20044])
Quad4_Ux = np.array([-0.00078276, -0.0014393, -0.00147509, -0.00149431, -0.00149817, -0.00149945, -0.00150076, -0.00150123, -0.00150134, -0.00150143])/two_D_Ux
Quad4_Uy = np.array([0.00620667, 0.0112254, 0.0115086, 0.0116894, 0.0116894, 0.0116992, 0.0117105, 0.0117123, 0.0117144, 0.0117151])/two_D_Uy

Quad8_dofs = np.array([142, 286, 466, 1090, 2870, 6450, 10346, 12342, 15656, 22344])
Quad8_Ux = np.array([-0.00120593, -0.00139123, -0.00139228, -0.00147418, -0.00149483, -0.00149948, -0.00150103, -0.00150163, -0.00150166, -0.00150183])/two_D_Ux
Quad8_Uy = np.array([0.00947769, 0.0108697, 0.0108725, 0.0115056, 0.0116652, 0.0117018, 0.0117032, 0.0117056, 0.0117079, 0.0117186])/two_D_Uy

Tet4_dofs = np.array([54, 243, 1395, 9315, 24579, 34632, 53307, 64343, 76443, 96567])
Tet4_Ux = np.array([6.320, 6.372, 9.295, 9.36, 9.36, 9.37, 9.37, 9.37, 9.37, 9.37])/three_D_Ux

Tet10_dofs = np.array([243, 579, 13857, 36312, 43521, 57537, 60299, 79683, 84322, 101321])
Tet10_Ux = np.array([9.37, 9.37, 9.372, 9.378, 9.378, 9.378, 9.378, 9.378, 9.378, 9.378])/three_D_Ux

# Create plots with pre-defined labels.
# Alternatively, you can pass labels explicitly when calling `legend`.
fig, ax = plt.subplots()
#ax.plot(Tri3_dofs, Tri3_Ux, 'g-', label='Tri3 Ux')
#ax.plot(Tri6_dofs, Tri6_Ux, 'b-', label='Tri6 Ux')
#ax.plot(Quad4_dofs, Quad4_Ux, 'm-', label='Quad4 Ux')
#ax.plot(Quad8_dofs, Quad8_Ux, 'k-', label='Quad8 Ux')

#ax.plot(Tri3_dofs, Tri3_Uy, 'g-', label='Tri3 Uy')
#ax.plot(Tri6_dofs, Tri6_Uy, 'b-', label='Tri6 Uy')
#ax.plot(Quad4_dofs, Quad4_Uy, 'm-', label='Quad4 Uy')
#ax.plot(Quad8_dofs, Quad8_Uy, 'k-', label='Quad8 Uy')

#ax.plot(Tet4_dofs, Tet4_Ux, 'g-', label='Tet4 Ux')
#ax.plot(Tet10_dofs, Tet10_Ux, 'b-', label='Tet10 Ux')

# Now add the legend with some customizations.
#legend = ax.legend(loc='lower right', shadow=True)

legend = ax.legend(loc='lower right', shadow=True)


# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.90')

# pylab.xlim([-1000, 110000])
pylab.ylim([0.55,1.1])
plt.xlabel('DOFs [-]')
plt.ylabel(r'Uy(amfe)/Uy(ansys) [-]')
# Set the fontsize
# for label in legend.get_texts():
#     label.set_fontsize('large')
#
# for label in legend.get_lines():
#     label.set_linewidth(1.5)  # the legend line width

plt.show()



# with PdfPages('foo.pdf') as pdf:
#     rc('text', usetex=True)
#     plt.plot(y_dis, stress_xx)
#
#     plt.xlabel('Verschiebung in y Richtung Pfad A-A $[mm]$')
#     plt.ylabel(r'$\sigma_{xx} [N/mm^2]$')
#     pdf.savefig()
#     plt.close()
