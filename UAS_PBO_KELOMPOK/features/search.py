def search_game(games):
    keyword = input("Masukkan nama game: ").lower()
    found = False

    for game in games:
        if keyword in game["title"].lower():
            print(f"Ditemukan: {game['title']} | Genre: {game['genre']} | Rating: {game['rating']}")
            found = True

    if not found:
        print("Game tidak ditemukan.")
