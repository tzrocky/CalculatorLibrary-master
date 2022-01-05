"""Calculator library containing basic math operations."""

@overload
def add(first_term, second_term):
    return first_term + second_term

@overload
def subtract(first_term, second_term):
    return first_term - second_term

@overload
def multiply(first_term, second_term):
    return first_term * second_term
