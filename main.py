# Two type of implementing of fibonacci sequence

# Use temp factor
previous_term = 1
current_term = 1
i = 0
while i < 50:
    if i == 0:
        print(f'{previous_term}')
    elif i == 1:
        print(f'{current_term}')
    else:
        term_tmp = current_term
        current_term = current_term + previous_term
        previous_term = term_tmp
        print(f'{current_term}')
    i += 1

# Use python function(?)
previous = 0
current = 1
j = 1

while j <= 50:
    print(current)
    previous, current = current, current + previous
    j += 1