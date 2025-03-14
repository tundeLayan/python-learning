class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        @property
        def email(self):
            return f"{self.first}.{self.last}@email.com"

        @property
        def email(self):
            return f"{self.first}.{self.last}@email.com"

        @property
        def email(self):
            return f"{self.first}.{self.last}@email.com"

        def apply_raise(self):
            self.pay = int(self.pay * raise_amt)
