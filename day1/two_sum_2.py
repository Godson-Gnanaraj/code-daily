# Using sets/hashes.


class Solution:

    @staticmethod
    def two_sum(nums, k):
        pairs = set()
        for num in nums:
            if k - num in pairs:
                return True
            pairs.add(num)
        return False


def main():
    nums = [10, 15, 3, 7]
    k = 17
    solution = Solution()
    ans = solution.two_sum(nums, k)
    print(ans)


if __name__ == "__main__":
    main()
