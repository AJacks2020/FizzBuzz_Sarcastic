import time

def play_FizzBuzz(play_until, divis_by_three_string, divis_by_five_string):
    '''
        INPUTS
        play_until            : The integer the function will play BuzzFizz up to (inclusive) : int
        divis_by_three_string : The stirng to print if a number is divisible by three         : String
        divis_by_five_string  : The stirng to print if a number is divisible by five          : String

        RETURNS
        none

        SIDE EFFECT
        prints a game of BuzzFizz up to the desired number, using the specified strings
    '''

    # Loops over every positive integer less than (or equal to) the specified max value
    for integer in range(1, play_until + 1):

        # Computes if integer is a multiple of three and/or five
        is_mult_three, is_mult_five = integer%3 < 1, integer%5 < 1

        # Constructs the output string corresponding to integer: either Buzz, Fizz, or - if neither are needed - integer itself
        output_string = divis_by_three_string*is_mult_three + divis_by_five_string*is_mult_five or integer

        print(output_string)


### SETUP FOR THE EXPERIMENTS ###

# Sets the value that FizzBuzz is to be played up to
count_up_to = 40000 #Number just chosen to be large enough to give significant runtime differences

# Defines the experiements to run by specifying the strings for each experiment
printing_strings = [["Fizz", "Buzz"], ["F", "B"]]

# Sets up an array to hold the runtimes of the experiments
runtimes = []

### RUNS THE EXPERIMENTS ###

for experiment_index in [0,1]:
    
    # Starts the clock for the current experiment
    runtimes.append(time.time())
    
    # Runs the required game of BuzzFizz
    play_FizzBuzz(count_up_to, printing_strings[experiment_index][0], printing_strings[experiment_index][1])

    # Stops the clock for the current experiment
    runtimes[experiment_index] -= time.time()

    # Adds a pause between the two experiments to mitigate the potential effects of heat
    if(not experiment_index): 
        time.sleep(30)


time.sleep(2) #Pause for dramatic effect
print(" --- The normal FizzBuzz game took %s times as long as the 'compressed' FizzBuzz game --- " %(runtimes[0] / runtimes[1]))
