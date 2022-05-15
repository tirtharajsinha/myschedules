from mail_sender import sender, services

sender = sender()
sender.get_connection("tirtharaj.ubuntu@gmail.com", "ubuntu983221")

# message = services.keep_awake_site("https://tirtharajsinha.herokuapp.com")

message=services.newsService()
sender.send_mail("sinhatirtharaj@gmail.com", "Today's news", message, "random user")
