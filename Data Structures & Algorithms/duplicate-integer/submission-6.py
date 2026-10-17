class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # METHOD-1 Using Set
        # if len(nums) != len(set(nums)):
        #     return True
        # else:
        #     return False

        # METHOD-2 Using Dict
        # d = dict()
        # for k in nums:
        #     if k in d.keys():
        #         d[k] +=1
        #         if d[k] > 1:
        #             return True
        #     else:
        #         d[k] =1
        # return False

        # METHOD-3
        d = dict()
        for k in nums:
            d[k] = d.get(k,0)+1
            
            if d[k] > 1 :
                return True
        else:
            return False
    
        
