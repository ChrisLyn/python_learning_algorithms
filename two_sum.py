import unittest


class two_sum:
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            else:
                dict[nums[i]] = i


class Two_Sum_Unit_Test(unittest.TestCase):
    def testTwoSum(self):
        testTarget = two_sum()
        self.assertEqual([0, 3], testTarget.twoSum([1, 3, 5, 6, 9], 7))


if __name__ == '__main__':
    unittest.main()
