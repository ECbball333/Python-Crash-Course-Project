def make_shirt(shirt_size = 'large', shirt_text = 'I love python'):
    """Design a new shirt type"""
    print(f"\nMy shirt is a {shirt_size}.")
    print(f'"{shirt_text}", should be the text.')

make_shirt()
make_shirt('medium')
make_shirt('small', 'Learn Python!')