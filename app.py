from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


def send_news_update(mails):
    from mail_sender import sender, services
    sender = sender()
    sender.get_connection("tirtharaj.ubuntu@gmail.com", "ubuntu983221")

    message = services.newsService()
    for mailid in mails:
        sender.send_mail(mailid, "Today's news", message, "random user")


@sched.scheduled_job('interval', minutes=3)
def timed_job_m3():
    mails = ["sinhatirtharaj@gmail.com"]
    send_news_update(mails)


@sched.scheduled_job('interval', minutes=8)
def timed_job_m8():
    from mail_sender import services
    services.keep_awake_site("https://tirtharajsinha.herokuapp.com")


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    mails = ["sinhatirtharaj@gmail.com"]
    send_news_update(mails)


sched.start()
