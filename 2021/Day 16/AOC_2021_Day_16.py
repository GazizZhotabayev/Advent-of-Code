import os, sys

file_name = 'input_day_16.txt'
day = file_name.split('.')[0].split('_')[-1]

with open(os.path.join(sys.path[0], file_name)) as f:
    PACKET = ''.join(bin(int(h, 16))[2:].zfill(4) for h in f.read())

    #PACKET = '00111000000000000110111101000101001010010001001000000000'
    #PACKET = '11101110000000001101010000001100100000100011000001100000'
    #PACKET = ''.join(bin(int(h, 16))[2:].zfill(4) for h in 'C0015000016115A2E0802F182340')
    def parse(packet):

        if len(packet) < 8: return 0
        
        version = int(packet[:3], 2)
        type_id = int(packet[3:6], 2)

        if type_id == 4:
            packet = packet[6:]

            #parse 5 bits at a time, until we encounter a 0 in the first bit
            literal = ''
            while True:
                literal += packet[1:5]
                first_bit = packet[0]
                packet = packet[5:]
                if first_bit == '0': #encountered the last group
                    break
            
            literal = int(literal, 2)
            return version + parse(packet)

        else:
            length_type_id = packet[6]
            
            if length_type_id == '0':
                total_length = int(packet[7:22], 2)
                return version + parse(packet[22:22+total_length]) + parse(packet[22+total_length:])
            elif length_type_id == '1':
                number_subpackets = int(packet[7:18], 2)
                packet = packet[18:]
                return version + parse(packet)
            else:
                print(f"unexpected length type id: {length_type_id}")

    
    ans1 = parse(PACKET, 1)
    print(f'answer to first puzzle of day {day} is: {ans1}')

    ans2 = 0
    print(f'answer to second puzzle of day {day} is: {ans2}')
