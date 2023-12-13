class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.cookies_in_jar = 0
        self._size = 0
        if self._capacity < 0:
            raise ValueError("Negative values are not permitted")

    def __str__(self):
        string_cookies = str(self.size)

    def deposit(self, n):
        n_int = int(n)
        self.cookies_in_jar += n_int
        while self.cookies_in_jar < self._capacity:
            self._size = self.cookies_in_jar
            print("Total cookies in jar:", self._size)
            user_input = input("Would you like to add more?")
            if user_input == "yes":
                n = input("how many")
                int_n = int(n)
                print(self._size)
                self.deposit(n)
            if user_input == "no":
                user_input = input("What would you like to do")
                if user_input == "withdrawal":
                    self.withdrawal()
                else:
                    print("Total cookies in jar:", self._size)
        else:
            print("The jar is full")

    def withdrawal(self):
        user_input = input("How many cookies would you like to withdrawal")
        cookies_to_withdrawal = int(user_input)
        while self._size > 0:
            self._size -= cookies_to_withdrawal
            print("Cookies in jar:", self._size)
            user_input = input("Would you like more cookies?")
            if user_input == "Yes":
                self.withdrawal()
            if self._size == 0:
                print("The jar is empty, add more cookies")
                user_input = input("Would you like to add more cookies?")
                if user_input == "no":
                    print("Total cookies in jar:", self._size)

    @property
    def size(self):
        return self._size

    @property
    def capacity(self):
        return self._capacity


def main():
    # capacity_test = 12
    cookie = Jar()
    user_input = input("What would you like to do")
    if user_input == "deposit":
        n = input("How many cookies do you want to add?")
        cookie.deposit(n)
    if user_input == "withdrawal":
        cookie.withdrawal()


if __name__ == "__main__":
    main()
