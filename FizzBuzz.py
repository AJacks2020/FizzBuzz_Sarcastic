import time

# Sets the value that FizzBuzz is to be played up to
count_up_to = 40000

### NORMAL BUZZFIZZ EXPERIMENT ###

normal_start_time = time.time()

# Loops over every positive integer less than the desired count_up_to value
for integer in range(1, count_up_to + 1):

    # Computes if integer is a multiple of three and/or five
    is_mult_three, is_mult_five = integer%3 < 1, integer%5 < 1

    # Constructs the output string corresponding to integer
    output_string = "Fizz"*is_mult_three + "Buzz"*is_mult_five or integer

    print(output_string)
        
normal_end_time = time.time()

# Gives the computer some time to cool down, to mimimize the effect of heat on the results
time.sleep(35)


### COMPRESSED BUZZFIZZ EXPERIMENT ### This code is repeated to clearly seperate the two experiments and show there's nothing else that could be influencing the runtime.

compre_start_time = time.time()

# Loops over every positive integer less than the desired count_up_to value
for integer in range(1, count_up_to + 1):

    # Computes if integer is a multiple of three and/or five
    is_mult_three, is_mult_five = integer%3 < 1, integer%5 < 1

    # Constructs the output string corresponding to integer
    output_string = "F"*is_mult_three + "B"*is_mult_five or integer

    print(output_string)
        
compre_end_time = time.time()

print("--- The normal FizzBuzz took %s seconds ---" %(normal_end_time- normal_start_time ))
print("--- The compressed FizzBuzz took %s seconds ---" %(compre_end_time- compre_start_time ))
