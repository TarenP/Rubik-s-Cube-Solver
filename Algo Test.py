import numpy as np
# from picamera import PiCamera
from PIL import Image
# import RPi.GPIO as GPIO
from time import sleep
import collections
import random

DIR1 = 20
STEP1 = 21
DIR2 = 13
STEP2 = 6
DIR3 = 19
STEP3 = 26
DIR4 = 15
STEP4 = 14
DIR5 = 3
STEP5 = 2
DIR6 = 17
STEP6 = 4
DIR7 = 11
STEP7 = 0
DIR8 = 27
STEP8 = 22

CW = 1
CCW = 0

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(DIR1, GPIO.OUT)
# GPIO.setup(STEP1, GPIO.OUT)
# GPIO.setup(DIR3, GPIO.OUT)
# GPIO.setup(STEP3, GPIO.OUT)
# GPIO.setup(DIR2, GPIO.OUT)
# GPIO.setup(STEP2, GPIO.OUT)
# GPIO.setup(DIR4, GPIO.OUT)
# GPIO.setup(STEP4, GPIO.OUT)
# GPIO.setup(DIR5, GPIO.OUT)
# GPIO.setup(STEP5, GPIO.OUT)
# GPIO.setup(DIR6, GPIO.OUT)
# GPIO.setup(STEP6, GPIO.OUT)
# GPIO.setup(DIR7, GPIO.OUT)
# GPIO.setup(STEP7, GPIO.OUT)
# GPIO.setup(DIR8, GPIO.OUT)
# GPIO.setup(STEP8, GPIO.OUT)

#delay between steps for motor turns
delay = .015
sdelay = .03
#Sensitivity for reseting cube position after turn
# sensitivity = 3


      
#camera setup
# camera = PiCamera()
#Res must be divisible by 3
res = 720
# camera.resolution = (res, res)

faceColors = ["pink", "pink", "pink", "pink", "pink", "pink", "pink", "pink", "pink"]

#Solved cube corners for reference
AQN = ["yellow", "blue", "orange"]
BJM = ["yellow", "green", "orange"]
DRE = ["yellow", "blue", "red"]
CFI = ["yellow", "red", "green"]
HSU = ["red", "blue", "white"]
GLV = ["red", "green", "white"]
XTO = ["white", "blue", "orange"]
WKP = ["white", "green", "orange"]

am = ["yellow", "orange"]
bi = ["yellow", "green"]
ce = ["yellow", "red"]
dq = ["yellow", "blue"]
fl = ["red", "green"]
gu = ["red", "white"]
hr = ["red", "blue"]
tn = ["blue", "orange"]
sx = ["blue", "white"]
kv = ["green", "white"]
ow = ["orange", "white"]
jp = ["green", "orange"]



def Xturn():
    print("Xturn")
def Xprimeturn():
    print("Xprimeturn")
def Yturn():
    print("Yturn")

def Yprimeturn():
    print("Yprimeturn")

def Rturn():
    print("Rturn")
def Rprimeturn():
    print("Rprimeturn")

def Lturn():
    print("Lturn")

def Lprimeturn():
    print("Lprimeturn")
def Bturn():
    print("Bturn")

def Bprimeturn():
    print("Bprimeturn")
def Fturn():
    print("Fturn")

def Fprimeturn():
    print("Fprimeturn")
        
def Dturn():
    print("Dturn")

def Dprimeturn():
    print("Dprimeturn")
    
def Uturn():
    print("Uturn")
    
def Uprimeturn():
    print("Uprimeturn")

def lturn():
    print("lturn, two layer turn")

def lprimeturn():
    print("lprimeturn, two layer turn")

def dturn():
    print("dturn, two layer turn")

def dprimeturn():
    print("dprimeturn, two layer turn")

def AlteredYPermutation():
    Rturn()
    Uprimeturn()
    Rprimeturn()
    Uprimeturn()
    Rturn()
    Uturn()
    Rprimeturn()
    Fprimeturn()
    Rturn()
    Uturn()
    Rprimeturn()
    Uprimeturn()
    Rprimeturn()
    Fturn()
    Rturn()

def Tpermutation():
    Rturn()
    Uturn()
    Rprimeturn()
    Uprimeturn()
    Rprimeturn()
    Fturn()
    Rturn()
    Rturn()
    Uprimeturn()
    Rprimeturn()
    Uprimeturn()
    Rturn()
    Uturn()
    Rprimeturn()
    Fprimeturn()

def Jpermutation():
    Rturn()
    Uturn()
    Rprimeturn()
    Fprimeturn()
    Rturn()
    Uturn()
    Rprimeturn()
    Uprimeturn()
    Rprimeturn()
    Fturn()
    Rturn()
    Rturn()
    Uprimeturn()
    Rprimeturn()
    Uprimeturn()


def cornerActions():
    global A, Q, N, B, J, M, D, R, E, C, F, I, H, S, U, G, L, V, X, T, O, W, K, P
    solvedC2 = False
    solvedC3 = False
    solvedC4 = False
    solvedC5 = False
    solvedC6 = False
    solvedC7 = False
    solvedC8 = False
    
    mAQN = [A, Q, N]
    mBJM = [B, J, M]
    mDRE = [D, R, E]
    mCFI = [C, F, I]
    mHSU = [H, S, U]
    mGLV = [G, L, V]
    mXTO = [X, T, O]
    mWKP = [W, K, P]
    

    bankCorner = mAQN


    everythingSolved = False
    cornerSolveList = []

    print(A)
    print(a)
    print(B)
    print(d)
    print(b)
    print(D)
    print(c)
    print(C)
    print(Q)
    print(q)
    print(R)
    print(t)
    print(r)
    print(T)
    print(s)
    print(S)
    print(E)
    print(e)
    print(F)
    print(h)
    print(f)
    print(H)
    print(g)
    print(G)
    print(I)
    print(i)
    print(J)
    print(l)
    print(j)
    print(L)
    print(k)
    print(K)
    print(M)
    print(m)
    print(N)
    print(p)
    print(n)
    print(P)
    print(o)
    print(O)
    print(U)
    print(u)
    print(V)
    print(x)
    print(v)
    print(X)
    print(w)
    print(W)

    #Use a list of the moves to the positions the bank pieces need to go.
    while everythingSolved == False:
        #print(bankCorner)
        #checking if any corners are already solved
        if (mBJM == BJM):
            solvedC2 = True
        if (mDRE == DRE):
            solvedC3 = True
        if (mCFI == CFI):
            solvedC4 = True
        if (mHSU == HSU):
            solvedC5 = True
        if (mGLV == GLV):
            solvedC6 = True
        if (mXTO == XTO):
            solvedC7 = True
        if (mWKP == WKP):
            solvedC8 = True

        if (collections.Counter(bankCorner) == collections.Counter(AQN)):
            if (solvedC2 == True and solvedC3 == True and solvedC4 == True and solvedC5 == True and solvedC6 == True and solvedC7 == True and solvedC8 == True):
                print("already set")
                everythingSolved = True
            elif (solvedC2 == False):
                cornerSolveList.append('B')
                mBJM2 = bankCorner
                bankCorner = mBJM
                mBJM = mBJM2
                B = mBJM[0]
                J = mBJM[1]
                M = mBJM[2]
                print(mBJM)
                print(bankCorner)
            elif(solvedC3 == False):
                cornerSolveList.append('D')
                mDRE2 = bankCorner
                bankCorner = mDRE
                mDRE = mDRE2
                D = mDRE[0]
                R = mDRE[1]
                E = mDRE[2]
                print(mDRE)
                print(bankCorner)
            elif(solvedC4 == False):
                cornerSolveList.append('C')
                mCFI2 = bankCorner
                bankCorner = mCFI
                mCFI = mCFI2
                C = mCFI[0]
                F = mCFI[1]
                I = mCFI[2]
                print(mCFI)
                print(bankCorner)
            elif(solvedC5 == False):
                cornerSolveList.append('H')
                mHSU2 = bankCorner
                bankCorner = mHSU
                mHSU = mHSU2
                H = mHSU[0]
                S = mHSU[1]
                U = mHSU[2]
                print(mHSU)
                print(bankCorner)
            elif (solvedC6 == False):
                cornerSolveList.append('G')
                mGLV2 = bankCorner
                bankCorner = mGLV
                mGLV = mGLV2
                G = mGLV[0]
                L = mGLV[1]
                V = mGLV[2]
                print(mGLV)
                print(bankCorner)
            elif (solvedC7 == False):
                cornerSolveList.append('X')
                mXTO2 = bankCorner
                bankCorner = mXTO
                mXTO = mXTO2
                X = mXTO[0]
                T = mXTO[1]
                O = mXTO[2]
                print(mXTO)
                print(bankCorner)
            elif (solvedC8 == False):
                cornerSolveList.append('W')
                mWKP2 = bankCorner
                bankCorner = mWKP
                mWKP = mWKP2
                W = mWKP[0]
                K = mWKP[1]
                P = mWKP[2]
                print(mWKP)
                print(bankCorner)
            #Swap with an unsolved corner because it is in the bank place and cannot be solved
    
        elif(collections.Counter(bankCorner) == collections.Counter(BJM)):
            index = BJM.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('B')
                bankCorner = mBJM
                solvedC2 = True
            elif (index == 1):
                cornerSolveList.append('J')
                bankCorner = [J, M, B]
                solvedC2 = True
            else:
                cornerSolveList.append('M')
                bankCorner = [M, B, J]
                solvedC2 = True

        elif (collections.Counter(bankCorner) == collections.Counter(DRE)):
            index = DRE.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('D')
                bankCorner = mDRE
                solvedC3 = True
            elif (index == 1):
                cornerSolveList.append('R')
                bankCorner = [R, E, D]
                solvedC3 = True
            else:
                cornerSolveList.append('E')
                bankCorner = [E, D, R]
                solvedC3 = True

        elif(collections.Counter(bankCorner) == collections.Counter(CFI)):
            index = CFI.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('C')
                bankCorner = mCFI
                solvedC4 = True
            elif (index == 1):
                cornerSolveList.append('F')
                bankCorner = [F, I, C]
                solvedC4 = True
            else:
                cornerSolveList.append('I')
                bankCorner = [I, C, F]
                solvedC4 = True
        
        elif(collections.Counter(bankCorner) == collections.Counter(HSU)):
            index = HSU.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('H')
                bankCorner = mHSU
                solvedC5 = True
            elif (index == 1):
                cornerSolveList.append('S')
                bankCorner = [S, U, H]
                solvedC5 = True
            else:
                cornerSolveList.append('U')
                bankCorner = [U, H, S]
                solvedC5 = True

        elif(collections.Counter(bankCorner) == collections.Counter(GLV)):
            index = GLV.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('G')
                bankCorner = mGLV
                solvedC6 = True
            elif (index == 1):
                cornerSolveList.append('L')
                bankCorner = [L, V, G]
                solvedC6 = True
            else:
                cornerSolveList.append('V')
                bankCorner = [V, G, L]
                solvedC6 = True
        
        elif(collections.Counter(bankCorner) == collections.Counter(XTO)):
            index = XTO.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('X')
                bankCorner = mXTO
                solvedC7 = True
            elif (index == 1):
                cornerSolveList.append('T')
                bankCorner = [T, O, X]
                solvedC7 = True
            else:
                cornerSolveList.append('O')
                bankCorner = [O, X, T]
                solvedC7 = True

        elif (collections.Counter(bankCorner) == collections.Counter(WKP)):
            index = WKP.index(bankCorner[0])
            if (index == 0):
                cornerSolveList.append('W')
                bankCorner = mWKP
                solvedC8 = True
            elif (index == 1):
                cornerSolveList.append('K')
                bankCorner = [K, P, W]
                solvedC8 = True
            else:
                cornerSolveList.append('P')
                bankCorner = [P, W, K]
                solvedC8 = True
    return cornerSolveList
    # #use "list".sort() method for comparing the two corners.

def cornerSwapper(cornerSolveList):
    odd = False
    counter = 0
    if len(cornerSolveList)%2 != 0:
        odd = True
        print("odd")
    for i in cornerSolveList:
        letter = cornerSolveList[counter]
        if letter == 'B':
            Rturn()
            Dprimeturn()
            AlteredYPermutation()
            Dturn()
            Rprimeturn()
        elif letter == 'C':
            Fturn()
            AlteredYPermutation()
            Fprimeturn()
        elif letter == 'D':
            Fturn()
            Rprimeturn()
            AlteredYPermutation()
            Rturn()
            Fprimeturn()
        elif letter == 'E':
            Fprimeturn()
            Dturn()
            AlteredYPermutation()
            Dprimeturn()
            Fturn()
        elif letter == 'F':
            Fturn()
            Fturn()
            Dturn()
            AlteredYPermutation()
            Dprimeturn()
            Fprimeturn()
            Fprimeturn()
        elif letter == 'G':
            Dturn()
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
            Dprimeturn()
        elif letter == 'H':
            Dturn()
            AlteredYPermutation()
            Dprimeturn()
        elif letter == 'I':
            Rprimeturn()
            AlteredYPermutation()
            Rturn()
        elif letter == 'J':
            Rturn()
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
            Rprimeturn()
        elif letter == 'K':
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
        elif letter == 'L':
            AlteredYPermutation()
        elif letter == 'M':
            Rprimeturn()
            Fturn()
            AlteredYPermutation()
            Fprimeturn()
            Rturn()
        elif letter == 'O':
            Dprimeturn()
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
            Dturn()
        elif letter == 'P':
            Dprimeturn()
            AlteredYPermutation()
            Dturn()
        elif letter == 'R':
            Fturn()
            Fturn()
            AlteredYPermutation()
            Fprimeturn()
            Fprimeturn()
        elif letter == 'S':
            Dturn()
            Dturn()
            Rturn()
            AlteredYPermutation()
            Rprimeturn()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'T':
            Dturn()
            Dturn()
            AlteredYPermutation()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'U':
            Fprimeturn()
            AlteredYPermutation()
            Fturn()
        elif letter == 'V':
            Dprimeturn()
            Fprimeturn()
            AlteredYPermutation()
            Fturn()
            Dturn()
        elif letter == 'W':
            Dturn()
            Dturn()
            Fprimeturn()
            AlteredYPermutation()
            Fturn()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'X':
            Dturn()
            Fprimeturn()
            AlteredYPermutation()
            Fturn()
            Dprimeturn

        counter = counter + 1
    if odd == True:
        Xturn()
        Yturn()
        Xprimeturn()

        Lturn()
        Uprimeturn()
        Uprimeturn()
        Lprimeturn()
        Uprimeturn()
        Uprimeturn()
        Lturn()
        Fprimeturn()
        Lprimeturn()
        Uprimeturn()
        Lturn()
        Uturn()
        Lturn()
        Fturn()
        Lprimeturn()
        Lprimeturn()
        Uturn()

        Xturn()
        Yprimeturn()
        Xprimeturn()

def cornerMain():
    cList = cornerActions()
    print(cList)
    cornerSwapper(cList)

def edgeActions():
    global a, m, b, i, c, e, d, q, f, l, g, u, h, r, t, n, s, x, k, v, o, w, j, p
    solvedE2 = False
    solvedE3 = False
    solvedE4 = False
    solvedE5 = False
    solvedE6 = False
    solvedE7 = False
    solvedE8 = False
    solvedE9 = False
    solvedE10 = False
    solvedE11 = False
    solvedE12 = False

    mam = [a, m]
    mbi = [b, i]
    mce = [c, e]
    mdq = [d, q]
    mfl = [f, l]
    mgu = [g, u]
    mhr = [h, r]
    mtn = [t, n]
    msx = [s, x]
    mkv = [k, v]
    mow = [o, w]
    mjp = [j, p]

    bankEdge = mbi


    everythingSolved = False
    edgeSolveList = []

    #Use a list of the moves to the positions the bank pieces need to go.

    #finish
    while everythingSolved == False:
        #checking if any edges are already solved
        if (mam == am):
            solvedE2 = True
        if (mce == ce):
            solvedE3 = True
        if (mdq == dq):
            solvedE4 = True
        if (mfl == fl):
            solvedE5 = True
        if (mgu == gu):
            solvedE6 = True
        if (mhr == hr):
            solvedE7 = True
        if (mtn == tn):
            solvedE8 = True
        if (msx == sx):
            solvedE9 = True
        if (mkv == kv):
            solvedE10 = True
        if (mow == ow):
            solvedE11 = True
        if (mjp == jp):
            solvedE12 = True
        if (collections.Counter(bankEdge) == collections.Counter(bi)):
            if (solvedE2 == True and solvedE3 == True and solvedE4 == True and solvedE5 == True and solvedE6 == True and solvedE7 == True and solvedE8 == True and solvedE9 == True and solvedE10 == True and solvedE11 == True and solvedE12 == True):
                print("Edges already set")
                everythingSolved = True
            elif (solvedE2 == False):
                edgeSolveList.append('a')
                mam2 = bankEdge 
                bankEdge = mam 
                mam = mam2 
                a = mam[0]
                m = mam[1]
                print(mam)
                print(bankEdge)
            elif(solvedE3 == False):
                edgeSolveList.append('c')
                mce2 = bankEdge
                bankEdge = mce
                mce = mce2
                c = mce[0]
                e = mce[1]
                print(mce)
                print(bankEdge)
            elif(solvedE4 == False):
                edgeSolveList.append('d')
                mdq2 = bankEdge
                bankEdge = mdq
                mdq = mdq2
                d = mdq[0]
                q = mdq[1]
                print(mdq)
                print(bankEdge)
            elif(solvedE5 == False):
                edgeSolveList.append('f')
                mfl2 = bankEdge
                bankEdge = mfl
                mfl = mfl2
                f = mfl[0]
                l = mfl[1]
                print(mfl)
                print(bankEdge)
            elif (solvedE6 == False):
                edgeSolveList.append('g')
                mgu2 = bankEdge
                bankEdge = mgu
                mgu = mgu2
                g = mgu[0]
                u = mgu[1]
                print(mgu)
                print(bankEdge)
            elif (solvedE7 == False):
                edgeSolveList.append('h')
                mhr2 = bankEdge
                bankEdge = mhr
                mhr = mhr2
                h = mhr[0]
                r = mhr[1]
                print(mhr)
                print(bankEdge)
            elif (solvedE8 == False):
                edgeSolveList.append('t')
                mtn2 = bankEdge
                bankEdge = mtn
                mtn = mtn2
                t = mtn[0]
                n = mtn[1]
                print(mtn)
                print(bankEdge)
            elif (solvedE9 == False):
                edgeSolveList.append('s')
                msx2 = bankEdge
                bankEdge = msx
                msx = msx2
                s = msx[0]
                x = msx[1]
                print(msx)
                print(bankEdge)
            elif (solvedE10 == False):
                edgeSolveList.append('k')
                mkv2 = bankEdge
                bankEdge = mkv
                mkv = mkv2
                k = mkv[0]
                v = mkv[1]
                print(mkv)
                print(bankEdge)
            elif (solvedE11 == False):
                edgeSolveList.append('o')
                mow2 = bankEdge
                bankEdge = mow
                mow = mow2
                o = mow[0]
                w = mow[1]
                print(mow)
                print(bankEdge)
            elif (solvedE12 == False):
                edgeSolveList.append('j')
                mjp2 = bankEdge
                bankEdge = mjp
                mjp = mjp2
                j = mjp[0]
                p = mjp[1]
                print(mjp)
                print(bankEdge)
            #Swap with an unsolved Edge because it is in the bank place and cannot be solved
    
        elif(collections.Counter(bankEdge) == collections.Counter(am)):
            index = am.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('a')
                bankEdge = mam
                solvedE2 = True
            elif (index == 1):
                edgeSolveList.append('m')
                bankEdge = [m, a]
                solvedE2 = True

        elif(collections.Counter(bankEdge) == collections.Counter(ce)):
            index = ce.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('c')
                bankEdge = mce
                solvedE3 = True
            elif (index == 1):
                edgeSolveList.append('e')
                bankEdge = [e, c]
                solvedE3 = True
        
        elif(collections.Counter(bankEdge) == collections.Counter(dq)):
            index = dq.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('d')
                bankEdge = mdq
                solvedE4 = True
            elif (index == 1):
                edgeSolveList.append('q')
                bankEdge = [q, d]
                solvedE4 = True
            
        elif(collections.Counter(bankEdge) == collections.Counter(fl)):
            index = fl.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('f')
                bankEdge = mfl
                solvedE5 = True
            elif (index == 1):
                edgeSolveList.append('l')
                bankEdge = [l, f]
                solvedE5 = True
        
        elif(collections.Counter(bankEdge) == collections.Counter(gu)):
            index = gu.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('g')
                bankEdge = mgu
                solvedE6 = True
            elif (index == 1):
                edgeSolveList.append('u')
                bankEdge = [u, g]
                solvedE6 = True

        elif(collections.Counter(bankEdge) == collections.Counter(hr)):
            index = hr.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('h')
                bankEdge = mhr
                solvedE7 = True
            elif (index == 1):
                edgeSolveList.append('r')
                bankEdge = [r, h]
                solvedE7 = True
        
        elif(collections.Counter(bankEdge) == collections.Counter(tn)):
            index = tn.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('t')
                bankEdge = mtn
                solvedE8 = True
            elif (index == 1):
                edgeSolveList.append('n')
                bankEdge = [n, t]
                solvedE8 = True

        elif(collections.Counter(bankEdge) == collections.Counter(sx)):
            index = sx.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('s')
                bankEdge = msx
                solvedE9 = True
            elif (index == 1):
                edgeSolveList.append('x')
                bankEdge = [x, s]
                solvedE9 = True

        elif(collections.Counter(bankEdge) == collections.Counter(kv)):
            index = kv.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('k')
                bankEdge = mkv
                solvedE10 = True
            elif (index == 1):
                edgeSolveList.append('v')
                bankEdge = [v, k]
                solvedE10 = True
        
        elif(collections.Counter(bankEdge) == collections.Counter(ow)):
            index = ow.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('o')
                bankEdge = mow
                solvedE11 = True
            elif (index == 1):
                edgeSolveList.append('w')
                bankEdge = [w, o]
                solvedE11 = True

        elif(collections.Counter(bankEdge) == collections.Counter(jp)):
            index = jp.index(bankEdge[0])
            if (index == 0):
                edgeSolveList.append('j')
                bankEdge = mjp
                solvedE12 = True
            elif (index == 1):
                edgeSolveList.append('p')
                bankEdge = [p, j]
                solvedE12 = True

    return edgeSolveList

def edgeSwapper(edgeSolveList):
    counter = 0
    for i in edgeSolveList:
        letter = edgeSolveList[counter]
        if letter == 'a':
            lturn()
            lturn()
            Dprimeturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dturn()
            lprimeturn()
            lprimeturn()
        elif letter == 'c':
            Jpermutation()
        elif letter == 'd':
            Tpermutation()
        elif letter == 'e':
            lturn()
            Dprimeturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dturn()
            lprimeturn()
        elif letter == 'f':
            dturn()
            dturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            dprimeturn()
            dprimeturn()
        elif letter == 'g':
            lprimeturn()
            Jpermutation()
            lturn()
        elif letter == 'h':
            Lprimeturn()
            Tpermutation()
            Lturn()
        elif letter == 'j':
            dturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            dprimeturn()
        elif letter == 'k':
            Dprimeturn()
            lprimeturn()
            Jpermutation()
            lturn()
            Dturn()
        elif letter == 'l':
            dprimeturn()
            Lprimeturn()
            Tpermutation()
            Lturn()
            dturn()
        elif letter == 'm':
            lturn()
            Jpermutation()
            lprimeturn()
        elif letter == 'n':
            Lturn()
            Tpermutation()
            Lprimeturn()
        elif letter == 'o':
            Dturn()
            Dturn()
            lprimeturn()
            Jpermutation()
            lturn()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'p':
            dturn()
            dturn()
            Lprimeturn()
            Tpermutation()
            Lturn()
            dprimeturn()
            dprimeturn()
        elif letter == 'q':
            Lturn()
            Lturn()
            dturn()
            lprimeturn()
            Jpermutation()
            lturn()
            dprimeturn()
            Lprimeturn()
            Lprimeturn()
        elif letter == 'r':
            dprimeturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            dturn()
        elif letter == 's':
            Dturn()
            lprimeturn()
            Jpermutation()
            lturn()
            Dprimeturn()
        elif letter == 't':
            dturn()
            Lprimeturn()
            Tpermutation()
            Lturn()
            dprimeturn()
        elif letter == 'u':
            Dprimeturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dturn()
        elif letter == 'v':
            Dturn()
            Dturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dprimeturn()
            Dprimeturn()
        elif letter == 'w':
            Dturn()
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()
            Dprimeturn()
        elif letter == 'x':
            Lturn()
            Lturn()
            Tpermutation()
            Lprimeturn()
            Lprimeturn()

        counter = counter + 1

def edgeMain():
    eList = edgeActions()
    print("done")
    print(eList)
    edgeSwapper(eList)

def main():
    cornerMain()
    edgeMain()

def scrambleTurn(matrix):
    turned = [[matrix[3][0], matrix[2][0], matrix[1][0]],
            [matrix[4][0], matrix[3][1], matrix[2][1], matrix[1][1], matrix[0][0]],
            [matrix[4][1], matrix[3][2], matrix[1][2], matrix[0][1]],
            [matrix[4][2], matrix[3][3], matrix[2][2], matrix[1][3], matrix[0][2]],
            [matrix[3][4], matrix[2][3], matrix[1][4]]]
    print(turned)
    return turned

def cubeScrambler(num):
    global A, Q, N, B, J, M, D, R, E, C, F, I, H, S, U, G, L, V, X, T, O, W, K, P
    global a, m, b, i, c, e, d, q, f, l, g, u, h, r, t, n, s, x, k, v, o, w, j, p
    A = "yellow"
    a = "yellow"
    B = "yellow"
    d = "yellow"
    b = "yellow"
    D = "yellow"
    c = "yellow"
    C = "yellow"
    Q = "blue"
    q = "blue"
    R = "blue"
    t = "blue"
    r = "blue"
    T = "blue"
    s = "blue"
    S = "blue"
    E = "red"
    e = "red"
    F = "red"
    h = "red"
    f = "red"
    H = "red"
    g = "red"
    G = "red"
    I = "green"
    i = "green"
    J = "green"
    l = "green"
    j = "green"
    L = "green"
    k = "green"
    K = "green"
    M = "orange"
    m = "orange"
    N = "orange"
    p = "orange"
    n = "orange"
    P = "orange"
    o = "orange"
    O = "orange"
    U = "white"
    u = "white"
    V = "white"
    x = "white"
    v = "white"
    X = "white"
    w = "white"
    W = "white"

    for ii in range(num):
        Rside = [[C, b, B],
                [F, I, i, J, M],
                [f, l, j, p],
                [G, L, k, K, P],
                [V, v, W]]
        Lside = [[A, d, D],
                [N, Q, q, R, E],
                [n, t, r, h],
                [O, T, s, S, H],
                [X, x, U]]
        Fside = [[D, c, C],
                [R, E, e, F, I],
                [r, h, f, l],
                [S, H, g, G, L],
                [U, u, V]]
        Bside = [[B, a, A],
                [J, M, m, N, Q],
                [j, p, n, t],
                [K, P, o, O, T],
                [W, w, X]]
        Uside = [[N, m, M],
                [Q, A, a, B, J],
                [q, d, b, i],
                [R, D, c, C, I],
                [E, e, F]]
        Dside = [[H, g, G],
                [S, U, u, V, L],
                [s, x, v, k],
                [T, X, w, W, K],
                [O, o, P]]
        randomNum = random.randint(1, 6)
        if (randomNum == 1):
            Rturn()
            Rref = scrambleTurn(Rside)      
            C = Rref[0][0]
            b = Rref[0][1]
            B = Rref[0][2]
            F = Rref[1][0]
            I = Rref[1][1]
            i = Rref[1][2]
            J = Rref[1][3]
            M = Rref[1][4]
            f = Rref[2][0]
            l = Rref[2][1]
            j = Rref[2][2]
            p = Rref[2][3]
            G = Rref[3][0]
            L = Rref[3][1]
            k = Rref[3][2]
            K = Rref[3][3]
            P = Rref[3][4]
            W = Rref[4][2]
            v = Rref[4][1]
            V = Rref[4][0]
        elif(randomNum == 2):
            Lturn()
            Lref = scrambleTurn(Lside)   
            A = Lref[0][0]
            d = Lref[0][1]
            D = Lref[0][2]
            N = Lref[1][0]
            Q = Lref[1][1]
            q = Lref[1][2]
            R = Lref[1][3]
            E = Lref[1][4]
            n = Lref[2][0]
            t = Lref[2][1]
            r = Lref[2][2]
            h = Lref[2][3]
            O = Lref[3][0]
            T = Lref[3][1]
            s = Lref[3][2]
            S = Lref[3][3]
            H = Lref[3][4]
            U = Lref[4][2]
            x = Lref[4][1]
            X = Lref[4][0]
        elif(randomNum == 3):
            Fturn()
            Fref = scrambleTurn(Fside)   
            D = Fref[0][0]
            c = Fref[0][1]
            C = Fref[0][2]
            R = Fref[1][0]
            E = Fref[1][1]
            e = Fref[1][2]
            F = Fref[1][3]
            I = Fref[1][4]
            r = Fref[2][0]
            h = Fref[2][1]
            f = Fref[2][2]
            l = Fref[2][3]
            S = Fref[3][0]
            H = Fref[3][1]
            g = Fref[3][2]
            G = Fref[3][3]
            L = Fref[3][4]
            U = Fref[4][0]
            u = Fref[4][1]
            V = Fref[4][2]
        elif(randomNum == 4):
            Bturn()
            Bref = scrambleTurn(Bside)   
            B = Bref[0][0]
            a = Bref[0][1]
            A = Bref[0][2]
            J = Bref[1][0]
            M = Bref[1][1]
            m = Bref[1][2]
            N = Bref[1][3]
            Q = Bref[1][4]
            j = Bref[2][0]
            p = Bref[2][1]
            n = Bref[2][2]
            t = Bref[2][3]
            K = Bref[3][0]
            P = Bref[3][1]
            o = Bref[3][2]
            O = Bref[3][3]
            T = Bref[3][4]
            W = Bref[4][0]
            w = Bref[4][1]
            X = Bref[4][2]
        elif(randomNum == 5):
            Uturn()
            Uref = scrambleTurn(Uside)   
            N = Uref[0][0]
            m = Uref[0][1]
            M = Uref[0][2]
            Q = Uref[1][0]
            A = Uref[1][1]
            a = Uref[1][2]
            B = Uref[1][3]
            J = Uref[1][4]
            q = Uref[2][0]
            d = Uref[2][1]
            b = Uref[2][2]
            i = Uref[2][3]
            R = Uref[3][0]
            D = Uref[3][1]
            c = Uref[3][2]
            C = Uref[3][3]
            I = Uref[3][4]
            F = Uref[4][2]
            e = Uref[4][1]
            E = Uref[4][0]
        elif(randomNum == 6):
            Dturn()
            Dref = scrambleTurn(Dside)   
            H = Dref[0][0]
            g = Dref[0][1]
            G = Dref[0][2]
            S = Dref[1][0]
            U = Dref[1][1]
            u = Dref[1][2]
            V = Dref[1][3]
            L = Dref[1][4]
            s = Dref[2][0]
            x = Dref[2][1]
            v = Dref[2][2]
            k = Dref[2][3]
            T = Dref[3][0]
            X = Dref[3][1]
            w = Dref[3][2]
            W = Dref[3][3]
            K = Dref[3][4]
            O = Dref[4][0]
            o = Dref[4][1]
            P = Dref[4][2]

        
#cubeScrambler(15)
A = "red"
a = "yellow"
B = "orange"
d = "red"
b = "red"
D = "yellow"
c = "blue"
C = "white"
Q = "white"
q = "white"
R = "orange"
t = "blue"
r = "yellow"
T = "green"
s = "green"
S = "orange"
E = "blue"
e = "white"
F = "green"
h = "red"
f = "orange"
H = "white"
g = "white"
G = "yellow"
I = "red"
i = "blue"
J = "white"
l = "blue"
j = "green"
L = "red"
k = "green"
K = "green"
M = "blue"
m = "orange"
N = "blue"
p = "yellow"
n = "yellow"
P = "yellow"
o = "orange"
O = "yellow"
U = "green"
u = "green"
V = "blue"
x = "red"
v = "orange"
X = "red"
w = "white"
W = "orange"

main()

