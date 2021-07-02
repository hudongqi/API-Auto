import smtplib
from email.mime.text import MIMEText
from email.mime.nonmultipart import MIMENonMultipart
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class Send_email():
    def send_html(self,receiver,msg):
        # 发送纯文本格式的邮件，邮件正文一定要是有意义的内容，不然会被163服务器识别为垃圾邮件，无法发送
        msg = MIMEText(_text=msg, _subtype='html', _charset='utf-8')
        # 发送邮箱地址
        sender = ''
        # 邮箱授权码，非登陆密码
        password = ''
        # 收件箱地址
        receiver
        # smtp服务器
        smtp_server = 'smtp.mxhichina.com'
        # 发送邮箱地址
        msg['From'] = sender
        # 收件箱地址
        msg['To'] = receiver
        # 主题，主题也必须是有意义的内容，否则同样会被识别为垃圾邮件，无法发送
        msg['Subject'] = 'test'
        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        server.login(sender, password)  # login()方法用来登录SMTP服务器
        server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息。
        server.sendmail(sender, receiver, msg.as_string())  # msg.as_string()把MIMEText对象变成str server.quit()
        server.quit()

    def send_fujian(self):
        msg1 = MIMEMultipart()
        # 发送邮箱地址
        sender = ''
        # 邮箱授权码，非登陆密码
        password = ''
        # 收件箱地址
        receiver = ''
        # smtp服务器
        smtp_server = 'smtp.mxhichina.com'
        # 发送邮箱地址
        msg1['From'] = sender
        # 收件箱地址
        msg1['To'] = receiver
        # 主题，主题也必须是有意义的内容，否则同样会被识别为垃圾邮件，无法发送
        msg1['Subject'] = 'test'

        msg1.attach(MIMEText('send with file...', 'plain', 'utf-8'))

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open('/Users/hudongqi/Library/Containers/com.microsoft.Excel/Data/Library/Application Support/Microsoft/Office/16.0/DTS/zh-CN{883A5F3B-211B-E84B-BAF5-B06B316D0EE3}/{4A2EB7B7-B16A-EE4D-8A50-9E9673D4C5FF}mm10000056.png', 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'png', filename='test.png')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='test.png')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg1.attach(mime)
        server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
        server.login(sender, password)  # ogin()方法用来登录SMTP服务器
        server.set_debuglevel(1)  # 打印出和SMTP服务器交互的所有信息。
        server.sendmail(sender, receiver, msg1.as_string())  # msg.as_string()把MIMEText对象变成str server.quit()
        server.quit()

