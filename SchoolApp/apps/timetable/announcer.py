from typing import List

from apscheduler.schedulers.background import BackgroundScheduler
from discord_webhook import DiscordWebhook

from apps.timetable.models import PostAnnouncementDiscord
from apps.timetable.utils import get_class_announcement


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(announce, "cron", minute="10/15")
    scheduler.start()
    print("Started APS Scheduler")


def post_to_discord(announcements: List[PostAnnouncementDiscord]):
    for data in announcements:
        DiscordWebhook(url=data.link, content=data.message).execute()
        print(f"Sent webhook to {data.link} with message {data.message}")
        # TODO: Add error handling and success checks


def announce():
    classes = get_class_announcement()
    if classes:
        for record in classes:
            post_to_discord(record.key_class.announcements.all())
