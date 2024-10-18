from dbOperations import add_feature, get_features_by_country, delete_feature_by_id, update_feature_active_status
def main():
    while True:
        command = input("Enter command (add, get, delete, update, exit): ")
         
        # Ввод данных для новой записи
        if command == "add":
            data = {
                'country': input("Country: "),
                'network': input("Network: "),
                'mcc_mnc': input("MCC MNC: "),
                'vendor': input("Vendor: "),
                'vendor_product': input("Vendor Product: "),
                'necessary_information': input("Necessary Information: "),
                'features': input("Features: "),
                'primary_contact': input("Primary Contact: "),
                'additional_contact': input("Additional Contact: "),
                'eta_for_registration': input("ETA for Registration: "),
                'registration_window': input("Registration Window: "),
                'am_to_confirm_notify': input("AM to Confirm & Notify: "),
                'fees_for_client': input("Fees for Client: "),
                'fees_for_us': input("Fees for Us: "),
                'necessary_tag': input("Necessary Tag: "),
                'is_active': True
            }
            add_feature(data)

        # Получение данных по названию страны
        elif command == "get":
            country = input("Enter country: ")
            results = get_features_by_country(country)
            for feature in results:
                print(f"id: {feature.id}| features: {feature.features}| country: {feature.country}\n")
                print(f"id: {feature.id}| network: {feature.network}")
                print(f"id: {feature.id}| mcc_mnc:  {feature.mcc_mnc}")
                print(f"id: {feature.id}| vendor:  {feature.vendor}")
                print(f"id: {feature.id}| vendor_product:  {feature.vendor_product}")
                print(f"id: {feature.id}| necessary_information:  {feature.necessary_information}")
                print(f"id: {feature.id}| primary_contact:  {feature.primary_contact}")
                print(f"id: {feature.id}| additional_contact:  {feature.additional_contact}")
                print(f"id: {feature.id}| eta_for_registration:  {feature.eta_for_registration}")
                print(f"id: {feature.id}| registration_window:  {feature.registration_window}")
                print(f"id: {feature.id}| am_to_confirm_notify:  {feature.am_to_confirm_notify}")
                print(f"id: {feature.id}| fees_for_client:  {feature.fees_for_client}")
                print(f"id: {feature.id}| fees_for_us:  {feature.fees_for_us}")
                print(f"id: {feature.id}| necessary_tag:  {feature.necessary_tag}")

        # Удаление записи по id
        elif command == "delete":
            feature_id = int(input("Enter feature ID to delete: "))
            delete_feature_by_id(feature_id)
        
        # Обновление поля актуальности по id записи
        elif command == "update":
            feature_id = int(input("Enter feature ID to update: "))
            is_active = input("Set active status (true/false): ").lower() == 'true'
            update_feature_active_status(feature_id, is_active)
        # Завершение работы программы
        elif command == "exit":
            break

if __name__ == "__main__":
    main()