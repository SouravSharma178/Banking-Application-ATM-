class RBI:
    def _init_(self, name):
        self.name = name
        self.min_bal = 5000

    def display_dank_name(self):
        print("Bank Name :" + str(self.name))
        print("Current and Minimum Balance for A/C is :" + str(self.min_bal))


class HDFC(RBI):
    def _init_(self, val):
        super()._init_(val)
        self.n = None
        self.balance = self.min_bal
        self.deposit = None
        self.Withdraw = None

    def cal(self):
        while True:
            print("1.Check Balance 2.Withdraw 3.Deposit 4.Close")
            self.n = int(input())
            if self.n == 1:
                print("The balance is :" + str(self.balance))
                continue

            elif self.n == 2:
                self.Withdraw = input("Enter the Withdrawl Amount \n")
                if self.balance <= 5000:
                    print("Insufficient Balance to Withdraw \n")
                    continue
                else:
                    self.balance = int(self.balance) - int(self.Withdraw)
                    continue

            elif self.n == 3:
                self.deposit = input("Enter the Withdrawl Amount \n")
                self.balance = int(self.balance) + int(self.deposit)
                print("The balance is :" + str(self.balance))
                continue
            else:
                break


val = input("enter the bank name \n")
h1 = HDFC(val)
h1.cal()