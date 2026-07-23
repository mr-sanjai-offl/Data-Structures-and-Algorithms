class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def isLeapYear(y):
            return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

        def countDays(y, m, d):
            total = 0
            for i in range(1971, y):
                total += 365 + isLeapYear(i)
            for i in range(1, m):
                total += arr[i - 1]
            if m > 2 and isLeapYear(y):
                total += 1
            total += d
            return total

        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))

        days1 = countDays(y1, m1, d1)
        days2 = countDays(y2, m2, d2)

        return abs(days1 - days2)