class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Time: O(B)
        # Space: O(B)
        if a[0] == '0':
            return b
        if b[0] == '0':
            return a
        A = len(a)
        B = len(b)
        if A > B:
            return self.addBinary(b, a)

        ret = []
        # a is shorter or equal
        a_i = A - 1
        b_i = B - 1
        carry = False
        while a_i >= 0:
            if a[a_i] == '0' and b[b_i] == '0':
                if carry:
                    ret.append('1')
                else:
                    ret.append('0')
                carry = False
            elif a[a_i] == '0' and b[b_i] == '1' or a[a_i] == '1' and b[b_i] == '0':
                if carry:
                    ret.append('0')
                else:
                    ret.append('1')
                    carry = False
            else:
                if carry:
                    ret.append('1')
                else:
                    ret.append('0')
                    carry = True
            a_i -= 1
            b_i -= 1

        while b_i >= 0 and carry:
            if b[b_i] == '0':
                ret.append('1')
                carry = False
            else:
                ret.append('0')
            b_i -= 1

        while b_i >= 0:
            ret.append(b[b_i])
            b_i -= 1

        if carry:
            ret.append('1')

        ret.reverse()
        return ''.join(ret)

# Runtime: 38 ms, faster than 86.47% of Python3 online submissions for Add Binary.
# Memory Usage: 14.1 MB, less than 24.29% of Python3 online submissions for Add Binary.
