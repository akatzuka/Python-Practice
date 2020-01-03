class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:                 #if intervals is empty return
            return

        intervals = sorted(intervals)       #sort intervals
        output = [intervals[0]]             #set output to first interval
        counter = 1                         #initialize counter

        while counter < len(intervals):     #while counter is less than elements in intervals
            if output[-1][1] >= intervals[counter][0]:  #if last intervals end [[x][y]] is greater than or equal to current element start [[y][x]] then set merge intervals in output
                output[-1] = [min(output[-1][0], intervals[counter][0]), max(output[-1][1], intervals[counter][1])]
            else:                           #otherwise append interval to output
                output.append(intervals[counter])
            counter += 1                    #increment counter

        return output                       #return merged intervals
