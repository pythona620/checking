def  enter_source_destination(stops):
    while True:
        source = input('Enter your boarding bus stop: ')
        if source in stops:
            while True:
                destination = input('Enter your destination: ')
                if destination in stops:
                    return source, destination
                else:
                    print('Could you please enter a valid destination stop')
                    continue
        else:
            print('Could you please enter a valid boarding point')
            continue

stops = ['vizag', 'hyderabad', 'vijayawada']
source, destination = enter_source_destination(stops)
print('The sourceing point is ', source, 'and the destination is ', destination)
