def add(numbers: str) -> int:
    if len(numbers) == 0:
        return 0
    
    if numbers[:2] == "//":
        # custom delimiter is defined
        ix = numbers.index('\n')
        delimiter = numbers[2:ix]
        if delimiter[0] == '[' and delimiter[-1] == ']':
            delimiter = delimiter[1:-1]
        numbers = numbers[ix:]
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
