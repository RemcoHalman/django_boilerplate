# TODO: Change the company data
COMP_NAME = '[COMP name]'
COMP_PHONE = '[0612345678]'
COMP_EMAIL = '[test@mail.com]'
CITY = '[CITY]'
ADDRESS_LINE_1 = '[Adressline 1]' # Adres + number
ADDRESS_LINE_2 = '[Adressline 2]' # Zipcode
SUMMARY = """
Post your summary here
......................
"""

def COMPdata(request):
    COMP_data = {
        'name' : f"{COMP_NAME}",
        'phone' : f"{COMP_PHONE}",
        'email' : f"{COMP_EMAIL}",
        'city' : f"{CITY}",
        'adres1' : f"{ADDRESS_LINE_1}",
        'adres2' : f"{ADDRESS_LINE_2}",
        'summary' : f"{SUMMARY}",
        }
    return {'COMP': COMP_data}
