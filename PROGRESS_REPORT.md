# Progress report of the CRAPy project


## Progress: Monday 07 June, 2021

#### Chris:
- Familierized myself with the rover and the team
- layed out goals for the project
- brainstormed ideas for the rotating solar panel
- split up into groups to tackle individual problems
- lost my soldering virginity!
- analyized rover electronic components and wiring

#### Gabriel:

- Get to know the team and the rover
- brainstormed about solar panel attachment
- start figuring out the wiring of the rover
- changing broken parts
- melting screholders into plastic parts
- re-attach loose tyres

#### Justus:
- learn abour the team
- learn about he rover and its functions
- work out the solar tracking solar panel attachement
- work out how to attach the solar panel to the rover

#### Linus:
- Get to know the team and the rover
- brainstorming about possible future software advancements 
- started considering alternative solutions for the autopilot

#### Lucas:
- Familiarized myself with the team and rover 
- Brainstormed potential rover parts that may new reprinting/reworking as well as new functional parts
- Downloaded fusion360
- Starting sketching solar pannel support part
#### Marc:
- showed current state of the rover
- looked at flask/html tutorials

#### Milan:
- brainstorming solution for the solarpanel mount
- getting to know fusion 360 a bit

#### Timon: 
- Set up Fusion360 team and upload the rover designs that have been made so far
- Print stuff
- Show stuff about the rover and answer questions


#### Xavier:
- Brainstroming for autopilot solutions
- Figuring out the code written by the previous groups
- Research of different autopilot solutions (ardupilot, dronekit, autopilot hardware)

## Progress: Tuesday 08 June, 2021

#### Chris:
- deatached all the wires from the sensors and the breadboard
- bought wires and breadboard at the electronics store
- tested the sensors and saw how they connected to the arduino while gabe found the code that went along with them
#### Gabriel:

First Chris detached all the sensors while I researched their specifications. Then started testing all the sensors with the Arduino. LDR missing for light sensors, pressure, temp and altitude sensor working. need 10k resistor for humidity sensor, GPS code works -> have to solder the antenna and make sure it works. Went to the electronics store twice.

#### Justus:
- Testing on the solar panel, output, power, etc.
- looked into some of the possible ai UI and possible app
- research solar tracking mod
- work on rasberry pi

#### Linus:
 - Looked into the software part of alternative autopilots but decided again them in the end 
 - started to look into the AI code

#### Lucas:
- Tested the solar pannel and measured its dimensions
- Started designing the solar panel bracket within Fusion360

#### Marc:
- setup github; enabled progress report & invited contributors
- flashing the pi and figurring out connection with other devices

#### Milan:
- reading up on gearing systems and further playing around with fusion
- starting to design the attachment holders between the solar panel and its mount

#### Timon: 
- redesign front untrasound holder
- modify sensor tower bracket that attaches to the chassis
- print more stuff


#### Xavier:
- Continuing research for autopilot solutions, focusing on pixhawk or Navio as a flight controller (+finding a seller that doesnt ship from China), with ROS and Ardupilot)
- Testing light sensor and Humidity/Pressure/Temp sensor with Gabe and Chris


## Progress: Wednesday 09 June, 2021

#### Chris:
 Got the following sensors to work with Gabe:
  - MH FLyinh Fish sensor to work with both the LDR and the soil moisture sensor
  - BMP280 for pressure, temperature and altitude
  - MQ2 Gas detection sensor
  - HC-SR04 Ultrasound distance sensor
  - AMG8833 Infrared Heat sensor

worked on wiring the whole system together and connecting to a singular power source

#### Gabriel:

Got the following sensors to work with Chris:
  - MH FLyinh Fish sensor to work with both the LDR and the soil moisture sensor
  - BMP280 for pressure, temperature and altitude
  - MQ2 Gas detection sensor
  - HC-SR04 Ultrasound distance sensor
  - AMG8833 Infrared Heat sensor

Wrote unified script for operating all the sensors from the Arduino

#### Justus: 
- research into solar panel tracking etc.
- solar movement mechanism
- make list of needed parts for tracking sun
- work on flashing rasberry

#### Linus:
- Worked myself through Jonas' AI code
- Got the simulation running again

#### Lucas:
- Further improved the first prototype of the solar panel bracket, especially the implementation of the first rotation mechanism with the rotor/ball bearing
- Discussed cryptocurrencies and how they will takeover the world

#### Marc:
- got a screen and installed a hardware setup for the pi
- tried flashing Raspberry Pi again --> installations did not work(very frustrating)
- reflashed many more times

#### Milan:
- finished designing the attachment holders and started on the gear design for the solar panel mount
- lost all my projects due to fusion crashing
- starting over with what i did yesterday

#### Timon: 
- Find more things that we need to order as one order takes ages
- provide input for the solar panel bracket
- got a bunch of 2.5mm allen keys

#### Xavier:
- Dropped the pixhawk flght controller in favor of an imu sensor to perform slam with ros, Lidar, the ultrasound sensors and the the raspberry
- Got walked through Jonas' code by Linus

## Progress: Thursday 10 June, 2021

#### Chris:
- connected the sensors to arduino but with power from the battery on the rover, struggled 
- had issues with the multimeter and failed to remeber basic circuit design :(
- tried to find ways to lower amps in the circuit
- researched how to utilize the energy from the solar panel and convert it into usable energy

#### Gabriel:
- tested the Arduino with all the sensors connected with an external power source
- ran into some issues with that, Multimeter was damaged from first day, had to replace the fuse
- started finding solutions for the circuit design to reduce current but still supply all the sensors with enough power

#### Justus:
- worked from home 
- worked on curcuit diagram for solar tracking system
- worked on code for arduino solar tracker

#### Linus:
- Comunicated with Jonas about the code, the problems and solutions for the AI
- Added a sensor range input for the simulated rover

#### Lucas:
- First print of the solar panel bracket
- Evaluated issues with the first print as well as potential solutions improving the design 

#### Marc:
- looked at many videos regarding raspberry pi setup
- started looking into sqlite

#### Milan:
- started brainstorming a sample box for the rover
- had a look at the previous one and collected data of the servo and the rover

#### Timon: 
- do some troubleshooting as the printer is heavily underextruding
- print more things

#### Xavier:
- Started modifying Jonas' algorithm with Linus (changing the sensors in the simulation to give a distance input rather than a boolean)
- Installed a dual boot on my PC to be able to run Ubuntu with ROS and test the Lidar

## Progress: Friday 11 June, 2021

#### Chris:
- used a parallel circuit to power the sensors so they all had equal voltage, but accidentaly fried some components so replacements had to be ordered
- looked at sensor placement and also arduino/rasberry/etc configuration

#### Gabriel:
- got the sensors to be powered by the rover battery while in a parallel circuit - some are broken, sent list of parts to Timon
- discussed about sensor placement and design for a chassis
- probably going to solder the sensors to a board

#### Justus:
- finished code for solar aduino
- cheched and finished solar tracking curcuit diagram

#### Linus:
- Experimented with different mutationRate functions
- Added a new select function 
- Worked on the fitness function
- then threw myself from a bridge

#### Lucas:
- Tweaked the design of the inital solar panel bracket
- Worked more on the rotating axis of the bracket joint

#### Marc:
- finally made the raspberry pi work again :V also the webserver works aswell
- connected the infrared camera to the pi and ran some experiements on the live stream and interpolation 

#### Milan:
- designed the entire sample box in fusion 360
- edited some small things in order to make it 3d printable
- designed 5 different gear cutouts for sample printing to see which clearance fits onto the servo

#### Timon: 
- redesign second arm of the robot arm
- transfering info to milan for designing the sample box
- talking through milans design with him
- help with electronics
- help with the solar tilt mechanism 
- think about how the second tilting mechanism could be built & take some measurements on build volume and desired tilt angle

#### Xavier:
- Installed ros on my computer and tried to test out the LIDAR

## Progress: Saturday 12 June, 2021

#### Chris:
- got drunk to forget the dark demons of my past

#### Gabriel:

#### Justus:

#### Linus:
- intoxicated myself
#### Lucas:
- 

#### Marc:
- St.Pieters and chill

#### Milan:
- brainstormed ideas to integrade a hygrometer in the sample box
- looked up the dimensions of the one that is already there
- designed some cut outs in the smaple box which will fit the sensor and cabeling
- design of the sample box almost completely finished

#### Timon: 
- print stuff

#### Xavier:

## Progress: Sunday 13 June, 2021

#### Chris: 
- see saturday 12 June 2021

#### Gabriel:

#### Justus:

#### Linus:
- Digged into literature to learn how neat algorithms are applied in professional autopilots 
- Looked into genetic encoding on ANNs

#### Lucas:

#### Marc:
- read my book in the park

#### Milan:

#### Timon: 
- print a lot more prototypes and other things
- picking up motors for testing
#### Xavier:

## Progress: Monday 14 June, 2021

#### Chris: 
- brainstormed on how to intergrate solar power into powering components, will probably only power the mechanism it needs to follow the sun
- started learning fusion 360 so i can 3D pring sensor tray (hopefully)
- soldered odd things for some people

#### Gabriel:
- got an overview of what the solar people have been working on 
- brainstormed on the integration of sensors in the sample box
- put together a concept for a circuit to harness the power from the solar panel

#### Justus:
-some 3d printing (solar panel bracket attachement tool)
- started work with arduino that has now arrived
- testing components of solar trackign circuit

#### Linus:
- Now the rover gets punished for rotating over and over 
- Also removed any random factors from the starting position of the rover in order to reduce luck from which rover is chosen 
- Now the rover is actually pretty decent at avoiding objects - implementing the sensor range once again sounds promissing 

#### Lucas:
- Further worked on the second rotating mechanism of the solar panel mount, which will utilize a 2-1 gear ratio as well as teeth surface onto which the larger gear can be fitted on --> facilitates 3d printing of the part

#### Marc: 
- looked more into interpolation; tried higher resolution for the camera --> pi overheated
- looked into lidar connection 
- set up report on google docs

#### Milan:
- designed a gear and rack system to slide the sensor in and out of the sample box
- continued designing the sample box in fusion. 
- started 3d printing some samples

#### Timon: 

#### Xavier: 
- worked on ai with linus (cf. linus bulletpoints).

## Progress: Tuesday 15 June, 2021

#### Chris: 
- found the parts needed for converting the solar power into usable energy and ordered them
- finished some soldering things that i failed to finish on moday
- drew up basic designs for sensor placement 

#### Gabriel:
- sent Timon list of necessary parts to order for building the circuit that harnesses the solar energy
- built and tested the 2-servo solar tracking circuit with Justus
- confirmed with Milan and Lucas (Fusion 360) that we would work closely together to design the sensor tray

#### Justus:
-soldering solar tracking circuit with arduino
-putting code on arduino
-testing solar tracking system put together
-some 3d printing

#### Linus:
- Debugged the sensor range implementation from last week 
- reworked the network decisions and inputs
- implemented speed control

#### Lucas:
- Measuring and calculating the 
- More CAD design of the rotating axis + the joint with two ball bearing supporting the mast

#### Marc:
- together with Xavier; downloaded ros and set up pi for lidar

#### Milan:
- designed double helical gears in fusion for the mount of the solar panel
- finished the design of the sample box
- started brainstorming about a multitool head system of the arm with timon

#### Timon: 

#### Xavier:

## Progress: Wednesday 16 June, 2021

#### Chris:
- had some personal things to take care of so i took the day off from the project

#### Gabriel:
- as the sensors had not yet arrived, I started working on the report
- wrote an introduction, the start of the methods section and started on the sensors & circuitry part of the report

#### Justus: 
-worked from home, brainstorm on how to attach the LDR for solar trackign to the solar panel
-started in fusion with LDR attachement bracket

#### Linus:
- Implemented genetic enharence as reproduction mechanism 
- Reworked population control

#### Lucas:
- Tweaked the design of the double helical gears with Milan
- Starting brainstorming the design of the base of the solar panel mount

#### Marc:
- together with Xavier; troubleshoot ros/lidar functioning
- looked into SLAM 

#### Milan:
- started assembling the first parts of the sample box
- designed another rack and pinion systems for the multitool head system of the gripper arm

#### Timon: 

#### Xavier:

## Progress: Thursday 17 June, 2021

#### Chris:
- New sensors arrived so gabe and I intergrated them into the circuit and updated the code so everything would work well (gabe did the heavy lifting for the code) 
- finalized sensor placement and began drawing up a desing in fusion 360 for a tray that houses them
- soldered some things for mark and xavier

#### Gabriel:
- integrated new sensors into the circuit and adjusted arduino output to be easily readable and processable by the Raspberry
- brainstormed about the sensor arrangement with Chris
- designed and finished circuit diagram for the sensors

#### Justus:
- fusion for LDR attachemetn bracket, finished
- measuring all the points for existing solar panel brackets to make it accurate and ready to print
- outline for work on paper

#### Linus:
- Implemented exploration trade for rovers 
- Cleaned up the code - looking to have a first good version by beginning of next week 
- Reworked the simulation and added real dimensions of the rover
- forced left right motion 

#### Lucas:
- Further working on the base of the solar panel mount. Due to shape of the part, the gear section of the base will be bolted onto the rest.
- Tweaked the design in order to add the second motor, which rotates the smaller gear.

#### Marc:
- together with Xavier; integrated hector-SLAM!
- looked at imu integration

#### Milan:
. started looking into bevel gears
- designed a new system of the current gripper that is on the arm so it will fit on the universal tool that is suppo9sed to be on the arm in the end
- constructed some bevel gears for the gripper to change the rotating motion by 90 degrees

#### Timon: 

#### Xavier:

## Progress: Friday 18 June, 2021

#### Chris:

#### Gabriel:
- got the Arduino output to be displayed on the Raspberry Pi
- wanted to store each set of data in an array and display it live but had some hiccups with that -> will do on monday
- new BMP280 thanks to Chris' incredible soldering job
- wrote a new paragraph on the report

#### Justus:

#### Linus:

#### Lucas:
- Added screw holes onto the bottom of the solar panle mount base in order to attach it to the plexiglass on the rover
- Final tweaks (filleting,etc...) to the design before the 3D printing of many this weekend

#### Marc:

#### Milan:
- almost completely finished the new gripper tool in fusion
- did some final changes on the sample box with a drill in order to fit everything together. 1 part has to be reprinted with some more clearance

#### Timon: 

#### Xavier:

## Progress: Saturday 19 June, 2021

#### Chris:

#### Gabriel:

#### Justus:

#### Linus:

#### Lucas:

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Sunday 20 June, 2021

#### Chris:

#### Gabriel:

#### Justus:

#### Linus:

#### Lucas:

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Monday 21 June, 2021

#### Chris:

#### Gabriel:
- re-wired all the sensors together with chris
- got the live graphing for the sensor data to work on the raspberry pi
- the sensor data is now stored in 10 different arrays, which are updated every second
- the sensors are now powered via the arduino which is powered by the raspberry

#### Justus:

#### Linus:

#### Lucas: 
- Tripping in Amsterdam

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Tuesday 22 June, 2021

#### Chris:

#### Gabriel:
- tested and included a new IMU sensor into the arduino code
- started to figure out how to get the charging circuit to work

#### Justus:

#### Linus:

#### Lucas:
 - Added onto the solar panel section of the report

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Wednesday 23 June, 2021

#### Chris:

#### Gabriel:
- took a while to get the DC-DC booster to work -> the internal wiring seems to be wrongly noted on the board
- tried to get the new GPS sensor to work, didn't succeed
- read over Lucas' contribution to the report and made suggestions

#### Justus:

#### Linus:

#### Lucas:
 - Cleaned and tested the parts of the solar panel mount
 - Started assembling the mount  
#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Thursday 24 June, 2021

#### Chris:

#### Gabriel:

#### Justus:

#### Linus:

#### Lucas:
 - Finished assembling the solar panel mount and fitted the solar panel with it
 - Fitted the contraption onto plexiglass
 - Tested the Arduino code with the tilting mechanisms
#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Friday 25 June, 2021

#### Chris:

#### Gabriel:

#### Justus:

#### Linus:

#### Lucas:

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Saturday 26 June, 2021

#### Chris:

#### Gabriel:

#### Justus:

#### Linus:

#### Lucas:

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Sunday 27 June, 2021

#### Chris:

#### Gabriel:

#### Justus:

#### Linus:

#### Lucas:

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Monday 28 June, 2021

#### Chris:

#### Gabriel:

#### Justus:

#### Linus:

#### Lucas:

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Tuesday 29 June, 2021

#### Chris:

#### Gabriel:

#### Justus:

#### Linus:

#### Lucas:

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:

## Progress: Wednesday 30 June, 2021

#### Chris:

#### Gabriel:

#### Justus:

#### Linus:

#### Lucas:

#### Marc:

#### Milan:

#### Timon: 

#### Xavier:
