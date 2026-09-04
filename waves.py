"""
Initial code for the testing of the Wave Cipher.
This uses 'ascii waves' (based on char - ascii line graphs) to diffuse text
Started by Aarsh Garg on 16th Dec, 2025.
"""

import json
import math
def divide(a, b):  # helper for DN*Wave series
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a // b, a % b
def FOEWave_series(text, freq):
    if freq > 50:
        raise ValueError("Frequency may exceed ASCII safe limits")

    out = []
    for i, c in enumerate(text, start=1):
        n = ord(c) + freq if i % 2 == 1 else ord(c) - freq
        out.append(chr(n))
    return "".join(out)
def FDNWave_series(text, freq, divis):
    if divis > len(text):
        raise ValueError("Divisor too large for text length")
    if divis > 100:
        raise ValueError("Divisor exceeds limit of 100")
    if freq > 50:
        raise ValueError("Frequency may exceed ASCII safe limits")
    out = []
    for i, c in enumerate(text, start=1):
        n = ord(c) + freq if i % divis == 0 else ord(c) - freq
        out.append(chr(n))
    return "".join(out)
def DNIWave_series(text, divisor):
    if divisor <= 0:
        raise ValueError("Divisor must be positive")

    out = []
    inc = 1
    for c in text:
        out.append(chr(ord(c) + inc))
        inc = 1 if inc >= divisor else inc + 1
    return "".join(out)
def DNDWave_series(text, divisor):
    if divisor <= 0:
        raise ValueError("Divisor must be positive")

    out = []
    inc = 1
    for c in text:
        out.append(chr(ord(c) - inc))
        inc = 1 if inc >= divisor else inc + 1
    return "".join(out)
def SineWave_series(text, amplitude, frequency):
    phase = 0.0
    out = []
    for c in text:
        out.append(chr(round(ord(c) + amplitude * math.sin(phase))))
        phase += frequency
    return "".join(out)
def TriangleWave_series(text, amplitude, frequency):
    phase = 0.0
    out = []
    for c in text:
        t = (phase / (2 * math.pi)) % 1
        value = 4 * abs(t - 0.5) - 1
        out.append(chr(round(ord(c) + amplitude * value)))
        phase += frequency
    return "".join(out)
def SawtoothWave_series(text, amplitude, frequency):
    phase = 0.0
    out = []
    for c in text:
        t = (phase / (2 * math.pi)) % 1
        value = 2 * t - 1
        out.append(chr(round(ord(c) + amplitude * value)))
        phase += frequency
    return "".join(out)
def SquareWave_series(text, amplitude, frequency):
    phase = 0.0
    out = []
    for c in text:
        value = 1 if math.sin(phase) >= 0 else -1
        out.append(chr(round(ord(c) + amplitude * value)))
        phase += frequency
    return "".join(out)
def generate_wave_configs():
    foe = {}
    for freq in range(1, 51):
        foe[f"FOE{freq}"] = {
            "series": "FOEWave",
            "frequency": freq
        }
    json.dump(foe, open("FOEWConfigs.json", "w"), indent=4)
    fdn = {}
    for divis in range(2, 101):
        for freq in range(1, 51):
            fdn[f"FDN{divis}|{freq}"] = {
                "series": "FDNWave",
                "divisor": divis,
                "frequency": freq
            }
    json.dump(fdn, open("FDNWConfigs.json", "w"), indent=4)
    dni = {}
    dnd = {}
    for divis in range(1, 101):
        dni[f"DNI{divis}"] = {
            "series": "DNIWave",
            "divisor": divis
        }
        dnd[f"DND{divis}"] = {
            "series": "DNDWave",
            "divisor": divis
        }
    json.dump(dni, open("DNIWConfigs.json", "w"), indent=4)
    json.dump(dnd, open("DNDWConfigs.json", "w"), indent=4)
    sine = {}
    tri = {}
    saw = {}
    sqr = {}
    for amp in range(1, 51):
        for freq in range(1, 21):
            sine[f"SINE{amp}|{freq}"] = {
                "series": "SineWave",
                "amplitude": amp,
                "frequency": freq
            }
            tri[f"TRI{amp}|{freq}"] = {
                "series": "TriangleWave",
                "amplitude": amp,
                "frequency": freq
            }
            saw[f"SAW{amp}|{freq}"] = {
                "series": "SawtoothWave",
                "amplitude": amp,
                "frequency": freq
            }
            sqr[f"SQR{amp}|{freq}"] = {
                "series": "SquareWave",
                "amplitude": amp,
                "frequency": freq
            }
    json.dump(sine, open("SINEWConfigs.json", "w"), indent=4)
    json.dump(tri, open("TRIWConfigs.json", "w"), indent=4)
    json.dump(saw, open("SAWWConfigs.json", "w"), indent=4)
    json.dump(sqr, open("SQRWConfigs.json", "w"), indent=4)
    all_waves = {**foe, **fdn, **dni, **dnd, **sine, **tri, **saw, **sqr}
    json.dump(all_waves, open("AllWaveConfigs.json", "w"), indent=4)
if __name__ == "__main__":
    generate_wave_configs()
