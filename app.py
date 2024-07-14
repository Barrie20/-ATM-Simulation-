print("Welcome to ATM Simulation!")
Balance = 1000
user_Pin = "1234"
enter_pin = input("Enter your Pin: ")

if enter_pin != user_Pin:
      print("Invalid PIN... Exiting.......")
      atm_on = False
else:
      atm_on = True

while atm_on:
      print("Main Menu")
      print("1. Check Balance")
      print("2. Withdraw")
      print("3. Deposit")
      print("4. Exit")

      choice = input("Enter your choice (1-4): ")

      if choice == "1":
          print(f"Your current balance is: ${Balance}")
      elif choice == "2":
          amount = float(input("Enter the amount to withdraw: "))
          if amount > Balance:
              print("Insufficient funds.")
          else:
              Balance -= amount
              print(f"You have withdrawn ${amount}. Your new balance is ${Balance}.")
      elif choice == "3":
          amount = float(input("Enter the amount to deposit: "))
          Balance += amount
          print(f"You have deposited ${amount}. Your new balance is ${Balance}.")
      elif choice == "4":
          print("Thank you for using the ATM. Goodbye!")
          atm_on = False
      else:
          print("Invalid choice. Please try again.")
