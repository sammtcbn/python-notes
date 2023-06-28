# ref to http://yhhuang1966.blogspot.com/2018/10/python-hinet.html

import smtplib
from email.mime.text import MIMEText

with open("hinet_sendmail_attach_txtfile.txt", "rb") as file:
    filecontent=file.read()

mime=MIMEText(filecontent, "base64", "utf-8")   
mime["Content-Type"]="application/octet-stream"   
mime["Content-Disposition"]='attachment; filename="hinet_sendmail_attach_txtfile.txt"'
mime["Subject"]="Hinet mail sent by Python scripts(TEXT)"
mime["From"]="Your best friend"
mime["To"]="mailgroup"
# mime["Cc"]="myyahoomail@yahoo.com" '''
msg=mime.as_string()
print(msg)

smtp=smtplib.SMTP("msr.hinet.net")
smtp.ehlo()
smtp.starttls()
smtp.login("john@msa.hinet.net", "1234")
from_addr="john@msa.hinet.net"
to_addr=["sam@gmail.com"]
status=smtp.sendmail(from_addr, to_addr, msg)
if status=={}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
smtp.quit()
