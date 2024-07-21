radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    if (receivedNumber == 1) {
        received_number_ = 1
    } else if (receivedNumber == 0) {
        received_number_ = 0
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    TELEGRAM("success ")
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
})
function TELEGRAM(TEXT: string) {
    esp8266.sendTelegramMessage("7177644587:AAEqu6MG3eQ6yzhSlEBybgAsXJ66M-_Np9Q", "-4154883213", TEXT)
    if (!esp8266.isTelegramMessageSent()) {
        esp8266.sendTelegramMessage("7177644587:AAEqu6MG3eQ6yzhSlEBybgAsXJ66M-_Np9Q", "-4154883213", TEXT)
        basic.showIcon(IconNames.No)
    } else {
        basic.showIcon(IconNames.Yes)
        basic.pause(200)
    }
    
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
}

let received_number_ = 0
radio.setGroup(107)
esp8266.init(SerialPin.P15, SerialPin.P16, BaudRate.BaudRate115200)
esp8266.connectWiFi("Who?", "Robowis7332")
if (esp8266.isWifiConnected()) {
    basic.showIcon(IconNames.Happy)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
} else {
    esp8266.connectWiFi("Who?", "Robowis7332")
    basic.showIcon(IconNames.Sad)
}

basic.forever(function on_forever() {
    if (received_number_ == 1) {
        TELEGRAM("ALERTS AT [173]")
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . # . .
            `)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    
})
