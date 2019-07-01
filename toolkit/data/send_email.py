# coding:utf-8
import smtplib
from email.mime.text import MIMEText


def account_activate(receiver, url):
    smtpserver = "smtp.qq.com"  # 发件服务器
    port = 465  # 端口
    sender = "929783514@qq.com"  # 发件邮箱账号
    psw = "ccuptymchfrdbahd"  # 密码
    receiver = receiver  # 发件邮箱接收人
    subject = "激活邮件"  # 邮件主体
    body = '''<p>感谢你注册易恒健康通行证。<br/>你的登录邮箱为：{}。请点击以下链接激活账号，{} <br/>如果以上链接无法点击，请将上面的地址复制到你的浏览器进入。<br/>易恒健康</p>'''.format(
        receiver, url)  # 邮件正文
    msg = MIMEText(body, "html", "utf-8")
    msg['from'] = sender  # 发送者
    msg['to'] = receiver  # 接收人
    msg['subject'] = subject
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()


def account_activate_163(receiver, url):
    # ----------1.跟发件相关的参数------
    smtpserver = "smtp.163.com"  # 发件服务器
    port = 0  # 端口
    sender = "m18739409973_1@163.com"  # 发件邮箱账号
    psw = "*********"  # 密码
    receiver = receiver  # 发件邮箱接收人

    # ----------2.编辑邮件的内容------
    subject = "这个是主题163"  # 邮件主体
    body = '<p>这个是发送的163邮件</p>'  # 邮件正文
    msg = MIMEText(body, "html", "utf-8")
    msg['from'] = sender  # 发送者
    msg['to'] = receiver  # 接收人
    msg['subject'] = subject

    # ----------3.发送邮件------
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)  # 连服务器
    smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()  # 关闭


def account_activate_echo(receiver, url):
    smtpserver = "smtp.exmail.qq.com"  # 发件服务器
    port = 465  # 端口
    sender = "libo@ecmoho.com"  # 发件邮箱账号
    psw = "AfgPhefByo3AkGoU"  # 密码
    receiver = receiver  # 发件邮箱接收人
    subject = "激活邮件"  # 邮件主体
    body = '''<p>你好！<br/>感谢你绑定邮箱。请复制下面链接到浏览器使用微信扫码激活激活账号：{}<br/>易恒健康</p>'''.format(url)
    msg = MIMEText(body, "html", "utf-8")
    msg['from'] = sender  # 发送者
    msg['to'] = receiver  # 接收人
    msg['subject'] = subject
    smtp = smtplib.SMTP_SSL(smtpserver, port)
    smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()
