# Programmers:  Laure Patera and Owen Sanchez
# Course:  CS151 05 Professor Zee
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem Statement: Finds an estimated population for a country a certain number of years into the future, along with
# telling the user whether it has increased or decreased, and what the change in population is.
# Data In: the birth rate in terms of how many seconds between births, the death rate in seconds, the rate of new
# immigrants in seconds, the current population, and how many years into the future the user wants to know the population.
# Data Out:  Whether the population has increased or decreased, and what the projected future population will be
# Credits: Code based on instructions given in README.md file

# Purpose of program is outputted to user
print('This program will calculate an estimated population for a country after a certain number of years into the future, and describe whether the population has increased or decreased.')

# User is asked to input the birth rate in terms of how many seconds between births, the death rate in seconds,
# the rate of new immigrants in seconds, the current population, and how many years into the future the user wants to
# know the population.
between_births = float(input('What is the birth rate in terms of seconds between births?'))
between_deaths = float(input('What is the death rate in terms of seconds between deaths?'))
between_immigration = float(input('What is the immigration rate in terms of seconds between immigrations?'))
current_population = float(input('What is the current population?'))
future_years = float(input('How many years into the future do you want to know the population?'))

# Calculation of seconds per year stored in this variable
secs_per_year = 365 * 24 * 60 * 60

# (secs_per_year / births + secs_per_year / immigration - secs_per_year / deaths) * num_years