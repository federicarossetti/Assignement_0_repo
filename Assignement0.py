#Heat loss through a double pane window
L=0.8
w=1.5
L_glass=0.004
L_air=0.01
k_glass=0.78
k_air=0.026
T1inf=20
T2inf=-10
h1=10
h2=40

A=L*w
R_conv1=1/(h1*A)
R_conv2=1/(h2*A)
R_cond_glass=L_glass/(k_glass*A)
R_cond_air=L_air/(k_air*A)
R_tot=R_conv1+R_conv2+2*R_cond_glass+R_cond_air
Q=(T1inf-T2inf)/R_tot
DeltaT=R_cond*Q
T2=T1inf-Q*R_conv1
