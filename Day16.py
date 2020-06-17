def find_lucky(arr):
        count_map = {}
        ans = -1
        for v in arr:
            count_map[v] = count_map.get(v,0) + 1 
        
        for v in arr:
            if count_map[v] == v and v > ans:
                ans = v
        return ans