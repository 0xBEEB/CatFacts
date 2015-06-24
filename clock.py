from apscheduler.schedulers.blocking import BlockingScheduler
from sqlalchemy import create_engine, BoundMetaData

db = create_engine("mysql://heroku_mysql_instance")

db.echo = True

metadata = BoundMetaData(db)

users = Table('user', metadata, autoload=True)

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def send_facts_job():
    connection = engine.connect()
    sql = 'select phone_number from USER LIMIT 100'
    users = connection.execute(text(sql))


sched.start()
