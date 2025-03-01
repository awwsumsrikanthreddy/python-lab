#type1
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
pick = random.choice(friends)
print(pick)

#type2

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_gen = random.randint(0,4)
print(friends[random_gen])

#type 3
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
picks = random.choices(friends, k=3)  # Picks 3 random friends (duplicates possible)
print(picks)
