# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('PinMatrixRequest')
t.wire_type = const(18)
t.add_field(1, 'type', p.UVarintType)
PinMatrixRequest = t