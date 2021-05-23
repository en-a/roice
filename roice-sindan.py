import tkinter as tk

class Checkbutton(tk.Button):
    def __init__(self,master,cnf={},**kw):
        tk.Checkbutton.__init__(self,master,cnf={},**kw)
        self.configure(fg = "black",font = ("",14))
        
class cd(tk.Label):
    def __init__(self,master,cnf={},**kw):
         tk.Label.__init__(self, master,cnf={},**kw)
         self.configure(bg = "#a0522d",fg = "black",font = ("",14,"bold"))


#ウィンドウ
root=tk.Tk()
root.geometry("550x450+40+15")
root.title("royce")

#テキストラベル
l1=cd(root,text="あなたにおすすめのロイズの生チョコレートを教えるよ")
l2=cd(root,text="好きなものを選択してね")
l3=cd(root,text="(いくつでもオーケーだよ)")

l1.pack()
l2.pack()
l3.pack()

#ファイル読み込み
f = open("royce.txt","r" ,encoding="utf-8")

#ボタンクリック時
def bclick(event):
      global lbl,line
      if v2.get() ==True and v5.get() ==True:#普通＆お酒なし
        lbl = tk.Label(text="おすすめはカカオが香る「マイルドカカオ」です",font = ("",14,"bold"))
        lbl.pack()
        line = f.readlines()[3]
        print(line)
      elif v8.get() ==True or v5.get() ==True:#8定番or5お酒なし
        lbl = tk.Label(text="おすすめは定番のオレオです",font = ("",14,"bold"))
        lbl.pack()
        line = f.readlines()[1]
        lbl.pack()
        print(line)
      elif v6.get() ==True:#6抹茶
        lbl = tk.Label(text="おすすめは「抹茶」です",font = ("",14,"bold"))
        lbl.pack()
        line = f.readlines()[9]
        lbl.pack()
        print(line)
      elif v3.get() ==True:#3苦い
        lbl = tk.Label(text="おすすめは「ビター」です",font = ("",14,"bold"))
        lbl.pack()
        line = f.readlines()[1]
        print(line)
      elif v7.get() ==True:#7オレンジ
        lbl = tk.Label(text="おすすめは夏季限定販売の「オレンジ&マンゴー」です",font = ("",14,"bold"))
        lbl.pack()
        line = f.readlines()[13]
        lbl.pack()
        print(line)
      elif v1.get() ==True:#1ホワイト
        lbl = tk.Label(text="おすすめはホワイトです",font = ("",14,"bold"))
        lbl.pack()
        line = f.readlines()[7]
        print(line)
      elif v3.get() ==True and v4.get() ==True:#洋酒＆ほろにが
        lbl = tk.Label(text="おすすめはブランデーが香る「ビター」です",font = ("",14,"bold"))
        lbl.pack()
        line = f.readlines()[17]
        print(line)
      elif v4.get() ==True :#4洋酒あり
        lbl = tk.Label(text="おすすめはシャンパンです",font = ("",14,"bold"))
        lbl.pack()
        line = f.readlines()[11]
        print(line)
      elif v2.get() ==True:#2普通
        lbl = tk.Label(text="おすすめはカカオが香る「マイルドカカオ」です",font = ("",14,"bold"))
        lbl.pack()
        line = f.readlines()[3]
        print(line)
      else:
        anser()

#elseの場合
def anser():
    ans=input("　公式サイトのURLを表示する?(y/n)--->")
    if ans=="y":
        print("https://www.royce.com/goods/detail/?o_no=2050&in_category=C010")
    elif ans=="n":
        print("またね")
        
#チェックの認知
v1 = tk.BooleanVar()
v2 = tk.BooleanVar()
v3 = tk.BooleanVar()
v4 = tk.BooleanVar()
v5 = tk.BooleanVar()
v6 = tk.BooleanVar()
v7 = tk.BooleanVar()
v8 = tk.BooleanVar()

#チェックボックスの設定
c1=Checkbutton(root,text="甘い", variable=v1)
c2=Checkbutton(root,text="普通", variable=v2)
c3=Checkbutton(root,text="ほろ苦い", variable=v3)
c4=Checkbutton(root,text="洋酒入り", variable=v4)
c5=Checkbutton(root,text="洋酒なし", variable=v5)
c6=Checkbutton(root,text="抹茶", variable=v6)
c7=Checkbutton(root,text="柑橘系", variable=v7)
c8=Checkbutton(root,text="定番", variable=v8)

c1.pack()
c2.pack()
c3.pack()
c4.pack()
c5.pack()
c6.pack()
c7.pack()
c8.pack()

#ボタンの設定
button = tk.Button(root, text='結果',width=20,font = ("",15))
button.bind("<Button>",bclick)
button.pack()

root.mainloop()
