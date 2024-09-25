# Professor Z
# CS151 Lab 02
# Programmers: Laure and Owen

between_births = float(input('How many seconds between birth?'))
between_deaths = float(input('How many seconds between deaths?'))
between_immigration = float(input('How many seconds between immigrations?'))
current_population = float(input('What is the current population?'))
future_years = float(input('How many years are you looking into the future?'))
secs_per_year = 365 * 24 * 60 * 60
# (secs_per_year / births + secs_per_year / immigration - secs_per_year / deaths) * num_years