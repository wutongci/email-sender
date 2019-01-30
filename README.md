### 介绍

本项目主要功能为发送邮件使用

### 安装

```
pipenv install -e git+https://github.com/cielpy/hiii-email-sender.git#egg=hiii-email-sender
```

### 使用

```python
from email_sender.mail import send

send('邮件内容', '邮件标题', '收件人列表')
```

使用时需要配置环境变量如下：

```
MAIL_SMTP_SERVER=smtp.exmail.qq.com
MAIL_SERVER_PORT=465
MAIL_USER=noreply@hiii-life.com
MAIL_PASSWORD=pwddd
```