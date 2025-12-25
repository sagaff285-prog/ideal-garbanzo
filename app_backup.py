#!/data/data/com.termux/files/usr/bin/python3
import os
import datetime

def display_menu():
    print("\n" + "="*40)
    print("     PYTHON APP ON TERMUX")
    print("="*40)
    print("1. Say Hello")
    print("2. Check System Info")
    print("3. File Operations")
    print("4. Calculator")
    print("5. Exit")
    print("="*40)

def say_hello():
    name = input("\nWhat's your name? ")
    print(f"\nHello {name}! 👋")
    print(f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')}")

def system_info():
    print("\n" + "-"*30)
    print("SYSTEM INFORMATION")
    print("-"*30)
    
    # Get Termux info
    home = os.path.expanduser("~")
    print(f"Home directory: {home}")
    print(f"Current directory: {os.getcwd()}")
    
    # List files
    print(f"\nFiles in current directory:")
    files = os.listdir(".")
    for f in files:
        if os.path.isfile(f):
            print(f"  📄 {f}")
        else:
            print(f"  📁 {f}/")
    
    print(f"\nTotal: {len(files)} items")

def file_operations():
    print("\n" + "-"*30)
    print("FILE OPERATIONS")
    print("-"*30)
    
    filename = input("Enter filename to create/edit: ")
    
    if os.path.exists(filename):
        print(f"\n{filename} already exists!")
        with open(filename, 'r') as f:
            content = f.read()
            print(f"\nCurrent content:\n{'-'*20}")
            print(content)
            print(f"{'-'*20}")
        
        action = input("\n[A]ppend or [O]verwrite? (a/o): ").lower()
        mode = 'a' if action == 'a' else 'w'
    else:
        mode = 'w'
        print(f"\nCreating new file: {filename}")
    
    content = input("\nEnter text to write: ")
    
    with open(filename, mode) as f:
        f.write(content + "\n")
    
    print(f"\n✅ File saved: {filename}")
    print(f"Size: {os.path.getsize(filename)} bytes")

def calculator():
    print("\n" + "-"*30)
    print("CALCULATOR")
    print("-"*30)
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print(f"\n{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} × {num2} = {num1 * num2}")
        if num2 != 0:
            print(f"{num1} ÷ {num2} = {num1 / num2}")
        else:
            print("Cannot divide by zero!")
            
    except ValueError:
        print("❌ Please enter valid numbers!")

def main():
    print("Welcome to Termux Python App!")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nSelect option (1-5): ")
            
            if choice == "1":
                say_hello()
            elif choice == "2":
                system_info()
            elif choice == "3":
                file_operations()
            elif choice == "4":
                calculator()
            elif choice == "5":
                print("\n👋 Goodbye! Thanks for using Termux!")
                break
            else:
                print("❌ Invalid choice! Please select 1-5")
                
        except KeyboardInterrupt:
            print("\n\n⚠️ Program interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\n⚠️ An error occurred: {e}")

if __name__ == "__main__":
    main()
