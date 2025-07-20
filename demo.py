class Hello:
    def greet(self):
        return "Hello, World!"
    
    def farewell(self):
        return "Goodbye, World!"
    
if __name__ == "__main__":
    hello = Hello()
    print(hello.greet())
    print(hello.farewell())