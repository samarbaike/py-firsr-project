n=int(input("Enter number of variables: "))
def det_2x2(a11, a12, a21, a22): 
    determinant2=a11*a22-a12*a21
    return determinant2
def det_3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    determinant3=a11*a22*a33 + a12*a23*a31 + a13*a21*a32 - a13*a22*a31 - a12*a21*a33 - a11*a23*a32
    return determinant3
def det_4x4(a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44):
    determinant4=a11*det_3x3(a22, a23, a24, a32, a33, a34, a42, a43, a44)-a12*det_3x3(a21, a23, a24, a31, a33, a34, a41, a43, a44)+a13*det_3x3(a21, a22, a24, a31, a32, a34, a41, a42, a44)-a14*det_3x3(a21, a22, a23, a31, a32, a33, a41, a42, a43)
    return determinant4
def det_5x5(a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45, a51, a52, a53, a54, a55):
    determinant5=a11*det_4x4(a22, a23, a24, a25, a32, a33, a34, a35, a42, a43, a44, a45, a52, a53, a54, a55)-a12*det_4x4(a21, a23, a24, a25, a31, a33, a34, a35, a41, a43, a44, a45, a51, a53, a54, a55)+a13*det_4x4(a21, a22, a24, a25, a31, a32, a34, a35, a41, a42, a44, a45, a51, a52, a54, a55)-a14*det_4x4(a21, a22, a23, a25, a31, a32, a33, a35, a41, a42, a43, a45, a51, a52, a53, a55)+a15*det_4x4(a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44, a51, a52, a53, a54)
    return determinant5

if n==2:
    a11=int(input("Enter a11 of equation: "))
    a12=int(input("Enter a12 of equation: "))
    a21=int(input("Enter a21 of equation: "))
    a22=int(input("Enter a22 of equation: "))
    b1=int(input("Enter b1 of equation: "))
    b2=int(input("Enter b2 of equation: "))
    if a11/a21==a12/a22==b1/b2:
        print("The system is consistent, and there is infinitely many solutions")
    elif a11/a21==a12/a22!=b1/b2:
        print("The system is inconsistent, that is why there is no solution")
    elif det_2x2(a11, a12, a21, a22)==0:
        print("The system is inconsistent, that is why there is no solution")
    
    else:
        x1=det_2x2(b1, a12, b2, a22)/det_2x2(a11, a12, a21, a22)
        x2=det_2x2(a11, b1, a21, b2)/det_2x2(a11, a12, a21, a22)
        print("The system is consistent, and its solution:")
        print("x1 =", x1)
        print("x2 =", x2)

#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
#3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

elif n==3:
    a11=int(input("Enter a11 of equation: "))
    a12=int(input("Enter a12 of equation: "))
    a13=int(input("Enter a13 of equation: "))
    a21=int(input("Enter a21 of equation: "))
    a22=int(input("Enter a22 of equation: "))
    a23=int(input("Enter a23 of equation: "))
    a31=int(input("Enter a31 of equation: "))
    a32=int(input("Enter a32 of equation: "))
    a33=int(input("Enter a33 of equation: "))
    b1=int(input("Enter b1 of equation: "))
    b2=int(input("Enter b2 of equation: "))
    b3=int(input("Enter b3 of equation: "))
    if a11/a21==a12/a22==a13/a23==b1/b2 or a11/a31==a12/a32==a13/a33==b1/b3 or a21/a31==a22/a32==a23/a33==b2/b3:
        print("The system is consistent, and there is infinitely many solutions")
    elif a11/a21==a12/a22==a13/a23!=b1/b2 or a11/a31==a12/a32==a13/a33!=b1/b3 or a21/a31==a22/a32==a23/a33!=b2/b3:
        print("The system is inconsistent, that is why there is no solution")
    elif det_3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33)==0:
        print("The system is inconsistent, that is why there is no solution")
    else:
        x1=det_3x3(b1, a12, a13, b2, a22, a23, b3, a32, a33)/det_3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
        x2=det_3x3(a11, b1, a13, a21, b2, a23, a31, b3, a33)/det_3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
        x3=det_3x3(a11, a12, b1, a21, a22, b2, a31, a32, b3)/det_3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
        print("The system is consistent, and its solution:")
        print("x1 =", x1)
        print("x2 =", x2)
        print("x3 =", x3)


#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

elif n==4:
    a11=int(input("Enter a11 of equation: "))
    a12=int(input("Enter a12 of equation: "))
    a13=int(input("Enter a13 of equation: "))
    a14=int(input("Enter a14 of equation: "))
    a21=int(input("Enter a21 of equation: "))
    a22=int(input("Enter a22 of equation: "))
    a23=int(input("Enter a23 of equation: "))
    a24=int(input("Enter a24 of equation: "))
    a31=int(input("Enter a31 of equation: "))
    a32=int(input("Enter a32 of equation: "))
    a33=int(input("Enter a33 of equation: "))
    a34=int(input("Enter a34 of equation: "))
    a41=int(input("Enter a41 of equation: "))
    a42=int(input("Enter a42 of equation: "))
    a43=int(input("Enter a43 of equation: "))
    a44=int(input("Enter a44 of equation: "))
    b1=int(input("Enter b1 of equation: "))
    b2=int(input("Enter b2 of equation: "))
    b3=int(input("Enter b3 of equation: "))
    b4=int(input("Enter b4 of equation: "))
    if a11/a21==a12/a22==a13/a23==a14/a24==b1/b2 or a11/a31==a12/a32==a13/a33==a14/a34==b1/b3 or a11/a41==a12/a42==a13/a43==a14/a44==b1/b4 or a21/a31==a22/a32==a23/a33==a24/a34==b2/b3 or a21/a41==a22/a42==a23/a43==a24/a44==b2/b4 or a31/a41==a32/a42==a33/a43==a34/a44==b3/b4:
        print("The system is consistent, and there is infinitely many solutions")
    elif a11/a21==a12/a22==a13/a23==a14/a24!=b1/b2 or a11/a31==a12/a32==a13/a33==a14/a34!=b1/b3 or a11/a41==a12/a42==a13/a43==a14/a44!=b1/b4 or a21/a31==a22/a32==a23/a33==a24/a34!=b2/b3 or a21/a41==a22/a42==a23/a43==a24/a44!=b2/b4 or a31/a41==a32/a42==a33/a43==a34/a44!=b3/b4:
        print("The system is inconsistent, that is why there is no solution")
    elif det_4x4(a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44)==0:
        print("The system is inconsistent, that is why there is no solution")

    else:
        x1=det_4x4(b1, a12, a13, a14, b2, a22, a23, a24, b3, a32, a33, a34, b4, a42, a43, a44)/det_4x4(a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44)
        x2=det_4x4(a11, b1, a13, a14, a21, b2, a23, a24, a31, b3, a33, a34, a41, b4, a43, a44)/det_4x4(a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44)
        x3=det_4x4(a11, a12, b1, a14, a21, a22, b2, a24, a31, a32, b3, a34, a41, a42, b4, a44)/det_4x4(a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44)
        x4=det_4x4(a11, a12, a13, b1, a21, a22, a23, b2, a31, a32, a33, b3, a41, a42, a43, b4)/det_4x4(a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44)
        print("The system is consistent, and its solution:")
        print("x1 =", x1)
        print("x2 =", x2)
        print("x3 =", x3)
        print("x4 =", x4)

elif n==5:
    a11=int(input("Enter a11 of equation: "))
    a12=int(input("Enter a12 of equation: "))
    a13=int(input("Enter a13 of equation: "))
    a14=int(input("Enter a14 of equation: "))
    a15=int(input("Enter a15 of equation: "))
    a21=int(input("Enter a21 of equation: "))
    a22=int(input("Enter a22 of equation: "))
    a23=int(input("Enter a23 of equation: "))
    a24=int(input("Enter a24 of equation: "))
    a25=int(input("Enter a25 of equation: "))
    a31=int(input("Enter a31 of equation: "))
    a32=int(input("Enter a32 of equation: "))
    a33=int(input("Enter a33 of equation: "))
    a34=int(input("Enter a34 of equation: "))
    a35=int(input("Enter a35 of equation: "))
    a41=int(input("Enter a41 of equation: "))
    a42=int(input("Enter a42 of equation: "))
    a43=int(input("Enter a43 of equation: "))
    a44=int(input("Enter a44 of equation: "))
    a45=int(input("Enter a45 of equation: "))
    a51=int(input("Enter a51 of equation: "))
    a52=int(input("Enter a52 of equation: "))
    a53=int(input("Enter a53 of equation: "))
    a54=int(input("Enter a54 of equation: "))
    a55=int(input("Enter a55 of equation: "))
    b1=int(input("Enter b1 of equation: "))
    b2=int(input("Enter b2 of equation: "))
    b3=int(input("Enter b3 of equation: "))
    b4=int(input("Enter b4 of equation: "))
    b5=int(input("Enter b5 of equation: "))
    if a11/a21==a12/a22==a13/a23==a14/a24==a15/a25==b1/b2 or a11/a31==a12/a32==a13/a33==a14/a34==a15/a35==b1/b3 or a11/a41==a12/a42==a13/a43==a14/a44==a15/a45==b1/b4 or a11/a51==a12/a52==a13/a53==a14/a54==a15/a55==b1/b5:
        print("The system is consistent, and there is infinitely many solutions")
    elif a21/a31==a22/a32==a23/a33==a24/a34==a25/a35==b2/b3 or a21/a41==a22/a42==a23/a43==a24/a44==a25/a45==b2/b4 or a21/a51==a22/a52==a23/a53==a24/a54==a25/a55==b2/b5 or a31/a41==a32/a42==a33/a43==a34/a44==a35/a45==b3/b4 or a31/a51==a32/a52==a33/a53==a34/a54==a35/a55==b3/b5 or a41/a51==a42/a52==a43/a53==a44/a54==a45/a55==b4/b5:
        print("The system is consistent, and there is infinitely many solutions")
    elif a11/a21==a12/a22==a13/a23==a14/a24==a15/a25!=b1/b2 or a11/a31==a12/a32==a13/a33==a14/a34==a15/a35!=b1/b3 or a11/a41==a12/a42==a13/a43==a14/a44==a15/a45!=b1/b4 or a11/a51==a12/a52==a13/a53==a14/a54==a15/a55!=b1/b5:
        print("The system is inconsistent, that is why there is no solution")
    elif a21/a31==a22/a32==a23/a33==a24/a34==a25/a35!=b2/b3 or a21/a41==a22/a42==a23/a43==a24/a44==a25/a45!=b2/b4 or a21/a51==a22/a52==a23/a53==a24/a54==a25/a55!=b2/b5 or a31/a41==a32/a42==a33/a43==a34/a44==a35/a45!=b3/b4 or a31/a51==a32/a52==a33/a53==a34/a54==a35/a55!=b3/b5 or a41/a51==a42/a52==a43/a53==a44/a54==a45/a55!=b4/b5:
        print("The system is inconsistent, that is why there is no solution")
    elif det_5x5(a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45, a51, a52, a53, a54, a55)==0:
        print("The system is inconsistent, that is why there is no solution")
    else:
        x1=det_5x5(b1, a12, a13, a14, a15, b2, a22, a23, a24, a25, b3, a32, a33, a34, a35, b4, a42, a43, a44, a45, b5, a52, a53, a54, a55)/det_5x5(a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45, a51, a52, a53, a54, a55)
        x2=det_5x5(a11, b1, a13, a14, a15, a21, b2, a23, a24, a25, a31, b3, a33, a34, a35, a41, b4, a43, a44, a45, a51, b5, a53, a54, a55)/det_5x5(a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45, a51, a52, a53, a54, a55)
        x3=det_5x5(a11, a12, b1, a14, a15, a21, a22, b2, a24, a25, a31, a32, b3, a34, a35, a41, a42, b4, a44, a45, a51, a52, b5, a54, a55)/det_5x5(a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45, a51, a52, a53, a54, a55)
        x4=det_5x5(a11, a12, a13, b1, a15, a21, a22, a23, b2, a25, a31, a32, a33, b3, a35, a41, a42, a43, b4, a45, a51, a52, a53, b5, a55)/det_5x5(a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45, a51, a52, a53, a54, a55)
        x5=det_5x5(a11, a12, a13, a14, b1, a21, a22, a23, a24, b2, a31, a32, a33, a34, b3, a41, a42, a43, a44, b4, a51, a52, a53, a54, b5)/det_5x5(a11, a12, a13, a14, a15, a21, a22, a23, a24, a25, a31, a32, a33, a34, a35, a41, a42, a43, a44, a45, a51, a52, a53, a54, a55)
        print("The system is consistent, and its solution:")
        print("x1 =", x1)
        print("x2 =", x2)
        print("x3 =", x3)
        print("x4 =", x4)
        print("x5 =", x5)
