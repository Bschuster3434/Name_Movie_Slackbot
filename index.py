

replacement_word = "Schuster"


def get_movie_title():
    pass

def replace_word_in_movie_title(movie_title):
    

def lambda_handler(event, context):
    '''
    Lambda Function for posting results.
    First, it grabs a random top movie from a list of names.
    Then it replaces one keyword with your replacement_word.
    Then it posts that information to a slack webhook.
    '''

    movie_title = get_movie_title()
    replaced_word_movie_title = replace_word_in_movie_title(movie_title)
    post_to_slack_webhook(replaced_word_movie_title)
