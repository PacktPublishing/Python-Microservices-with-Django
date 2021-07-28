from pubsub import pub
def listener_mayank(arg):
    print('Mayank receives message about', arg['script'])
    print(arg['price'])
    print()
 
def listener_shayank(arg):
    print('Shayank receives message about', arg['script'])
    print(arg['price'])
    print()
 
# Register listeners
pub.subscribe(listener_mayank, 'share price')
pub.subscribe(listener_shayank, 'share tip')
pub.subscribe(listener_shayank, 'share price')
 
# Send messages to all listeners of topics
pub.sendMessage('share price', arg={'script': 'TCS', 'price': '3200'})
pub.sendMessage('share tip', arg={'script': 'ITC', 'price': '205'})
pub.sendMessage('share price', arg={'script': 'INFY', 'price': '1400'})