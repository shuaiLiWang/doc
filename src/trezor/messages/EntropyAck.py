# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('EntropyAck')
t.wire_type = const(36)
t.add_field(1, 'entropy', p.BytesType)
EntropyAck = t