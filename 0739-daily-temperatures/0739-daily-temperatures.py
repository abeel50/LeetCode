class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st = [] #stack
        result= [0] * len(temperatures) #results array
        for i in range(len(temperatures)):
            if len(st) == 0: #if atck is empty
                st.append(i) #push current temp.
            else:
                # pop and ave results till temprature is warmer
                while len(st) !=0  and temperatures [i] > temperatures[st[-1]]:
                    result[st[-1]] = i - st[-1]
                    st.pop()
                st.append(i)
            
        return result