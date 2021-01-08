import sys
import random
import time
def sub_calc():
    try:

        # Inputting valid IP address
        while True:
            ip_address = input('Enter an IP address: ')
            ip_octets = ip_address.split('.')
            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break
            else:
                print('\nThe IP address is invalid! Please retry\n')
                continue

        # Inputting valid subnet mask
        while True:
            octets = ''
            count = 0
            subnet_mask = input('Enter a subnet mask: ')
            mask_octets = subnet_mask.split('.')
            if len(mask_octets) == 4:
                for octet in mask_octets:
                    octets = octets + str(bin(int(octet))).lstrip('0b').zfill(8)
                # octets = re.sub('0b', '', octets)
                #print(octets)
                for i in range(len(octets) - 1):
                    if (int(octets[i]) >= int(octets[i + 1])):
                        count = count + 1
                if count == len(octets) - 1:
                    # print('valid')
                    break
                else:
                    print('The subnet mask is invalid! Please try again')
            else:
                print('The subnet mask is invalid! Please try again')

        #Calculating number of valid hosts in a network
        mask_binary_octets = []

        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b').zfill(8)
            mask_binary_octets.append(binary_octet)

        binary_mask = "".join(mask_binary_octets)

        no_of_zeros = binary_mask.count('0')
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)

        #Caclculating Wildcard mask for a network
        wildcard_octets = []
        for octet in mask_octets:
            wildcard_octet = 255 - int(octet)
            wildcard_octets.append(str(wildcard_octet))

        wildcard_mask = ".".join(wildcard_octets)

        #Finding Network and Broadcast address
        ip_address_binary = ''

        for ip_octet in ip_octets:
            ip_octet_binary = bin(int(ip_octet)).lstrip('0b').zfill(8)
            ip_address_binary = ip_address_binary + ip_octet_binary

        network_addr_binary = ip_address_binary[:(no_of_ones)] + '0' * no_of_zeros
        broadcast_addr_binary = ip_address_binary[:(no_of_ones)] + '1' * no_of_zeros

        # Network address
        net_addr_octets = []
        for bit in range(0, 32, 8):
            net_addr_octets.append(str(int(network_addr_binary[bit:bit + 8], 2)))

        net_addr = '.'.join(net_addr_octets)

        #Broadcast address
        broad_addr_octets = []
        for bit in range(0, 32, 8):
            broad_addr_octet = int(broadcast_addr_binary[bit: bit + 8], 2)
            broad_addr_octets.append(str(broad_addr_octet))

        broad_addr = '.'.join(broad_addr_octets)
        print("\n")
        print("Network address is: %s" %net_addr)
        print("Broadcast address is: %s" %broad_addr)
        print("Number of valid hosts in the network: %s" %no_of_hosts)
        print("Wildcard mask is: %s" %wildcard_mask)
        print("Mask bits: %s" %no_of_ones)
        print("\n")

        #Generating random IP address within a network
        while True:
            generate = input('\nGenerate random ip adress from this subnet? (y/n):')
            if generate == 'y' or generate == 'Y':
                geneated_ip = []
                for indexb, oc_broad in enumerate(broad_addr_octets):
                    for indexn, oc_net in enumerate(net_addr_octets):
                        if indexb == indexn:
                            if oc_broad == oc_net:
                                geneated_ip.append(oc_broad)
                            else:
                                geneated_ip.append(str(random.randint(int(oc_net) + 1, int(oc_broad) - 1)))
                random_ip_addr = '.'.join(geneated_ip)
                print("Random IP address is: %s" %random_ip_addr)

            else:
                print("\nOk, Bye!")
                break
    except KeyboardInterrupt:
        print("\n\nProgram aborted by user, bye!")
        sys.exit()
sub_calc()
time.sleep(3)






















