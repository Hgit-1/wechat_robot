from PyOfficeRobot.core.WeChatType import*
wx=WeChat()
wx.GetSessionList()
who='民大附中初一学生群（总群）'
msg='testmsg'
wx.ChatWith(who)
for i in range(2):
    wx.SendMsg(msg)
who='sb'
wx.ChatWith(who)
wx.SendMsg(msg)