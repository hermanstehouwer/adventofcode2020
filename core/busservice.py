import copy
from typing import List, Generator
import math


class Bus:
    ID: int
    offset: int

    def __init__(self, ID: int, offset: int):
        self.ID = ID
        self.offset = offset

    def WaitTime(self, time: int) -> int:
        factor = math.ceil(time / self.ID)
        return (factor * self.ID) - time


class BusService:
    busses: List[Bus]

    def __init__(self, timetable: str):
        self.busses = [Bus(int(id), i)
                       for i, id in enumerate(timetable.split(","))
                       if id != "x"]

    def firstBusAfter(self, time) -> Bus:
        return next(iter(sorted(self.busses, key=lambda bus: bus.WaitTime(time))))

    def specialtime(self) -> int:
        # Solve for a bus, find time for next bus and so on until you solve for all.
        time, increment = 1, 1
        for bus in self.busses:
            while (time + bus.offset) % bus.ID != 0:
                time += increment
            increment *= bus.ID
        return time



