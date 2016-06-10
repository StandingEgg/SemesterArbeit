
import math

# Quad4

# DOFs = [854, 2320, 3448, 4882, 7856, 9128, 12310, 21060]
#
# S11 = [1214.92, 1140.36, 1178.80, 1118.92, 1065.53, 1159.79, 1115.66, 1104.15]
#
# S22 = [1138.91, 1167.07, 1083.72, 1143.34, 1173.20, 1084.34, 1117.62, 1112.87]
#
# S12 = [917.94, 995.45, 1017.86, 1024.63, 1032.94, 1033.29, 1039.59, 1045.15]
#
# S_analy = 1

# Quad8

# DOFs = [2372, 6314, 9890, 13648, 18340, 22036, 25724, 35096]
#
# S11 = [1067.99, 1074.89, 1070.44, 1070.46, 1077.27, 1074.91, 1072.23, 1073.12]
#
# S22 = [1070.88, 1077.97, 1070.42, 1074.49, 1073.20, 1077.33, 1073.07, 1070.20]
#
# S12 = [1049.97, 1058.90, 1063.10, 1066.42, 1064.53, 1065.43, 1067.58, 1065.83]

# Tri3

DOFs = [870, 2682, 4172, 5788?, 9354, 10952, 15490, 27332]

S11 = [1060.97, 1034.59, 1102.81, 927.25?, 1106.52, 1102.23, 1064.35, 1065.72]

S22 = [902.01, 1038.82, 987.14, 563.64?, 1013.17, 1016.81, 1064.81, 1066.06]

S33 = [876.12, 955.04, 970.54, 461.74?, 999.11, 1005.29, 1015.50, 1026.81]

Sv = []
for i, s11 in enumerate(S11):
    s22 = S22[i]
    s12 = S12[i]
    Sv.append(math.sqrt(s11**2 - s11*s22 + s22**2 + 3*s12**2))


# Create plots with pre-defined labels.
# Alternatively, you can pass labels explicitly when calling `legend`.
fig, ax = plt.subplots()
ax.plot(DOFs, Sv, 'g-', label='Quad4 von Mises stress')
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
# pylab.ylim([0.55,1.1])
plt.xlabel('DOFs [-]')
plt.ylabel(r'von Mises stress [-]')
# Set the fontsize
# for label in legend.get_texts():
#     label.set_fontsize('large')
#
# for label in legend.get_lines():
#     label.set_linewidth(1.5)  # the legend line width

plt.show()



print(Sv)
