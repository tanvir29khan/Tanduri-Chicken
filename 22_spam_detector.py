spam_words_list = [
    "buy now",
    "limited time offer",
    "click here",
    "free gift",
    "urgent",
    "act fast",
    "exclusive deal",
    "risk-free",
    "guaranteed",
    "no strings attached",
    "money back",
    "unbeatable price",
]

user_comments = input("Enter your comments: ").lower()

if any(spam_word in user_comments for spam_word in spam_words_list):
    print("Your comment contains spam words.")

else:
    print("Your comment is clean and does not contain spam words.")




    