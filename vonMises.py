from matplotlib import pyplot as plt
import math

#Quad4
DOFs = [854, 2320, 3448, 4882, 7856, 9128, 12310, 21060, 26384, 29056, 32548, 36750]

S11 = [1214.92, 1140.36, 1178.80, 1118.92, 1065.53, 1159.79, 1115.66, 1104.15, 1134.41, 1106.96, 1099.36, 1128.21]

S22 = [1138.91, 1167.07, 1083.72, 1143.34, 1173.20, 1084.34, 1117.62, 1112.87, 1083.56, 1102.97, 1106.54, 1081.23]

S12 = [917.94, 995.45, 1017.86, 1024.63, 1032.94, 1033.29, 1039.59, 1045.15, 1047.83, 1050.48, 1050.12, 1049.56]

# S_analy = 1

# Tri3
#DOFs = [870, 2682, 4172, 5788, 9354, 10952, 15490, 27332, 33770, 45032, 68943]
#
#S11 = [1060.97, 1034.59, 1102.81, 1053.96, 1106.52, 1102.23, 1064.35, 1065.72, 1099.14, 1070.32, 1073.11]
#
#S22 = [902.01, 1038.82, 987.14, 1054.97, 1013.17, 1016.81, 1064.81, 1066.06, 1040.24, 1071.12, 1078.66]
#
#S12 = [876.12, 955.04, 970.54, 987.60, 999.11, 1005.29, 1015.50, 1026.81, 1031.10, 1047.45, 1057.43]

Sv = []
for i, s11 in enumerate(S11):
    s22 = S22[i]
    s12 = S12[i]
    Sv.append(math.sqrt(s11**2 - s11*s22 + s22**2 + 3*s12**2))

# Quad8
#DOFs_2 = [2372, 6314, 9890, 13648, 18340, 22036, 25724, 35096]
#
#S11 = [1067.99, 1074.89, 1070.44, 1070.46, 1077.27, 1074.91, 1072.23, 1073.12]
#
#S22 = [1070.88, 1077.97, 1070.42, 1074.49, 1073.20, 1077.33, 1073.07, 1070.20]
#
#S12 = [1049.97, 1058.90, 1063.10, 1066.42, 1064.53, 1065.43, 1067.58, 1065.83]

# Tri6
DOFs_2 = [3132, 10058, 15892, 22286, 36028, 42344, 49044, 60214]

S11 = [1063.33, 1069.57, 1068.94, 1076.37, 1072.80, 1072.04, 1079.17, 1079.79]

S22 = [1062.98, 1070.43, 1069.32, 1071.62, 1071.71, 1072.23, 1073.55, 1072.67]

S12 = [1049.67, 1061.93, 1064.01, 1064.33, 1068.42, 1068.85, 1065.88, 1065.82]


Sv_2 = []
for i, s11 in enumerate(S11):
    s22 = S22[i]
    s12 = S12[i]
    Sv_2.append(math.sqrt(s11**2 - s11*s22 + s22**2 + 3*s12**2))



# for 3D Von Miese
# Tet4
#DOFs = [ 1101, 1725, 3039, 4440, 5652, 6366, 10461,12432]
#S11 = [ 64.39, 56.72, 43.49, 40.13, 38.20, 37.08, 34.00, 34.34]
#S22 = [ 64.36, 56.23, 44.52, 42.26, 41.78, 40.85, 34.45, 34.54]
#S33 = [ -24.36, -29.24, -28.85, -30.56, -30.15, -30.88, -35.19, -35.33]
#S23 = [ 6.62, 4.76, 6.33, 4.92, 4.01, 3.57, 1.99, 2]
#S31 = [ 0.20, 2.69, -1.22, -0.98, -0.53, -0.74, 0.77, 0.32]
#S12 = [ -6,68e-03, 1.08, 1.40, 0.71, 0.47, 0.61, 0.85, 0.65]
#
#Sv = []
#for i, s11 in enumerate(S11):
#    s22 = S22[i]
#    s33 = S33[i]
#    s12 = S12[i]
#    s23 = S23[i]
#    s31 = S31[i]
#    Sv.append(math.sqrt(0.5*((s11-s22)**2 + (s22-s33)**2 +\
#     (s33-s11)**2 + 6*(s12**2 + s23**2 + s31**2))))
#
## Tet10
#
#DOFs_2 = [588, 906, 1352, 2258, 3396, 4351, 5243, 11721]
#S11 = [38.21,  34.00, 33.18, 33.25, 33.19, 33.19, 33.12, 33.21]
#S22 = [42.81,  35.65, 35.06, 35.02, 34.13, 34.13, 34.13, 34.11]
#S33 = [-30.31,  -35.28, -35.05, -35.02, -35.28, -35.23, -35.24, -35.21]
#S23 = [4.01,  3.27, 3.79, 3.03, 3.31, 3.32, 3.32, 3.29]
#S31 = [1.54,  1.62, 1.00, 1.01, 1.03, 1.01, 1.02, 1.02]
#S12 = [0.71,  0.61, 0.85, 0.21, 0.21, 0.25, 0.25,0.26]
##
#Sv_2 = []
#for i, s11 in enumerate(S11):
#    s22 = S22[i]
#    s33 = S33[i]
#    s12 = S12[i]
#    s23 = S23[i]
#    s31 = S31[i]
#    Sv_2.append(math.sqrt(0.5*((s11-s22)**2 + (s22-s33)**2 +\
#     (s33-s11)**2 + 6*(s12**2 + s23**2 + s31**2))))


# Create plots with pre-defined labels.
# Alternatively, you can pass labels explicitly when calling `legend`.
fig, ax = plt.subplots()
ax.plot(DOFs, Sv, 'g-', label='Tri3')
ax.plot(DOFs_2, Sv_2, 'b-', label='Tri6')
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
# pylab.ylim([0.55,1.1])
plt.xlabel('DOFs [-]')
plt.ylabel(r'von Mises stress [N/mm2]')
# Set the fontsize
# for label in legend.get_texts():
#     label.set_fontsize('large')
#
# for label in legend.get_lines():
#     label.set_linewidth(1.5)  # the legend line width

plt.show()



print(Sv)
