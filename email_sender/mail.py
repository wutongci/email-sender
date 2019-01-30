#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
import os
from sender import Mail
from sender import Message

def send(text, subject, toAdd, cc=None, attachments=None):
    """邮件发送方法
    
    Arguments:
        text {str} -- 邮件内容，可以为字符串或者 HTML 字符串
        subject {str} -- 邮件标题
        toAdd {list} -- 收件人列表 
    
    Keyword Arguments:
        cc {list} -- 抄送人列表 (default: {None}) 
        attachments {list} -- 附件列表，示例：[{'path': '/path/to/file', 'file_name': '附件文件名'}] (default: {None})
    """
    
    assert subject is not None
    assert toAdd is not None
    sslPort = os.getenv('MAIL_SERVER_PORT')
    server = os.getenv('MAIL_SMTP_SERVER')
    user = os.getenv('MAIL_USER')
    passwd = os.getenv('MAIL_PASSWORD')

    assert server is not None
    assert user is not None
    assert passwd is not None
    if not sslPort:
        sslPort = 465

    mail = Mail(server, port=sslPort, username=user, password=passwd,
                use_tls=False, use_ssl=True, debug_level=None)
    msg = Message(subject)
    msg.fromaddr = (user, user)
    msg.to = toAdd
    if cc:
        msg.cc = cc 
    if attachments:
        for att in attachments:
            with open(att['path'], 'rb') as f:
                mail_attachment = Attachment(att['file_name'], "application/octet-stream", f.read())
                msg.attach(mail_attachment)
    
    msg.html = text
    msg.charset = "utf-8"
    mail.send(msg)
