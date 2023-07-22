#dictionary : a unordered , changable, can access a value



capitals = {'USA':'wASHINGTON DC',
            'INDIA':'DELHI',
            'RUSSIA':'MOSCOW'}

capitals.update({'germany':'berlin'})
capitals.update({'USA':'LAS VEGAS'})

capitals.pop('INDIA')
#print(capitals['RUSSIA'])
#
# print(capitals.get('germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
for key,values in capitals.items():
    print(key, values)
