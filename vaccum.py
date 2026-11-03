
# Environment
environment = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Initial location
location = 'A'

# Simple Reflex Agent
def vacuum_agent(location, status):

    if status == 'Dirty':
        return 'Suck'

    elif location == 'A':
        return 'Move Right'

    elif location == 'B':
        return 'Move Left'


# Execute the agent
for step in range(6):

    status = environment[location]

    action = vacuum_agent(location, status)

    print("Step:", step + 1)
    print("Location:", location)
    print("Status:", status)
    print("Action:", action)

    if action == 'Suck':
        environment[location] = 'Clean'

    elif action == 'Move Right':
        location = 'B'

    elif action == 'Move Left':
        location = 'A' 

    print("Updated Environment:", environment)
    print("--------------------------")

print("Final Environment:", environment)
