import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="parkinggarage"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT current_ FROM registration ORDER BY current_ DESC LIMIT 1")

myresult = mycursor.fetchall()

timestamps = []
for r in myresult:
    timestamps.append(r[0])
# print(timestamps)
timestamps_=timestamps[0]
# logintime=datetime(timestamps_)
print(f"login time {timestamps_}")
print(type(timestamps_))
print("__________")
currenttime = datetime.now()
print(f"Current time {currenttime}")
print(type(currenttime))

print("__________")
duration=currenttime-timestamps_
print(f"Duration {duration}")
print(type(duration))

d_secs=duration.total_seconds()

print(f"Duration in seconds {d_secs}")

d_hrs=d_secs//(60*60)

print(f"Duration in hours {d_hrs}")