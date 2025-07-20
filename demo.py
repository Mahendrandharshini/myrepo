class Hello:
    def greet(self):
        return "Hello, World!"
    
    def farewell(self):
        return "Goodbye, World!"
    

    def custom_message(self, message):
        return f"Message: {message}"
    
    def __str__(self):
        return "This is a Hello class instance."
    
# Example usage
if __name__ == "__main__":
    hello_instance = Hello()
    print(hello_instance.greet())
    print(hello_instance.farewell())
    print(hello_instance.custom_message("This is a custom message."))
# myrepo/demo.py
#adding for testing
    print(hello_instance)
