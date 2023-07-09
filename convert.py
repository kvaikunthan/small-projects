# Lists of bad words and their corresponding replacements
bad_words = ["dumb", "hate", "idiot", "jerk", "loser", "stupid"]
good_words = ["unintelligent", "dislike", "unintelligent person", "mean person", "runner up",
              "unintelligent"]


# Function to convert the input and print the output
def convert(input: "list") -> "list":
    if not input:  # Check if input is blank
        print("Input is empty.")
    else:
        output = []
        for word in input:
            if word in bad_words:
                index = bad_words.index(word)  # Index of the word in bad_words list
                output.append(good_words[index])  # Add word in good_words list which corresponds to the index of the
                # original word
            else:
                output.append(word)  # If it is a normal word, then add it to output as is
        print("Output:", ' '.join(output))


# Get user input and split it into a list of words
user_input = input("Enter your input: ").split()

# Call the conversion function with the user input
convert(user_input)
