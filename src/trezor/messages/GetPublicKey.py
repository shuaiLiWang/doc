# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('GetPublicKey')
t.wire_type = const(11)
t.add_field(1, 'address_n', p.UVarintType, flags=p.FLAG_REPEATED)
t.add_field(2, 'ecdsa_curve_name', p.UnicodeType)
t.add_field(3, 'show_display', p.BoolType)
GetPublicKey = t