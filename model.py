def calculate_stress_level(responses):
    # Dictionary mapping response options to stress level increments
    response_map = {
        'Very Often': 2,
        'Sometimes': 1,
        'Never': 0
    }
    
    # Calculate stress level based on responses
    stress_level = sum(response_map.get(response, 0) for response in responses)
    
    return stress_level

# Example usage (can be run standalone for testing)
if __name__ == '__main__':
    # Example responses
    example_responses = [
        'Very Often', 'Sometimes', 'Never', 'Very Often', 'Sometimes',
        'Very Often', 'Never', 'Sometimes', 'Never', 'Sometimes'
    ]
    
    # Calculate stress level
    stress_level = calculate_stress_level(example_responses)
    
    # Determine stress result
    if stress_level >= 10:
        result = 'High Stress'
    else:
        result = 'Low Stress'
    
    print(f"Stress Level: {stress_level}")
    print(f"Result: {result}")
