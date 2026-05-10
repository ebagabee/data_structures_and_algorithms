'''
Implement the [count_marketers] function.
It should accept a list of strings (job titles) and return the number of users who've
set their title to "marketer". LockedIn users sometimes use different cassing in their titles,
so make sure to account for that.
'''

def count_marketers(job_titles):
    target_string = 'marketer'
    count = 0

    for job in job_titles:
        if job.lower() == target_string:
            count += 1
    
    return count

count = count_marketers(['programmer', 'marketer', 'doctor', 'marketer'])
print(count)