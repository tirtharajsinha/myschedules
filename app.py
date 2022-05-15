from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


def send_news_update(mails):
    from mail_sender import sender, services
    message = services.newsService()
    feedback = ""
    for mailid in mails:
        sender = sender()
        sender.get_connection("tirtharaj.ubuntu@gmail.com", "ubuntu098")
        feed = sender.send_mail(mailid, "Today's news", message, "NewsUpdate")
        feedback += mailid + " : " + feed + "\n"
    admin = "sinhatirtharaj@gmail.com"
    sender.get_connection("tirtharaj.ubuntu@gmail.com", "ubuntu098")
    feed = sender.send_mail(admin, "Feedback from SchedulerApp", feedback, "schedulerApp")


# @sched.scheduled_job('interval', minutes=3)
# def timed_job_m3():
# mails = ["sinhatirtharaj@gmail.com"]
# send_news_update(mails)


@sched.scheduled_job('interval', minutes=8)
def timed_job_m8():
    from mail_sender import services
    services.keep_awake_site("https://tirtharajsinha.herokuapp.com")


@sched.scheduled_job('cron', day_of_week='*', hour=13, minute=30)
def scheduled_job():
    mails = ["sinhatirtharaj@gmail.com", "anuragunnikannan7@gmail.com"]
    send_news_update(mails)


sched.start()
