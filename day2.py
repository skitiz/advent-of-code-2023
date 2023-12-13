# Read a file in.
sumOfIdx = 0
powerOfCubes = 0
maxValues = {"red": 12, "green": 13, "blue": 14 }
with open('./files/day2.txt', 'r') as f:
    lines = f.readlines()
    # For each line in the file, split the string into two parts based on a colon.
    for line in lines:
        parts = line.split(':')
        # Now we split the second part based on ;
        rules = parts[1].split(';')
        validCombo = True
        minimumCubes = {"red": 0, "green": 0, "blue": 0}
        for rule in rules:
            # Split the rule based on a comma.
            combinations = rule.split(',')

            # For each combination, check if the number is greater than the max value for that color.
            for combination in combinations:
                number, color = combination.split()
                if int(number) > maxValues[color]:
                    validCombo = False
                
                # Check if the number is greater than the minimum number of cubes for that color.
                if int(number) > minimumCubes[color]:
                    minimumCubes[color] = int(number)
        
        # Add the multiplication of each of the minimum cubes to each other to the powerOfCubes.
        powerOfCubes += minimumCubes["red"] * minimumCubes["green"] * minimumCubes["blue"]
            
        if validCombo:
            sumOfIdx += int(parts[0])

print(sumOfIdx)
print(powerOfCubes)