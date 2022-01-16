import time
import mouse

def click (seconds=10):
    end = time.time() + seconds
    while time.time() < end:
       mouse.press()
       mouse.release()

if __name__ == "__main__":
    time.sleep(1)
    click()
    print("done")