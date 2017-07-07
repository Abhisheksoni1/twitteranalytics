import json
import ast
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError

from analytics.models import TwitterData
import os
from datetime import datetime

from twitteranalytics.settings import BASE_DIR

months = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}
# TwitterData.objects.values('location').annotate(dcount=Count('location'))


def convert_to_datetime(date):
    d_list = date.split(" ")
    month = months[d_list[1]]
    date = '{}-{}-{}'.format(d_list[5], month, d_list[2])
    return datetime.strptime(date, '%Y-%m-%d').date()


class Command(BaseCommand):
    help = 'populate database from Twitter data'

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.join(os.path.join(BASE_DIR, 'analytics'), 'fixtures'), 'twitter_data.txt')
        self.stdout.write(file_path)
        tweets_file = open(file_path, "r")
        for tweet in tweets_file:

            tweet = ast.literal_eval(tweet)
            # self.stdout.write(tweet)
            tweet['created'] = convert_to_datetime(tweet['created'])
            try:
                TwitterData.objects.create(**tweet)
            except IntegrityError:
                pass
        self.stdout.write('Successfully insert into database')
