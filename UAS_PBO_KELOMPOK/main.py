from data.games import games
from data.consoles import consoles
from utils.menu import show_menu
from features.search import search_game
from features.wishlist import add_wishlist, show_wishlist

def show_games():
    print("\n=== DAFTAR GAME PLAYSTATION ===")
    for i, game in enumerate(games, start=1):
        print(f"{i}. {game['title']} | Genre: {game['genre']} | Rating: {game['rating']}")

def show_consoles():
    print("\n=== DAFTAR KONSOL PLAYSTATION ===")
    for console in consoles:
        print(f"- {console['name']} ({console['year']})")

while True:
    show_menu()
    choice = input("Pilih menu: ")

    if choice == "1":
        show_games()
    elif choice == "2":
        show_consoles()
    elif choice == "3":
        search_game(games)
    elif choice == "4":
        add_wishlist(games)
    elif choice == "5":
        show_wishlist()
    elif choice == "0":
        print("Terima kasih telah menggunakan PlayStation Hub!")
        break
    else:
        print("Pilihan tidak valid!")
