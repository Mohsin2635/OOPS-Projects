class TemperatureConvertor:
    @staticmethod
    def celcius_to_farhenheit(celcius):
        Farhenheit = (celcius * 9 / 5) + 32
        return Farhenheit

print(TemperatureConvertor().celcius_to_farhenheit(33))