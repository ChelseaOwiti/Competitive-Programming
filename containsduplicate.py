class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create hashmap
        hashset = set()
        #add items to hashmap by iterating thru the array
        for i in nums:
            #if item is already in hashmap return true
            if i in hashset:
                return True

            hashset.add(i)
        return False