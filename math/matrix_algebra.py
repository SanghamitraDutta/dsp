# Matrix Algebra
import numpy as np

# Do not change these variables
#Matrices - Double [] and capital letters as variables
A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

# Vectors - single [] and small letters as variables
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5])


# Q1: record the dimensions of A, B, C, D, u, v respectively in the dict below. 
#     Do not type the answers, make python do the work

dimensions = {
    'A': A.shape,
    'B': B.shape,
    'C': C.shape,
    'D': D.shape,
    'u': u.shape,
    'v': v.shape,
    'w': w.shape,
}

print(dimensions)

# Q2: vector operations
#     assign `None` if the operation is not defined
#     do not type the answers, make python do the work
alpha = 6

u_plus_v = u+v               # or np.add(u,v)            # u+v
u_minus_v = u-v              # or np.subtract(u,v)           # u-v
alpha_times_u = alpha * u    #alpha * u, alpha = 6
u_dot_v = np.dot(u,v)        #u . v
norm_u = np.linalg.norm(u)              # ||u|| 


print('u+v=',u_plus_v,             # u+v
      'u-v=', u_minus_v,           # u-v
      'alpha*u=',alpha_times_u,    # alpha * u, alpha = 6
      'u.v=', u_dot_v,             # u . v
      '||u||=', norm_u)            # ||u|| 



# Q3: compute the following and assign to variables below:
#     do not type the answers, make python do the work

for i in range(5):
    try:
        if i == 0:
            print('A_plus_C =')
            A_plus_C = A+C     # A + C
            print(A_plus_C)
        elif i == 1:
            print('A_minus_Ctranspose =')
            A_minus_Ctranspose = A- (C.T) # or np.subtract(A,C.T)   # A - C.T
            print( A_minus_Ctranspose)
        elif i == 2:
            print('Ctranspose_plus_3D =')
            Ctranspose_plus_3D = C.T + 3*D   # C.T + 3*D
            print(Ctranspose_plus_3D)
        elif i == 3:
            print('B_times_A=')
            B_times_A = np.dot(B,A) # Not defined for np.multipy(B,A) & B*A as they r used for * constnats # B*A
            print(B_times_A)
        elif i == 4:
            print('B_times_Atranspose=')
            B_times_Atranspose = np.dot(B,(A.T))   # B*A.T
            print(B_times_Atranspose)       
     except Exception as ev:
        print("Failed as: %s" % ev)
        continue

for i in range(5):
    try:
        if i == 0:
            print('B_times_C =')
            B_times_C = np.dot(B,C)         # B*C
            print(B_times_C)
        elif i == 1:
            print('C_times_B =')
            C_times_B = np.dot(C,B)  # C*B 
            print(C_times_B)
        elif i == 2:
            print('B_exp_4 =')
            B_exp_4 = np.dot(B,np.dot(B,np.dot(B,B)))   # B^4
            print(B_exp_4)
        elif i == 3:
            print('A_times_Atranspose')
            A_times_Atranspose = np.dot(A,A.T)   # A*A.T
            print(A_times_Atranspose)
        elif i == 4:
            print('Dtranspose_times_D=')
            Dtranspose_times_D = np.dot(D.T,D)   # D.T*D
            print(Dtranspose_times_D)       
    except Exception as ev:
        print("Failed as: %s" % ev)
        continue

    

