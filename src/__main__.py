import ATMController
import time

if __name__ == "__main__":
    users = []
    user1 = ATMController.User(
        "kim", 1234, [ATMController.BankAccount(0), ATMController.BankAccount(0)])
    user2 = ATMController.User(
        "lee", 5678, [ATMController.BankAccount(0), ATMController.BankAccount(0)])

    users.append(user1)
    users.append(user2)

    print("Insert Card...")
    time.sleep(3)

    while(True):
        number = input("PIN number : ")
        if(int(number) != users[0].pin):
            print("Incorrect PIN.")
        else:
            break

    # user1 - account#2
    user1.account[0].seeBalance()
    deposit_doller = 10000
    print("The balance in account #1 of {} is {} dollers.".format(
        user1.name, user1.account[0].balance))
    user1.account[0].deposit(deposit_doller)
    print("{} dollers has been deposited into account #1 of {}.".format(
        deposit_doller, user1.name))
    withdraw_doller = 1000
    user1.account[0].withdraw(withdraw_doller)
    print("{} dollers has been debited from {}'s account #1.".format(
        withdraw_doller, user1.name))
    print("The balance in account #1 of {} is {} dollers.".format(
        user1.name, user1.account[0].balance))

    print("")
    # user1 - account#1
    user1.account[1].seeBalance()
    deposit_doller = 500
    print("The balance in account #2 of {} is {} dollers.".format(
        user1.name, user1.account[1].balance))
    user1.account[0].deposit(deposit_doller)
    print("{} dollers has been deposited into account #2 of {}.".format(
        deposit_doller, user1.name))
    withdraw_doller = 100
    user1.account[0].withdraw(withdraw_doller)
    print("{} dollers has been debited from {}'s account #2.".format(
        withdraw_doller, user1.name))
    print("The balance in account #2 of {} is {} dollers.".format(
        user1.name, user1.account[1].balance))
