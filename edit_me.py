
def monotonic(lst):
  """Return True if lst is monotonic; return False, otherwise."""   
increasing = decreasing = True  

for i in range(len(list) - 1):  
        if list[i] > list[i + 1]:  
            increasing = False
        if list[i] < list[i + 1]:  
            decreasing = False

return increasing or decreasing  


def test_monotonic():
    test_cases = [
        ([1, 2, 3, 4, 5], True), 
        ([5, 4, 3, 2, 1], True),  
        ([1, 2, 2, 3], True),     
        ([3, 3, 3], True),        
        ([1, 3, 2, 4], False),    
        ([], True),               
        ([1], True),              
    ]

    for test in test_cases:
        lst, expected = test  
        result = monotonic(lst)
        print(f"List: {lst} → {result} (Expected: {expected})")
        assert result == expected, "Test case failed!"

    print("All test cases passed!")


test_monotonic()