"""
This class showcases in interesting Python equivalents of instance method and static method as well as static variable
and instance variable in the hands of a Java developer
"""

class Fib:
    cache = {}

    def fib(self, n: int) -> int:

        if n in self.cache:
            return self.cache[n]

        if n < 2:
            self.cache[n] = n
            return n
        else:
            result = self.fib(n - 1) + self.fib(n - 2)
            self.cache[n] = result
            return result

    def static_fib(n: int) -> int:

        if n in Fib.cache:
            return Fib.cache[n]

        if n < 2:
            Fib.cache[n] = n
            return n
        else:
            result = Fib.static_fib(n - 1) + Fib.static_fib(n - 2)
            Fib.cache[n] = result
            return result

class_instance = Fib()

print(class_instance.fib(10))

print(Fib.static_fib(20))
