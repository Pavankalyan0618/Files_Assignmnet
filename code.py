import os
import json
import pandas as pd

def read_json():
    
    try:
        folder = input("Enter the folder name where the JSON file is located: ")
        file_name = "Pavan-Kalyan-Pendyala_adoptions.json" 
        file_path = os.path.join(folder, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found:",file_path)
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError as e:
        print(e)
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
        return None
    except Exception as e:
        print("An unexpected error occurred:",e)
        return None
    

data = read_json()

def save_contacts_to_csv(data):
    contacts = []
    for record in data:
        for contact in record['contacts']:
            contacts.append({
                "Adoption ID": record['id'],
                "Order": contact['order'],
                "First Name": contact['firstname'],
                "Last Name": contact['lastname'],
                "Gender": contact['gender']
            })
    contacts_df = pd.DataFrame(contacts)
    contacts_df.to_csv('contacts.csv', index=False)
    print("Contacts saved to contacts.csv")
    print(contacts_df)

save_contacts_to_csv(data)