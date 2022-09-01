import xml.etree.ElementTree as ET


class TemperatureConverter:
    def __init__(self, day, celsius) -> None:
        self.day = day
        self.celsius = celsius
        self.fahrenheit = 0

    def convert_celsius_to_fahrenheit(self):
        self.fahrenheit =  9/5 * self.celsius + 32
        print(f"{self.day}: {self.celsius} Celsius, {self.fahrenheit} Fahrenheit")


class ForecastXmlParser:
    def __init__(self) -> None:
        self.tree = ET.parse('forecast.xml')
        self.root = self.tree.getroot()

    def convert(self):
        for item in self.root.findall('item'):
            day = item[0].text
            celsius = int(item[1].text)
            converter = TemperatureConverter(day, celsius)
            converter.convert_celsius_to_fahrenheit()
    

xml = ForecastXmlParser()
xml.convert()