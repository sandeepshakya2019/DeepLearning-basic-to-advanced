from multiprocessing import Process
import time

def task(name):
    print(f"Task {name} started", flush=True)
    time.sleep(1)
    print(f"Task {name} finished", flush=True)

if __name__ == "__main__":
    p1 = Process(target=task, args=("A",))
    p2 = Process(target=task, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both processes completed", flush=True)
