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
# print(timestamps)
# print("--------")
# print(timestamps_)
currenttime = datetime.now()
duration=currenttime-timestamps_
d_secs=duration.total_seconds()
d_hrs=d_secs//(60*60)
if d_hrs<=1:
    fees="Rs 10"
elif d_hrs>1:
    fee=10+((d_hrs-1)*5)
    fees=f"Rs {fee}"
feeshtml=f'''
<html>
<head>

</head>
<body>
    <div>Login Time: { timestamps_ }</div>
    <div>Login Time: { currenttime }</div>
    <div>Duration: { d_hrs }</div>
    <div>Parking Fees: { fees }</div>
</body>
</html>
'''
with open("templates/fees.html", "w") as f:
    f.write(feeshtml)