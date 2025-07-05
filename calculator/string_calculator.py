def add(numbers: str) -> int:
    if len(numbers) == 0:
        return 0
    
    if numbers[:2] == "//" and numbers[3] == '\n':
        # custom delimiter is defined
        delimiter = numbers[2]
        numbers = numbers[4:]
        numbers = numbers.split(delimiter)
    else:
        if ',' in numbers:
            numbers = numbers.split(',')
        elif '\n' in numbers:
            numbers = numbers.split('\n')
        
    numbers_l = []
    
    for i in numbers:
        i = int(i)
        if i < 0:
            raise ValueError(f"negative numbers not allowed {i}")
        if i < 1000:
            numbers_l.append(i)
    
    return sum(numbers_l)
