/* 
  BFRee intermittency test.
  
*/


const int ledPin = 13;
const int powerPin = 0;
const int startPin = 1;
const int donePin = 2;

unsigned int off_time;
unsigned int on_time;

enum action {
  ACTION_UNKNOWN,
  ACTION_START,
  ACTION_CONFIGURE,
};

String get_string() {
  String str;
  
  while (true) {
    if (!Serial.available()) {
      delay(10);
      continue;
    }
    
    char c = Serial.read();
    if (c == '\n')
      break;
    str += c;
  }
  
  return str;
}

int get_int() {
  String str = get_string();
  return str.toInt();
}

void get_config() {

  Serial.println("Intermittency testing tool version 0.01 alpha");
  Serial.println("Enter the desired on-time in ms");
  on_time = get_int();
  Serial.println("Enter the desired off-time in ms");
  off_time = get_int();

  Serial.print("On-time: "); Serial.print(on_time); Serial.println(" ms");
  Serial.print("Off-time: "); Serial.print(off_time); Serial.println(" ms");
}

enum action get_action() {
  Serial.println("Send \'s\' to start or \'c\' to reconfigure'");
  String str = get_string();

  if (str == "s") {
    return ACTION_START;
  } else if (str == "c") {
    return ACTION_CONFIGURE;
  }
  return ACTION_UNKNOWN;
}

static inline void set_power_high() {
  digitalWrite(ledPin, HIGH);
  digitalWrite(powerPin, HIGH);
}

static inline void set_power_low() {
  digitalWrite(ledPin, LOW);
  digitalWrite(powerPin, LOW);
}

static inline void set_start_high() {
  digitalWrite(startPin, HIGH);
}

static inline void set_start_low() {
  digitalWrite(startPin, LOW);
}

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(powerPin, OUTPUT);
  pinMode(startPin, OUTPUT);
  pinMode(donePin, INPUT_PULLDOWN);

  delay(4000);

  set_power_high();


  // Flush the serial
  char c;
  while(Serial.available() > 0) {
    c += Serial.read();
  }

  enum action act = ACTION_UNKNOWN;
  while (act != ACTION_START) {
    get_config();
    act = get_action();
  }

  Serial.print("Starting in: ");
  for(int i=5; i>0; i--) {
    Serial.print(" "); Serial.print(i);
    delay(1000);
  }
  Serial.println(" GO!");
}


void loop() {

  elapsedMillis benchmarkTime;
  elapsedMillis onTime;
  //elapsedMillis offTime;
  
  int on_cnt = 0;
  int off_cnt = 0;

  benchmarkTime = 0;
  set_start_high();

  if (off_time != 0) {
    while (true) {
      set_power_high();
      on_cnt += 1;
            
      onTime = 0;
      while (onTime < on_time) {
        if (digitalRead(donePin) == HIGH) {
          break;
        }
      }
      //delay(on_time);
      if (digitalRead(donePin) == HIGH) {
        break;
      }

      set_power_low();
      set_start_low();
      off_cnt += 1;
      delay(off_time); // can be a delay, nothing will happen when it's off
    }
  } else {
    on_cnt += 1;
    while (true) {
      if (digitalRead(donePin) == HIGH) {
        break;
      }
    }
  }  

  
  int time_benchmark_ms = benchmarkTime;

  set_start_low();

  Serial.println("Done signal received!");
  Serial.print("Benchmark ran for: "); Serial.print(time_benchmark_ms); Serial.println(" ms");
  Serial.print("i.e.: "); Serial.print(time_benchmark_ms/1000); Serial.println(" s");

  String d = ", ";
  String csv_title = "On-time, Off-time, On count, Off count, runtime (ms)";
  String csv_entry = on_time + d + off_time + d + on_cnt + d + off_cnt + d + time_benchmark_ms;

  Serial.println(csv_title);
  Serial.println(csv_entry);

  while (true) {
    delay(1000);
  }
}
