class Restaurant:
    def __init__(self, num_tables, opening_time, closing_time, data_file):
        self.num_tables = num_tables
        self.tables = {table_number: None for table_number in range(1, num_tables + 1)}
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.reservations = {}
        self.menu = {'Plats': {'Salade': 5000, 'Soupe': 3000, 'Pâtes': 8000, 'Grillades': 10000},
                     'Boissons': {'Eau minérale': 500, 'Jus': 1000, 'Thé': 500, 'Café': 700},
                     'Complements': {'Frites natures': 500, 'Frites épicées': 500}}
        self.data_file = data_file

    def display_menu(self):
        print("Menu du restaurant :")
        for category, items in self.menu.items():
            print(f"\n{category}:")
            for item, price in items.items():
                print(f"{item} - {price} FCFA")

    def display_available_tables(self):
        available_tables = [table for table, status in self.tables.items() if status is None]
        if available_tables:
            print("Tables disponibles :", available_tables)
        else:
            print("Aucune table disponible.")

    def make_reservation(self, table_number, guest_name, reservation_time):
        if table_number not in self.tables:
            print("La table spécifiée n'existe pas.")
            return

        if self.tables[table_number] is None:
            self.tables[table_number] = guest_name
            self.reservations[table_number] = {'guest_name': guest_name, 'reservation_time': reservation_time}
            print(f"Réservation effectuée pour la table {table_number} au nom de {guest_name}.")
        else:
            print(f"La table {table_number} est déjà réservée.")

    def cancel_reservation(self, table_number):
        if table_number not in self.tables:
            print("La table spécifiée n'existe pas.")
            return

        if self.tables[table_number] is not None:
            cancelled_guest = self.tables.pop(table_number)
            cancelled_reservation = self.reservations.pop(table_number)
            print(f"Réservation annulée pour la table {table_number} au nom de {cancelled_guest}.")
        else:
            print(f"La table {table_number} n'a pas de réservation.")

    def check_table_availability(self, table_number):
        return self.tables.get(table_number) is None

    def check_reservation(self, table_number):
        return self.reservations.get(table_number)

    def display_reservation(self):
        print("Liste des réservations:")
        for table, reservation in self.reservations.items():
            print(f"Table {table}: {reservation['guest_name']} - {reservation['reservation_time']}")

    def place_order(self, table_number, client_name, order):
        if table_number not in self.tables:
            print("La table spécifiée n'existe pas.")
            return

        if self.tables[table_number] is not None:
            print(f"La table {table_number} est déjà réservée.")
            return

        if not order:
            print("La commande est vide.")
            return

        self.tables[table_number] = {'client_name': client_name, 'order': []}  # Initialiser order comme une liste vide
        for item in order:
            self.tables[table_number]['order'].append(item)  # Ajouter les articles de la commande
        print(f"Commande placée pour {client_name} à la table {table_number}.")


    def display_current_orders(self):
        print("Commandes en cours :")
        for table, order in self.tables.items():
            if order:
                client_name = order['client_name']
                items = order['order']
                print(f"Table {table} - {client_name}:")
                for item in items:
                    print(f"\t{item['name']} - {item['price']} FCFA")
            else:
                print(f"Table {table} - Libre")
    def generate_bill(self, table_number):
        if table_number not in self.tables:
            print("La table spécifiée n'existe pas.")
            return

        if not self.tables[table_number]:
            print("La table n'a pas de commande.")
            return

        total_price = sum(item['price'] for item in self.tables[table_number]['order'])
        print(f"Facture pour la table {table_number} : {total_price} FCFA")
    def display_sales_statistics(self):
        print("Statistiques de ventes :")
        total_sales = {'Plats': 0, 'Boissons': 0, 'Complements': 0}

        for table, order in self.tables.items():
            if order and isinstance(order, dict):  # Vérifiez si order est un dictionnaire
                items = order['order']
                for item in items:
                    for category, menu_items in self.menu.items():
                        if item['name'] in menu_items:
                            total_sales[category] += item['price']

        for category, sales in total_sales.items():
            print(f"{category}: {sales} FCFA")
    def free_table(self, table_number):
        if table_number not in self.tables:
            print("La table spécifiée n'existe pas.")
            return

        if self.tables[table_number] is None:
            print(f"La table {table_number} est déjà libre.")
            return

        print(f"La table {table_number} a été libérée.")
        self.tables[table_number] = None

def get_user_input(message, data_type=str):
    while True:
        user_input = input(message)
        try:
            return data_type(user_input)
        except ValueError:
            print("Veuillez saisir une entrée valide.")
def save_data(self):
        with open(self.data_file, 'w') as f:
            f.write(f"Date de sauvegarde : {datetime.datetime.now()}\n")
            f.write(f"Nombre de tables : {self.num_tables}\n")
            f.write(f"Heure d'ouverture : {self.opening_time}\n")
            f.write(f"Heure de fermeture : {self.closing_time}\n")
            f.write("Tables :\n")
            for table, status in self.tables.items():
                f.write(f"Table {table}: {status}\n")
            f.write("Réservations :\n")
            for table, reservation in self.reservations.items():
                f.write(f"Table {table}: {reservation}\n")
            f.write("Menu :\n")
            for category, items in self.menu.items():
                f.write(f"{category}:\n")
                for item, price in items.items():
                    f.write(f"{item} - {price} FCFA\n")

