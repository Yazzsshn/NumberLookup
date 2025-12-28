import phonenumbers
from phonenumbers import geocoder, carrier

def phone_location_lookup():
    phone_number = input("Enter phone number with country code (e.g. +905xxxxxxxxx): ")

    try:
        parsed_number = phonenumbers.parse(phone_number)

        if not phonenumbers.is_valid_number(parsed_number):
            print("Invalid phone number.")
            return

        country = geocoder.description_for_number(parsed_number, "en")
        operator = carrier.name_for_number(parsed_number, "en")

        print("\nPhone Number Information")
        print("------------------------")
        print("Country / Region :", country)
        print("Carrier          :", operator if operator else "Unknown")

    except phonenumbers.NumberParseException:
        print("Error parsing phone number.")


phone_location_lookup()
