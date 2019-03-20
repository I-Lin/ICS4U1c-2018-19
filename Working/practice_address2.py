class Address(object):
    """
    A class representing an address
    """
    def __init__(self):
        self.address_line1 = ""
        self.address_line2 = ""
        self.postal_code = ""
        self.city = ""
        self.province = ""
        self.country = ""


    def print_address(self):
        print(self.address_line1)
        print(self.address_line2)
        print(self.city, self.province, self.postal_code)
        print(self.country)


def main():
    # Home Address
    home_address = Address()

    # Set home address information
    home_address.address_line1 = "123 Sesame St"
    home_address.address_line2 = "000 Easy Rd"
    home_address.city = "Toronto"
    home_address.province = "Ontario"
    home_address.postal_code = "123 ABC"
    home_address.country = "Canada"

    # Print home address information-
    Address.print_address(home_address)

    print()

    # Work Address
    work_address = Address()

    # Set work address information
    work_address.address_line1 = "456 Working St"
    work_address.address_line2 = "789 Work Ave"
    work_address.city = "Toronto"
    work_address.province = "Ontario"
    work_address.postal_code = "456 DEF"
    work_address.country = "Canada"

    # Print work address information
    Address.print_address(work_address)


main()