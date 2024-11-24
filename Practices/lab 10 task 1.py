import random

# Create first two lists with random values
list1 = [random.randint(1, 9) for _ in range(10)]
list2 = [random.randint(1, 9) for _ in range(10)]

user_answers = []

for i in range(len(list1)):
    answer = input(f"{list1[i]} + {list2[i]} = ")
    user_answers.append(int(answer))

score = 0
incorrect_statements = []
correct_statements = []
for i in range(len(list1)):
    if user_answers[i] == list1[i] + list2[i]:
        score += 1
    else:
        incorrect_statements.append(f"{list1[i]} + {list2[i]} = {user_answers[i]}")
        correct_statements.append(f"{list1[i]} + {list2[i]} = {list1[i] + list2[i]}")

# Print the results
print("\n".join([f"{list1[i]} + {list2[i]} = {user_answers[i]}" ]))
print(f"Score {score} / {len(list1)}")
print("Incorrect\tCorrect")
for i in range(len(incorrect_statements)):
    print("\n".join([f"{incorrect_statements[i]}\t{correct_statements[i]}" ]))
