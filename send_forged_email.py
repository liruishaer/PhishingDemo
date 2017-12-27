import smtplib
import traceback
from email.message import Message


def send_email(subject, content):
    try:
        real_sender, passwd, server = "real_user_name", "password", "smtp.abc.cn"
        fake_sender = "fake_sender@abc.cn"
        real_recipients = ["real_recipients1@abc.cn", "real_recipients2@abc.cn", "real_recipients3@abc.cn"]
        fake_recipients = ["fake_recipients1@abc.cn", "fake_recipients2@abc.cn"]

        message = Message()
        message["Subject"] = subject
        message["From"] = fake_sender
        message["To"] = ";".join(fake_recipients)
        #Copy to
        #message["CC"] is only for display, to send the email we must specify it in the method "SMTP.sendmail".
        #message["CC"] = "real_recipients1@abc.cn,real_recipients2@abc.cn"
        message.set_payload(content)
        message.set_charset("utf-8")
        msg = message.as_string()

        sm = smtplib.SMTP(server)
        sm.set_debuglevel(0)    #sm.set_debuglevel(1)
        sm.ehlo()
        sm.starttls()
        sm.ehlo()
        sm.login(real_sender, passwd)

        sm.sendmail(fake_sender, real_recipients, msg)    # 注意： 这里必须是fake_sender，否则会出现"由XXX代发"的问题。
        sm.quit()
        return 0
    except Exception as e:
        traceback.print_exc()
        return 1


def main():
    subject = "明天上午会议取消"
    content = "伪造收件人、发件人、抄送人、邮件主题、邮件内容..."
    if send_email(subject, content) == 0:
        print("邮件发送成功")
    else:
        print("邮件发送失败")


if __name__ == '__main__':
    main()
