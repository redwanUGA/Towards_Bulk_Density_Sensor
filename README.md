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
  - Follow Lesson 2 of `37 SENSOR KIT TUTORIAL FOR UNO AND MEGA（v1.0）.pdf`
  - DHT library is needed to be imported 
 


