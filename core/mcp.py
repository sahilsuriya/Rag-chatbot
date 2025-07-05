# core/mcp.py

class MCPMessage:
    def __init__(self, sender, receiver, message_type, trace_id, payload):
        self.sender = sender
        self.receiver = receiver
        self.message_type = message_type
        self.trace_id = trace_id
        self.payload = payload

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "type": self.message_type,
            "trace_id": self.trace_id,
            "payload": self.payload
        }
