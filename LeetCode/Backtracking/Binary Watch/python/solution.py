class Solution:
    def readBinaryWatch(self, t: int) -> List[str]:
        res = []
        if t >= 9:
            return res
        # h = 0
        # m = t
        # while m !=  and m != 0:
        #     for i in range(12):
        #         b = bin(i)[2:]
        #         if b.count('1') == h:
        #             res.append(f"{i}:00")
        #     for i in range(60):
        #         b = bin(i)[2:]
        #         if b.count('1') == m:
        #             res.append(f"0:{i:02d}")
        #     h += 1
        #     m -= 1

        for i in range(12):
            for j in range(60):
                b1 = bin(i)[2:]
                b2 = bin(j)[2:]
                if b1.count('1') + b2.count('1') == t:
                    res.append(f"{i}:{j:02d}")
        print(res)
        return res
