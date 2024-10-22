def konversisuhu(temperature, value):
    if value == 'c':
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu,'c'
    else:
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'f'
    
celsius_temperature = 30
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'f')
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

fahrenheit_temperature = 86
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'c')
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}")   