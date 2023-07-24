import time
import threading

def cal_sq(arr):
    for i in arr:
        time.sleep(0.5)
        print(f'square : {i**2}')

def cal_cube(arr):
    for i in arr:
        time.sleep(0.5)
        print(f'cube : {i**3}')

t=time.time()
#cal_sq([1,2,3,4,5])
#cal_cube([1,2,3,4,5])
arr = [1,2,3,4,5]
t1 = threading.Thread(target=cal_sq, args = (arr,))
t2 = threading.Thread(target=cal_cube, args = (arr,))

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Ran in {round(time.time() - t,2)} seconds")

# -----------------------------TRADITIONAL WAY---------------------------
t=time.time()
cal_sq([1,2,3,4,5])
cal_cube([1,2,3,4,5])
print(f"Finished in {round(time.time() - t,2)} seconds")

