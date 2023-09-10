import socket

class Assignment2:
    def __init__(self, year): #takes year
        self.year = year

    def tellAge(self, currentYear): #used year wit current year passed
        birth_year = currentYear - self.year
        print(f"Your age is {birth_year}")

    def listAnniversaries(self): #every 10 years adds to anniversary
        current_year = 2022
        anniversaries = []
        for i in range(10, current_year - self.year + 1, 10):
            anniversaries.append(i)
        return anniversaries


    def modifyYear(self, n):
        year_str = str(self.year)  # Convert the year to its text representation
        first_two_chars = year_str[:2] * n  # Repeat the first two characters n times
        
        multiply_by_n = year_str * n
        
        # Initialize variables to store the result and index for every other digit
        result = ""
        add_every_other_num = 0
        
        for i in range(len(multiply_by_n)):
            # Check if the current index is even (0-based index)
            if i % 2 == 0:
                # Add the digit to the result string
                add_every_other_num += int(multiply_by_n[i])


        
        # Convert add_every_other_num back to a string
        add_every_other_num = str(add_every_other_num)
        
        
        # Print the final result
        result = first_two_chars + add_every_other_num  # Concatenate the two parts 
        return result

    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
        if not string[0].islower() or not string[0].isalpha():
            return False
        num_count = sum(1 for char in string if char.isdigit())
        if num_count != 1:
            return False
        return True

    @staticmethod
    def connectTcp(host, port):
        try:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except Exception as e:
            return False

# Example usage:
a = Assignment2(2000)
a.tellAge(2023)
anniversaries = a.listAnniversaries()
print(anniversaries)
modified_year = a.modifyYear(5)
print(modified_year)
is_good_string = Assignment2.checkGoodString("f1obar0more")
print(is_good_string)
is_connected = Assignment2.connectTcp("www.google.com", 80)
print(is_connected)