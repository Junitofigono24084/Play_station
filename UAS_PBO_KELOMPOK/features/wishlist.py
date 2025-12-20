wishlist = []

def add_wishlist(games):
    title = input("Masukkan nama game ke wishlist: ").lower()

    for game in games:
        if title in game["title"].lower():
            wishlist.append(game)
            print(f"{game['title']} berhasil ditambahkan ke wishlist.")
            return

    print("Game tidak ditemukan.")

def show_wishlist():
    print("\n=== WISHLIST GAME ===")
    if not wishlist:
        print("Wishlist kosong.")
    else:
        for game in wishlist:
            print(f"- {game['title']} | Rating: {game['rating']}")
