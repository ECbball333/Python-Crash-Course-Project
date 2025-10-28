users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'location_state': 'New Jersey',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'location_country': 'france',
        },
    'econner': {
        'first': 'elliot',
        'last': 'conner',
        'location': 'fort mill',
        'location_state': 'south carolina',
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")