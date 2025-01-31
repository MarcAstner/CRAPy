from app import app, p, p1, vs, outputFrame, lock
from app import prot,pa1, pa2, proll, ppitch, pgrip
from flask import Flask, Response, render_template, request, flash, redirect, url_for, json

#imports for Stream
import RPi.GPIO as GPIO
from time import sleep
import cv2
import imutils
import datetime
from app.singlemotiondetect import SingleMotionDetect

#imports for GPS and sensors
import os
from app.dataProcessingLib import sqliteToJson_GPS, sqliteToJson_sensors


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

##################### STREAM ##########################

@app.route('/stream')
def stream():
    slider1 = 10
    slider2 = 10

    return render_template('stream.html', lastval1=slider1, lastval2=slider2)

@app.route("/send", methods=["POST"])
def send():
    val1 = request.form["slider1"]
    val2 = request.form["slider2"]

    p.ChangeDutyCycle(float(val1))
    p1.ChangeDutyCycle(float(val2))
    # Give servo some time to move
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
    p1.ChangeDutyCycle(0)

    return render_template('stream.html', lastval1=val1, lastval2=val2)

@app.route('/video')
def video():
    return render_template('video.html')

def detect_motion(frameCount):
    global vs, outputFrame, lock

    md = SingleMotionDetect(accumWeight=0.1)
    total = 0
    
    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        timestamp = datetime.datetime.now()
        cv2.putText(frame, timestamp.strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

        if total > frameCount:
            # detect motion in the image
            motion = md.detect(gray)
            # check to see if motion was found in the frame
            if motion is not None:
            # unpack the tuple and draw the box surrounding the
            # "motion area" on the output frame
                (thresh, (minX, minY, maxX, maxY)) = motion
                cv2.rectangle(frame, (minX, minY), (maxX, maxY),(0, 0, 255), 2)
    
        # update the background model and increment the total number
        # of frames read thus far
        md.update(gray)
        total += 1
        # acquire the lock, set the output frame, and release the
        # lock
        with lock:
            outputFrame = frame.copy()

def generate():
    # grab global references to the output frame and lock variables
    global outputFrame, lock
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if outputFrame is None:
                continue
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
            # ensure the frame was successfully encoded
            if not flag:
                continue
        # yield the output frame in the byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(generate(), mimetype = "multipart/x-mixed-replace; boundary=frame")

######################### GPS ###################################

@app.route('/gps')
def map():
    #This creates the json file that the script will use when rendered
    sqliteToJson_GPS("app/static/", "app/GPS_data.db")
    return render_template('gps.html')

@app.route('/gps', methods=['POST'])
def map_form():
    numSamples = int (request.form['numSamples'])
    #This creates the json file that the script will use when rendered
    sqliteToJson("app/static/", "app/GPS_data.db",numSamples)
    return render_template('gps.html')

########################### ROBOTIC ARM ######################################

@app.route("/roboArm")
def roboArm():
    Rotation = 190
    Arm_1 = 127
    Arm_2 = 100
    Roll = 133
    Pitch = 144
    Gripper = 8

    return render_template('roboarm.html', lastval1=Rotation, lastval2=Arm_1, lastval3=Arm_2, lastval4=Roll, lastval5=Pitch, lastval6=Gripper )

@app.route("/roboArm_send", methods=["POST"])
def armSend():
    # Get slider Values
    val1 = request.form["Rotation"]
    val2 = request.form["Arm_1"]
    val3 = request.form["Arm_2"]
    val4 = request.form["Roll"]
    val5 = request.form["Pitch"]
    val6 = request.form["Gripper"]
    val7 = request.form["Lock"]
    val8 = request.form["Turnbox"]
    val9 = request.form["Move_Sensor"]
    
    #Renormalize values from 2-15.5 to degree
    nval1 = float(val1)*10.5/270+2
    nval2 = float(val2)*10.5/270+2
    nval3 = float(val3)*10.5/270+2
    nval4 = float(val4)*10.5/270+2
    nval5 = float(val5)*10.5/270+2
    nval6 = float(val6)*10.5/270+2
    nval7 = float(val7)*10.5/270+2
    nval8 = float(val8)*10.5/270+2
    nval9 = float(val9)*10.5/270+2
    
    # Change duty cycle
    prot.ChangeDutyCycle(float(nval1))
    pa1.ChangeDutyCycle(float(nval2))
    pa2.ChangeDutyCycle(float(nval3))
    proll.ChangeDutyCycle(float(nval4))
    ppitch.ChangeDutyCycle(float(nval5))
    pgrip.ChangeDutyCycle(float(nval6))
    plock.ChangeDutyCycle(float(nval7))
    pturnbox.ChangeDutyCycle(float(nval8))
    pmove_sensor.ChangeDutyCycle(float(nval9))
    
    # Give servo some time to move
    sleep(1)
    # Pause the servo
    
    return render_template('roboarm.html', lastval1=val1, lastval2=val2, lastval3=val3, lastval4=val4, lastval5=val5, lastval6=val6, lastval7=val7, lastval8=val8, lastval9=val9)

@app.route('/stop_arm')
def stopArm():
    Rotation = 190
    Arm_1 = 127
    Arm_2 = 100
    Roll = 133
    Pitch = 144
    Gripper = 8
    
    prot.ChangeDutyCycle(0)
    pa1.ChangeDutyCycle(0)
    pa2.ChangeDutyCycle(0)
    proll.ChangeDutyCycle(0)
    ppitch.ChangeDutyCycle(0)
    pgrip.ChangeDutyCycle(0)
    
    return render_template('roboarm.html',lastval1=Rotation, lastval2=Arm_1, lastval3=Arm_2, lastval4=Roll, lastval5=Pitch, lastval6=Gripper, lastval7=lock, lastval8=Turnbox, lastval9=Move_Sensor)

@app.route('/lock_arm')
def lockArm():
    Lock = 110
    
    plock.ChangeDutyCycle(0)
    
@app.route('/unlock_arm')
def unlock_Arm():
    Lock = 0
    
    plock.ChangeDutyCycle(0)
    
@app.route('/open_samplebox')
def open_samplebox():
    Lock = 180
    
    pturnbox.ChangeDutyCycle(0)
    
@app.route('/close_samplebox')
def close_samplebox():
    Lock = 90
    
    pturnbox.ChangeDutyCycle(0)
    
@app.route('/insert_sensor')
def insert_sensor():
    Lock = 180
    
    pmove_sensor.ChangeDutyCycle(0)
    
@app.route('/take_sensor_out')
def take_sensor_out():
    Lock = 0
    
    pmove_sensor.ChangeDutyCycle(0)

############################ SENSORS #########################################
@app.route('/sensors')
def sensors():
#This creates a json file where to store the data from the sqlite database
    sqliteToJson_sensors("app/static", "app/ArduinoData.db")
    return render_template('sensors.html')

########################### CONTROL SGVHAK ###################################

# Randomly generated key means session cookies will not be usable across
# instances. This is acceptable for now but may need changing later.
app.secret_key = os.urandom(24)

import sys
sys.path.append('./app')
from subprocess import call
import socket
import roverchassis as roverchassis

# Rover chassis geometry, including methods to calculate wheel angle and
# velocity based on chassis geometry.
chassis = roverchassis.chassis()

class main_menu:

  @app.route('/control')
  def control():
    """
    Main menu, home of rover UI.
    """
    chassis.ensureready()
    return render_template("ctrlRover.html",
      page_title = 'Main Menu')

  @app.route('/stop_motors')
  def stop_motors():
    """
    Stop motors immediately
    """
    chassis.ensureready()
    for wheel in chassis.wheels.values():
      wheel.poweroff()
    flash("Motors Stopped","success")
    return render_template("ctrlRover.html")

  @app.route('/drive')
  def drive():
    """
    Drive by circular touchpad control for polar coordinates
    """
    chassis.ensureready()
    return render_template("drive.html",
      ui_angle=70,
      page_title = 'Polar Pad')

  @app.route('/drive_cartesian')
  def drive_cartesian():
    """
    Drive by rectangular touchpad control for cartesian coordinates
    """
    chassis.ensureready()
    return render_template("drive_cartesian.html",
      page_title = 'Cartesian Pad')

  @app.route('/drive_command', methods=['GET','POST'])
  def drive_command():
    """
    Allows user to send a single angle+velocity command to chassis.
    """
    chassis.ensureready()

    if request.method == 'GET':
      return render_template("drive_command.html",
        page_title = 'Velocity & Angle Commands')
    else:
      # TODO: Limit the frequency of updates to one every 50ms. If more
      # than one update arrive within the window, use the final one. This
      # reduces workload on RoboClaw serial network and the mechanical bits
      # can't respond super fast anyway.
      # EXCEPTION: If a stop command arrives, stop immediately.
      pct_angle = float(request.form['pct_angle'])
      magnitude = float(request.form['magnitude'])

      if pct_angle == 0:
        radius = float("inf")
      elif pct_angle>0:
        radius = chassis.minRadius + (chassis.maxRadius-chassis.minRadius) * (100-pct_angle)/100.0
      else:
        radius = -chassis.minRadius - (chassis.maxRadius-chassis.minRadius) * (100+pct_angle)/100.0

      chassis.move_velocity_radius(magnitude, radius)

      return json.jsonify({'Success':1})

  @app.route('/chassis_config')
  def chassis_config():
    """
    Returns HTML to display current chassis configuration, including status
    like desired angle and velocity of individual wheels.
    """
    chassis.ensureready()

    # Generate a table where unique wheel X/Y value gets a column/row so
    # we know where to place them relative to each other on screen.
    rows = set()
    columns = set()

    # Count the unique X/Y coordinates into columns/rows
    for wheel in chassis.wheels.values():
      rows.add(wheel.y)
      columns.add(wheel.x)

    # Sets enforced uniqueness, now we turn them into a list so we can sort.
    rowlist = list(rows)
    rowlist.sort(reverse=True)
    columnlist = list(columns)
    columnlist.sort()

    # Create a dictionary of dicationaries to hold entries.
    wheelTable = dict()
    for row in rowlist:
      wheelTable[row] = dict()
      for column in columnlist:
        wheelTable[row][column] = list()

    # Put each wheel into its matching location in the table.
    for wheel in chassis.wheels.values():
      wheelTable[wheel.y][wheel.x].append(wheel)

    # To help space out the above information properly, generate a table for
    # CSS grid layout column offsets.
    wheelOffset = dict()
    for row in wheelTable.values():
      # Every row starts with zero accumulated offset
      cumulative_offset = 0
      for column in row.values():
        if len(column) == 0:
          # Each column without information will add an offset of 2 for
          # the first following non-empty column
          cumulative_offset = cumulative_offset + 2
        else:
          for wheel in column:
            if cumulative_offset > 0:
              # Pick up the accumulated offset, reset accumulator to zero.
              wheelOffset[wheel.name] = "offset-m{}".format(cumulative_offset)
              cumulative_offset = 0
            else:
              wheelOffset[wheel.name] = ""

    # Get local IP address, copy/pasted from StackOverflow
    # https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IP = 'unknown'
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = 'Exception encountered while retrieving IP address'
    finally:
        s.close()

    # Render table
    return render_template("chassis_config.html",
      wheelTable = wheelTable,
      wheelOffset = wheelOffset,
      local_ip = IP,
      page_title = 'Chassis Configuraton')

  @app.route('/request_wheel_status', methods=['POST'])
  def request_wheel_status():
    """
    Return a JSON representation of current chassis wheel status. Use POST
    instead of GET to clearify this data should not be cached.
    Polled regularly by chassis_config.js to update onscreen display of
    chassis_config.html.
    """
    chassis.ensureready()
    wheelInfo = dict()
    for name, wheel in chassis.wheels.iteritems():
      wheelInfo[name] = dict()
      wheelInfo[name]['velocity'] = wheel.velocity
      wheelInfo[name]['angle'] = wheel.angle
    return json.jsonify(wheelInfo)

  @app.route('/steering_trim', methods=['GET','POST'])
  def steering_trim():
    """
    Steering control motor can go off-center for various reasons. The steering
    trim function allows the user to adjust the wheel center position.
    """
    chassis.ensureready()

    if request.method == 'GET':
      # Find all the wheels that we can steer
      steered_wheels = list()
      for name, wheel in chassis.wheels.iteritems():
        if wheel.steeringcontrol:
          steered_wheels.append(name)
      steered_wheels.sort()

      # Pass the list of wheels along for display
      return render_template("steering_trim.html",
        steered_wheels=steered_wheels,
        page_title = 'Steering Trim')
    else:
      adjWheel = chassis.wheels[request.form['wheel']]

      if "move_to" in request.form:
        # Steer wheel to requested angle
        adjWheel.steerto(int(request.form['move_to']))

        return json.jsonify({'wheel':adjWheel.name, 'move_to':request.form['move_to']})
      elif "set_zero" in request.form:
        # Accept the current steering angle as new zero
        adjWheel.steersetzero()

        return json.jsonify({'wheel':adjWheel.name, 'set_zero':request.form['set_zero']})
      else:
        raise ValueError("Invalid POST parameters.")

  @app.route('/system_power', methods=['GET','POST'])
  def system_power():
    """
    Allows an user to either reboot or shut the system down. Depends on the
    ability to call out to system control ('systemctl') which may vary from
    system to system. (Known to work on Raspberry Pi running Raspbian OS)
    """
    if request.method == 'GET':
      return render_template("system_power.html",
        page_title = 'System Power')
    else:
      action = request.form.get('power_command',None)

      if action == "shutdown":
        r = call("systemctl poweroff", shell=True)
        if r == 0:
          flash("Shutting down...", "success")
        else:
          flash("Shutdown attempt failed with error {0}".format(r), "error")
      elif action == "reboot":
        r = call("systemctl reboot", shell=True)
        if r == 0:
          flash("Rebooting...", "success")
        else:
          flash("Reboot attempt failed with error {0}".format(r), "error")
      else:
        flash("Invalid Action {}".format(action), "error")

      return redirect(url_for('ctrlRover'))

  @app.route('/input_voltage')
  def input_voltage():
    """
    Most motor controllers report their battery input voltage. Retrieve and
    display this information for the user.
    """
    chassis.ensureready()
    voltages = dict()

    for name,wheel in chassis.wheels.iteritems():
      voltages[name] = wheel.motor_voltage()

    return render_template("input_voltage.html",
      voltages = voltages,
      page_title = "Input Voltage")
