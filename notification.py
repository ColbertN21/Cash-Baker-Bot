import sched
import time
import asyncio

def notification(times):
    s = sched.scheduler(time.time, time.sleep)
    s.enter(times, 1, arbfunc)
    s.run()
    g = 1
    return g

def arbfunc():
    print("execute")
    return
