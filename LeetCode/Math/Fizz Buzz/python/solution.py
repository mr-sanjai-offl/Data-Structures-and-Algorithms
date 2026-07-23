class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        # result = []
        # for i in range(1, n + 1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         result.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         result.append("Fizz")
        #     elif i % 5 == 0:
        #         result.append("Buzz")
        #     else:
        #         result.append(str(i))
        # return result
        return ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1,n+1)]