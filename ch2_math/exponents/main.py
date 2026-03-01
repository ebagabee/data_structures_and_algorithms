def get_estimated_spread(audiences_followers):
    sum_of_audience = 0
    for audience in audiences_followers:
        sum_of_audience += audience
    
    length_audience_followers = len(audiences_followers)

    if (length_audience_followers < 1):
        return 0
    
    average_audience_followers = sum_of_audience / length_audience_followers

    estimated_spread = average_audience_followers * (length_audience_followers ** 1.2)
    return estimated_spread
    