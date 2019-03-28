// Salinity Sensor Connected to Analog 1
// Moisture Sensor Connected to Analog 2


float rawCountSalinity; //create global variable for reading from A/D converter (0-1023)
float voltageSalinity; //create global variable for voltage (0-5V)
float sensorValueSalinity; //create global variable for sensor value
float slopeSalinity = 15.28; //create global variable for slope for a Salinity Sensor Sensor 
float interceptSalinity = -3.23; //create global variable for intercept for a Salinity Sensor
String unitsSalinity = "ppt"; //create global variable for units for a Salinity Sensor

float rawCountMoisture; //create global variable for reading from A/D converter (0-1023)
float voltageMoisture; //create global variable for voltage (0-5V)
float sensorValueMoisture; //create global variable for sensor value
float slopeMoisture = 108.00; //create global variable for slope for a Moisture Sensor Sensor 
float interceptMoisture = -42; //create global variable for intercept for a Moisture Sensor
String unitsMoisture = "%"; //create global variable for units for a Moisture Sensor

String JSONvalue;

 
void setup() {
  Serial.begin(9600); //setup communication to display
}

void loop() {
  
  rawCountSalinity=analogRead(A1); //read one data value (0-1023)
  voltageSalinity=rawCountSalinity/1023*5; //convert raw count to voltage (0-5V)
  sensorValueSalinity=slopeSalinity*voltageSalinity+interceptSalinity; //convert to sensor value with linear calibration equation
  // Serial.print(sensorValue); //print sensor value 
  // Serial.println(units); //print units and skip to next line
  // delay(500); //wait half second

  rawCountMoisture=analogRead(A2); //read one data value (0-1023)
  voltageMoisture=rawCountMoisture/1023*5; //convert raw count to voltage (0-5V)
  sensorValueMoisture=slopeMoisture*voltageMoisture+interceptMoisture; //convert to sensor value with linear calibration equation

  JSONvalue = String("{") + 
              String("\"Salinity\":") +
              sensorValueSalinity +
              String(",") +
              String("\"SoilMoisture\":") +
              sensorValueMoisture +  
              String("}");
  Serial.println(JSONvalue);
  delay(1000);
  
}
