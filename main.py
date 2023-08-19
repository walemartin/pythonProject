import temperature,future_value_module
import random

number=random.randint(-4 , 15)

f=temperature.to_fahrenheit(number)
print("Temperature is :",f)
temperature.main()

future_value_module.calculate_future_value(100,12,1)