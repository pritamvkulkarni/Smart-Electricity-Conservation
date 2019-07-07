# Import python package used for RPi programming
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

# You have 2 options to refer to Raspberry Pi pins 
# 1) Via Pin number ; using this method for this project 
GPIO.setmode(GPIO.BOARD)

# 2) Via Broadcom SOC channel" number ( For more reference please refer diagram in repo)
#   GPIO.setmode(GPIO.BCM)

# Pin 3 is output pin where our LED anode is connected and earthed at Pin 8
output_pin = 3
GPIO.setup(3,output_pin)

# Importing MySQL db for storing usage data
import MySQLdb

# For image processing
import datetime
import imutils
import time
import cv2
import os
import glob

# For alerting user about daily usage and conservated units via email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Use your database credentials 
db= MySQLdb.connect(host="localhost",user="xxxxxxx",passwd="xxxxxxx",db="Energy_conservation_data" )
cursor = db.cursor()
  
# Start Capturing vedio through webcam
camera = cv2.VideoCapture(0)
time.sleep(1)

# initialize the first frame in the video stream
firstFrame = None
flag=0
avg=None

# loop over the frames of the video
while True:  
   # grab the current frame and initialize the occupied/unoccupied text
  (grabbed, frame) = camera.read()
  timestamp = datetime.datetime.now()
  text = "Unoccupied"

  # if the frame could not be grabbed, then we have reached the end
  # of the video
  if not grabbed:
    break

  # resize the frame, convert it to grayscale, and blur it( Image blurring) 
  frame = imutils.resize(frame, width=500)
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (21, 21), 0)

  # Initialize first frame
  if firstFrame is None:
    firstFrame = gray
    continue

  if avg is None:
       avg = gray.copy().astype("float")
   
  # compute the absolute difference between the current frame and
  # first frame 
  cv2.accumulateWeighted(gray, avg, 0.4999)
  frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
  
  # dilate the thresholded image to fill in holes, then find contours
  # on thresholded image
  thresh = cv2.threshold(frameDelta,20, 255, cv2.THRESH_BINARY)[1]

  
  thresh = cv2.dilate(thresh, None, iterations=2)
  (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)

  # loop over the contours
  for c in cnts:
    # if the contour is too small (area < 500), ignore it ; 	
    if cv2.contourArea(c) < 500:
      continue
    
    # compute the bounding box for the contour, draw it on the frame,
    # and update the text
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    text = "Occupied"
  
  # Displaying frames to visualize image processing
  cv2.imshow("Current stream", frame)
  cv2.imshow("Thresh image", thresh)
  cv2.imshow(" Delta frame", frameDelta)
  key = cv2.waitKey(1) & 0xFF
  

  if text is "Occupied":
    if flag is 0:
       flag=1
       t1=datetime.datetime.now()
       GPIO.output(3,GPIO.HIGH)
  
    else:
       t2=datetime.datetime.now()
       flag=0
       td=(t2-t1).seconds
       t1=t1.strftime("%H:%M:%S")
       t2=t2.strftime("%H:%M:%S")
       curr_date=datetime.datetime.now().strftime("%Y-%d-%m")
	   print "Writing to database..."
       sql = "INSERT INTO INSTANCES(DEVICE_NO,DATE,STATUS,ON_TIME, OFF_TIME, CONSUMED)VALUES ('%d','%s','%s', '%s', '%s', '%f')" % (1,curr_date,'ON',t1,t2,td*0.00139)
       GPIO.output(3,GPIO.LOW)
       try:  
		   print "Write Complete"
           cursor.execute(sql)
           db.commit()
       except:
		   print "Write Failed"
           db.rollback()


    if datetime.datetime.now().strftime("%H:%M:%S")=="21:00:00":
       d=datetime.datetime.now().stftime("%Y-&d-%m")
       sql2="select sum(CONSUMED) from INSTANCES where DATE = '%s'" % ( d)

       try:
	   cur.execute(sql)
	   result=cur.fetchone()
	   db.commit()

       except:
	   db.rollback()
    fromaddr = "dabc03055@gmail.com"
    toaddr = "pritamvkulkarni@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Todays Smart Energy Meter"

    body = d+": You have consumed "+result[0]+" Units of Energy today and conserved"+ (total_time*appliance_per_second_consumtion-result)
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "9405979596")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()