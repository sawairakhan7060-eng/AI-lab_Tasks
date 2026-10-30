class SmartAC:
    def __init__(self):
        self.last_mode = None

    def control_ac(self, occupied, temp):
        previous = self.last_mode

        if occupied:
            if temp < 18:
                target = "HEAT"
            elif temp > 28:
                target = "COOL"
            else:
                target = "OFF"
        else:
            target = "OFF"

        if target == previous:
            status = "No Command"
        else:
            status = "Send Command"

        self.last_mode = target

        return previous, target, status


ac = SmartAC()

readings = [
    (True, 16),
    (True, 16),
    (True, 26),
    (True, 28),
    (True, 30),
    (True, 23),
    (False, 23)
]

for occupied, temp in readings:
    old, current, result = ac.control_ac(occupied, temp)

    print(f"Previous Mode: {old} | Temperature: {temp} | "
          f"Occupied: {occupied} | Target Mode: {current} | Action: {result}")