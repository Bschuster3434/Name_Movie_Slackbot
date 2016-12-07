import boto3
import StringIO
import csv
from random import choice

replacement_word = "Schuster"

def get_movie_csv():
    #Retrieve the full csv file from the s3 bucket
    s3 = boto3.resource('s3')
    bucket = 'top1001movies'
    key = 'top_1001_movies.csv'
    obj = s3.Object(bucket, key)
    raw_csv = obj.get()['Body'].read()

    #read the csv as a string and use csv library to parse
    f = StringIO.StringIO(raw_csv)
    reader = csv.reader(f, delimiter=',')

    #Find all the titles and put them into a single list
    titles = []
    first_line = 0
    for i in reader:
        if first_line == 0:
            first_line = 1
            continue
        else:
            title = i[1]
            titles.append(title)

    return titles

def get_movie_title(movie_list):
    next_movie = choice(movie_list)
    if len(next_movie.split(' ')) > 1:
        return next_movie
    else:
        return get_movie_title(movie_list)

def replace_word_in_movie_title(movie_title):
    '''
    Create a new title from the movie title, using your replacement_word.
    Eliminates common stop words that aren't replacable with title.
    '''
    stop_words = ["a","about","above","after","again","against","all","am","an",\
    "and","any","are","aren't","as","at","be","because","been","before","being",\
    "below","between","both","but","by","can't","cannot","could","couldn't","did",\
    "didn't","do","does","doesn't","doing","don't","down","during","each","few",\
    "for","from","further","had","hadn't","has","hasn't","have","haven't","having",\
    "he","he'd","he'll","he's","her","here","here's","hers","herself","him",\
    "himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into",\
    "is","isn't","it","it's","its","itself","let's","me","more","most","mustn't",\
    "my","myself","no","nor","not","of","off","on","once","only","or","other",\
    "ought","our","ours","ourselves","out","over","own","same","shan't","she",\
    "she'd","she'll","she's","should","shouldn't","so","some","such","than",\
    "that","that's","the","their","theirs","them","themselves","then","there",\
    "there's","these","they","they'd","they'll","they're","they've","this",\
    "those","through","to","too","under","until","up","very","was","wasn't",\
    "we","we'd","we'll","we're","we've","were","weren't","what","what's","when",\
    "when's","where","where's","which","while","who","who's","whom","why","why's",\
    "with","won't","would","wouldn't","you","you'd","you'll","you're","you've",\
    "your","yours","yourself","yourselves"]

    word_list = movie_title.split(' ')

    word_index_to_replace = []
    for n,i in enumerate(word_list):
        if i.lower() not in stop_words:
            word_index_to_replace.append(n)

    #If all the words are stop words, just replace one word with the replacement word
    if len(word_index_to_replace) == 0:
        movie_title.replace(choice(word_list), replacement_word)
        return movie_title
    else:
        index = choice(word_index_to_replace)
        word_list[index] = replacement_word
        movie_title = ' '.join(word_list)
        return movie_title

def post_to_slack_webhook(replaced_word_movie_title):
    

def lambda_handler(event, context):
    '''
    Lambda Function for posting results.
    First, it grabs a random top movie from a list of names.
    Then it replaces one keyword with your replacement_word.
    Then it posts that information to a slack webhook.
    '''

    movie_list = get_movie_csv()
    movie_title = get_movie_title(movie_list)
    replaced_word_movie_title = replace_word_in_movie_title(movie_title)
    post_to_slack_webhook(replaced_word_movie_title)
