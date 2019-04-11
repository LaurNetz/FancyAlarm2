import Sound
import Motion
import Cam

# Die zwei Variablen Sound und Motion Zustandsfefinition. IN den Codes der Sensoren muss also die jeweilige Zustände gesetzt werden


if (Sound = 0) + (Motion = 0):
    actor = False
if (Sound = 1) + (Motion = 1):
    actor = True
if (Sound = 1) + (Motion = 0):
    actor = False
if (Sound = 0) + (Motion = 1):
    actor = False

while actor = FALSE:
    open
    DateiProtokoll
    "r" as pfile
    pfile(print("peace" + date + time))

    if actor = TRUE:
        cam()
        stream()
        open
        DateiProtokoll
        "r" as pfile
        pfile(print("Alarm" + date + time))


