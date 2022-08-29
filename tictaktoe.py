def sum(a,b,c):
    return a+b+c
# board of a game 
def board(xs,xz):
    zero='X'if xs[0] else ('0'if xz[0] else 0)
    one='X'if xs[1] else ('0'if xz[1] else 1)
    two='X'if xs[2] else ('0'if xz[2] else 2)
    three='X'if xs[3] else ('0'if xz[3] else 3)
    four='X'if xs[4] else ('0'if xz[4] else 4)
    five='X'if xs[5] else ('0'if xz[5] else 5)
    six='X'if xs[6] else ('0'if xz[6] else 6)
    seven='X'if xs[7] else ('0'if xz[7] else 7)
    eight='X'if xs[8] else ('0'if xz[8] else 8)

    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")

#win cheacker

def wincheacker(xs,xz):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xs[win[0]],xs[win[1]],xs[win[2]])==3):
            print("X won yhe match")
            return 1
        if(sum(xz[win[0]],xz[win[1]],xz[win[2]])==3):
            print(" o won yhe match")
            return 0
    return -1

#main function
if __name__=="__main__":
    xs=[0,0,0,0,0,0,0,0,0]
    xz=[0,0,0,0,0,0,0,0,0]
    turn=1
    print("welcome to the game...")
    while True:
        board(xs,xz)
        if (turn==1):
            print ("x change...")
            value=int(input("enter values..."))
            xs[value]=1
        else:
            print ("0 chance..")
            value=int(input("enter values..."))
            xz[value]=1
        cwin=wincheacker(xs,xz)
        if (cwin !=-1):
            print("match over")
            break

        turn=1-turn