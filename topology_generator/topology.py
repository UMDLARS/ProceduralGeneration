from node import Node, NodeType, NodeSchema

# For json encoding
from marshmallow import Schema, fields, post_load
class Topology:
    """Represent a topology graph"""
    def __init__(self, nodes=[]):
        """Create an empty network topology"""
        self.nodes = nodes

    def add_node(self, node):
        """Add a node to the topology
        Args: 
        node = The node to add.
        """
        self.nodes.append(node)

class TopologySchema(Schema):
    """Marshmallow schema for JSON serialization of the Topology class"""
    nodes = fields.Nested(NodeSchema, many=True)

    @post_load
    def make_topology(self, data):
        return Topology(**data)

