def solution(citations):
    citations.sort(reverse=True)
    
#     for citation in citations:
#         h = 0
#         for v in citations:
#             if citation >= v:
#                 h += 1
                
#         if h == citation:
#             return citation

    for i in range(len(citations)):
        # rank = i + 1
        
        if i >= citations[i]:
            return i
        
    return len(citations)