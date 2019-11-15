# -*- coding: utf-8 -*-
# Code By Songdaoyuan, Last Edited at 2019.11.15 Final Version
#https://github.com/songdaoyuan/PythonClassWork/blob/master/Exam1_PythonSocketAndGUI/GUI_wxFormBuilder_Socket

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import socket
import time
import threading

import wx
import wx.xrc

###########################################################################
# Class MainFrame
###########################################################################


class MainFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Let's Chat!", pos=wx.DefaultPosition, size=wx.Size(
            960, 590), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        MainSizer = wx.BoxSizer(wx.VERTICAL)

        self.ConnectionParameterEnterBar = wx.ToolBar(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TB_HORIZONTAL)
        self.ConnectionParameterEnterBar.SetToolBitmapSize(wx.Size(25, 25))
        self.ConnectIP = wx.StaticText(
            self.ConnectionParameterEnterBar, wx.ID_ANY, u"Connect IP:", wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.ConnectIP.Wrap(-1)

        self.ConnectionParameterEnterBar.AddControl(self.ConnectIP)
        self.ConnectIPEnterBox = wx.TextCtrl(
            self.ConnectionParameterEnterBar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, 40), 0)
        self.ConnectionParameterEnterBar.AddControl(self.ConnectIPEnterBox)
        self.ConnectPort = wx.StaticText(
            self.ConnectionParameterEnterBar, wx.ID_ANY, u"Connect Port:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ConnectPort.Wrap(-1)

        self.ConnectionParameterEnterBar.AddControl(self.ConnectPort)
        self.ConnectPortEnterBox = wx.TextCtrl(
            self.ConnectionParameterEnterBar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 40), 0)
        self.ConnectionParameterEnterBar.AddControl(self.ConnectPortEnterBox)
        self.ListenPort = wx.StaticText(
            self.ConnectionParameterEnterBar, wx.ID_ANY, u"Listen Port:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ListenPort.Wrap(-1)

        self.ConnectionParameterEnterBar.AddControl(self.ListenPort)
        self.ListenPortEnterBox = wx.TextCtrl(
            self.ConnectionParameterEnterBar, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, 40), 0)
        self.ConnectionParameterEnterBar.AddControl(self.ListenPortEnterBox)
        self.ConectionButtion = wx.Button(
            self.ConnectionParameterEnterBar, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.Size(50, 40), 0)
        self.ConnectionParameterEnterBar.AddControl(self.ConectionButtion)
        self.ConnectionParameterEnterBar.Realize()

        MainSizer.Add(self.ConnectionParameterEnterBar, 0, wx.EXPAND, 5)

        TextSizer = wx.BoxSizer(wx.VERTICAL)

        self.DisplayText = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(960, 250), wx.TE_MULTILINE)
        self.DisplayText.Enable(False)

        TextSizer.Add(self.DisplayText, 0, wx.ALL, 5)

        self.SendButtion = wx.Button(
            self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.Size(80, 40), 0)
        TextSizer.Add(self.SendButtion, 0, wx.ALL, 5)

        self.EnterText = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(960, 200), 0)
        TextSizer.Add(self.EnterText, 0, wx.ALL, 5)

        MainSizer.Add(TextSizer, 1, wx.EXPAND, 5)

        self.SetSizer(MainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.ConectionButtion.Bind(wx.EVT_BUTTON, self.Conneciton2AnotherUser)
        self.SendButtion.Bind(wx.EVT_BUTTON, self.SendMessage)
        #self.Bind( wx.EVT_TIMER, self.onTimer, id=wx.ID_ANY )

        self.noLog = True

    def __del__(self):
        pass

    def appendText(self, text):
        if self.noLog:
            current = '%s\n%s\n' % (time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime()), text)
            self.noLog = False
        else:
            current = '-----------\n%s\n%s\n' % (time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime()), text)
        self.DisplayText.AppendText(current)

    # Virtual event handlers, overide them in your derived class
    def Conneciton2AnotherUser(self, event):
        listenIP = self.ConnectIPEnterBox.GetValue()
        listenPort = self.ListenPortEnterBox.GetValue()
        print('连接的目标主机地址为：' + listenIP + '，监听端口号为' + listenPort)
        net_thread = ServerThread(listenIP, int(listenPort), self)
        net_thread.start()

    def SendMessage(self, event):
        targetIP = self.ConnectIPEnterBox.GetValue()
        targetPort = self.ConnectPortEnterBox.GetValue()
        listenPort = self.ListenPortEnterBox.GetValue()
        EnterTextContent = self.EnterText.GetValue()
        self.EnterText.Clear()

        # print(EnterTextContent)
        client = Client(targetIP, int(targetPort))
        client.sendmsg(EnterTextContent)
        self.appendText(EnterTextContent)


class Server():
    def __init__(self, address, port):
        self.host = address
        self.port = port

    def run(self, ChatFrame):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        while True:
            print('Waiting for Connection')
            conn_socket, addr = self.socket.accept()
            buf_recv = conn_socket.recv(1024)
            ChatFrame.appendText(buf_recv.decode('utf-8'))


class Client():
    def __init__(self, address, port):
        self.host = address
        self.port = port

    def sendmsg(self, message):
        buf_send = message.encode('utf-8')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.socket.send(buf_send)
        self.socket.close()


class ServerThread(threading.Thread):
    def __init__(self, address, port, ChatFrame):
        threading.Thread.__init__(self)
        self.addr = str(address)
        self.port = int(port)
        self.frame = ChatFrame

    def run(self):
        self.srv = Server(self.addr, self.port)
        print('Server is running now')
        self.srv.run(self.frame)


if __name__ == '__main__':
    app = wx.App()

    main_window = MainFrame(None)
    main_window.Show()

    app.MainLoop()
