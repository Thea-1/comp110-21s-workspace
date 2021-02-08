"""A vaccination calculator."""

__author__ = "730432480"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("how much is population?"))
doses_administered: int = int(input("how many doese are administered?"))
doses_per_day: int = int(input("how many doses are given per day?"))
target_percent_vaccinated: int = int(input("what is the target percent vaccinated?"))
target_population: int = round(target_percent_vaccinated / 100 * population)
vaccinated_population: int = round(doses_administered / 2)
popu_vaccinated_per_day: int = round(doses_per_day / 2) 
waiting_population: int = int(target_population - vaccinated_population)
days_needed: int = round(waiting_population / popu_vaccinated_per_day)
today: datetime = datetime.today()
end_day: datetime = timedelta(days_needed) + today
print(end_day.strftime("%B %d, %Y"))


