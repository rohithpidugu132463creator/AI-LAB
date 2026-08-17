message = input("Enter your message: ").upper()

spam_words = ["win", "free", "cash", "lottery","delivery"]
ham_words = ["hello", "hi", "hey"]

is_spam = False
is_ham = False

# First, check for spam words
for word in spam_words:
    # Convert the spam word to uppercase for case-insensitive comparison
    if word.upper() in message:
        is_spam = True
        break # Found a spam word, no need to check further

# If it's not spam, then check for ham words
if not is_spam:
    for word in ham_words:
        # Convert the ham word to uppercase for case-insensitive comparison
        if word.upper() in message:
            is_ham = True
            break # Found a ham word, no need to check further

# Determine the final message type
if is_spam:
    print("Spam Message")
elif is_ham:
    print("Ham Message")
else:
    # If neither spam nor ham words were found, default to "Ham Message"
    print("Ham Message")