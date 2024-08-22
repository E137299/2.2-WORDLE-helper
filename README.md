# 2.2 WORDLE Helper

## Objective:
In this assignment, you'll develop a program to assist with Wordle puzzles. The program will take a user's guessed word and the scoring results to help narrow down potential solutions from a word bank.

## Instructions:
1. **Import Word Bank:**
    - The New York Times' word bank is provided to you. 
2. **User Input for the Guess:**
    - Write a function get_guess() that prompts the user to input their guessed word. Ensure that the input is exactly 5 letters long and only contains alphabetic characters. If the input is invalid, prompt the user again until they provide a valid guess.
3. **User Input for the Scoring:**
    - Write a function get_score() that prompts the user to input the score for their guess. The score should be a 5-character string containing only the characters "G", "Y", and "X".
    - Validate the input to ensure it matches the required format. If the input is invalid, prompt the user again.
4. **Writing Helper Functions to Filter the Word Bank:**
    - Write the following four helper functions to filter the word_bank:

        - contains_letter(word_bank, letter):

            This function should return a list of words from the word_bank that contain the specified letter anywhere in the word.
        - does_not_contain_letter(word_bank, letter)

            This function should return a list of words from the word_bank that do not contain the specified letter at all.
        - letter_at_position(word_bank, letter, position)

            This function should return a list of words from the word_bank where the specified letter is at the exact position (0-based index).
        - letter_not_at_position(word_bank, letter, position)

            This function should return a list of words from the word_bank where the specified letter is not at the given position (0-based index).
    - These helper functions will be essential for filtering the word bank based on the user’s input.

5. **Filtering the Word Bank:**

    - Write a function filter_word_bank(word_bank, guess, score) that takes the word_bank, the user's guess, and the score as inputs.
    - This function should use the helper functions above to return a new list of words from the word_bank that match the given score criteria:
        - If the score is "G", use letter_at_position() to filter words where the corresponding letter is in the exact position.
        - If the score is "Y", use both contains_letter() and letter_not_at_position() to filter words where the letter is present but not in the specified position.
        - If the score is "X", use does_not_contain_letter() to filter out words that contain the corresponding letter.
6. **Testing the Program:**

Test your program by running it multiple times with different guesses and scores. After each round, print out the filtered list of potential words from the word_bank.
Example Interaction:
python
Copy code
# Example Interaction

Word Bank: ['apple', 'grape', 'lemon', 'berry', 'mango']

Enter your guess: apple
Enter the score (G/Y/X): GXYYY

Filtered Word Bank: ['grape']
Part 2: Enhancing the Wordle Helper
Instructions:
Looping for Multiple Rounds:

Modify your program to loop, allowing the user to guess and score multiple times. After each round, update the word_bank with the filtered list of words.
Displaying Remaining Words:

After each guess, display the remaining possible words in the word_bank. If only one word remains, inform the user that the word has been found.
Ending the Program:

The program should end either when the user finds the correct word (when only one word remains) or when the user decides to quit.
Add an option for the user to exit the program after each round.
Handling Edge Cases:

Consider edge cases, such as when no words match the given criteria. In this case, inform the user that no words fit the criteria and prompt them to start over or exit.
Optional Enhancements:

Allow the user to reset the word bank and start a new game.
Implement a feature to randomly generate a word bank from a larger list of words.
Example Interaction:
python
Copy code
# Example Interaction

Word Bank: ['apple', 'grape', 'lemon', 'berry', 'mango']

Enter your guess: mango
Enter the score (G/Y/X): GGXXX

Filtered Word Bank: ['mango']

Word found: mango
Part 3: Word Scoring Based on Letter Frequency
Instructions:
Letter Frequency Analysis:

Write a function letter_frequency(word_bank) that takes the current word_bank (a list of remaining possible words) as input and returns a dictionary where:
The keys are individual letters (from 'a' to 'z').
The values are the number of words in the word_bank that contain that letter at least once.
Scoring the Words:

Write a function score_words(word_bank, letter_freq) that takes the word_bank and the letter_freq dictionary as inputs.
This function should return a new dictionary where:
The keys are the words from the word_bank.
The values are the scores for each word, calculated by summing the frequency values of each letter in the word (from the letter_freq dictionary).
Ordering the Words:

Write a function order_words_by_score(word_scores) that takes the word_scores dictionary as input and returns a list of words ordered from highest to lowest score.
Integration with the Wordle Helper:

After each round of guessing and filtering the word_bank, perform the letter frequency analysis and score the remaining words.
Display the ordered list of words based on their scores to help guide the next guess.
Testing Your Enhanced Program:

Test your enhanced program by running it with different guesses and checking how the word bank is updated and how the words are scored and ordered.
Example Interaction:
python
Copy code
# Example Interaction

Word Bank: ['apple', 'grape', 'lemon', 'berry', 'mango']

Enter your guess: apple
Enter the score (G/Y/X): GXYYY

Filtered Word Bank: ['grape', 'lemon']

Letter Frequency:
{'a': 1, 'e': 2, 'g': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 0, 'r': 2}

Word Scores:
grape: 8
lemon: 7

Ordered Words:
['grape', 'lemon']
