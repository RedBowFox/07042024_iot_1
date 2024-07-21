def on_received_number(receivedNumber):
    global received_number_
    if receivedNumber == 1:
        received_number_ = 1
    elif receivedNumber == 0:
        received_number_ = 0
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    TELEGRAM("success ")
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def TELEGRAM(TEXT: str):
    esp8266.send_telegram_message("7177644587:AAEqu6MG3eQ6yzhSlEBybgAsXJ66M-_Np9Q",
        "-4154883213",
        TEXT)
    if not (esp8266.is_telegram_message_sent()):
        esp8266.send_telegram_message("7177644587:AAEqu6MG3eQ6yzhSlEBybgAsXJ66M-_Np9Q",
            "-4154883213",
            TEXT)
        basic.show_icon(IconNames.NO)
    else:
        basic.show_icon(IconNames.YES)
        basic.pause(200)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
received_number_ = 0
radio.set_group(107)
esp8266.init(SerialPin.P15, SerialPin.P16, BaudRate.BAUD_RATE115200)
esp8266.connect_wi_fi("Who?", "Robowis7332")
if esp8266.is_wifi_connected():
    basic.show_icon(IconNames.HAPPY)
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
else:
    esp8266.connect_wi_fi("Who?", "Robowis7332")
    basic.show_icon(IconNames.SAD)

def on_forever():
    if received_number_ == 1:
        TELEGRAM("ALERTS AT [173]")
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . # . .
            """)
    else:
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
