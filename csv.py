import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host = "localhost",
    user = "whats",
    password = "password",
    database = "whats",
    auth_plugin = "mysql_native_password"
)

cursor = conn.cursor()

sql = "insert into messages (mDate, mTime, mFrom, mContent) values (%s, %s, %s, %s)"

# open file in read only mode "r"
file = open("bla.txt","r")

counter = 0
#Repeat for each line in the text file
for line in file:
  fields = line.split(",", 1) # split the string in the first ","
  msgDate = fields[0] # first part (before comma) - Date
  msgRest = fields[1] # second part (after comma) - All the rest

  getTime = msgRest.split("-", 1) # split the string in the first "-"
  msgTime = getTime[0] # Time
  msgRest2 = getTime[1] # all the rest

  getFrom = msgRest2.split(":", 1) # split the string in the first ":"
  
  if len(getFrom) < 2: # Check for whatsapp warning (miss one column)
      continue # bypass

  msgFrom = getFrom[0] # From
  msgContent = getFrom[1] # Content

  splitDate = msgDate.split("/")
  day = splitDate[0]
  month = splitDate[1]
  year = splitDate[2]

  newDate = year+"-"+month+"-"+day
    
  toDate = datetime.strptime(newDate, "%Y-%m-%d").date()
  
  data = (toDate, msgTime, msgFrom, msgContent)
  cursor.execute(sql, data)
  conn.commit()
  counter += 1
    
file.close()
cursor.close()
conn.close()

print(f"Foram inseridos {counter} registros.")

#agora eu quero ver
