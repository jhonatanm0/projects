const int POT_PIN = A0; // Use A0 for analog input
const int _led_yellow = 7;
const int _led_blue = 6;
const int _led_green = 5;
const int _led_red = 4;

void setup() {
    pinMode(POT_PIN, INPUT);
    pinMode(_led_yellow, OUTPUT);
    pinMode(_led_blue, OUTPUT);
    pinMode(_led_green, OUTPUT);
    pinMode(_led_red, OUTPUT);
}

void loop() {
    int value = analogRead(POT_PIN);

    if (value < 300) {
        digitalWrite(_led_yellow, HIGH);
        digitalWrite(_led_blue, LOW);
        digitalWrite(_led_green, LOW);
        digitalWrite(_led_red, LOW);
    } else if (value >= 300 && value < 500) {
        digitalWrite(_led_yellow, LOW);
        digitalWrite(_led_blue, HIGH);
        digitalWrite(_led_green, LOW);
        digitalWrite(_led_red, LOW);
    } else if (value >= 500 && value < 800) {
        digitalWrite(_led_yellow, LOW);
        digitalWrite(_led_blue, LOW);
        digitalWrite(_led_green, HIGH);
        digitalWrite(_led_red, LOW);
    } else {
        digitalWrite(_led_yellow, LOW);
        digitalWrite(_led_blue, LOW);
        digitalWrite(_led_green, LOW);
        digitalWrite(_led_red, HIGH);
    }
}



