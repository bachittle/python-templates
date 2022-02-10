def greet(user):
    """Greet a user in the command line.
    Says hi, and adds an exclamation mark to sound more excited to meet the user. 
    """
    print(f"Hello {user}!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} (usernames)+")
        sys.exit(0)
    
    for user in sys.argv[1:]:
        greet(user)