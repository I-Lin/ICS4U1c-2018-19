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


def print_address(addr):
    print(addr.address_line1)
    print(addr.address_line2)
    print(addr.city, addr.province, addr.postal_code)
    print(addr.country)


def main():
    # Home Address
    home_address = Address()

    # Set home address information
    home_address.address_line1 = "123 Sesame St"
    home_address.address_line2 = ""
    home_address.city = "Toronto"
    home_address.province = "Ontario"
    home_address.postal_code = "123 ABC"
    home_address.country = "Canada"

    # Print home address information
    print_address(home_address)

    # Work Address
    work_address = Address()

    # Set work address information
    work_address.address_line1 = "456 Working St"
    work_address.address_line2 = ""
    work_address.city = "Toronto"
    work_address.province = "Ontario"
    work_address.postal_code = "456 DEF"
    work_address.country = "Canada"

    # Print work address information
    print_address(home_address)


main()