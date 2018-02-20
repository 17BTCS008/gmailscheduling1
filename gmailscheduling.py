import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("avinashshekar12345@gmail.com","AvinashShekar87654321")
msg='fakjsddsakfgdsafgkjhjdfdsafh'
s.sendmail('avinashshekar12345@gmail.com','avinash8169@gmail.com',msg)
s.quit()
