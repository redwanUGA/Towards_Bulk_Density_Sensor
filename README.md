# Towards_Bulk_Density_Sensor
This repository holds necessary codes, documentations, and credentials for the prototyping and development of the IoT platform of Bulk Density sensor

# 1. System Architecture
```
Sensors --[wired connection]--> Arduino --[Serial]--> Raspberry pi --[Wi-fi]--> Cloud --[Internet]--> UI
```
- Physical Sensors will connect  to Arduino via direct wire connection.  
- Arduino connect to Raspberry pi via USB. 
- Raspberry pi connects to the cloud via Wi-fi. 
- From Local PC there is an interface where you can view the data over time. 

# 2. Current Status

- __Sensors__ 
  - [x] Temperature : 
  - [x] Humidity 
  - [ ] pH
  - [ ] ORP

- __Arduino__
  - Follow Lesson 2 of `37 SENSOR KIT TUTORIAL FOR UNO AND MEGA（v1.0）.pdf` for circuit connection. 
    <b class="warning"> ! Caution :: externally powered sensor is not working at this point. </b> 
  - DHT library is needed to be imported to make the code work
  - After importing DHT library in the IDE and plugging everything up, simply upload DHT11 example code in Arduino board. 
- __Raspberry Pi__
  - [ ] Configuration guidance will be added later on
  - [x] Fully configured for SSH and VNC connection
  - To do ssh use Putty or MobaXterm 
  - To do VNC use RealVNC
  - To run the code, open terminal and type the following command
  > ``` python3 /home/pi/Desktop/workspace/send_over_cloud.py ```
- __UI__
  - UI is now an IPython notebook which can be run via Jupyter notebook or Google Colab.
  - Run the code and view the graph at the end of the code
  - [ ] Maximum 15-20 runs can be done. After that API key gets filled up.  
