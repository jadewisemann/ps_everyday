def solution(phone_book):
    headers = {}
    for phone in phone_book:
        headers[phone] = 1
    
    for phone in phone_book:
        if phone in headers and headers != phone:
            return False

    return True