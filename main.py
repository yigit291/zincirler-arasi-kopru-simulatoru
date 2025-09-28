# İki farklı blokzincir arasında token transferi mantığını simüle eder.

# Zincirlerdeki bakiye durumlarını temsil edelim
chain_a_balances = {'user1': {'TOKEN': 100}}
chain_b_balances = {'user1': {'WRAPPED_TOKEN': 0}}

def bridge_tokens(user, amount):
    print(f"--- Köprüleme Başladı: {user}, {amount} TOKEN ---")

    # 1. Adım: Zincir A'da tokenları kilitle
    if chain_a_balances[user]['TOKEN'] >= amount:
        chain_a_balances[user]['TOKEN'] -= amount
        print(f"Adım 1: Zincir A'da {amount} TOKEN kilitlendi.")

        # 2. Adım: Zincir B'de sarılmış (wrapped) tokenları mintle
        chain_b_balances[user]['WRAPPED_TOKEN'] += amount
        print(f"Adım 2: Zincir B'de {amount} WRAPPED_TOKEN mintlendi.")
    else:
        print("Hata: Zincir A'da yeterli bakiye yok.")

    print("--- Köprüleme Tamamlandı ---")

if __name__ == "__main__":
    print("Başlangıç Durumu:")
    print(" - Zincir A:", chain_a_balances)
    print(" - Zincir B:", chain_b_balances)

    bridge_tokens('user1', 70)

    print("\nSon Durum:")
    print(" - Zincir A:", chain_a_balances)
    print(" - Zincir B:", chain_b_balances)