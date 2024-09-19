# Professor Z
# CS151 Lab 02
# Programmers: Laure and Owen

between_births = print('How many seconds between birth?'),int(input())
between_deaths = print('How many seconds between deaths'),int(input())
between_immigration = print('How many seconds between immigration'),int(input())
population = print('What is the current population'),int(input())
future_years = print('How many years in the future'),int(input())
secs_per_year = 365*24*60
# (secs_per_year / births + secs_per_year / immigration - secs_per_year / deaths) * num_years