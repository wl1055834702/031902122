# coding=gbk
# ����
# ���ͳ���
import sys
import pygame
import random
import time
import pygame.locals
import pygame.freetype
import requests
import tkinter
import tkinter.messagebox#������
pygame.init()
d = {'fangkuai01': pygame.image.load('pokes/fangkuai1.jpg'),  #���˿���ͼƬ�����ֵ䣬���������ʾ
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

player1 = []                #��ʼ�����һ����Ҷ������ԣ����ƣ����������ƶ�����
player2 = []
setpoker = []
pai = newpai[:]

turn = 1  #��ʾ���Ʒ���1Ϊ���һ��-1Ϊ��Ҷ����ߵ���
def begin():
    pygame.init()  # ��ʼ��init()������
    size = width, height = 566, 565  # �������ͼƬ�Ĵ�С�������һ�»ᵼ��ͼƬ��ʾ����ȫ�����߲�����϶
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)  # ���ڴ�С
    pygame.display.set_caption("�û���¼")  # ��������
    # icon=pygame.image.load("snake.jpg")���ش���ͼƬ
    # pygame.display.set_icon(icon)#���ô���ͼƬ
    background = pygame.image.load("ͼƬ/backgroud.png")
    RED = pygame.Color("red")
    BLUE = pygame.Color("blue")
    BLACK = pygame.Color("black")
    GAINSBORO = pygame.Color("gainsboro")
    WHITESMOKE = pygame.Color("whitesmoke")
    MOCCASIN = pygame.Color("moccasin")
    WHITE = pygame.Color("white")
    # screen.fill(MOCCASIN)���Ժ�����ı���ͼ��ѡһ
    screen.blit(background, (0, 0))
    f1 = pygame.freetype.Font('C:\Windows\Fonts\simkai.ttf', size=50)  # �������ֵ�����
    f1.render_to(screen, [100, 150], "�û��� ��", fgcolor=WHITE, bgcolor=None, size=30)  # ǿ������
    f1.render_to(screen, [100, 210], "��  �� ��", fgcolor=WHITE, bgcolor=None, size=30)
    pygame.draw.rect(screen, WHITESMOKE, (230, 150, 200, 35))  # ����������λ�ã������������������ֻ����ʾЧ��������ʵ�����ֵ���ʾ
    pygame.draw.rect(screen, WHITESMOKE, (230, 210, 200, 35))
    a, b = [], []  # �����������б������ֱ�洢�û���������
    while True:
        # Ϊ��ʵ������Ƶ���ť�����ı���ɫ����Ҫ�����ػ���겻�ڰ�ť��ʱ�İ�ť
        dl = f1.render_to(screen, [100, 400], "�Ǽ�", fgcolor=BLACK, bgcolor=WHITESMOKE, size=50)
        zc = f1.render_to(screen, [400, 400], "��¼", fgcolor=BLACK, bgcolor=WHITESMOKE, size=50)
        # �¼����
        Flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.locals.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()  # ���ĵ��λ��
                if 230 <= mouse_x <= 430 and 150 <= mouse_y <= 185:  # �жϵ������һ�������
                    pygame.draw.rect(screen, WHITE, (230, 150, 200, 35))
                    pygame.draw.rect(screen, WHITESMOKE, (230, 210, 200, 35))
                    wz = True  # ���ڸı��������������ʾ��λ��
                elif 230 <= mouse_x <= 430 and 210 <= mouse_y <= 245:
                    pygame.draw.rect(screen, WHITE, (230, 210, 200, 35))
                    pygame.draw.rect(screen, WHITESMOKE, (230, 150, 200, 35))
                    wz = False
                elif 400 < mouse_x < 400 + dl[2] and 400 < mouse_y < 400 + dl[3]:
                    Flag = True
                    print("��¼�ɹ���")  # �жϰ�ť�����λ���Ƿ����ڵ�¼��ť��������
            elif event.type == pygame.KEYDOWN:  # ��ⰴ���Ƿ������ּ���ͨ����ӡ��3���жϰ�������
                if wz and len(a) < 13:  # ��������ĳ��ȣ�����WZ�������������ݵ���ʾλ��
                    a.append(event.unicode)
                elif wz == False and len(b) < 13:
                    b.append(event.unicode)
        str_a = ""  # ���������ݴ洢���б�
        for i in a:
            str_a += str(i)  # ת��ƴ��Ϊ�ַ���
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
        # ��ʾ�ַ���
        f1.render_to(screen, [235, 159], str_a, fgcolor=BLACK, bgcolor=WHITE, size=30)
        f1.render_to(screen, [235, 219], str_b, fgcolor=BLACK, bgcolor=WHITE, size=30)
        x, y = pygame.mouse.get_pos()  # �ж�����ƶ����Ǹ�λ���ˣ��������ֵı���ɫ�����ֵ���ʾ������һ������
        if x > 100 and y > 400 and x < 100 + zc[2] and y < 400 + zc[3]:
            f1.render_to(screen, [100, 400], "�Ǽ�", fgcolor=BLACK, bgcolor=GAINSBORO, size=50)
        elif x > 400 and y > 400 and x < 400 + dl[2] and y < 400 + dl[3]:
            f1.render_to(screen, [400, 400], "��¼", fgcolor=BLACK, bgcolor=GAINSBORO, size=50)
        pygame.display.update()
        if Flag == True and s['message'] == 'Success':

            return s['data']['token']
            sys.exit()
from tkinter import *

class MyDialog:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="�����뷿���").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)
    def ok(self):
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo('��ʾ', '���뷿��ɹ���')
        self.top.destroy()
class choose():
    global token_
    global uuid_
    def __init__(self,token):
        pygame.init()
        pygame.display.set_caption('���߶�ս')
        screen = pygame.display.set_mode((1400, 750))
        background = pygame.image.load('ͼƬ/backgroud.png')
        screen.blit(background, (0, 0))
        botton1=pygame.image.load('��ť/��ť1.png')
        botton2=pygame.image.load('��ť/��ť2.png')
        botton3= pygame.image.load('��ť/��ť3.png')
        botton4 = pygame.image.load('��ť/��ť4.png')
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
        if s['msg'] == '�����ɹ�':
            root = tkinter.Tk()
            root.withdraw()
            tkinter.messagebox.showinfo('��ʾ', '�㴴���ķ����Ϊ:' + str(s['data']['uuid']))

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
        if s['msg'] == '�����ɹ�':
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
                            tkinter.messagebox.showinfo('��ʾ', '��δ�������䣡' )



            pygame.display.flip()
class begingame:                             #ģʽѡ�񣬹���˵��
    def __init__(self):
        pygame.init()
        self.rule = 0
        pygame.display.set_caption("��β��")
        self.screen = pygame.display.set_mode((1400, 750))
        self.begingame = pygame.image.load('ͼƬ/��ʼ��Ϸ.png')
        self.typeselect = pygame.image.load('ͼƬ/ģʽѡ��.png')
        self.rule1 = pygame.image.load('ͼƬ/����1.png')
        self.rule2 = pygame.image.load('ͼƬ/����2.png')
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
            if self.pvp.collidepoint(xy):                     #˫��ģʽ
                self.ai = Cardgame()
                self.ai.run_game()
            if self.pve.collidepoint(xy):                     #�˻�ģʽ
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


class Cardgame:                                     #��������Ϸ��
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("��β��")
        self.screen = pygame.display.set_mode((1400, 750))
        self.background = pygame.image.load('ͼƬ/backgroud.png')
        self.screen.blit(self.background, (0, 0))
        self.cardpile = pygame.image.load('ͼƬ/�ƶ�.png')  # �������ƶѺͷ����������ƣ�����������»���
        self.cadempty = pygame.image.load('ͼƬ/���ƶ�.png')  # ���ƶ�
        self.screen.blit(self.cardpile, (260, 255))
        self.cardset = pygame.image.load('ͼƬ/������.png')
        self.screen.blit(self.cardset, (950, 255))
        self.area = pygame.Rect(280, 316, 123, 151)
        self.fire1area = pygame.Rect(620, 476, 130, 64)
        self.fire2area = pygame.Rect(620, 210, 130, 64)
        self.again_area = pygame.Rect(470, 580, 180, 80)
        self.return_area = pygame.Rect(720, 580, 180, 80)
        self.player1auto = pygame.Rect(972, 542, 152, 55)
        self.player2auto = pygame.Rect(282, 175, 152, 55)
        self.firebotton = pygame.image.load('��ť/����.png')
        self.newcard = pygame.image.load('ͼƬ/������.png')  # ������������һ����
        self.bequick = pygame.image.load('��ť/�����.png')
        self.auto = pygame.image.load('��ť/�й�.png')
        self.notauto =pygame.image.load('��ť/ȡ���й�.png')
        self.win1 = pygame.image.load('ͼƬ/player1win.png')
        self.win2 = pygame.image.load('ͼƬ/player2win.png')
        self.draw = pygame.image.load('ͼƬ/ƽ��.png')
        self.again_game = pygame.image.load('��ť/����һ��.png')
        self.return_game = pygame.image.load('��ť/�������˵�.png')
        self.player2image =pygame.image.load('ͼƬ/ͷ�������.png')
        self.player1image =pygame.image.load('ͼƬ/ũ��.png')
        self.player1name = pygame.image.load('��ť/���һ.png')
        self.player2name = pygame.image.load('��ť/��Ҷ�.png')
        self.autoname = pygame.image.load('��ť/������.png')
        self.font = pygame.font.Font(None, 40)
        self.text = self.font.render(f'cards:{len(pai)}', True, (0, 0, 0), (255, 255, 255))
        self.lnewcard = ''  # �µ�newcard
        self.ischupai = 0  # �ж��Ƿ����
        self.ifauoto=0
        self.chupai = -1                             #�ڼ����ƣ�-1��ʾû����
        self.istrusteeship1 = False                  #��ʾ�Ƿ��й�
        self.istrusteeship2 = False
        self.tuopai=1                                #�ж��й��Ƿ�Ӧ�ó��ƣ�1Ϊ����0Ϊ����
    def pve(self):               #�˻�ģʽ            #�˻�ģʽ�Ķ����ʼ������ģʽѡ��ʱ�����
        self.istrusteeship2=True
        self.ifauoto=1                              #�����˻�ģʽ

    def reset(self, lst):                           #���Ʋ���
        random.shuffle(lst)
        self.newcard = lst[-1]  # ��¼���������������
        setpoker.append(lst.pop())  # ���ƶѵ������Ʒ�����������У�ͬʱ��¼������
        global turn
        self.eatcard(setpoker)
        turn = -turn                                # ����ҳ���

    def eatcard(self, lst):                        #�жϳ���
        global turn
        if len(lst) > 1:
            if lst[-1][0:2] == lst[-2][0:2]:  # �ж�����ǰ�����ַ�һ������
                if (turn == 1):
                    player1.extend(lst)
                elif (turn == -1):
                    player2.extend(lst)
                lst.clear()
                self.newcard=''
                self.lnewcard=''

    def update(self):                  # ������Ļ
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
        if self.chupai != -1 and turn == 1:  # ����
            self.screen.blit(self.firebotton, (620, 476))
        if self.chupai != -1 and turn == -1:
            self.screen.blit(self.firebotton, (620, 210))
        if len(setpoker) != 0:
            self.screen.blit(d[self.newcard], (980, 321))           #���ϵ���Ϊ������ʾ

        self.text = self.font.render(f'cards:{len(pai)}', True, (0, 0, 0), (255, 255, 255))     #ʣ������
        self.screen.blit(self.text, (120, 360))
        player1.sort()                                               # ��������
        player2.sort()
        l1 = (1400 - len(player1) * 20 - 85) / 2                     #������룬�������ƾ���
        l2 = (1400 - len(player2) * 20 - 85) / 2
        if self.istrusteeship1==False:
            j=0  # �������1������
            for i in player1:                                    #���й����һ������ʾ
                if j == self.chupai and turn == 1:
                    self.screen.blit(d[i], (j * 20 + l1, 560))
                else:
                    self.screen.blit(d[i], (j * 20 + l1, 600))
                j = j + 1
        else:
            j = 0
            for i in player1:                                     #�й�ʱ���һ������ʾ
                self.screen.blit(d[i], (j * 20 + l1, 600))
                j = j + 1
        if self.istrusteeship2==False:
            j=0  # �������2������
            for i in player2:                                    #��Ҷ�������ʾ
                if j == self.chupai and turn == -1:
                    self.screen.blit(d[i], (j * 20+l2, 40))
                else:
                    self.screen.blit(d[i], (j * 20+l2,0))
                j = j + 1
        else:
            j = 0
            for i in player2:                                   #���Ի���Ҷ��й�ʱ������ʾ
                self.screen.blit(d[i], (j * 20+l2, 0))
                j = j + 1

        if turn == 1:                                            #�������Ѱ���
            self.screen.blit(self.bequick, (282, 542))
        else:
            self.screen.blit(self.bequick, (972, 175))

        if len(pai) == 0:                                        #ʤ������
            if (len(player1) < len(player2)):
                self.screen.blit(self.win1, (470, 190))
            elif (len(player1)>len(player2)):
                self.screen.blit(self.win2, (470, 190))
            else:
                self.screen.blit(self.draw,(470,190))
            self.screen.blit(self.again_game, (470, 580))
            self.screen.blit(self.return_game, (720, 580))

    def renew(self):                                             #һ����Ϸ�������ʼ���������鼰����
        global pai
        global setpoker
        global player1
        global player2
        self.chupai=-1
        pai = newpai[:]
        setpoker = []
        player1 = []
        player2 = []

    def mouse(self, xy):                         # �ж���������Ϊ�������
        turnchange = 0
        global turn
        x = xy[0]
        y = xy[1]
        if self.player1auto.collidepoint(xy):     #���һ�й���ȡ���й�
            if self.istrusteeship1==False:
                self.istrusteeship1 = True
            else:
                self.istrusteeship1 =False
            self.update()
        elif self.player2auto.collidepoint(xy) and self.ifauoto==0:      #˫��ʱ��Ҷ��й���ȡ���й�
            if self.istrusteeship2==False:
                self.istrusteeship2 = True
            else:
                self.istrusteeship2 =False
            self.update()

        else:
            if self.area.collidepoint(xy) and len(pai) != 0:              #����
                self.reset(pai)
                self.eatcard(setpoker)
                self.chupai = -1  # ���˰ѳ��ƻָ�
            if self.fire1area.collidepoint(xy) and self.chupai != -1 and turn == 1:  #���һ����
                if len(player1) != 0:
                    setpoker.append(player1[self.chupai])
                    self.newcard = player1.pop(self.chupai)
                    self.chupai = -1
                    self.eatcard(setpoker)
                    turn=-turn
            if self.fire2area.collidepoint(xy) and self.chupai != -1 and turn == -1:  #���Ի���Ҷ�����
                if len(player2) != 0:
                    setpoker.append(player2[self.chupai])
                    self.newcard = player2.pop(self.chupai)
                    self.chupai = -1
                    self.eatcard(setpoker)
                    turn=-turn
            l1 = (1400 - len(player1) * 20 - 85) / 2                                  #�ֵ����һʱ�жϵ�ĵڼ����ƣ�ͻ����ʾ
            if x < len(player1) * 20 + 85 + l1 and 600 < y < 750 and turn == 1 and self.istrusteeship1 ==False:
                if x <= len(player1) * 20 + l1:
                    self.ifchupai = int((x - l1) // 20)
                else:
                    self.ifchupai = len(player1) - 1
                if self.ifchupai == self.chupai:
                    self.chupai = -1
                else:
                    self.chupai = self.ifchupai
            l2 = (1400 - len(player2) * 20 - 85) / 2                                  #�ֵ���Ҷ�ʱ�жϵ�ĵڼ����ƣ�ͻ����ʾ
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

    def tuoguan(self):                         #�йܻ����
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
        """��ʼ��Ϸ����ѭ��"""
        self.update()
        Flag = True
        while Flag == True:
            if self.istrusteeship1 == True and turn == 1 and len(pai)!=0:       #�ж��йܼ��˻���ս
                self.tuoguan()
            elif self.istrusteeship2 == True and turn == -1 and len(pai)!=0:
                self.tuoguan()
            for event in pygame.event.get():                                   #������
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse(event.pos)  # ����¼�������mouse����
                    if len(pai) == 0 and self.return_area.collidepoint(event.pos):
                        Flag = False  # ��ֹͣ��ͣ�ˣ����½������
                        self.renew()
                    if len(pai) == 0 and self.again_area.collidepoint(event.pos):
                        self.renew()
                        self.update()
            pygame.display.flip()

    def secondcard(self):                             #�����Զ����й�ģʽ�´������
        global turn
        if self.istrusteeship1==True and turn == 1:   #���һ�йܸ��´����������
            self.newcard = self.lnewcard
            setpoker.append(self.newcard)
            player1.remove(self.newcard)
        elif self.istrusteeship2==True and turn == -1 :   #��Ҷ��йܸ��´����������
            self.newcard = self.lnewcard
            setpoker.append(self.newcard)
            player2.remove(self.newcard)
        turn = -turn

    def trusteeship(self, lst):         # �ж��Զ�ģʽ��Ӧ�ô���������ƻ���ѡ������
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
        if turn==1 and (len(player1)+3*len(pai)+len(setpoker)-2)<len(player2):     #�Զ������ai�ж���һ������³��Ʊ�Ӯ����������Ҳ�Զ�����
            self.tuopai=0
        if turn==-1 and (len(player2)+3*len(pai)+len(setpoker)-2)<len(player1):
            self.tuopai=0
        if len(setpoker)==0:
            for item in lst:
                if max1[10] == item[4]:  # new_card��ѡ��Ҫ�����ȥ����
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
                    if max1[10] == item[4]:  # new_card��ѡ��Ҫ�����ȥ����
                        new_card = item
                        break
            else:
                self.tuopai = 0
        self.lnewcard = new_card

if __name__ == '__main__':                #���г���
    # ������Ϸʵ����������Ϸ
    bi = begingame()
    bi.runbegin()