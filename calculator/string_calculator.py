def add(numbers: str) -> int:
    if len(numbers) == 0:
        return 0
    
    if ',' in numbers:
        numbers = numbers.split(',')
    elif '\n' in numbers:
        numbers = numbers.split('\n')
        
    numbers = [int(i) for i in numbers]
    
    return sum(numbers)
