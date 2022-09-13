import pickle
from selenium import webdriver
from multiprocessing import Process, current_process, Pool

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height


rect = Rectangle(10, 20)


# 사각형 rect 객체를 직렬화 (Serialization)
# with open('driver.data', 'wb') as f:
#     pickle.dump(driver, f)
#
# # 역직렬화 (Deserialization)
# with open('driver.data', 'rb') as f:
#     r = pickle.load(f)

# print(rect.data)
def a(b):
    print(b)
#
#
# numbers = [1]
# procs = []
#
# for index, number in enumerate(numbers):
#     # proc = Process(target=crolling, args=(driver,))
#     proc = Process(target=a, args=(driver,))
#     procs.append(proc)
#     proc.start()
#
#
# for proc in procs:
#     proc.join()
driver = webdriver.Chrome("/Users/kimsungsik/Documents/Develop/chrome/chromedriver")
pool = Pool(processes=4)
pool.map(a, driver)
