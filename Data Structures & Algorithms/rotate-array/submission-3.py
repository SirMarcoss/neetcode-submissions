class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Normalizziamo k per prevenire rotazioni superflue o errori di indice
        k = k % n 
        
        # Ottimizzazione: se k è 0, l'array non deve ruotare
        if k == 0:
            return
            
        # Funzione di supporto per invertire una porzione di array in-place
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        # 1. Inverti tutto l'array
        reverse(0, n - 1)
        
        # 2. Inverti i primi k elementi
        reverse(0, k - 1)
        
        # 3. Inverti i restanti n-k elementi
        reverse(k, n - 1)