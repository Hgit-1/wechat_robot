'''
tips:WARNING, THIS IS A CHINESE PROGRAM! It may not friendly for peoples from countries expect China.
tips:this code is an open source code.
tips:please call +86 182-0169-7173 when there is any problem
tips:follow GPL licence
--------------------------------EULA--------------------------------

ENG:
----------------DOCUMENTS BEGIN----------------
this is a python program for chat in wechat.
if you use this, we will think that you had agreed the EULA.
1:install:
    if you see this, you must be installed this program.
    input "pip install pyofficerobot" in 'cmd'[you must have a python enviroment under 3.10]
    and you can try it!
2:must/should change something:
    if you see this, you must be seen this program.
    change the line which has been noticed 'can be change' by your self
    MUST CHANGE THE LINE WHICH HAS BEEN NOTICED 'must be change'!
    you can delete the line which has been noticed 'can be delete'
    [you must know my school and my grade :)]
3:use:
    maybe you want to use this. now I want to introduce that.
    1:/call:
        /call is a special command. you can use it with your good friends.[DO NOT USE IT WHEN YOU FACED TO SOME STRANGER!!!]
        you can just use it follow the instruction.
    2:/rand:
        /rand can rand something between 0 to 32768, and we char it.
    3:/repeat:
        /repeat can repeat something, just follow the instruction.
    4:/record:
        /record can record something, just follow the instruction.
use it!
----------------DOCUMENTS END----------------
CHN(ChatGPT translate):
----------------开始文档----------------
这是一个用于在微信中聊天的Python程序。
如果您使用此程序，我们将认为您已同意下面的协议。
1：安装：
    如果您看到这个，您想必已经安装了这个程序。
    在'cmd'中输入“pip install pyofficerobot”[您必须有一个Python环境在3.10以下]，然后您可以尝试使用它！
2：必须/应该更改的内容：
    如果您看到这个，您想必已经看到了这个程序。
    您必须自己更改已经被标记为“can be change”的行
    必须更改已经被标记为“must be change”的行！
    您可以删除已被标记为“can be delete”的行
    [您想必知道我的学校和年级 :)]
3：使用：
    也许您想使用这个程序。现在我想介绍一下。
1：/call：
    /call是一个特殊的命令。您可以与您的好朋友一起使用。[当您面对一些陌生人时，不要使用它！]
    您只需按照指示使用即可。
2：/rand：
    /rand可以随机生成0到32768之间的char化的数字，并将其发送到微信中。
3：/repeat：
    /repeat可以重复某些内容，只需按照指示使用即可。
4：/record：
    /record可以记录某些内容，只需按照指示使用即可。
使用它吧！
----------------结束文档----------------
'''
'''
注意:上方警示无效,已过期.最后一次检查时间:2023/5/11/19:55:00.00
'''
psw1=0
def read_txt_value(file_path, key):
    """
    通过键读取txt文件中特定行的某个值
    :param file_path: 文件路径
    :param key: 键名
    :return: 对应的数值
    """
    
    value = 0
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith(key):
                # 获取键值对
                kv_list = line.strip().split(':')
                # 如果键值对格式不正确或没有值则返回 None
                if len(kv_list) != 2 or not kv_list[1]:
                    return -1
                value = kv_list[1]
                break
    # 如果没有找到键，则在文件中写入“字母:0”
    if value == -1:
        with open(file_path, 'a') as f:
            f.write(f"{key}:0\n")
        value = 0
    # 对读取到的内容进行调制
    value=int(value)
    return value


from PyOfficeRobot.core.WeChatType import*
import random
import requests
wx=WeChat()
wx.GetSessionList()
def requests1(domain):
    """
    test
    """
    a=requests.get(domain)
    r=a.text
    return r
try:
    #a=input("请输入接收人")#can be delete
    who='民大附中初一学生群（总群）'#can be change
    #who='微信机器人测试群'#can be change
    #who=a#can be delete
    msg='testmsg'
    wx.ChatWith(who)
    for i in range(2):
        wx.SendMsg(msg)
    msg1='此人工智能为Halpha-wxrobot-1.0ser,请输入 /help 来进行下一步操作'
    wx.SendMsg(msg1)
    while True:
        glm=wx.GetLastMessage[1]
        if glm=='/help':
            msg2='请输入命令[系统主动询问时请在20秒内回答][/call:向Halpha主机里的某个人发送消息,/rand:随机一个未知的东西,/repeat:重复某条消息[禁止输入/repeat,否则会停机],/record:记录消息,/check:签到[不要改名][如要@我，请先写"@Halpha",等到"请输入信息"被发送时再留言[20sec内回答]]'#can be change
            wx.SendMsg(msg2)
        glm1=wx.GetLastMessage[1]
        if glm1=='/call':
            msg3='请输入对象'
            wx.SendMsg(msg3)
            glm2=wx.GetLastMessage[1]
            if glm2!='请输入对象':
                who1=glm2
                msg4='请输入内容'
                wx.SendMsg(msg4)
                glm3=wx.GetLastMessage[1]
                if glm3!='请输入内容':
                    wx.ChatWith(who1)
                    msg5=glm3
                    wx.SendMsg(msg5)
                    wx.ChatWith(who)
                    wx.SendMsg(msg='over')
        if glm1=='/rand':
            msg6=chr(random.randint(0,32767))
            wx.SendMsg(msg6)
        if glm1=='/repeat':
            msg7='请输入内容'
            wx.SendMsg(msg7)
            glm4=wx.GetLastMessage[1]
            if glm4!=msg7:
                if glm4=='repeat':
                    break
                msg8=glm4
                wx.SendMsg(msg8)
        if glm1=='/record':
            wx.SendMsg(msg='Start to record......[输入/stoprecord以停止收录]')
            x=wx.GetLastMessage[1]
            glm_rec=x
            if glm_rec!=x:
                if x=='/stoprecord':
                    wx.SendMsg(msg='record over')
                    break
                with open('record-self.txt', 'a') as f:
                    f.write(x)
                    if x=='/stoprecord':
                        f.close()
                        wx.SendMsg(msg='record over')
        if glm1=='@Halpha' or glm1=='@Halpha扰民人工智障[v1.0]别改群名':#can be change
            wx.SendMsg(msg='请输入信息')
            y=wx.GetLastMessage[1]
            if y!='请输入信息':
                with open('record-spe-call.txt', 'a') as g:
                    g.write(y)
                    g.close()
                    wx.SendMsg(msg='over')
            glm_ans='blank'#define
        if glm1=='/check':
            glm5=wx.GetLastMessage[0]
            value=read_txt_value('check.txt',glm5)
            value=int(value)
            value+=1
            value=str(value)
            wx.SendMsg(msg='您现在已经打卡 '+value+' 次了!')
            with open('check.txt','r') as g:
                for line in g:
                    if line.startswith(glm5):
                        # 获取键值对
                        kv_list = line.strip().split(':')
            with open('check.txt','w') as w:
                w.write(glm5)
                w.write(':')
                w.write(value)
        if glm1=='/ban':
            while 1:
                glm6=wx.GetLastMessage[0]
                glm7=wx.GetLastMessage[1]
                if psw1==0:
                    psw1=random.randint(0,999999)
                    print(psw1)
                psw1=str(psw1)
                if glm7=='/endban':
                    wx.SendMsg(msg='请输入密码')
                    while 1:
                        glm8=wx.GetLastMessage[1]
                        if glm8==psw1:
                            wx.SendMsg(msg='over')
                            break
                else:
                    with open('ban.txt','w') as ban:
                        ban.close()
                    msg9=read_txt_value('ban.txt',glm6)
                    msg9+=1
                    msg9=str(msg9)
                    if glm6!='H':
                        wx.SendMsg(msg='您已经说话 '+msg9+' 次了!')
                    with open('ban.txt','w') as w:
                        w.write(glm6)
                        w.write(':')
                        w.write(msg9)
except Exception as e:
    wx.SendMsg(msg='error, have to restart')
    wx.SendMsg(msg='error by:')
    a='错误类型是'
    b='错误明细是'
    c=e.__class__.__name__
    wx.SendMsg(a)
    wx.SendMsg(c)
    wx.SendMsg(b)
    wx.SendMsg(e)
    print(a,c)
    print(b,e)