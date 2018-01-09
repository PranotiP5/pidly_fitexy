import pidly

#start session
idl=pidly.IDL('/opt/idl/exelis/idl85/bin/idl')#give correct path to executable idl file

#create python variables or arrays
x1=[1,2,3]
ex1=[0.1,0.1,0.1]

#create idl arrays
idl('x=[]')
idl('y=x')
idl('ex=x')
idl('ey=x')

#assign python variables to IDL variables
idl.x=x1
idl.y=idl.x
idl.ex=ex1
idl.ey=idl.x

#use procedure with IDl variables
idl('FITEXY,x,y,A,B,X_SIG=ex,Y_SIG=ey, sigma_A_B, chi_sq, q')

#Use IDL output
print idl.sigma_A_B[0]

#end session
idl.close()




