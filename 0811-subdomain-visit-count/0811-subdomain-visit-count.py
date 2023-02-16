
'''
Workflow Timestamps
1. 0:00 - 5:35 Make Sure You Understand the Problem
2. 5:35 - 13:10 Design a Solution / Runtime and Space Complexity
3. 13:10 - 22:30 Write a Template for Code in Logical Blocks. Aka Pseudocode
4. Write the Code And Pass Test Cases.
'''
'''
1. Make Sure You Understand the Problem
test cases:
input = [] -> []

input ['1 mail.com', '2 wiki.org', '3 mail.com' ] -> ['4 mail.com', '1 wiki.org']

2. Design a Solution / Runtime and Space Complexity
- For each pair in cpdomains. Split off visits count, split domains. 
- Check if domains are in map with domain:count. 
- if domain in map, then increase count by visits
- add domain to map with visit count.

len(max(cpdomain)) = M
number of cpdomains = N
Runtime: O(N*M)
Space: O(N)

3. Write a Template for Code in Logical Blocks. Aka Pseudocode
    # Initialize domain_count map and output string total_visits
    domain_count = {}
    total_visits = ''

    for pair in cpdomains:
        cur_domains = []
        split off visit count

        # Check len(domains) 
        domains = split off domains
        
        # Have two domains
        if len(domains) == 2:
            create appropriate domains 
            append to cur_domains
        # Increase count if in map 
        for domain in cur_domains:
            if in domain_count map increase value by visits  
        # add domain and visit to map
        else add to map with visit count
    
    # Create output string of total visits 
    for domain, visits in domain_count:
        s = f'{visits} {domain}'
        total_visits.append()
    
    return total_visits
4. Write the Code And Pass Test Cases.
'''

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # Initialize domain_count map and output string total_visits
        domain_count = {}
        total_visits = []

        # For each pair in cpdomains. Split off visits count, split domains. 
        for pair in cpdomains:
            cur_domains = []
            visits_domains = pair.split()
            visits = visits_domains[0]
            domains = visits_domains[1]

            # Check len(domains) 
            separate_domains = domains.split('.')
            
            
            # Have two domains
            if len(separate_domains) == 2:
                domain_1 = separate_domains[0] + '.' + separate_domains[1] 
                domain_2 = separate_domains[1]
                cur_domains.append(domain_1)
                cur_domains.append(domain_2)
            # Have three domains 
            else:
                domain_1 = separate_domains[0] + '.' + separate_domains[1] + '.' + separate_domains[2]
                domain_2 = separate_domains[1] + '.' + separate_domains[2] 
                domain_3 = separate_domains[2]
                cur_domains.append(domain_1)
                cur_domains.append(domain_2)
                cur_domains.append(domain_3)

            # Increase count if in map 
            for domain in cur_domains:
                if domain in domain_count:
                    domain_count[domain] += int(visits)
                else:
                    domain_count[domain] = int(visits)

        # domain_count map is done
        # Create output string of total visits 
        for domain, visits in domain_count.items():
            s = f'{visits} {domain}'
            total_visits.append(s)
        
        return total_visits