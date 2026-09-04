from waves import (
    FOEWave_series,
    FDNWave_series,
    DNIWave_series,
    DNDWave_series,
    SineWave_series,
    TriangleWave_series,
    SawtoothWave_series,
    SquareWave_series
)

from asciigraph import plot_text_ascii

TEXT = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"  # fixed text for all tests
TEXT2 = "Hi! My name is Aarsh Garg, and I am testing the Wave Cipher."

def show_ascii(label, result):
    print(label)
    print("result:", result)
    print("ascii :", [ord(c) for c in result])
    print("-" * 50)

print("=== WAVE CIPHER TESTER ===")
print("TEXT =", TEXT)
print("TEXT2 =", TEXT2)
print("=" * 50)

def glyph_warn():
    print("The tester might rais errors on encrypting TEXT2 due to missing glyphs of extended ASCII.")
    confirmation = str(input("Do you want to proceed? (Y/n): "))
    if confirmation == 'Y':
        pass
    else:
        quit()

glyph_warn()

# ---- FOE WAVE ----
show_ascii(
    "FOEWave | freq=4",
    FOEWave_series(TEXT, 4)
)
plot_text_ascii(FOEWave_series(TEXT, 4))

# ---- FDN WAVE ----
show_ascii(
    "FDNWave | divisor=3 | freq=6",
    FDNWave_series(TEXT, 6, 3)
)
plot_text_ascii(FDNWave_series(TEXT, 6, 3))

# ---- DNI WAVE ----
show_ascii(
    "DNIWave | divisor=5",
    DNIWave_series(TEXT, 5)
)
plot_text_ascii(DNIWave_series(TEXT, 5))

# ---- DND WAVE ----
show_ascii(
    "DNDWave | divisor=5",
    DNDWave_series(TEXT, 5)
)
plot_text_ascii(DNDWave_series(TEXT, 5))

# ---- SINE WAVE ----
show_ascii(
    "SineWave | amplitude=5 | frequency=1",
    SineWave_series(TEXT, amplitude=5, frequency=1)
)
plot_text_ascii(SineWave_series(TEXT, amplitude=5, frequency=1))

# ---- TRIANGLE WAVE ----
show_ascii(
    "TriangleWave | amplitude=5 | frequency=1",
    TriangleWave_series(TEXT, amplitude=5, frequency=1)
)
plot_text_ascii(TriangleWave_series(TEXT, amplitude=5, frequency=1))

# ---- SAWTOOTH WAVE ----
show_ascii(
    "SawtoothWave | amplitude=5 | frequency=1",
    SawtoothWave_series(TEXT, amplitude=5, frequency=1)
)
plot_text_ascii(SawtoothWave_series(TEXT, amplitude=5, frequency=1))

# ---- SQUARE WAVE ----
show_ascii(
    "SquareWave | amplitude=5 | frequency=1",
    SquareWave_series(TEXT, amplitude=5, frequency=1)
)
plot_text_ascii(SquareWave_series(TEXT, amplitude=5, frequency=1))

# ---- FOE WAVE ----
show_ascii(
    "FOEWave | freq=4",
    FOEWave_series(TEXT2, 4)
)
plot_text_ascii(FOEWave_series(TEXT2, 4))

# ---- FDN WAVE ----
show_ascii(
    "FDNWave | divisor=3 | freq=6",
    FDNWave_series(TEXT2, 6, 3)
)
plot_text_ascii(FDNWave_series(TEXT2, 6, 3))

# ---- DNI WAVE ----
show_ascii(
    "DNIWave | divisor=5",
    DNIWave_series(TEXT2, 5)
)
plot_text_ascii(DNIWave_series(TEXT2, 5))

# ---- DND WAVE ----
show_ascii(
    "DNDWave | divisor=5",
    DNDWave_series(TEXT2, 5)
)
plot_text_ascii(DNDWave_series(TEXT2, 5))

# ---- SINE WAVE ----
show_ascii(
    "SineWave | amplitude=5 | frequency=1",
    SineWave_series(TEXT2, amplitude=5, frequency=1)
)
plot_text_ascii(SineWave_series(TEXT2, amplitude=5, frequency=1))

# ---- TRIANGLE WAVE ----
show_ascii(
    "TriangleWave | amplitude=5 | frequency=1",
    TriangleWave_series(TEXT2, amplitude=5, frequency=1)
)
plot_text_ascii(TriangleWave_series(TEXT2, amplitude=5, frequency=1))

# ---- SAWTOOTH WAVE ----
show_ascii(
    "SawtoothWave | amplitude=5 | frequency=1",
    SawtoothWave_series(TEXT2, amplitude=5, frequency=1)
)
plot_text_ascii(SawtoothWave_series(TEXT2, amplitude=5, frequency=1))

# ---- SQUARE WAVE ----
show_ascii(
    "SquareWave | amplitude=5 | frequency=1",
    SquareWave_series(TEXT2, amplitude=5, frequency=1)
)
plot_text_ascii(SquareWave_series(TEXT2, amplitude=5, frequency=1))

