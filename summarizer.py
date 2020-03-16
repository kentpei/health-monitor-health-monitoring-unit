import time

class ICU_Monitor:
    def __init__(interval):
        self.interval = interval
        pass

    def timer_run(self.interval):
        time_counter = 0
        while 1:
            try:
                time.sleep(self.interval)

                # if message from (Datacollect) is [abnormal]:
                    # send data from (Datacollect) to (Alarm) / run (Alarm)

                # send data from (Generator) to (Datacollect)

                # send data from (Datacollect) to (Monitor) / run (Monitor)

                # save data from (Datacollect) to (DataBase)

                # send data from (DataBase) to (Predictor)

                time_counter += 1
            except:
                break
        return time_counter

Monitor0 = ICU_Monitor()

Monitor0.timer_run(0.5)
"""
    expected result:
    each 0.5 second print:
        Time Now: xxx
        Pulse: xxx
        Blood Pressure: xxx
        Oxygen: xxx
        Status: [Safe / Alert]
        Pridicted Status in next 30 seconds: [Safe /Alert]
"""



