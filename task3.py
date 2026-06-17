contacts = {
    "Ahmed": "01012345678",
    "Mona": "01198765432",
    "Sara": "01255555555"
}
# Print all names
print("Contacts:")
for name in contacts:
    print(name)
search_name = input("Enter a name to search: ")
if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found")