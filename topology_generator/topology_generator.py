import json
import sys
from marshmallow import pprint

#This allows us to import from images
sys.path.append('../')

from node import Node, NodeType, NodeSchema
from topology import Topology, TopologySchema 

def design_topology(options):
    """ Given a list of options, generate a topology"""
    num_nodes = options["nodes"]
    topology = Topology()
    for n in range(0, num_nodes):
        node = Node(NodeType.SERVER)
        topology.add_node(node)
    return topology

def read_options():
    return default_options()

def default_options():
    return { "nodes": 2 }

def json_encode_topology(topology, pretty=False):
    return topology

def main():
    opts = read_options()
    topology = design_topology(opts)
    json_topo = json_encode_topology(topology, pretty=True)
    data, errors = TopologySchema().dumps(topology)
    pprint(data)
    open('data.json', 'w').write(data)


if __name__ == "__main__":
    main()

