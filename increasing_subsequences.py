LeetCode
Subscribe
Problems 
Mock 
Contest
Courses
Articles
Discuss
Book
Story
shaniavina
Notes Auto Saved.
|||

Type here...(Markdown is enabled)
​
491. Increasing Subsequences Add to List
DescriptionHintsSubmissionsSolutions
Total Accepted: 6862
Total Submissions: 17803
Difficulty: Medium
Contributors:
Stomach_ache
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
Subscribe to see which companies asked this question.

Show Tags
Have you met this question in a real interview? Yes  No
Discuss  Pick One   Editorial Solution
 


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(nums, pos, seq, result):
            if len(seq) >= 2:
                result.append(list(seq))
            lookup = set()
            for i in range(pos, len(nums)):
                if (not seq or nums[i] >= seq[-1]) and nums[i] not in lookup:
                    lookup.add(nums[i])
                    seq.append(nums[i])
                    helper(nums, i + 1, seq, result)
                    seq.pop()
        
        
        
        
        result, seq = [], []
        helper(nums, 0, seq, result)
        return result
Custom Testcase  
 Contribute Testcase
Run CodeSubmit Solution
Shortcut: Command + enter

Submission Result: Pending
Run Code Status: Some thing wrong

Frequently Asked Questions | Terms of Service



Copyright © 2017 LeetCode

Send Feedback
