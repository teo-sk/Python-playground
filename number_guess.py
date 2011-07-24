import random

cfg_range_start = 1
cfg_range_stop = 100
cfg_attempts = 10

print "Lemme think a number"
print "\nIt's between ", cfg_range_start, " and ", cfg_range_stop,". Guess it!"
print "You have", cfg_attempts, "attempts"

number = random.randrange(cfg_range_stop) + cfg_range_start

attempts = 1
guess = int(raw_input("Your guess: "))

while guess != number and attempts !=cfg_attempts:
    if guess < number:
        print "Your guess is too low"
    if guess > number:
        print "Your guess is too high"
    print "You have ", cfg_attempts - attempts," guesses left"
    attempts += 1
    guess = int(raw_input("Your guess: "))
    
if guess is number:
    print "You won"
else:
    print "You lost, sucker."
print "The number was ", number , "."
