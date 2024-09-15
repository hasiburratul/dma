import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar
    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

def blink(color, duration):
    """Blink the LED with the specified color and duration."""
    led[0] = color
    time.sleep(duration)
    led[0] = (0, 0, 0)
    time.sleep(duration)

def gradual_fade_to_half_blue(steps=10, total_duration=5):
    """Gradually fades the blue LED from full brightness to half brightness."""
    step_duration = total_duration / steps
    led[0] = (0, 0, 255)  # Set the color to blue
    for brightness in range(100, 50, -steps):  # Full brightness (1.0) to half brightness (0.5)
        led.brightness = brightness / 100
        time.sleep(step_duration)

def gradual_brighten_blue(steps=10, total_duration=5):
    """Gradually brightens the blue LED from half brightness to full brightness."""
    step_duration = total_duration / steps
    led[0] = (0, 0, 255)  # Set the color to blue
    for brightness in range(50, 101, steps):  # Half brightness (0.5) to full brightness (1.0)
        led.brightness = brightness / 100
        time.sleep(step_duration)

def arc_reactor_fade():
    """Simulates Tony Stark's Arc Reactor fading away"""
    led.brightness = 0.3

    # Gradual fade of Arc Reactor
    for brightness in range(50, 0, -5):
        led[0] = (255, 255, 255)  # White for the reactor
        led.brightness = brightness / 100
        time.sleep(0.3)
    led[0] = (0, 0, 0)  # Off, end of sequence

def sequence():
    led.brightness = 0.5
    """Infinity color sequence."""

    # The Infinity Stones - 6 colors representing the stones
    blink((255, 69, 0), 1)  # Orange (Soul Stone)
    blink((255, 255, 0), 1)  # Yellow (Mind Stone)
    blink((0, 0, 255), 1)    # Blue (Space Stone)
    blink((148, 0, 211), 1)  # Purple (Power Stone)
    blink((0, 255, 0), 1)    # Green (Time Stone)
    blink((255, 0, 0), 1)    # Red (Reality Stone)

    # Climax: Thanos Snap (bright white flash)
    led.brightness = 1
    blink((255, 255, 255), 0.3)  # Snap

    # Post-Snap: Universe fades away (slow dimming to half brightness)
    gradual_fade_to_half_blue()

    # Restoration Phase: Avengers collect stones for second snap
    led.brightness = 0.5
    time.sleep(1)  # Pause

    # Stones being collected again
    blink((255, 69, 0), 0.5)  # Orange (Soul Stone)
    blink((255, 255, 0), 0.5)  # Yellow (Mind Stone)
    blink((0, 0, 255), 0.5)    # Blue (Space Stone)
    blink((148, 0, 211), 0.5)  # Purple (Power Stone)
    blink((0, 255, 0), 0.5)    # Green (Time Stone)
    blink((255, 0, 0), 0.5)    # Red (Reality Stone)

    # Avengers Snap (White flash for reversal)
    led.brightness = 1
    blink((255, 255, 255), 0.5)  # Snap of restoration

    # Slowly glowing up the blue to full brightness from 0.5 to 1
    gradual_brighten_blue()
    time.sleep(1)  # Pause

    # Ending: Tony's death (Arc Reactor fading after blinks)
    arc_reactor_fade()

sequence()
