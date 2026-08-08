class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # 1. Correzione fondamentale per evitare IndexError
        
        if k == 0:
            return
            
        copia = nums.copy()  # Array di appoggio per leggere i dati intatti
        
        l = 0
        r = n - k  # L'indice da cui volevi partire tu
        
        # 2. IL TUO CICLO: portiamo in testa gli ultimi k elementi
        while r <= n - 1:
            nums[l] = copia[r]  # Leggiamo dalla copia, scriviamo in nums
            l += 1
            r += 1         
            
        # 3. IL PEZZO MANCANTE: ora prendiamo i primi (n-k) elementi 
        # originali e li accodiamo alla fine
        i = 0
        while l <= n - 1:
            nums[l] = copia[i]
            l += 1
            i += 1