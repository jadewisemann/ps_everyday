def solution(phone_book):
    phone_book.sort()

    for p1, p2,in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True

def solution_2(phone_book):
    headers = {}
    for phone in phone_book:
        headers[phone] = 1
    
    for phone in phone_book:
        if phone in headers and headers != phone:
            return False

    return True

solution(["119", "97674223", "1195524421"])