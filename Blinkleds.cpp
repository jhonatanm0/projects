const int DELAY_TIME = 1000; // Delay time in milliseconds
const int _led_yellow = 7;
const int _led_blue = 6;
const int _led_green = 5;
const int _led_red = 4;

void setup() {
    pinMode(_led_yellow, OUTPUT);
    pinMode(_led_blue, OUTPUT);
    pinMode(_led_green, OUTPUT);
    pinMode(_led_red, OUTPUT);
}

void loop() {
    digitalWrite(_led_yellow, HIGH);
    delay(DELAY_TIME);
    digitalWrite(_led_yellow, LOW);

    digitalWrite(_led_blue, HIGH);
    delay(DELAY_TIME);
    digitalWrite(_led_blue, LOW);

    digitalWrite(_led_green, HIGH);
    delay(DELAY_TIME);
    digitalWrite(_led_green, LOW);

    digitalWrite(_led_red, HIGH);
    delay(DELAY_TIME);
    digitalWrite(_led_red, LOW);
}