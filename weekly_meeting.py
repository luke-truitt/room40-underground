# Luke

## Pull up all events and their details
def retrieve_weekly_events():
    # Go into the events table and look for all the ones whose date field is within the week
    # Return an array of dictionaries where each is an event with all of its parameters
    return []

def get_initial_votes():
    # pull up all deals that are at initial vote stage and pass them to the front, or deals that have recently been voted on
    # return a list of dictionaries of these deals
    return []

def get_final_votes():
    # pull up all deals that are at final vote stage and pass them to the front, or deals that have recently been voted on
    # return a list of dictionaries of these deals
    return []

def add_final_votes(deal_id, eval):
    ## create new vote record that is flagged as final
    ## link it to deal via voteDeal table
    ## mark deal stage as one of the done statuses
    ## retunr the db copy of the vote record
    return {}

