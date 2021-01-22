from sidhuSearchEngine.PriorityQueueLL import PQLinkedList
from sidhuSearchEngine.TrieAC import TrieAC

data_storage = TrieAC()
topSuggestions = []


# adding data to data_storage
def create():
    dictionary = open("/Users/tarans1dhu/PycharmProjects/ACSearch/test.txt", "r")
    try:
        words = dictionary.readlines()
        for word in words:
            word = word.replace("[^a-zA-Z]", "")
            data_storage.insert(word)

    except FileNotFoundError:
        print("File Not Found")
    except:
        print("Something Else")


# auto completing query by providing suggestions
# and prioritizing suggestion
def auto_complete(query, feature, prior):
    restrict = False
    data_storage.auto_complete(query, feature)
    if feature is 1:
        restrict = True

    if prior:
        prioritize(data_storage.get_suggestion(), restrict)
    if restrict:
        data_storage.get_suggestion().clear()


# prioritize suggestion according to their weight
def prioritize(suggestions, restrict):
    size = 5  # default size
    length = len(suggestions)

    # if restrict is on and suggestion are not enough update size
    if restrict and length < 5:
        size = length

    # creating priority queue linked list
    prior = PQLinkedList()
    # adding data to prior
    for i in range(0, size):
        word = data_storage.get_suggestion()[i]
        weight = data_storage.find(word)
        prior.insert(word, weight)

    # adding prior data to topSuggestions
    for i in range(size):
        topSuggestions.append(prior.delete_max())


# update weight of specific key in trie
def update_data(key):
    key = data_storage.get_suggestion().index(key)
    # inserting weight into key
    data_storage.insert_weight(key)
    # clearing previous suggestions
    data_storage.get_suggestion().clear()


def print_suggestions():
    if len(topSuggestions) == 0:
        print("No Item")
    for word in topSuggestions:
        print(word)
    data_storage.print_trie()
