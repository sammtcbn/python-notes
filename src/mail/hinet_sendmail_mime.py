# ref to http://yhhuang1966.blogspot.com/2018/10/python-hinet.html

import smtplib
from email.mime.text import MIMEText

html="""
<!doctype html>
<html>
<head>
  <meta charset='utf-8'>
  <title>HTML mail</title>
</head>
<body>
  <b>HTML 郵件測試</b>
</body>
</html>
"""
mime=MIMEText(html, "html", "utf-8")
mime["Subject"]="Hinet mail sent by Python scripts(HTML)"
mime["From"]="Your best friend"
mime["To"]="mailgroup"
# mime["Cc"]="myyahoomail@yahoo.com"
msg=mime.as_string()
print(msg)

smtp=smtplib.SMTP("msr.hinet.net")
smtp.ehlo()
smtp.starttls()
smtp.login("john@msa.hinet.net", "1234")
from_addr="john@msa.hinet.net"
to_addr=["sam@gmail.com", "helen@blablabla.com.tw"]
status=smtp.sendmail(from_addr, to_addr, msg)
if status=={}:
    print("郵件傳送成功!")
else:
    print("郵件傳送失敗!")
smtp.quit()
