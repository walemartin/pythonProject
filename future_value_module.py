from datetime import datetime, timedelta
from dateutil.relativedelta import *

date=datetime.now()
def calculate_future_value(monthly_investment,yearly_interest,years):
    print("Entering calculate future value method")
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(1,months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
        print("Tenor =",(date + relativedelta(months=+i)).date()," future amount = ",round(future_value,2))

    return future_value