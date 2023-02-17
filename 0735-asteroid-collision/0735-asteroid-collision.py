class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:                
            if st and st[-1] > 0 and a < 0:
                while st and st[-1] > 0:
                    top = st.pop()
                    if top > abs(a):
                        st.append(top)
                        a = 0
                        break
                    elif top == abs(a):
                        a = 0
                        break
                    else: continue

                if a != 0 : st.append(a)  
            else:
                st.append(a)
        return st    