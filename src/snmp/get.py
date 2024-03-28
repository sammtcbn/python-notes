# Note: pip3 install pysnmp
from pysnmp.hlapi import *

def snmp_get(ip, oid, community='public', port=161):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        print(errorIndication)
        return None
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        return None
    else:
        for varBind in varBinds:
            return varBind[1].prettyPrint()


# Example usage
ip_address = '192.168.1.2'
oid = '1.3.6.1.2.1.1.1.0'  # Example OID for system description
community_string = 'private'

result = snmp_get(ip_address, oid, community_string)
if result is not None:
    print("Result:", result)
else:
    print("Failed to retrieve the value.")
