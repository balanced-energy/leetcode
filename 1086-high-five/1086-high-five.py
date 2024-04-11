'''
Understanding the problem
Designing a solution
- First sort items by ID, then scores

-Use while loop to iterate through each element in items (i < len(items))
    - track current ID items[i][0]
    - track sum 
    
    for loop in range 5
        - accessing score located at items[i+j][1]
        - sum += current score
    
    - average scores sum
    - add to results list 
    
    while is less than items length and i is equal to current ID
        - increse i
    


Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

sort = [[1,100],[1,92],[1,91],[1,87],[1,65],[1,60],[2,100],[2,97],[2,93],[2,77],[2,76]]



Implementing code

'''

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        results = []
        sorted_ids = sorted(items, key = lambda x: (-x[0], x[1]), reverse = True)
        i = 0
        
        while i < len(sorted_ids):
            current_id = sorted_ids[i][0]
            top_scores = 0
            
            for j in range(5):
                score = sorted_ids[i+j][1]
                top_scores += score
            
            average = top_scores // 5
            results.append([current_id, average])
            
            # Move to next ID
            while i < len(sorted_ids) and sorted_ids[i][0] == current_id:
                i += 1
                
        
        return results
        
        
        
        
    