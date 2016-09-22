def find_a_string():
    for _ in range(0, 11):
        string = input()
        pattern = input()
        length_of_string = len(string)
        length_of_pattern =len(pattern)
        pattern_counter = 0
        for string_part in range(0, length_of_string - length_of_pattern + 1):
            print(string[length_of_string - length_of_pattern  - string_part:length_of_string - string_part])
            if string[length_of_string - length_of_pattern  - string_part:length_of_string - string_part] == pattern:
                pattern_counter+=1
                
        print(pattern_counter)



if __name__ == "__main__":
    find_a_string()
