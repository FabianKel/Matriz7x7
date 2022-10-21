

print ("Primer Renglon")
c11 = int(input())
c12 = int(input())
c13 = int(input())
c14 = int(input())
c15 = int(input())
c16 = int(input())
c17 = int(input())
print("Segundo Renglon")
c21 = int(input())
c22 = int(input())
c23 = int(input())
c24 = int(input())
c25 = int(input())
c26 = int(input())
c27 = int(input())
print("Tercer Renglon")
c31 = int(input())
c32 = int(input())
c33 = int(input())
c34 = int(input())
c35 = int(input())
c36 = int(input())
c37 = int(input())
print("Cuarto Renglon")
c41 = int(input())
c42 = int(input())
c43 = int(input())
c44 = int(input())
c45 = int(input())
c46 = int(input())
c47 = int(input())
print("Quinto Renglon")
c51 = int(input())
c52 = int(input())
c53 = int(input())
c54 = int(input())
c55 = int(input())
c56 = int(input())
c57 = int(input())
print("Sexto Renglon")
c61 = int(input())
c62 = int(input())
c63 = int(input())
c64 = int(input())
c65 = int(input())
c66 = int(input())
c67 = int(input())
print("Septimo Renglon")
c71 = int(input())
c72 = int(input())
c73 = int(input())
c74 = int(input())
c75 = int(input())
c76 = int(input())
c77 = int(input())


print("| " + str(c11) + " " + str(c12) + " " + str(c13) + " " + str(c14) + " " + str(c15) + " " + str(c16) + " " + str(c17) + "|" )
print("| " + str(c21) + " " + str(c22) + " " + str(c23) + " " + str(c24) + " " + str(c25) + " " + str(c26) + " " + str(c27) + "|" )
print("| " + str(c31) + " " + str(c32) + " " + str(c33) + " " + str(c34) + " " + str(c35) + " " + str(c36) + " " + str(c37) + "|" )
print("| " + str(c41) + " " + str(c42) + " " + str(c43) + " " + str(c44) + " " + str(c45) + " " + str(c46) + " " + str(c47) + "|" )
print("| " + str(c51) + " " + str(c52) + " " + str(c53) + " " + str(c54) + " " + str(c55) + " " + str(c56) + " " + str(c57) + "|" )
print("| " + str(c61) + " " + str(c62) + " " + str(c63) + " " + str(c64) + " " + str(c65) + " " + str(c66) + " " + str(c67) + "|" )
print("| " + str(c71) + " " + str(c72) + " " + str(c73) + " " + str(c74) + " " + str(c75) + " " + str(c76) + " " + str(c77) + "|" )

def reducir ():
    print("")
    a11 =(c11*c22)-(c21*c12)
    a21 =(c21*c32)-(c31*c22)
    a31 =(c31*c42)-(c41*c32)
    a41 =(c41*c52)-(c51*c42)
    a51 =(c51*c62)-(c61*c52)
    a61 =(c61*c72)-(c71*c62)

    a12 =(c12*c23)-(c22*c13)
    a22 =(c22*c33)-(c32*c23)
    a32 =(c32*c43)-(c42*c33)
    a42 =(c42*c53)-(c52*c43)
    a52 =(c52*c63)-(c62*c53)
    a62 =(c62*c73)-(c72*c63)

    a13 =(c13*c24)-(c23*c14)
    a23 =(c23*c34)-(c33*c24)
    a33 =(c33*c44)-(c43*c34)
    a43 =(c43*c54)-(c53*c44)
    a53 =(c53*c64)-(c63*c54)
    a63 =(c63*c74)-(c73*c64)

    a14 =(c14*c25)-(c24*c15)
    a24 =(c24*c35)-(c34*c25)
    a34 =(c34*c45)-(c44*c35)
    a44 =(c44*c55)-(c54*c45)
    a54 =(c54*c65)-(c64*c55)
    a64 =(c64*c75)-(c74*c65)

    a15 =(c15*c26)-(c25*c16)
    a25 =(c25*c36)-(c35*c26)
    a35 =(c35*c46)-(c45*c36)
    a45 =(c45*c56)-(c55*c46)
    a55 =(c55*c66)-(c65*c56)
    a65 =(c65*c76)-(c75*c66)

    a16 =(c16*c27)-(c26*c17)
    a26 =(c26*c37)-(c36*c27)
    a36 =(c36*c47)-(c46*c37)
    a46 =(c46*c57)-(c56*c47)
    a56 =(c56*c67)-(c66*c57)
    a66 =(c66*c77)-(c76*c67)


    print("| " + str(a11) + " " + str(a12) + " " + str(a13) + " " + str(a14) + " " + str(a15) + " " + str(a16) + " |")
    print("| " + str(a21) + " " + str(a22) + " " + str(a23) + " " + str(a24) + " " + str(a25) + " " + str(a26) + " |")
    print("| " + str(a31) + " " + str(a32) + " " + str(a33) + " " + str(a34) + " " + str(a35) + " " + str(a36) + " |")
    print("| " + str(a41) + " " + str(a42) + " " + str(a43) + " " + str(a44) + " " + str(a45) + " " + str(a46) + " |")
    print("| " + str(a51) + " " + str(a52) + " " + str(a53) + " " + str(a54) + " " + str(a55) + " " + str(a56) + " |")
    print("| " + str(a61) + " " + str(a62) + " " + str(a63) + " " + str(a64) + " " + str(a65) + " " + str(a66) + " |")

    print("")
    b11 =((a11*a22)-(a21*a12))/c22
    b21 =((a21*a32)-(a31*a22))/c23
    b31 =((a31*a42)-(a41*a32))/c24
    b41 =((a41*a52)-(a51*a42))/c25
    b51 =((a51*a62)-(a61*a52))/c26


    b12 =((a12*a23)-(a22*a13))/c32
    b22 =((a22*a33)-(a32*a23))/c33
    b32 =((a32*a43)-(a42*a33))/c34
    b42 =((a42*a53)-(a52*a43))/c35
    b52 =((a52*a63)-(a62*a53))/c36


    b13 =((a13*a24)-(a23*a14))/c42
    b23 =((a23*a34)-(a33*a24))/c43
    b33 =((a33*a44)-(a43*a34))/c44
    b43 =((a43*a54)-(a53*a44))/c45
    b53 =((a53*a64)-(a63*a54))/c46
 
    b14 =(((a14*a25)-(a24*a15))/c52)
    b24 =(((a24*a35)-(a34*a25))/c53)
    b34 =(((a34*a45)-(a44*a35))/c54)
    b44 =(((a44*a55)-(a54*a45))/c55)
    b54 =(((a54*a65)-(a64*a55))/c56)


    b15 =((a15*a26)-(a25*a16))/c62
    b25 =((a25*a36)-(a35*a26))/c63
    b35 =(((a35*a46)-(a45*a36))/c64)
    b45 =((a45*a56)-(a55*a46))/c65
    b55 =((a55*a66)-(a65*a56))/c66
    

    print("| " + str(b11) + " " + str(b12) + " " + str(b13) + " " + str(b14) + " " + str(b15) + " |" )
    print("| " + str(b21) + " " + str(b22) + " " + str(b23) + " " + str(b24) + " " + str(b25) + " |" )
    print("| " + str(b31) + " " + str(b32) + " " + str(b33) + " " + str(b34) + " " + str(b35) + " |" )
    print("| " + str(b41) + " " + str(b42) + " " + str(b43) + " " + str(b44) + " " + str(b45) + " |" )
    print("| " + str(b51) + " " + str(b52) + " " + str(b53) + " " + str(b54) + " " + str(b55) + " |" )

    print("")
    d11 =((b11*b22)-(b21*b12))/a22
    d21 =((b21*b32)-(b31*b22))/a23
    d31 =((b31*b42)-(b41*b32))/a24
    d41 =((b41*b52)-(b51*b42))/a25

    d12 =((b12*b23)-(b22*b13))/a32
    d22 =((b22*b33)-(b32*b23))/a33
    d32 =((b32*b43)-(b42*b33))/a34
    d42 =((b42*b53)-(b52*b43))/a35

    d13 =((b13*b24)-(b23*b14))/a42
    d23 =((b23*b34)-(b33*b24))/a43
    d33 =((b33*b44)-(b43*b34))/a44
    d43 =((b43*b54)-(b53*b44))/a45

    d14 =((b14*b25)-(b24*b15))/a52
    d24 =((b24*b35)-(b34*b25))/a53
    d34 =((b34*b45)-(b44*b35))/a54
    d44 =((b44*b55)-(b54*b45))/a55
 
    print("| " + str(d11) + " " + str(d12) + " " + str(d13) + " " + str(d14) + " |" )
    print("| " + str(d21) + " " + str(d22) + " " + str(d23) + " " + str(d24) + " |" )
    print("| " + str(d31) + " " + str(d32) + " " + str(d33) + " " + str(d34) + " |" )
    print("| " + str(d41) + " " + str(d42) + " " + str(d43) + " " + str(d44) + " |" )

    print("")
    e11 =((d11*d22)-(d21*d12))/b22
    e21 =((d21*d32)-(d31*d22))/b23
    e31 =((d31*d42)-(d41*d32))/b24

    e12 =((d12*d23)-(d22*d13))/b32
    e22 =((d22*d33)-(d32*d23))/b33
    e32 =((d32*d43)-(d42*d33))/b34

    e13 =((d13*d24)-(d23*d14))/b42
    e23 =((d23*d34)-(d33*d24))/b43
    e33 =((d33*d44)-(d43*d34))/b44

    print("| " + str(e11) + " " + str(e12) + " " + str(e13) + " |" )
    print("| " + str(e21) + " " + str(e22) + " " + str(e23) + " |" )
    print("| " + str(e31) + " " + str(e32) + " " + str(e33) + " |" )


    print("")
    f11 =((e11*e22)-(e21*e12))/d22
    f21 =((e21*e32)-(e31*e22))/d23

    f12 =((e12*e23)-(e22*e13))/d32
    f22 =((e22*e33)-(e32*e23))/d33

    print("| " + str(f11) + " " + str(f12) + " |" )
    print("| " + str(f21) + " " + str(f22) + " |" )

    det= (f11*f22)-(f12*f21)

    print("")
    print("Determinante: " + str(det))

reducir()











