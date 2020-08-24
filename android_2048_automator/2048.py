#!./env/bin/python

from ppadb.client import Client
import time

client = Client()

device = client.devices()[0]

while True:
    device.shell("input swipe 540 1600 540 1200 35 && input swipe 900 900 600 900 35 && input swipe 500 1200 500 1600 35 && input swipe 600 900 900 900 35")

    # device.shell("input swipe 540 1600 540 1200 45")
    # #time.sleep(0.035)
    # device.shell("input swipe 900 900 600 900 45")
    # #time.sleep(0.05)
    # device.shell("input swipe 500 1200 500 1600 45")
    # #time.sleep(0.05)
    # device.shell("input swipe 600 900 900 900 45")
    # #time.sleep(0.05)
