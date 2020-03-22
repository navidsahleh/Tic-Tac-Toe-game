def tic_tac_toe():
    print("welcome to tic tac toe game! :D")
    l=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    k=False
    x=0
    while x<=5 :
        print("player1 give me row and col: ")
        row=int(input("row= "))
        row=row-1
        col=int(input("col= "))
        col=col-1
        while l[row][col]!=0:
            print("it's full!")
            print("player1 give me row and col: ")
            row=int(input("row= "))
            row=row-1
            col=int(input("col= "))
            col=col-1
        l[row][col]='x'
        print(size(l))
        if x>=2:
            k=checkGrid(l,k)
        if k==True:
            break
        if x>3:
            break
        print("player2 it's your turn!")
        print("give me row and col: ")
        row=int(input("row= "))
        row=row-1
        col=int(input("col= "))
        col=col-1
        while l[row][col]!=0:
            print("it's full!")
            print("player2 give me row and col: ")
            row=int(input("row= "))
            row=row-1
            col=int(input("col= "))
            col=col-1
        l[row][col]='o'
        print(size(l))
        if x>=2:
            k=checkGrid(l,k)
        if k==True:
            break
        x+=1
    print("do you want to play again?\n")
    z=input("")
    if z=="yes" :
        return tic_tac_toe()
    else:
        return "GAME OVER :D"


def checkGrid(grid,k):
    for x in range(0,3):
        row=set([grid[x][0],grid[x][1],grid[x][2]])
        if len(row)==1 and grid[x][0]!=0:
            if grid[x][0]=='x':
                print("player1 wins!!!")
                k=True
                return k
            else:
                print("player2 wins!!!")
                k=True
                return k
    for x in range(0,3):
        column=set([grid[0][x],grid[1][x],grid[2][x]])
        if len(column)==1 and grid[0][x]!=0:
            if grid[0][x]=='x' :
                print("player1 wins!!!")
                k=True
                return k
            else:
                print("player2 wins!!!")
                k=True
                return k
    diag1=set([grid[0][0],grid[1][1],grid[2][2]])
    diag2=set([grid[0][0],grid[1][1],grid[2][2]])
    if len(diag1)==1 or len(diag2)==1 and grid[1][1]!=0:
        if grid[1][1]=='x':
            print("player1 wins!!!")
            k=True
            return k
        else:
            print("player2 wins!!!")
            k=True
            return k


def size(l):
    print(" ---"*(3))
    print("| "+str(l[0][0])+" | "+str(l[0][1])+" | "+str(l[0][2])+' |')
    print(" ---"*(3))
    print("| "+str(l[1][0])+" | "+str(l[1][1])+" | "+str(l[1][2])+' |')
    print(" ---"*(3))
    print("| "+str(l[2][0])+" | "+str(l[2][1])+" | "+str(l[2][2])+' |')
    print(" ---"*(3))
    return "TIC TAC TOE GAME\n"



print(tic_tac_toe())
