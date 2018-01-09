import pidly

#start session
idl=pidly.IDL('/opt/idl/exelis/idl85/bin/idl')#give correct path to executable idl file

#create python variables or arrays
xp=[1,2,3]
yp=[1,2,3]
exp=[0.1,0.1,0.1]
eyp=[0.1,0.1,0.1]

#create idl arrays
idl('x=[]')
idl('y=[]')
idl('ex=[]')
idl('ey=[]')

#assign python variables to IDL variables
idl.x=xp
idl.y=yp
idl.ex=exp
idl.ey=eyp

#use procedure with IDl variables
idl('FITEXY,x,y,A,B,X_SIG=ex,Y_SIG=ey, sigma_A_B, chi_sq, q')

#Use IDL output
print idl.sigma_A_B[0]

#end session
idl.close()



