# models.py
class MeterReading:
    def __init__(self, timestamp, kwh):
        self.timestamp = timestamp
        self.kwh = kwh

class Building:
    def __init__(self, name):
        self.name = name
        self.meter_readings = []

    def add_reading(self, meter_reading):
        self.meter_readings.append(meter_reading)

    def calculate_total_consumption(self):
        return sum(r.kwh for r in self.meter_readings)

    def generate_report(self):
        total = self.calculate_total_consumption()
        return {"building": self.name, "total_kwh": total}

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def add_from_dataframe(self, df):
        # loop rows, create / reuse Building, add MeterReading
        ...
