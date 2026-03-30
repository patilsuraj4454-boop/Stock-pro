def convert(string):
    chars = {0: " ", 1: "?!.,", 2: "abc", 3: "def", 4: "ghi", 5: "jkl",
             6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    message = ""
    for word in string.split():
        for letter in word.split("-"):
            message += chars[int(letter[0])][len(letter)-1]
        message += " "
    print(message)
            
string = "666-55 22-666-666-6-33-777"
convert(string)