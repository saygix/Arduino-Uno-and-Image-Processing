const int kirmizi = 9;
const int yesil = 8;
const int sari = 10;

void setup() {
    pinMode(kirmizi, OUTPUT);
    pinMode(yesil, OUTPUT);
    pinMode(sari, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();

        if (command == '1') {
            digitalWrite(kirmizi, HIGH);  // Kırmızı LED'i aç
        } else if (command == '0') {
            digitalWrite(kirmizi, LOW);   // Kırmızı LED'i kapat
        }

        if (command == '2') {
            digitalWrite(yesil, HIGH);  // Yeşil LED'i aç
        } else if (command == '3') {
            digitalWrite(yesil, LOW);   // Yeşil LED'i kapat
        }

        if (command == '4') {
            digitalWrite(sari, HIGH);  // Sarı LED'i aç
        } else if (command == '5') {
            digitalWrite(sari, LOW);   // Sarı LED'i kapat
        }
    }
}
