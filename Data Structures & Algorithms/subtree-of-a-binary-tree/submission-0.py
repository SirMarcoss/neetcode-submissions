# Definizione del nodo (solitamente fornita da LeetCode)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Caso base 1: Un sotto-albero vuoto è sempre un sotto-albero di qualsiasi albero
        if not subRoot:
            return True
        
        # Caso base 2: Se l'albero principale è vuoto (e subRoot non lo è), 
        # è impossibile trovarvi il sotto-albero
        if not root:
            return False
        
        # Se i due alberi correnti sono strutturalmente identici, abbiamo finito
        if self.isSameTree(root, subRoot):
            return True
        
        # Altrimenti, la ricerca continua:
        # subRoot potrebbe trovarsi nel ramo sinistro OPPURE (or) nel ramo destro
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Funzione helper per verificare se due alberi sono esattamente identici.
        """
        # Se entrambi i nodi sono nulli, abbiamo raggiunto la fine senza discrepanze
        if not p and not q:
            return True
        
        # Se uno solo è nullo, oppure i valori differiscono, gli alberi non sono uguali
        if not p or not q or p.val != q.val:
            return False
        
        # I valori corrispondono, quindi controlliamo ricorsivamente 
        # che i rispettivi sotto-rami sinistri E destri siano identici
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
