class print_statements:

    def print_asterisk(self,times):
        output = "*" * int(times)
        print(output)

    

    def print_intro(self,title,author,description):
        self.print_asterisk(50)
        print(title)
        print(f"Author: {author}")
        print(f"Description: {description}")
        self.print_asterisk(50)
        print()
        
    def print_ending(self,list_of_messages):
        print()
        
        self.print_asterisk(50)
        print("DONE!")
        for l in list_of_messages:
            print(l)
        print()
        input("press any key to exit")

        
        
