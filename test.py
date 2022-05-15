def send_news_update(mails):
    from mail_sender import sender, services
    sender = sender()
    sender.get_connection("tirtharaj.ubuntu@gmail.com", "ubuntu098")

    message = services.newsService()
    for mailid in mails:
        sender.send_mail(mailid, "Today's news", message, "random user")

send_news_update(["sinhatirtharaj@gmail.com"])