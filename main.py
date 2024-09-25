# Programmers:  Laure Patera and Owen Sanchez
# Course:  CS151 05 Professor Zee
# Due Date: 9/25/2024
# Lab Assignment: 2
# Problem Statement: Finds an estimated population for a country a certain number of years into the future, along with
# telling the user whether it has increased or decreased, and what the change in population is.
# Data In: Seconds between births, seconds between deaths, seconds between immigrations, current population, and years
# into the future
# Data Out:  Whether the population has increased or decreased, the change in population, and what the projected future
# population will be
# Credits: Code based on instructions given in README.md file

# User is asked to input seconds between births, seconds between deaths, seconds between immigrations, current
# population, and years into the future
between_births = float(input('How many seconds between birth?'))
between_deaths = float(input('How many seconds between deaths?'))
between_immigration = float(input('How many seconds between immigrations?'))
current_population = float(input('What is the current population?'))
future_years = float(input('How many years are you looking into the future?'))

# Calculation of seconds per year stored in this variable
secs_per_year = 365 * 24 * 60 * 60

# (secs_per_year / births + secs_per_year / immigration - secs_per_year / deaths) * num_years