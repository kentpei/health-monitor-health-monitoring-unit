# coding: utf8
import time
import random
def generate_data():
    Pulse = random.randint(0,100) #range from 20-60 is normal else it alerms
    Blood_Pressure = random.randint(50,200) #range from 80-140 is normal else it alerms
    oxygen_Level = random.randint(30,150) #range from 60-110 is normal else it alerms
    data = (Pulse,Blood_Pressure,oxygen_Level)
    return data
# run every 1s.
def main():
    #description: generate data in the fixed range from generate_data() function
    #             then create three random parameters to make exception
    #input: None
    #output:format like this{Pulse:XXX, Blood_Pressure:XX,oxygen_Level:XX}
    data = generate_data()
    #time.sleep(1) this one controled by suli
    # end = time.time()
    # while end - start < 10:
    # lst.append(t2())
    dic = {}
    a = random.randint(0, 100) #create exception
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    if a < 10:
        data[0] = "None"# 让此数据为None
    if b < 10:
        data[1] = "None"# 让此数据为None
    if c < 10:
        data[2] = "None"# 让此数据为None
    dic["Pulse"] = data[0]
    dic["Blood_Pressure"] = data[1]
    dic["oxygen_Level"] = data[2]
    return dic
if __name__ == '__main__':
    print(main())
