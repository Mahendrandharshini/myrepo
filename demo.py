class Hello:
    def greet(self):
        return "Hello, World!"
    
    def farewell(self):
        return "Goodbye, World!"
    
    def custom_message(self, message):
        return f"Message: {message}"
    
# Example usage
if __name__ == "__main__":
    hello_instance = Hello()
    print(hello_instance.greet())
    print(hello_instance.farewell())
    