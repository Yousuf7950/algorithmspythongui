import os
from tkinter import *
import tkinter as tk
import tkinter.font as font

def maximummm(a, b): 
    if a >= b: 
        return a 
    else: 
        return b 

folder = 'E:\pythonProject'
fl1 = ['inputa','inputb','inputc','inputd','inpute','inputf','inputg','inputh','inputi','inputj']
fl2 = ['Longest Common Subsequence','Shortest Common Supersequence','Levenshtein Distance (edit-distance)','Longest Increasing Subsequence','Matrix Chain Multiplication','0-1-knapsack-problem','Partition-problem','Rod Cutting Problem','Coin-change-making-problem','Word Break Problem']
app = tk.Tk()
app.title("DAA Project")
app.geometry('750x450')
app.resizable(False,False)  #restricts the application window to a fixed resolution of 750x450

C = Canvas(app, bg="blue", height=250, width=300)
filename = PhotoImage(file = "algoimg.png")
background_label = Label(app, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

myFont = font.Font(family='Helvetica')

variable1 = tk.StringVar(app)
variable1.set("Select An Input File")
variable2 = tk.StringVar(app)
variable2.set("Select An Algorithm")
opt = tk.OptionMenu(app, variable1, *fl1)
opt2 = tk.OptionMenu(app, variable2, *fl2)
opt.config(width=30, font=('Helvetica', 12),bg='#ffffff', fg='#000000')
opt2.config(width=30, font=('Helvetica', 12),bg='#ffffff', fg='#000000')

opt.place(relx=0.29, y=145, anchor='w')
opt2.place(relx=0.29, y=200, anchor='w')
#opt2.pack()
#opt.pack()
def selectt():
    txtfile=variable1.get()
    pyfile=variable2.get()
    if txtfile=="inputa" and pyfile=='Longest Common Subsequence':
        op_file = open("inputa.txt", "r")

        def lcs(X, Y):
            #mm=max
            m = len(X)
            n = len(Y)
            L = [[None] * (n + 1) for i in range(m + 1)]

            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif X[i - 1] == Y[j - 1]:
                        L[i][j] = L[i - 1][j - 1] + 1
                    else:
                        L[i][j] = maximummm(L[i - 1][j], L[i][j - 1])
            return L[m][n]

        X: str = op_file.readline()
        Y: str = op_file.readline()
        intvar=IntVar(app,name="int")
        x1=lcs(X,Y)
        var=StringVar()
        var.set(x1)
        a = Label(app, textvariable=var,bd=1,relief=SOLID,background="white",height=2,width=30)
        a.place(relx=0.36, y=330, anchor='w')
        #a.pack()
        op_file.close()
        max=0
    elif txtfile=="inputb" and pyfile=='Shortest Common Supersequence':
        op_file = open("inputb.txt", "r")
        def superSeq(X, Y, m, n):
            if (not m):
                return n
            if (not n):
                return m

            if (X[m - 1] == Y[n - 1]):
                return 1 + superSeq(X, Y, m - 1, n - 1)

            return 1 + min(superSeq(X, Y, m - 1, n),
                           superSeq(X, Y, m, n - 1))

        X: str = op_file.readline()
        Y: str = op_file.readline()
        x1 = superSeq(X, Y, len(X), len(Y))
        var = StringVar()
        var.set(x1)
        
        a = Label(app, textvariable=var,bd=1,relief=SOLID,background="white",height=2,width=30)
        a.place(relx=0.36, y=330, anchor='w')
        #a.pack()
        op_file.close()

    elif txtfile=="inputc" and pyfile=='Levenshtein Distance (edit-distance)':
        op_file = open("inputc.txt", "r")

        def editDistance(X, Y, m, n):
            if m == 0:
                return n
            if n == 0:
                return m
            if X[m - 1] == Y[n - 1]:
                return editDistance(X, Y, m - 1, n - 1)

            return 1 + min(editDistance(X, Y, m, n - 1),  # Insert
                           editDistance(X, Y, m - 1, n),  # Remove
                           editDistance(X, Y, m - 1, n - 1)  # Replace
                           )

        X: str = op_file.readline()
        Y: str = op_file.readline()
        x1 = editDistance(X, Y, len(X), len(Y))
        var = StringVar()
        var.set(x1)
        
        a = Label(app, textvariable=var,bd=1,relief=SOLID,background="white",height=2,width=30)
        a.place(relx=0.36, y=330, anchor='w')
        #a.pack()

        op_file.close()

    elif txtfile=="inputd" and pyfile=='Longest Increasing Subsequence':
        op_file = open("inputde.txt", "r")

        def lis(arr):
            n = len(arr)

            lis = [1] * n

            for i in range(1, n):
                for j in range(0, i):
                    if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                        lis[i] = lis[j] + 1

            maximum = 0

            for i in range(n):
                maximum = maximummm(maximum, lis[i])

            return maximum

        arr = op_file.read()
        x1 = lis(arr)
        var = StringVar()
        var.set(x1)
        
        a = Label(app, textvariable=var,bd=1,relief=SOLID,background="white",height=2,width=30)
        a.place(relx=0.36, y=330, anchor='w')
        #a.pack()

        op_file.close()


    elif txtfile=="inpute" and pyfile=='Matrix Chain Multiplication':
        op_file = open("inpute.txt", "r")
        test = op_file.readlines()

        for i in range(0, len(test)):
            test[i] = int(test[i])

        def MatChainMul(arr, n):
            dp = [[0 for i in range(n)] for j in range(n)]
            for i in range(1, n):
                dp[i][i] = 0

            for L in range(2, n):
                for i in range(1, n - L + 1):
                    j = i + L - 1
                    dp[i][j] = 10 ** 10
                    for k in range(i, j):
                        q = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                        if q < dp[i][j]:
                            dp[i][j] = q

            return dp[1][n - 1]

        arr = test
        size = len(arr)

        x1 = str(MatChainMul(arr, size))
        var = StringVar()
        var.set(x1)
        
        a = Label(app, textvariable=var,bd=1,relief=SOLID,background="white",height=2,width=30)
        a.place(relx=0.36, y=330, anchor='w')
        #a.pack()

        op_file.close()

    elif txtfile == "inputf" and pyfile == '0-1-knapsack-problem':

        w_file = open("01w.txt", "r")
        wt_file = open("01wt.txt", "r")
        val_file = open("01val.txt", "r")
        test1 = w_file.read()
        test1 = int(test1)

        test2 = wt_file.readlines()
        for i in range(0, len(test2)):
            test2[i] = int(test2[i])

        test3 = val_file.readlines()
        for i in range(0, len(test3)):
            test3[i] = int(test3[i])

        def knapSack(W, wt, val, n):
            K = [[0 for x in range(W + 1)] for x in range(n + 1)]

            for i in range(n + 1):
                for w in range(W + 1):
                    if i == 0 or w == 0:
                        K[i][w] = 0
                    elif wt[i - 1] <= w:
                        K[i][w] = maximummm(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
                    else:
                        K[i][w] = K[i - 1][w]

            return K[n][W]

        val = test3
        wt = test2
        W = test1
        n = len(val)
        x1 = (knapSack(W, wt, val, n))
        var = StringVar()
        var.set(x1)
        a = Label(app, textvariable=var,bd=1,relief=SOLID,background="white",height=2,width=30)
        a.place(relx=0.36, y=330, anchor='w')
        #a.pack()
        w_file.close()
        wt_file.close()
        val_file.close()

    elif txtfile == "inputg" and pyfile == 'Partition-problem':
        op_file = open("inputg.txt", "r")
        test=op_file.readlines()
        for i in range(0, len(test)):
            test[i] = int(test[i])

        def isSubsetSum(arr, n, sum):
            if sum == 0:
                return True
            if n == 0 and sum != 0:
                return False
            if arr[n - 1] > sum:
                return isSubsetSum(arr, n - 1, sum)

            return isSubsetSum(arr, n - 1, sum) or isSubsetSum(arr, n - 1, sum - arr[n - 1])

        def findPartion(arr, n):
            sum = 0
            for i in range(0, n):
                sum += arr[i]
            if sum % 2 != 0:
                return False

            return isSubsetSum(arr, n, sum // 2)

        arr = (test)
        n = len(arr)

        
        if findPartion(arr, n) == True:
            a = Label(app, text="Can be partitioned",bd=1,relief=SOLID,background="white",height=2,width=30)
            a.place(relx=0.36, y=330, anchor='w')
            #a.pack()
        else:
            a = Label(app, text="Can't be partitioned",bd=1,relief=SOLID,background="white",height=2,width=30)
            a.place(relx=0.36, y=330, anchor='w')
            #a.pack()
        op_file.close()

    elif txtfile == "inputh" and pyfile == 'Rod Cutting Problem':
        op_file = open("inputh.txt", "r")
        test = op_file.readlines()

        for i in range(0, len(test)):
            test[i] = int(test[i])

        INF = 100000;
        r = [0] + [-1 * INF] * 5

        def max(x, y):
            if x > y:
                return x
            return y

        def bottom_up_rod_cutting(c, n):
            r = [0] * (n + 1)
            r[0] = 0

            for j in range(1, n + 1):
                maximum_revenue = -1 * INF
                for i in range(1, j + 1):
                    maximum_revenue = maximummm(maximum_revenue, c[i] + r[j - i])
                r[j] = maximum_revenue
            return r[n]

        if __name__ == '__main__':
            c = test
            s = len(test) - 1
            x1 = bottom_up_rod_cutting(c, s)
            var = StringVar()
            var.set(x1)
            a = Label(app, textvariable=var,bd=1,relief=SOLID,background="white",height=2,width=30)
            a.place(relx=0.36, y=330, anchor='w')
            #a.pack()


    elif txtfile == "inputi" and pyfile == 'Coin-change-making-problem':
        op_file = open("inputi.txt", "r")
        test = op_file.readlines()
        for i in range(0, len(test)):
            test[i] = int(test[i])

        def count(S, m, n):
            table = [[0 for x in range(m)] for x in range(n + 1)]

            for i in range(m):
                table[0][i] = 1

            for i in range(1, n + 1):
                for j in range(m):
                    x = table[i - S[j]][j] if i - S[j] >= 0 else 0

                    y = table[i][j - 1] if j >= 1 else 0

                    table[i][j] = x + y

            return table[n][m - 1]

        arr = test
        m = len(arr)
        n = 4
        x1 = count(arr, m, n)
        var = StringVar()
        var.set(x1)
        a = Label(app, textvariable=var,bd=1,relief=SOLID,background="white",height=2,width=30)
        a.place(relx=0.36, y=330, anchor='w')
        #a.pack()

    elif txtfile == "inputj" and pyfile == 'Word Break Problem':
        op_file = open("inputj.txt", "r")
        op_fileapple = open("apple.txt", "r")
        op_filepen = open("pen.txt", "r")

        class Solution(object):
            def wordBreak(self, s, wordDict):
                dp = [[False for i in range(len(s))] for x in range(len(s))]
                for i in range(1, len(s) + 1):
                    for j in range(len(s) - i + 1):
                        # print(s[j:j+i])
                        if s[j:j + i] in wordDict:
                            dp[j][j + i - 1] = True
                        else:
                            for k in range(j + 1, j + i):
                                if dp[j][k - 1] and dp[k][j + i - 1]:
                                    dp[j][j + i - 1] = True
                return dp[0][len(s) - 1]

        ob1 = Solution()
        t1 = op_file.read()
        t2 = op_fileapple.read()
        t3 = op_filepen.read()
        print(ob1.wordBreak(t1, [t2, t3]))
        x1 = ob1.wordBreak(t1, [t2, t3])
        var = BooleanVar()
        var.set(x1)
        a = Label(app, textvariable=var,bd=1,relief=SOLID,background="white",height=2,width=30)
        a.place(relx=0.36, y=330, anchor='w')
        #a.pack()
        op_file.close()
        op_fileapple.close()
        op_filepen.close()



# Create a Button
btn = Button(app, text='Proceed', bd='5',
             command=selectt, height=2,width=20,bg='#0052cc', fg='#ffffff',font=('Helvetica', 12,"bold"))

# Set the position of button on the top of window.
#btn.pack(side='bottom')
btn.place(relx=0.36, y=265, anchor='w')
# # set window size
# app.geometry("400x200")
#
# #set window color
# app.configure(bg='blue')
app.mainloop()

