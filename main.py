def on_button_pressed_a():
    music.play_tone(277, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.EIGHTH))
    music.play_tone(208, music.beat(BeatFraction.EIGHTH))
    music.play_tone(139, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(175, music.beat(BeatFraction.WHOLE))
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    music.play_tone(139, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.SIXTEENTH))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(147, music.beat(BeatFraction.WHOLE))
    music.play_tone(185, music.beat(BeatFraction.WHOLE))
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_leds("""
        . # . # .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    basic.show_string("liszt!")
input.on_button_pressed(Button.B, on_button_pressed_b)
