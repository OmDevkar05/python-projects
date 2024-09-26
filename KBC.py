total_winnings = 0

# Define the questions, options, correct answers, and rewards
questions = [
    ["Which is the largest continent on Earth?", "A) Africa", "B) Asia", "C) Europe", "D) North America", 'B', 10000],
    ["Who wrote the epic 'Mahabharata'?", "A) Valmiki", "B) Tulsidas", "C) Ved Vyas", "D) Kalidas", 'C', 20000],
    ["Which gas is most abundant in the Earth’s atmosphere?", "A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen",
     "D) Helium", 'C', 30000],
    ["What is the capital of France?", "A) Berlin", "B) Madrid", "C) Paris", "D) Rome", 'C', 40000],
    ["Which organ in the human body is responsible for pumping blood?", "A) Brain", "B) Liver", "C) Kidney", "D) Heart",'D', 50000],
    ["Which is the longest river in the world?", "A) Amazon", "B) Nile", "C) Ganges", "D) Yangtze", 'B', 100000],
    ["Which is the smallest planet in our solar system?", "A) Mars", "B) Mercury", "C) Venus", "D) Neptune", 'B',
     200000],
    ["In which sport is the term 'Love' used?", "A) Cricket", "B) Tennis", "C) Football", "D) Basketball", 'B', 500000],
    ["Which Indian festival is known as the 'Festival of Lights'?", "A) Holi", "B) Eid", "C) Diwali", "D) Christmas",
     'C', 1000000],
    ["Which element is represented by the symbol 'O' on the periodic table?", "A) Gold", "B) Hydrogen", "C) Oxygen",
     "D) Carbon", 'C', 68050000]
]
# Loop through each question
for i in range(len(questions)):
    q = questions[i]

    # Display the current question
    print("\nQues" + str(i + 1) + ": " + q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    # Get user's answer
    user_option = input("Enter your answer (A, B, C, D): ").upper()

    # Check if the user's answer is correct
    if user_option == q[5]:
        total_winnings += q[6]
        print("Correct! You win " + str(q[6]) + " RS. Total winnings: " + str(total_winnings))

    else:
        print("Wrong answer. You lost the game.")
        break

# For Show the final amount won
print("\n 7 करोड़🥳 Your total winnings are: " + str(total_winnings) + " RS")
