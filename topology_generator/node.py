import uuid
import sys
from enum import Enum, auto

from marshmallow import Schema, fields, post_load
from marshmallow_enum import EnumField

#This allows us to import from vulnerabilities
sys.path.append('../vulnerability_injector')

from vulnerabilitytype import VulnerabilityType

class NodeType (Enum):
    SERVER = auto()
    ENDUSER = auto()

class TrafficGeneratorType (Enum):
    NOTRAFFIC = auto()

class Node:
    """Represents a Node in a topology"""
    def __init__(self, type: NodeType, traffic_gen=[], edges=[], id=None, vulnerabilities=[]):
        """ Initialize a new node on the topology
        
        Args: 
            type = Type of this node
            traffic_gen = list of traffic generators this node will run
            edges = IDs of nodes this node has edges with
            id = id of this node (if it has one)
            vulnerabilities = list of vulnerabilities for this node
        """
        if not id:
            self.id = uuid.uuid4()
        else:
            self.id = id

        self.type = type
        self.traffic_gen = traffic_gen
        self.edges = edges
        self.vulnerabilities = vulnerabilities

class NodeSchema(Schema):
    """Marshmallow schema for JSON serialization of Node class"""
    id = fields.UUID()
    type = EnumField(NodeType)
    traffic_gen = fields.List(EnumField(TrafficGeneratorType))
    edges = fields.List(fields.UUID())
    vulnerabilities = fields.List(EnumField(VulnerabilityType))

    @post_load
    def make_node(self, data):
        return Node(**data)
