from pynput.keyboard import Listener, Controller, Key

controller = Controller()

running = True

def on_press(key):
    global running
    if str(key) == "'q'":
        running = False

listener = Listener(
    on_press=on_press)
listener.start()

while running:
    controller.press(Key.up)
    controller.release(Key.up)
    controller.press(Key.left)
    controller.release(Key.left)
    controller.press(Key.down)
    controller.release(Key.down)
    controller.press(Key.right)
    controller.release(Key.right)
