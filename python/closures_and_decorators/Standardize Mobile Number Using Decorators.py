def wrapper(f):
    def fun(l):
        # complete the function
        # Process numbers to standard format
        formatted = []
        for num in l:
            # Remove any existing +91 or 0 prefixes
            clean_num = num[-10:]  # Take last 10 digits
            formatted.append(f"+91 {clean_num[:5]} {clean_num[5:]}")
        return f(formatted)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


