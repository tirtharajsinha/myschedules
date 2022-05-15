from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


def send_news_update(mails):
    from mail_sender import sender, services
    message = services.newsService()
    feedback = "Feedback from your app\n"
    for mailid in mails:
        print("calling  mail sender")
        senderblock = sender()
        senderblock.get_connection("tirtharaj.ubuntu@gmail.com", "ubuntu098")
        feed = senderblock.send_mail(mailid, "Today's news", message, "NewsUpdate")

        feedback += mailid + " : " + str(feed) + "\n"
    senderblock = sender()
    admin = "sinhatirtharaj@gmail.com"
    senderblock.get_connection("tirtharaj.ubuntu@gmail.com", "ubuntu098")
    print(feedback,"................")
    feed = senderblock.send_mail(admin, "Feedback from SchedulerApp", feedback, "schedulerApp")


# @sched.scheduled_job('interval', minutes=3)
# def timed_job_m3():
# mails = ["sinhatirtharaj@gmail.com"]
# send_news_update(mails)


@sched.scheduled_job('interval', minutes=8)
def timed_job_m8():
    from mail_sender import services
    services.keep_awake_site("https://tirtharajsinha.herokuapp.com")


# @sched.scheduled_job('interval', minutes=5)
# def timed_job_m5():
#     mails = ["sinhatirtharaj@gmail.com", "anuragunnikannan7@gmail.com"]
#     send_news_update(mails)


@sched.scheduled_job('cron', day_of_week='*', hour=14, minute=30)
def scheduled_job():
    mails = ["sinhatirtharaj@gmail.com", "anuragunnikannan7@gmail.com"]
    send_news_update(mails)


sched.start()
