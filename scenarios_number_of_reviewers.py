import math


def scenarios_number_of_reviewers(total_reviews: int, reviewers_max: int=20):
    ''' Helper function to suggest possible number of reviewers that would
        result in an equal distribution of responsiblility (i.e., an equal
        number of reviews being done).

        Input:
            total_reviews: total number of reviews that are needed
            reviewers_max: maximum possible number of reviewers

        Return:

        Library Dependencies:
            1) math
    '''
    print(f'Total reviews to be done: {total_reviews}\n')

    possible_reviewer_numbers = []

    for number_of_reviewer in range(2, reviewers_max+1, 1):
        remainder = math.remainder(total_reviews, number_of_reviewer)
        if remainder == 0.0:
            possible_reviewer_numbers.append(number_of_reviewer)

    print(f'Possible scenarios:')
    for number_of_reviewers in possible_reviewer_numbers:
        reviews_per_reviewer = total_reviews/number_of_reviewers
        print(f'{number_of_reviewers} reviewers doing {reviews_per_reviewer} reviews.')


if __name__ == "__main__":

    scenarios_number_of_reviewers(total_reviews=70, reviewers_max=15)