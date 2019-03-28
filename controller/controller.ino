#include <Servo.h>

Servo coils[4];
int pins[] = {3, 5, 6, 9};

struct __attribute__ ((packed)) signal {
  float lh;
  float lv;
  float rh;
  float rv;
} controls;

int stick_to_pwm(float stick) {
  return (90 * stick) + 90;
}

void setup() {

  Serial.begin(9600);

  for (int i = 0; i < sizeof(pins); i++) {
    coils[i].attach(pins[i]);
  }
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {

  Serial.readBytes((uint8_t*)&controls, sizeof(signal));
  if (controls.lh > 0) {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else {
    digitalWrite(LED_BUILTIN, LOW);
  }
  coils[0].write(stick_to_pwm(controls.lh));
  coils[1].write(stick_to_pwm(controls.lv));
  coils[2].write(stick_to_pwm(controls.rh));
  coils[3].write(stick_to_pwm(controls.rv));

}
