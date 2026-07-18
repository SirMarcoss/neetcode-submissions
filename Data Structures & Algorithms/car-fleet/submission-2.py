class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # stack --> data structure that use the method of LIFO (Last In First Out)
        # merge the two information about a single car --> speed[i] + position[i] --> append it inside of the stack
        # time = space / speed --> if 2 or more cars have the same time they reach the destination, thy obviously became a fleet
        # if another car hav a time that is higher then the first one, this car cannot reach the fleet before and for this reason it became
        #another single fleet

        #time complexity O(N log N)) ? looking the costraints, this would be good but i don't think this is the optimal way.
        # Space complexity = O(N) cause we're using a stack  where n is the lenght of the input array

        stack = []
        fleet = 0

        pairs = sorted(zip(position, speed), reverse=True)
        print(list(pairs))

        for p, s in pairs:
            time = (target - p) / s
            if not stack:
                stack.append(time)
                fleet += 1
            else:
                if time > stack[-1]:
                    fleet += 1
                    stack.pop()
                    stack.append(time)
        return fleet




# TEST
# speed: [2,2,1,1] position: [4,1,0,7]
# first iteration: time = target - position[0] / speed[0] = (10 - 4) / 2 = 3
# not stack ? yes --> stack: [3], fleet = 1
# second iteration: time = target- position[1] / speed[1] = 10 - 1 / 2 = 4,5
# 4,5 > stack[-1] = 3 ? yes --> fleet = 2, stack = [4,5]
# third iteration: time = (target - position[2]) / speed[2] =  10 - 0 / 1 = 10
# 10 > stack[-1] = 4,5? yes --> fleet = 3, stack = 




            




        