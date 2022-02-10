def greet(user):
    print(f"Hello {user}!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} (usernames)+")
        sys.exit(0)
    
    for user in sys.argv[1:]:
        greet(user)