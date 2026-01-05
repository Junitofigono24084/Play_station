import json
import os

# ================= DATA (Tersimpan di variabel) =================
games = [
    {"title": "God of War Ragnarok", "genre": "Action", "rating": 4.9, "price": 879000},
    {"title": "Spider-Man 2", "genre": "Adventure", "rating": 4.8, "price": 1029000},
    {"title": "Elden Ring", "genre": "RPG", "rating": 4.7, "price": 599000},
    {"title": "Final Fantasy VII Rebirth", "genre": "RPG", "rating": 4.9, "price": 1029000},
    {"title": "Gran Turismo 7", "genre": "Racing", "rating": 4.5, "price": 879000},
]

consoles = [
    {"name": "PlayStation 5 Digital Edition", "year": 2020, "price": 8199000},
    {"name": "PlayStation 5 Standard", "year": 2020, "price": 9699000},
    {"name": "PlayStation 4 Pro", "year": 2016, "price": 4500000},
]

FILE_WISHLIST = "wishlist_data.json"

# ================= UTILS & FEATURES =================

def load_wishlist():
    if os.path.exists(FILE_WISHLIST):
        with open(FILE_WISHLIST, "r") as f:
            return json.load(f)
    return []

def save_wishlist(data):
    with open(FILE_WISHLIST, "w") as f:
        json.dump(data, f, indent=4)

def show_menu():
    print("\n" + "="*30)
    print("      PLAYSTATION HUB")
    print("="*30)
    print("1. Lihat Daftar Game")
    print("2. Lihat Daftar Konsol")
    print("3. Cari Game")
    print("4. Tambah ke Wishlist")
    print("5. Lihat Wishlist Saya")
    print("0. Keluar")
    print("="*30)

def show_games():
    print("\n=== DAFTAR GAME PLAYSTATION ===")
    print(f"{'No':<3} | {'Judul Game':<25} | {'Genre':<10} | {'Harga':<12}")
    print("-" * 60)
    for i, game in enumerate(games, start=1):
        print(f"{i:<3} | {game['title']:<25} | {game['genre']:<10} | Rp{game['price']:,}")

def show_consoles():
    print("\n=== DAFTAR KONSOL PLAYSTATION ===")
    for console in consoles:
        print(f"- {console['name']} ({console['year']}) | Rp{console['price']:,}")

def search_game():
    query = input("\nMasukkan judul game yang dicari: ").lower()
    found = [g for g in games if query in g['title'].lower()]
    
    if found:
        print(f"\nHasil ditemukan ({len(found)}):")
        for g in found:
            print(f"- {g['title']} | Rating: {g['rating']}")
    else:
        print("\nGame tidak ditemukan.")

def add_to_wishlist():
    show_games()
    try:
        pilihan = int(input("\nNomor game yang ingin ditambah ke wishlist: "))
        if 1 <= pilihan <= len(games):
            selected = games[pilihan-1]
            current_wishlist = load_wishlist()
            
            # Cek duplikat
            if any(item['title'] == selected['title'] for item in current_wishlist):
                print(f"--- {selected['title']} sudah ada di wishlist! ---")
            else:
                current_wishlist.append(selected)
                save_wishlist(current_wishlist)
                print(f"--- Berhasil menambah {selected['title']} ke wishlist! ---")
        else:
            print("Pilihan tidak tersedia.")
    except ValueError:
        print("Error: Masukkan angka saja!")

def show_my_wishlist():
    data = load_wishlist()
    print("\n=== WISHLIST SAYA ===")
    if not data:
        print("Wishlist kamu masih kosong.")
    else:
        total = 0
        for i, item in enumerate(data, start=1):
            print(f"{i}. {item['title']} - Rp{item['price']:,}")
            total += item['price']
        print("-" * 30)
        print(f"Total Estimasi: Rp{total:,}")

# ================= MAIN PROGRAM =================

def main():
    while True:
        show_menu()
        choice = input("Pilih menu (0-5): ")

        if choice == "1":
            show_games()
        elif choice == "2":
            show_consoles()
        elif choice == "3":
            search_game()
        elif choice == "4":
            add_to_wishlist()
        elif choice == "5":
            show_my_wishlist()
        elif choice == "0":
            print("\nTerima kasih telah menggunakan PlayStation Hub! Sampai jumpa.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
