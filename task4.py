access_template = ['switchport mode access {}', 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk allowed vlan{}']


inter_mode = input("Enter interface mode(access/trunk): ")



if inter_mode == "access":

    type_number = input("Enter interface type and number: ")

    vlan_number = input("Enter VLAN number: ")

    print ("Interface", type_number)
    print ("swichport mode access", inter_mode)
    print ("switchport access vlan", vlan_number)
    print ("spanning-tree bpduguard enable")

elif inter_mode == "trunk":

    type_number = input("Enter interface type and number: ")

    vlan_numbers = input("Enter allowed VLANs: ")

    print("Interface", type_number)
    print("swichport mode access", inter_mode)
    print("switchport trunk allowed vlan", vlan_numbers)
    print("switchport trunk encapsulation dot1q")

else:

    print ("wrong iput, please try again later")