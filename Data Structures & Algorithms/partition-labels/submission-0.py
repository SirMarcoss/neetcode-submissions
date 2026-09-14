class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        hashtable = {} # lettera --> ultimo indice di apparizione apparizione 

        for index, char in enumerate(s):
            hashtable[char] = index

        # hashtable {
        # x : 3
        # y : 4
        # z : 7
        # b : 9
        # i : 10
        # s : 11
        # l : 12 }


        res = []
        size = end = 0

        for index, char in enumerate(s):
            size += 1
            end = max(end, hashtable[char])

            if index == end:
                res.append(size)
                size = 0
        return res


        


        
            

        