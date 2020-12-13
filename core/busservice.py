import copy
from typing import List, Generator
import math


class Bus():
    ID: int
    offset: int

    def __init__(self, ID: int, offset: int):
        self.ID = ID
        self.offset = offset

    def WaitTime(self, time: int) -> int:
        factor = math.ceil(time / self.ID)
        return (factor * self.ID) - time


class BusService():
    busses: List[Bus]

    def __init__(self, timetable: str):
        self.busses = []
        offset = 0
        for id in timetable.split(","):
            if id != "x":
                b = Bus(int(id), offset)
                self.busses.append(b)
            offset += 1

    def firstBusAfter(self, time) -> Bus:
        ret = None
        minwait = 99999
        for bus in self.busses:
            buswait = bus.WaitTime(time)
            if buswait < minwait:
                minwait = buswait
                ret = bus
        return ret

    def specialtime(self) -> int:
        # Solve for a bus, find time for next bus and so on until you solve for all.
        time = self.busses[0].ID - self.busses[0].offset
        increment = self.busses[0].ID
        for bus in self.busses[1:]:
            while (time + bus.offset) % bus.ID != 0:
                time += increment
            increment *= bus.ID
        return time



