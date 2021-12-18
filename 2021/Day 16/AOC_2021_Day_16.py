import os, sys
from functools import reduce
import json

file_name = 'input_day_16.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    PACKET = ''.join(bin(int(h, 16))[2:].zfill(4) for h in f.read())

    #PACKET = ''.join(bin(int(h, 16))[2:].zfill(4) for h in 'C200B40A82')

    def parse(packet):

        if len(packet) < 8: return []
        
        d = {key: None for key in "version type_id".split()}
        d['version'] = int(packet[:3], 2)
        d['type_id'] = int(packet[3:6], 2)
        
        if d['type_id'] == 4:
            packet = packet[6:]

            #parse 5 bits at a time, until we encounter a 0 in the first bit
            literal = ''
            while True:
                literal += packet[1:5]
                first_bit = packet[0]
                packet = packet[5:]
                if first_bit == '0': #encountered the last group
                    break
            
            d['value'] = int(literal, 2)
            d['class'] = 'literal'
            ans = [d]
            ans.extend(parse(packet))
        else:
            d['length_type_id'] = packet[6]
            d['class'] = 'operator'
            d['subpackets'] = []

            if d['length_type_id'] == '0':
                total_length = int(packet[7:22], 2)
                d['total_length'] = total_length
                d['subpackets'] += parse(packet[22:22+total_length])
                packet = packet[22+total_length:]
                ans = [d]
                ans.extend(parse(packet))
            else:
                number_subpackets = int(packet[7:18], 2)
                d['num_subpackets'] = number_subpackets
                packet = packet[18:]
                x = parse(packet)
                d['subpackets'] = x[:number_subpackets]
                ans = [d]
                ans.extend(x[number_subpackets:])

        return ans

    def sum_versions(packet):
        if packet['class'] == 'literal': return packet['version']
        else: return packet['version'] + sum(sum_versions(subpacket) for subpacket in packet['subpackets'])

    def evaluate(packet):
        mul = lambda lst: reduce(lambda x,y:x*y, lst)
        if packet['type_id'] == 0:
            return sum(evaluate(subpacket) for subpacket in packet['subpackets'])
        elif packet['type_id'] == 1:
            return mul([evaluate(subpacket) for subpacket in packet['subpackets']])
        elif packet['type_id'] == 2:
            return min(evaluate(subpacket) for subpacket in packet['subpackets'])
        elif packet['type_id'] == 3:
            return max(evaluate(subpacket) for subpacket in packet['subpackets'])
        elif packet['type_id'] == 4:
            return packet['value']
        elif packet['type_id'] == 5:
            return 1 if evaluate(packet['subpackets'][0]) > evaluate(packet['subpackets'][1]) else 0
        elif packet['type_id'] == 6:
            return 1 if evaluate(packet['subpackets'][0]) < evaluate(packet['subpackets'][1]) else 0
        elif packet['type_id'] == 7:
            return 1 if evaluate(packet['subpackets'][0]) == evaluate(packet['subpackets'][1]) else 0
        else:
            pass

    PACKET = parse(PACKET)[0]
    #print(json.dumps(PACKET, indent=4))

    ans1 = sum_versions(PACKET)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = evaluate(PACKET)
    print(f'answer to second puzzle of day {day} is: {ans2}')
