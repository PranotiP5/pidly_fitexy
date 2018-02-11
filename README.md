# pidly_fitexy
This is a python code to run IDl fitexy procedure using  python variables.
Other procedures can be used the same way.

run the python code on terminal
> python test.py

Also, make sure you have all the necessary idl .pro files to run fitexy procedure.

Detailed explanation:
Step 1: Create an IDL session:
Make sure you have pexpect, pidly modules of python installed.

    Type "pip install pidly"

If that fails:

    Download https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    run it (type "python get-pip.py")
    Type "pip install pidly"


import pidly
idl=pidly.IDL("path/to/idl")

The IDL path to the executable IDL file. You can check .bashrc or .tcshrc file. Generally it is in /usr/local/bin/idl

Step 2: create your python varaibles :
xp=[1,2,3]
yp=[1,2,3]
exp=[0.1,0.1,0.1]
eyp=[0.1,0.1,0.1]

Step 3: Create IDL Variables
So, the main point is write IDL commands in idl('...').
Example:
idl('x=[]')
idl('y=[]')
idl('ex=[]')
idl('ey=[]')

Step 4: Assign Python variables to IDl Variables:
All IDl variables can be accessed by idl.variable_name
Example:
idl.x=xp
idl.y=yp
idl.ex=exp
idl.ey=eyp
Here, we assigned the variables we need to pass to IDL procedure

Step 5: Use the procedure
idl('FITEXY,x,y,A,B,X_SIG=ex,Y_SIG=ey, sigma_A_B, chi_sq, q')

Step 6: Use the IDL procedure Output
print idl.sigma_A_B[0]

Step 7: Close IDL session
idl.close()




