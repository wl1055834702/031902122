# coding=gbk
# 伍浪
# 加油冲冲冲
import sys
import pygame
import random
import time
import pygame.locals
import pygame.freetype
import requests
import tkinter
import tkinter.messagebox#弹窗库
pygame.init()
d = {'fangkuai01': pygame.image.load('pokes/fangkuai1.jpg'),  #将扑克牌图片放入字典，方便调用显示
     'fangkuai02': pygame.image.load('pokes/fangkuai2.jpg'),
     'fangkuai03': pygame.image.load('pokes/fangkuai3.jpg'),
     'fangkuai04': pygame.image.load('pokes/fangkuai4.jpg'),
     'fangkuai05': pygame.image.load('pokes/fangkuai5.jpg'),
     'fangkuai06': pygame.image.load('pokes/fangkuai6.jpg'),
     'fangkuai07': pygame.image.load('pokes/fangkuai7.jpg'),
     'fangkuai08': pygame.image.load('pokes/fangkuai8.jpg'),
     'fangkuai09': pygame.image.load('pokes/fangkuai9.jpg'),
     'fangkuai10': pygame.image.load('pokes/fangkuai10.jpg'),
     'fangkuai11': pygame.image.load('pokes/fangkuai11.jpg'),
     'fangkuai12': pygame.image.load('pokes/fangkuai12.jpg'),
     'fangkuai13': pygame.image.load('pokes/fangkuai13.jpg'),
     'heitao01': pygame.image.load('pokes/heitao1.jpg'),
     'heitao02': pygame.image.load('pokes/heitao2.jpg'),
     'heitao03': pygame.image.load('pokes/heitao3.jpg'),
     'heitao04': pygame.image.load('pokes/heitao4.jpg'),
     'heitao05': pygame.image.load('pokes/heitao5.jpg'),
     'heitao06': pygame.image.load('pokes/heitao6.jpg'),
     'heitao07': pygame.image.load('pokes/heitao7.jpg'),
     'heitao08': pygame.image.load('pokes/heitao8.jpg'),
     'heitao09': pygame.image.load('pokes/heitao9.jpg'),
     'heitao10': pygame.image.load('pokes/heitao10.jpg'),
     'heitao11': pygame.image.load('pokes/heitao11.jpg'),
     'heitao12': pygame.image.load('pokes/heitao12.jpg'),
     'heitao13': pygame.image.load('pokes/heitao13.jpg'),
     'hongtao01': pygame.image.load('pokes/hongtao1.jpg'),
     'hongtao02': pygame.image.load('pokes/hongtao2.jpg'),
     'hongtao03': pygame.image.load('pokes/hongtao3.jpg'),
     'hongtao04': pygame.image.load('pokes/hongtao4.jpg'),
     'hongtao05': pygame.image.load('pokes/hongtao5.jpg'),
     'hongtao06': pygame.image.load('pokes/hongtao6.jpg'),
     'hongtao07': pygame.image.load('pokes/hongtao7.jpg'),
     'hongtao08': pygame.image.load('pokes/hongtao8.jpg'),
     'hongtao09': pygame.image.load('pokes/hongtao9.jpg'),
     'hongtao10': pygame.image.load('pokes/hongtao10.jpg'),
     'hongtao11': pygame.image.load('pokes/hongtao11.jpg'),
     'hongtao12': pygame.image.load('pokes/hongtao12.jpg'),
     'hongtao13': pygame.image.load('pokes/hongtao13.jpg'),
     'meihua01': pygame.image.load('pokes/meihua1.jpg'),
     'meihua02': pygame.image.load('pokes/meihua2.jpg'),
     'meihua03': pygame.image.load('pokes/meihua3.jpg'),
     'meihua04': pygame.image.load('pokes/meihua4.jpg'),
     'meihua05': pygame.image.load('pokes/meihua5.jpg'),
     'meihua06': pygame.image.load('pokes/meihua6.jpg'),
     'meihua07': pygame.image.load('pokes/meihua7.jpg'),
     'meihua08': pygame.image.load('pokes/meihua8.jpg'),
     'meihua09': pygame.image.load('pokes/meihua9.jpg'),
     'meihua10': pygame.image.load('pokes/meihua10.jpg'),
     'meihua11': pygame.image.load('pokes/meihua11.jpg'),
     'meihua12': pygame.image.load('pokes/meihua12.jpg'),
     'meihua13': pygame.image.load('pokes/meihua13.jpg')}
newpai = ['fangkuai01','fangkuai02','fangkuai03','fangkuai04','fangkuai05','fangkuai06','fangkuai07','fangkuai08','fangkuai09',
     'fangkuai10','fangkuai11','fangkuai12','fangkuai13','heitao01','heitao02','heitao03','heitao04','heitao05',
     'heitao06','heitao07','heitao08','heitao09','heitao10','heitao11','heitao12','heitao13','hongtao01','hongtao02',
     'hongtao03','hongtao04','hongtao05','hongtao06','hongtao07','hongtao08','hongtao09','hongtao10','hongtao11',
     'hongtao12','hongtao13','meihua01','meihua02','meihua03','meihua04','meihua05','meihua06','meihua07','meihua08',
     'meihua09','meihua10','meihua11','meihua12','meihua13']

player1 = []                #初始化玩家一、玩家二（电脑）手牌，放置区、牌堆手牌
player2 = []
setpoker = []
pai = newpai[:]

turn = 1  #表示出牌方，1为玩家一，-1为玩家二或者电脑
def begin():
    pygame.init()  # 初始化init()及设置
    size = width, height = 566, 565  # 与下面的图片的大小，如果不一致会导致图片显示不完全，或者产生缝隙
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)  # 窗口大小
    pygame.display.set_caption("用户登录")  # 窗口名字
    # icon=pygame.image.load("snake.jpg")加载窗口图片
    # pygame.display.set_icon(icon)#设置窗口图片
    background = pygame.image.load("图片/backgroud.png")
    RED = pygame.Color("red")
    BLUE = pygame.Color("blue")
    BLACK = pygame.Color("black")
    GAINSBORO = pygame.Color("gainsboro")
    WHITESMOKE = pygame.Color("whitesmoke")
    MOCCASIN = pygame.Color("moccasin")
    WHITE = pygame.Color("white")
    # screen.fill(MOCCASIN)可以和下面的背景图二选一
    screen.blit(background, (0, 0))
    f1 = pygame.freetype.Font('C:\Windows\Fonts\simkai.ttf', size=50)  # 调出文字的字体
    f1.render_to(screen, [100, 150], "用户名 ：", fgcolor=WHITE, bgcolor=None, size=30)  # 强调文字
    f1.render_to(screen, [100, 210], "密  码 ：", fgcolor=WHITE, bgcolor=None, size=30)
    pygame.draw.rect(screen, WHITESMOKE, (230, 150, 200, 35))  # 两个输入框的位置，但不是真正的输入框，只是显示效果，可以实现文字的显示
    pygame.draw.rect(screen, WHITESMOKE, (230, 210, 200, 35))
    a, b = [], []  # 创建两个空列表，用来分别存储用户名和密码
    while True:
        # 为了实现鼠标移到按钮处，改变颜色，需要不断重绘鼠标不在按钮处时的按钮
        dl = f1.render_to(screen, [100, 400], "登记", fgcolor=BLACK, bgcolor=WHITESMOKE, size=50)
        zc = f1.render_to(screen, [400, 400], "登录", fgcolor=BLACK, bgcolor=WHITESMOKE, size=50)
        # 事件检测
        Flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()  # 鼠标的点击位置
                if 230 <= mouse_x <= 430 and 150 <= mouse_y <= 185:  # 判断点击了哪一个输入框
                    pygame.draw.rect(screen, WHITE, (230, 150, 200, 35))
                    pygame.draw.rect(screen, WHITESMOKE, (230, 210, 200, 35))
                    wz = True  # 用于改变后文文字输入显示的位置
                elif 230 <= mouse_x <= 430 and 210 <= mouse_y <= 245:
                    pygame.draw.rect(screen, WHITE, (230, 210, 200, 35))
                    pygame.draw.rect(screen, WHITESMOKE, (230, 150, 200, 35))
                    wz = False
                elif 400 < mouse_x < 400 + dl[2] and 400 < mouse_y < 400 + dl[3]:
                    Flag = True
                    print("登录成功！")  # 判断按钮点击的位置是否是在登录按钮的区域内
            elif event.type == pygame.KEYDOWN:  # 检测按键是否是数字键，通过打印输3出判断按键的码
                if wz and len(a) < 13:  # 限制输入的长度，利用WZ来更改输入内容的显示位置
                    a.append(event.unicode)
                elif wz == False and len(b) < 13:
                    b.append(event.unicode)
        str_a = ""  # 将输入内容存储到列表
        for i in a:
            str_a += str(i)  # 转化拼接为字符串
        str_b = ""
        for i in b:
            str_b += str(i)
        url = "http://172.17.173.97:8080/api/user/login"
        payload = {'student_id': str_a,
                   'password': str_b}
        files = [
        ]
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        s = eval(response.text)
        # 显示字符串
        f1.render_to(screen, [235, 159], str_a, fgcolor=BLACK, bgcolor=WHITE, size=30)
        f1.render_to(screen, [235, 219], str_b, fgcolor=BLACK, bgcolor=WHITE, size=30)
        x, y = pygame.mouse.get_pos()  # 判断鼠标移动到那个位置了，更改文字的背景色，文字的显示区域是一个矩形
        if x > 100 and y > 400 and x < 100 + zc[2] and y < 400 + zc[3]:
            f1.render_to(screen, [100, 400], "登记", fgcolor=BLACK, bgcolor=GAINSBORO, size=50)
        elif x > 400 and y > 400 and x < 400 + dl[2] and y < 400 + dl[3]:
            f1.render_to(screen, [400, 400], "登录", fgcolor=BLACK, bgcolor=GAINSBORO, size=50)
        pygame.display.update()
        if Flag == True and s['message'] == 'Success':

            return s['data']['token']
            sys.exit()
from tkinter import *

class MyDialog:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="请输入房间号").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)
    def ok(self):
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('提示', '加入房间成功！')
        self.top.destroy()
class choose():
    global token_
    global uuid_
    def __init__(self,token):
        pygame.init()
        pygame.display.set_caption('在线对战')
        screen = pygame.display.set_mode((1400, 750))
        background = pygame.image.load('图片/backgroud.png')
        screen.blit(background, (0, 0))
        botton1=pygame.image.load('按钮/按钮1.png')
        botton2=pygame.image.load('按钮/按钮2.png')
        botton3= pygame.image.load('按钮/按钮3.png')
        botton4 = pygame.image.load('按钮/按钮4.png')
        screen.blit(botton1,(450,400))
        screen.blit(botton2,(450,520))
        screen.blit(botton3, (800, 400))
        screen.blit(botton4, (800, 520))
        self.botton1_area=pygame.Rect(460, 411, 155,60)
        self.botton2_area = pygame.Rect(469,526,150,60)
        self.mouse_position=''
        self.token=token
        self.uudi=''
    def uuid1(self):
        return self.uudi
    def get_uuid(self,token):
        url = "http://172.17.173.97:9000/api/game"
        payload = {'student_id': '031902129',
                   'password': 'yuanyuan520'}
        files = [
        ]
        headers = {
            'Authorization': token}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        s = eval(response.text)
        if s['msg'] == '操作成功':
            root = tkinter.Tk()
            root.withdraw()
            tkinter.messagebox.showinfo('提示', '你创建的房间号为:' + str(s['data']['uuid']))

        return s['data']['uuid']
    def join_uuid(self,token):
        url = "http://172.17.173.97:9000/api/game/"+str(self.uuid)
        payload = {'student_id': '031902129',
                   'password': 'yuanyuan520'}
        files = [
        ]
        headers = {
            'Authorization':token
        }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        s = eval(response.text)
        if s['msg'] == '操作成功':
            root = Tk()
            Button(root, text="Hello!").pack()
            root.update()

            d = MyDialog(root)

            root.wait_window(d.top)
            root.mainloop()
            pygame.display.update()

    def run_game(self):
        Flag=False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_position = pygame.mouse.get_pos()
                    print(event.pos)
                    if self.botton1_area.collidepoint(self.mouse_position):
                        self.uuid=self.get_uuid(self.token)
                        print(self.uuid)

                    if self.botton2_area.collidepoint(self.mouse_position):
                        try:
                            pygame.quit()
                            self.join_uuid(self.token)
                        except:
                            root = tkinter.Tk()
                            root.withdraw()
                            tkinter.messagebox.showinfo('提示', '还未创建房间！' )



            pygame.display.flip()
class begingame:                             #模式选择，规则说明
    def __init__(self):
        pygame.init()
        self.rule = 0
        pygame.display.set_caption("猪尾巴")
        self.screen = pygame.display.set_mode((1400, 750))
        self.begingame = pygame.image.load('图片/开始游戏.png')
        self.typeselect = pygame.image.load('图片/模式选择.png')
        self.rule1 = pygame.image.load('图片/规则1.png')
        self.rule2 = pygame.image.load('图片/规则2.png')
        self.beginarea = pygame.Rect(584, 640, 236, 72)
        self.pve = pygame.Rect(580, 400, 270, 90)
        self.pvp = pygame.Rect(580, 515, 270, 90)
        self.net = pygame.Rect(580, 630, 270, 90)
        self.rulearea = pygame.Rect(1230, 0, 170, 60)
        self.returnarea1 = pygame.Rect(0, 0, 175, 65)
        self.returnarea2 = pygame.Rect(1220, 0, 280, 70)
        self.changerulearea = pygame.Rect(1224, 682, 176, 68)
        self.s = 1

    def update(self):
        if self.s == 1:
            if self.rule == 1:
                self.screen.blit(self.rule1, (0, 0))
            elif self.rule == 2:
                self.screen.blit(self.rule2, (0, 0))
            else:
                self.screen.blit(self.begingame, (0, 0))
        else:
            self.screen.blit(self.typeselect, (0, 0))

    def mouse(self, xy):
        if self.s == 1:
            if self.rulearea.collidepoint(xy) and self.rule == 0:
                self.rule = 1
            elif self.changerulearea.collidepoint(xy) and self.rule == 1:
                self.rule = 2
            elif self.changerulearea.collidepoint(xy) and self.rule == 2:
                self.rule = 1
            elif self.returnarea1.collidepoint(xy) and self.rule != 0:
                self.rule = 0
            elif self.beginarea.collidepoint(xy) and self.rule == 0:
                self.s = 2
            self.update()
        elif self.s == 2:
            if self.pvp.collidepoint(xy):                     #双人模式
                self.ai = Cardgame()
                self.ai.run_game()
            if self.pve.collidepoint(xy):                     #人机模式
                self.ai=Cardgame()
                self.ai.pve()
                self.ai.run_game()
            if self.net.collidepoint(xy):
                a = choose(begin())
                a.run_game()

                ##############
            if self.returnarea2.collidepoint(xy):
                self.s = 1

    def runbegin(self):
        while True:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse(event.pos)
            pygame.display.flip()


class Cardgame:                                     #真正的游戏类
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("猪尾巴")
        self.screen = pygame.display.set_mode((1400, 750))
        self.background = pygame.image.load('图片/backgroud.png')
        self.screen.blit(self.background, (0, 0))
        self.cardpile = pygame.image.load('图片/牌堆.png')  # 更改了牌堆和放置区的名称，方便后续更新画面
        self.cadempty = pygame.image.load('图片/空牌堆.png')  # 空牌堆
        self.screen.blit(self.cardpile, (260, 255))
        self.cardset = pygame.image.load('图片/放置区.png')
        self.screen.blit(self.cardset, (950, 255))
        self.area = pygame.Rect(280, 316, 123, 151)
        self.fire1area = pygame.Rect(620, 476, 130, 64)
        self.fire2area = pygame.Rect(620, 210, 130, 64)
        self.again_area = pygame.Rect(470, 580, 180, 80)
        self.return_area = pygame.Rect(720, 580, 180, 80)
        self.player1auto = pygame.Rect(972, 542, 152, 55)
        self.player2auto = pygame.Rect(282, 175, 152, 55)
        self.firebotton = pygame.image.load('按钮/出牌.png')
        self.newcard = pygame.image.load('图片/放置区.png')  # 放置区最外面一张牌
        self.bequick = pygame.image.load('按钮/快出牌.png')
        self.auto = pygame.image.load('按钮/托管.png')
        self.notauto =pygame.image.load('按钮/取消托管.png')
        self.win1 = pygame.image.load('图片/player1win.png')
        self.win2 = pygame.image.load('图片/player2win.png')
        self.draw = pygame.image.load('图片/平局.png')
        self.again_game = pygame.image.load('按钮/再来一局.png')
        self.return_game = pygame.image.load('按钮/返回主菜单.png')
        self.player2image =pygame.image.load('图片/头像机器人.png')
        self.player1image =pygame.image.load('图片/农民.png')
        self.player1name = pygame.image.load('按钮/玩家一.png')
        self.player2name = pygame.image.load('按钮/玩家二.png')
        self.autoname = pygame.image.load('按钮/阿尔发.png')
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render(f'cards:{len(pai)}', True, (0, 0, 0), (255, 255, 255))
        self.lnewcard = ''  # 新的newcard
        self.ischupai = 0  # 判断是否出牌
        self.ifauoto=0
        self.chupai = -1                             #第几张牌，-1表示没出牌
        self.istrusteeship1 = False                  #表示是否托管
        self.istrusteeship2 = False
        self.tuopai=1                                #判断托管是否应该出牌，1为出，0为不出
    def pve(self):               #人机模式            #人机模式的额外初始化，在模式选择时候调用
        self.istrusteeship2=True
        self.ifauoto=1                              #代表人机模式

    def reset(self, lst):                           #摸牌操作
        random.shuffle(lst)
        self.newcard = lst[-1]  # 记录放置区最上面的牌
        setpoker.append(lst.pop())  # 将牌堆弹出的牌放入放置区队列，同时记录这张牌
        global turn
        self.eatcard(setpoker)
        turn = -turn                                # 换玩家出牌

    def eatcard(self, lst):                        #判断吃牌
        global turn
        if len(lst) > 1:
            if lst[-1][0:2] == lst[-2][0:2]:  # 判断牌名前三个字符一样即可
                if (turn == 1):
                    player1.extend(lst)
                elif (turn == -1):
                    player2.extend(lst)
                lst.clear()
                self.newcard=''
                self.lnewcard=''

    def update(self):                  # 更新屏幕
        global turn
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player1image,(10,600))
        self.screen.blit(self.player2image,(1250,10))
        self.screen.blit(self.cardset, (950, 255))
        self.screen.blit(self.player1name,(17,542))
        if self.istrusteeship1==1:
            self.screen.blit(self.notauto,(972,542))
        else:
            self.screen.blit(self.auto, (972, 542))
        if self.ifauoto==0:
            self.screen.blit(self.player1image, (1250, 10))
            self.screen.blit(self.player2name, (1257, 175))
            if self.istrusteeship2 == 1:
                self.screen.blit(self.notauto, (282, 175))
            else:
                self.screen.blit(self.auto, (282, 175))
        else:
            self.screen.blit(self.player2image, (1250, 10))
            self.screen.blit(self.autoname, (1257, 175))
        if len(pai) != 0:
            self.screen.blit(self.cardpile, (260, 255))
        else:
            self.screen.blit(self.cadempty, (260, 255))
        if self.chupai != -1 and turn == 1:  # 开火
            self.screen.blit(self.firebotton, (620, 476))
        if self.chupai != -1 and turn == -1:
            self.screen.blit(self.firebotton, (620, 210))
        if len(setpoker) != 0:
            self.screen.blit(d[self.newcard], (980, 321))           #以上到这为基础显示

        self.text = self.font.render(f'cards:{len(pai)}', True, (0, 0, 0), (255, 255, 255))     #剩余牌数
        self.screen.blit(self.text, (120, 360))
        player1.sort()                                               # 手牌排序
        player2.sort()
        l1 = (1400 - len(player1) * 20 - 85) / 2                     #计算距离，用于手牌居中
        l2 = (1400 - len(player2) * 20 - 85) / 2
        if self.istrusteeship1==False:
            j=0  # 更新玩家1手牌区
            for i in player1:                                    #非托管玩家一手牌显示
                if j == self.chupai and turn == 1:
                    self.screen.blit(d[i], (j * 20 + l1, 560))
                else:
                    self.screen.blit(d[i], (j * 20 + l1, 600))
                j = j + 1
        else:
            j = 0
            for i in player1:                                     #托管时玩家一手牌显示
                self.screen.blit(d[i], (j * 20 + l1, 600))
                j = j + 1
        if self.istrusteeship2==False:
            j=0  # 更新玩家2手牌区
            for i in player2:                                    #玩家二手牌显示
                if j == self.chupai and turn == -1:
                    self.screen.blit(d[i], (j * 20+l2, 40))
                else:
                    self.screen.blit(d[i], (j * 20+l2,0))
                j = j + 1
        else:
            j = 0
            for i in player2:                                   #电脑或玩家二托管时手牌显示
                self.screen.blit(d[i], (j * 20+l2, 0))
                j = j + 1

        if turn == 1:                                            #出牌提醒按键
            self.screen.blit(self.bequick, (282, 542))
        else:
            self.screen.blit(self.bequick, (972, 175))

        if len(pai) == 0:                                        #胜利结算
            if (len(player1) < len(player2)):
                self.screen.blit(self.win1, (470, 190))
            elif (len(player1)>len(player2)):
                self.screen.blit(self.win2, (470, 190))
            else:
                self.screen.blit(self.draw,(470,190))
            self.screen.blit(self.again_game, (470, 580))
            self.screen.blit(self.return_game, (720, 580))

    def renew(self):                                             #一局游戏结束后初始化各个牌组及参数
        global pai
        global setpoker
        global player1
        global player2
        self.chupai=-1
        pai = newpai[:]
        setpoker = []
        player1 = []
        player2 = []

    def mouse(self, xy):                         # 判断鼠标操作，为鼠标坐标
        turnchange = 0
        global turn
        x = xy[0]
        y = xy[1]
        if self.player1auto.collidepoint(xy):     #玩家一托管与取消托管
            if self.istrusteeship1==False:
                self.istrusteeship1 = True
            else:
                self.istrusteeship1 =False
            self.update()
        elif self.player2auto.collidepoint(xy) and self.ifauoto==0:      #双人时玩家二托管与取消托管
            if self.istrusteeship2==False:
                self.istrusteeship2 = True
            else:
                self.istrusteeship2 =False
            self.update()

        else:
            if self.area.collidepoint(xy) and len(pai) != 0:              #抽牌
                self.reset(pai)
                self.eatcard(setpoker)
                self.chupai = -1  # 换人把出牌恢复
            if self.fire1area.collidepoint(xy) and self.chupai != -1 and turn == 1:  #玩家一出牌
                if len(player1) != 0:
                    setpoker.append(player1[self.chupai])
                    self.newcard = player1.pop(self.chupai)
                    self.chupai = -1
                    self.eatcard(setpoker)
                    turn=-turn
            if self.fire2area.collidepoint(xy) and self.chupai != -1 and turn == -1:  #电脑或玩家二出牌
                if len(player2) != 0:
                    setpoker.append(player2[self.chupai])
                    self.newcard = player2.pop(self.chupai)
                    self.chupai = -1
                    self.eatcard(setpoker)
                    turn=-turn
            l1 = (1400 - len(player1) * 20 - 85) / 2                                  #轮到玩家一时判断点的第几张牌，突出显示
            if x < len(player1) * 20 + 85 + l1 and 600 < y < 750 and turn == 1 and self.istrusteeship1 ==False:
                if x <= len(player1) * 20 + l1:
                    self.ifchupai = int((x - l1) // 20)
                else:
                    self.ifchupai = len(player1) - 1
                if self.ifchupai == self.chupai:
                    self.chupai = -1
                else:
                    self.chupai = self.ifchupai
            l2 = (1400 - len(player2) * 20 - 85) / 2                                  #轮到玩家二时判断点的第几张牌，突出显示
            if x < len(player2) * 20 + 85 + l2 and 0 < y < 150 and turn == -1 and self.istrusteeship2 == False:
                if x <= len(player2) * 20 + l2:
                    self.ifchupai = int((x - l2) // 20)
                else:
                    self.ifchupai = len(player2) - 1
                if self.ifchupai == self.chupai:
                    self.chupai = -1
                else:
                    self.chupai = self.ifchupai
            self.update()

    def tuoguan(self):                         #托管或机器
        self.tuopai=1
        if turn == 1:
            if len(player1)==0 and len(pai)!=0:
                self.reset(pai)
                self.chupai = -1
                self.update()
                time.sleep(0.3)
            else:
                self.trusteeship(player1)
                if self.tuopai==0:
                    self.reset(pai)
                    self.chupai = -1
                self.update()
                time.sleep(0.3)
                if self.tuopai==1:
                    self.secondcard()
                    self.update()
                    time.sleep(0.3)
        else:
            if len(player2) == 0 and len(pai) != 0:
                self.reset(pai)
                self.chupai = -1
                self.update()
                time.sleep(0.3)
            else:
                self.trusteeship(player2)
                if self.tuopai == 0:
                    self.reset(pai)
                    self.chupai = -1
                self.update()
                time.sleep(0.3)
                if self.tuopai == 1:
                    self.secondcard()
                    self.update()
                    time.sleep(0.3)


    def run_game(self):
        """开始游戏的主循环"""
        self.update()
        Flag = True
        while Flag == True:
            if self.istrusteeship1 == True and turn == 1 and len(pai)!=0:       #判断托管及人机对战
                self.tuoguan()
            elif self.istrusteeship2 == True and turn == -1 and len(pai)!=0:
                self.tuoguan()
            for event in pygame.event.get():                                   #鼠标操作
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse(event.pos)  # 鼠标事件，调用mouse函数
                    if len(pai) == 0 and self.return_area.collidepoint(event.pos):
                        Flag = False  # 把停止先停了，看下结算界面
                        self.renew()
                    if len(pai) == 0 and self.again_area.collidepoint(event.pos):
                        self.renew()
                        self.update()
            pygame.display.flip()

    def secondcard(self):                             #处理自动或托管模式下打出的牌
        global turn
        if self.istrusteeship1==True and turn == 1:   #玩家一托管更新打出的那张牌
            self.newcard = self.lnewcard
            setpoker.append(self.newcard)
            player1.remove(self.newcard)
        elif self.istrusteeship2==True and turn == -1 :   #玩家二托管更新打出的那张牌
            self.newcard = self.lnewcard
            setpoker.append(self.newcard)
            player2.remove(self.newcard)
        turn = -turn

    def trusteeship(self, lst):         # 判断自动模式下应该打出的那张牌或者选择摸牌
        new_card = ''
        max1=''
        dict = {'count_meihua': 0, 'count_fangkuai': 0, 'count_hongtao': 0, 'count_heitao': 0}
        #if len(lst) == 0:
        #    self.reset(lst)
        for item in lst:
            if item[4] == 'u':
                dict['count_meihua'] += 1
            elif item[4] == 'k':
                dict['count_fangkuai'] += 1
            elif item[4] == 't':
                dict['count_hongtao'] += 1
            else:
                dict['count_heitao'] += 1
        for k, v in dict.items():
            if v == max(dict.values()):
                max1 = k
        if turn==1 and (len(player1)+3*len(pai)+len(setpoker)-2)<len(player2):     #自动或机器ai判定，一定情况下抽牌必赢，则有手牌也自动摸牌
            self.tuopai=0
        if turn==-1 and (len(player2)+3*len(pai)+len(setpoker)-2)<len(player1):
            self.tuopai=0
        if len(setpoker)==0:
            for item in lst:
                if max1[10] == item[4]:  # new_card放选中要被打出去的牌
                    new_card = item
                    break
        else:
            if max1[10] == self.newcard[4]:
                del dict[max1]
                if max(dict.values()) == 0:
                    max1 = ''
                else:
                    for k, v in dict.items():
                        if v == max(dict.values()):
                            max1 = k
            if max1 != '':
                for item in lst:
                    if max1[10] == item[4]:  # new_card放选中要被打出去的牌
                        new_card = item
                        break
            else:
                self.tuopai = 0
        self.lnewcard = new_card

if __name__ == '__main__':                #运行程序
    # 创建游戏实例并运行游戏
    bi = begingame()
    bi.runbegin()