def add(numbers: str) -> int:
    if len(numbers) == 0:
        return 0
    
    numbers = numbers.split(',')
    numbers = [int(i) for i in numbers]
    
    return sum(numbers)
