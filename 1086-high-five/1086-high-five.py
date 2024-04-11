'''
   sort by id, then scores
   for id, score in items 
   add top five for id
   skip to next id
    
    
    
'''

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        items = sorted(items, key = lambda x: (-x[0], x[1]), reverse = True)
        results = []
        i = 0
        
        # Get top five scores of each score and add average to output
        while i < len(items):
            current_id = items[i][0]
            scores_sum = 0
            
            print(items)
            # Get top 5 scores for student
            for j in range(5):
                scores_sum += items[i+j][1]
                top_average = scores_sum // 5
            results.append([current_id, top_average])
            
            # Move to next student 
            while i < len(items) and items[i][0] == current_id:
                i += 1

        return results
            