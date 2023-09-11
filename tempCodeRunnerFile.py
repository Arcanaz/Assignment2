    year_str = str(self.year)  # Convert the year to its text representation
        first_two_chars = year_str[:2] * n  # Repeat the first two characters n times
        
        year_multiplied = self.year * n
        print(year_multiplied)

        year_multiplied_str = str(year_multiplied)
        
        result = ""  # Initialize result as an empty string

        for i in range(len(year_multiplied_str)):
            if i % 2 == 0:
                result += year_multiplied_str[i]

        print(result)

        ret