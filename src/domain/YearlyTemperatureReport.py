class YearlyTemperatureReport:
    year = ""
    min_temperature = max_temperature = 0.0

    def __init__(self):
        pass

    def merge(self, raw_temperature):
        raw_temperature_entries = raw_temperature.split(',')
        self.merge_max_temperature(raw_temperature_entries[1])
        self.merge_min_temperature(raw_temperature_entries[3])
        self.year = raw_temperature_entries.split('-')[0]

    def merge_max_temperature(self, max_temperature):
        if max_temperature != "" and self.max_temperature > max_temperature:
            self.max_temperature = max_temperature

    def merge_min_temperature(self, min_temperature):
        if min_temperature != "" and self.min_temperature > min_temperature:
            self.min_temperature = min_temperature