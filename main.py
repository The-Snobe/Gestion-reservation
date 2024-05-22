#coding: utf-8

from restaurant import Restaurant
import datetime

def get_user_input(message, data_type=str):
    while True:
        user_input = input(message)
        try:
            return data_type(user_input)
        except ValueError:
            print("Veuillez saisir une entrée valide.")

def save_data(restaurant):
    with open(restaurant.data_file, 'w') as f:
        f.write(f"Date de sauvegarde : {datetime.datetime.now()}\n")
        f.write(f"Nombre de tables : {restaurant.num_tables}\n")
        f.write(f"Heure d'ouverture : {restaurant.opening_time}\n")
        f.write(f"Heure de fermeture : {restaurant.closing_time}\n")
        f.write("Tables :\n")
        for table, status in restaurant.tables.items():
            f.write(f"Table {table}: {status}\n")
        f.write("Réservations :\n")
        for table, reservation in restaurant.reservations.items():
            f.write(f"Table {table}: {reservation}\n")
        f.write("Menu :\n")
        for category, items in restaurant.menu.items():
            f.write(f"{category}:\n")
            for item, price in items.items():
                f.write(f"{item} - {price} FCFA\n")


def main():
    print("Bienvenue dans le système de gestion du restaurant.")

    num_tables = get_user_input("Nombre de tables dans le restaurant : ", int)
    opening_time = get_user_input("Heure d'ouverture du restaurant (format HH:MM) : ")
    closing_time = get_user_input("Heure de fermeture du restaurant (format HH:MM) : ")
    data_file = "restaurant_data.txt"  # Nom du fichier où les données seront enregistrées

    restaurant = Restaurant(num_tables, opening_time, closing_time, data_file)

    while True:
        print("\n=== Menu Principal ===")
        print("1. Afficher les tables disponibles")
        print("2. Réserver une table")
        print("3. Annuler une réservation")
        print("4. Vérifier la disponibilité d'une table")
        print("5. Vérifier une réservation")
        print("6. Afficher les réservations")
        print("7. Afficher le menu")
        print("8. Passer une commande")
        print("9. Afficher les commandes en cours")
        print("10. Générer la facture")
        print("11. Total des ventes")
        print("12. Libérer une table")
        print("13. Quitter")

        choice = get_user_input("Choix : ", int)

        if choice == 1:
            restaurant.display_available_tables()
        elif choice == 2:
            table_number = get_user_input("Numéro de la table à réserver : ", int)
            guest_name = get_user_input("Votre nom : ")
            reservation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            restaurant.make_reservation(table_number, guest_name, reservation_time)
        elif choice == 3:
            table_number = get_user_input("Numéro de la table à annuler la réservation : ", int)
            restaurant.cancel_reservation(table_number)
        elif choice == 4:
            table_number = get_user_input("Numéro de la table à vérifier : ", int)
            if restaurant.check_table_availability(table_number):
                print(f"La table {table_number} est disponible.")
            else:
                print(f"La table {table_number} est occupée.")
        elif choice == 5:
            table_number = get_user_input("Numéro de la table à vérifier : ", int)
            reservation = restaurant.check_reservation(table_number)
            if reservation:
                print(f"Réservation pour la table {table_number}: {reservation['guest_name']} - {reservation['reservation_time']}")
            else:
                print(f"Aucune réservation pour la table {table_number}.")
        elif choice == 6:
            restaurant.display_reservation()
        elif choice == 7:
            restaurant.display_menu()
        elif choice == 8:
            table_number = get_user_input("Numéro de la table pour passer la commande : ", int)
            if restaurant.check_table_availability(table_number):
                print("La table sélectionnée est disponible.")
                client_name = get_user_input("Votre nom : ")
                order = []
                while True:
                    
                    print("\nMenu du restaurant :")
                    for category, items in restaurant.menu.items():
                        print(f"\n{category}:")
                        for item, price in items.items():
                            print(f"{item} - {price} FCFA")
                    item_name = input("Nom de l'article à commander (ou appuyez sur Entrée pour terminer) : ")
                    if not item_name:
                        break
                    if item_name not in restaurant.menu['Plats'] and item_name not in restaurant.menu['Boissons'] and item_name not in restaurant.menu['Complements']:
                        print("Cet article n'est pas disponible dans le menu.")
                        continue
                    quantity = get_user_input("Quantité : ", int)
                    if item_name in restaurant.menu['Plats']:
                        item_price = restaurant.menu['Plats'][item_name]
                    elif item_name in restaurant.menu['Boissons']:
                        item_price = restaurant.menu['Boissons'][item_name]
                    else:
                        item_price = restaurant.menu['Complements'][item_name]
                    order.append({'name': item_name, 'price': item_price * quantity})
    
                    restaurant.place_order(table_number, client_name, order)
            else:
                print(f"La table {table_number} est déjà occupée.")
        elif choice == 9:
            restaurant.display_current_orders()
        elif choice == 10:
            table_number = get_user_input("Numéro de la table pour générer la facture : ", int)
            restaurant.generate_bill(table_number)
        elif choice == 11:
            restaurant.display_sales_statistics()
        elif choice == 12:
            table_number = get_user_input("Numéro de la table à libérer : ", int)
            restaurant.free_table(table_number)
        elif choice == 13:
            print("Merci d'avoir utilisé notre service de réservation.")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
            
if __name__ == "__main__":
    data_file = "restaurant_data.txt"
    
    main()
