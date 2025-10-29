
phrases = ["get over here!", "it's a home run!", "strike three you're out!"]
new_received_messages = []

def send_messages(phrases, new_received_messages):
    """ Print phrases and remove from phrases list"""
    while phrases:
        new_phrase = phrases.pop()
        print(f"\nThe phrase: ({new_phrase}) has been moved.")
        new_received_messages.append(new_phrase)

def received_messages(new_received_messages):
    """Show completed messages added to sent_messages"""
    for message in new_received_messages:
        print("\n--- Incoming Message---")
        print(f"The following phrase has been received: \n\t{message}")

#Added to retain original list (Phrases)
send_messages(phrases[:], new_received_messages)
received_messages(new_received_messages)

#Print Lists to prove items have been moved to the other list
print(f"\n{new_received_messages}")
print(f"\n{phrases}")