import random, time, winsound

while True:
    temp = random.randint(1, 100)
    if temp > 60:
        print("Alert Temparature is high!!")
        winsound.PlaySound("ENGALRT-07a.wav", winsound.SND_FILENAME)
    else:
        print("Temparature is Normal")

        time.sleep(1)
