class YearlyTemperatureReport:
    year = ""
    min_temperature = max_temperature = 0.0

    def __init__(self):
        pass

    def __init__(self, year, min_temperature, max_temperature):
        self.year = year
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature
