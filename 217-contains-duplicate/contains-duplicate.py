class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:   # nếu num đã xuất hiện
                return True
            seen.add(num)     # nếu chưa có thì thêm vào set
        return False
               
