import peewee as pw
import os

db = (pw.MySQLDatabase(
            os.environ['CTC_TWITTER_DB'],
            host=os.environ['CTC_TWITTER_HOST'],
            port=int(os.environ['CTC_TWITTER_PORT']),
            user=os.environ['CTC_TWITTER_USER'],
            passwd=os.environ['CTC_TWITTER_PASSWORD']))

class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db

class Tweet(MySQLModel):
    timestamp = pw.CharField(null=True)
    text = pw.TextField(null=True)
    positive = pw.DecimalField(null=True)
    negative = pw.DecimalField(null=True)
    neutral = pw.DecimalField(null=True)

    class Meta:
        db_table = 'tweets'
