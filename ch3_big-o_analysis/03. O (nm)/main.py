def get_avg_brand_followers(all_handles, brand_name):
    count_brand_name = 0
    
    for handle in all_handles:
        for username in handle:
            if brand_name in username:
                count_brand_name += 1

    return count_brand_name / len(all_handles)