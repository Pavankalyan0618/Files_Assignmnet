import os
import json
import pandas as pd

def read_json():
    
    try:
        folder = input("Enter the folder name where the JSON file is located: ")
        file_name = "Pavan_Kalyan_Pendyala_adoptions.json" 
        file_path = os.path.join(folder, "Pavan_Kalyan_Pendyala_adoptions.json")
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

def save_universities_to_csv(data):
    universities = []
    for record in data:
            if 'address' not in record['university']:
                universities.append({
                "Adoption ID": record['id'],
                "University ID": record['university']['id'],
                "University Name": record['university']['name'],
                "University Address": "N/A",
                "University City": record['university']['city'],
                "University State": record['university']['state'],
                "University ZIP": record['university']['zip'],
                "University Longitude": record['university']['longitude'],
                "University Latitude": record['university']['latitude'],
                "University Classification": record['university']['classification'],
                "University Website": record['university']["website"]
                })
            elif 'website' not in record['university']:
                universities.append({
                "Adoption ID": record['id'],
                "University ID": record['university']['id'],
                "University Name": record['university']['name'],
                "University Address": "record['university']['address']",
                "University City": record['university']['city'],
                "University State": record['university']['state'],
                "University ZIP": record['university']['zip'],
                "University Longitude": record['university']['longitude'],
                "University Latitude": record['university']['latitude'],
                "University Classification": record['university']['classification'],
                "University Website": "N/A"
                })

            else:
             universities.append({
                "Adoption ID": record['id'],
                "University ID": record['university']['id'],
                "University Name": record['university']['name'],
                "University Address": record['university']['address'],
                "University City": record['university']['city'],
                "University State": record['university']['state'],
                "University ZIP": record['university']['zip'],
                "University Longitude": record['university']['longitude'],
                "University Latitude": record['university']['latitude'],
                "University Classification": record['university']['classification'],
                "University Website": record['university']["website"]
             })
    universities_df = pd.DataFrame(universities)
    universities_df.to_csv('universties.csv', index=False)
    print("Universiies Information saved to universities.csv")
    print(universities_df)

save_universities_to_csv(data)

def save_adoptions_to_csv(data):
    adoptions = []
    for record in data:
        for adoption in record['adoptions']:
            adoptions.append({
                "Adoption ID": record['id'],
                "ID": adoption['id'],
                "Date": adoption['date'],
                "Quantity ": adoption['quantity'],
                "Book ID": adoption['book']['id'],
                "Book isbn10": adoption['book']['isbn10'],
                "Book isbn13": adoption['book']['isbn13'],
                "Book title": adoption['book']['title'],
                "Book Category": adoption['book']['category']
            })
    adoptions_df = pd.DataFrame(adoptions)
    adoptions_df.to_csv('adoptions.csv', index=False)
    print("Adoptions saved to adoptions.csv")
    print(adoptions_df)

save_adoptions_to_csv(data)

def save_messages_to_csv(data):
    messages = []
    for record in data:
        for message in record['messages']:
            messages.append({
                "Adoption ID": record['id'],
                "ID": message['id'],
                "Date": message['date'],
                "Content": message['content'],
                "Category": message['category']
            })
    messages_df = pd.DataFrame(messages)
    messages_df.to_csv('messages.csv', index=False)
    print("messages saved to messages.csv")
    print(messages_df)

save_messages_to_csv(data)

def list_universities_by_state_csv(data):
    state = input("Enter the state name:")
    universities = []
    for record in data:
        if record['university']['state'] == state[0].upper()+state[1:]:
            universities.append({'University':record['university']['name'],'State':state})
    if universities:
        universities_df = pd.DataFrame(universities)
        universities_df.to_csv(f"universities_{state}.csv",index=False)
        print("Universities in",state,":")
        for uni in universities:
            print(uni['University'])
        print(f'universities list is saved as csv file under the name universities_{state}')
    else:
        print("No universities found in",state)    

list_universities_by_state_csv(data)           

def save_books_by_category(data):
    categories = set()
    for record in data:
        for adoption in record['adoptions']:
            categories.add(adoption['book']['category'])
    print("Available book categories:")
    for category in categories:
        print(category)
    user_choice = input("Enter the category of books you want to save: ")
    book_titles = []
    for record in data:
        for adoption in record['adoptions']:
            if adoption['book']['category'] == user_choice[0].upper()+user_choice[1:]:
                book_titles.append(adoption['book']['title'])
    if book_titles:
        with open(f"{user_choice}_books.txt", 'w') as file:
            for title in book_titles:
                file.write(f"{title}\n")
        print(f"Books in the {user_choice} category have been saved to {user_choice}_book.txt")
    else:
        print("No books found in the",user_choice,"category.")

save_books_by_category(data)