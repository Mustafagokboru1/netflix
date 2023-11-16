import smtplib
from email.message import EmailMessage

from_name = input("Gönderenin Adı ve Soyadı: ")
from_email = input("Gönderenin E-posta Adresi: ")
to_email = input("Alıcı E-posta Adresi: ")
subject = input("Konu: ")
message = input("Mesajınız: ")

# E-posta oluşturma
msg = EmailMessage()
msg.set_content(message)
msg['Subject'] = subject
msg['From'] = f"{from_name} <{from_email}>"
msg['To'] = to_email

# SMTP sunucusuna bağlanma ve e-posta gönderme
try:
    smtp_email = 'smtp-relay.brevo.com'
    smtp_port = 587
    smtp_username = 'mustafagokboru3@gmail.com'  # Güncellenmiş kullanıcı adı
    smtp_password = 'cwKTE7mkgzMspI6Q'  # SMTP sunucusuna bağlanmak için kullanılacak şifre
    
    with smtplib.SMTP(smtp_email, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(msg)
        print("E-posta başarıyla gönderildi!")
except Exception as e:
    print("E-posta gönderilirken hata oluştu:", e)
