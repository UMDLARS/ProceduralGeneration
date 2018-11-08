# Procedural Content Generation for Capture The Flag competitions (PCGCTF)

This project has three core components. These are the topology generator, the vulnerability injector, and the image creator. 

## Topology Generator

This component is responsible for creating realistic business-network
topologies. Topologies are represented as graphs, where nodes are the machines
in the topology and edges are physical links between machines. 

The generator can be run like this: 

`TODO: example usage`

and generates JSON in this form:

```
{
	"nodes": [ 
		{
			id: this_nodes_id,
			edges: [other_node_id, some_other_node_id],
			type: type_of_node(server, end user, etc),
			traffic_generators: [list of traffic generation utilities to use and their targets]
		}
	]
}
```

## Vulnerability Injector

This component is responsible for generating a path of vulnerabilities through
a topology such that there is a path from node `start` to node `end`. It will
also assign vulnerability types to nodes on the path from `start` to `end` such
that the path can be traversed. 

```
{
	"start": some_node_id,
	"end": some_node_id,
	"nodes": [ 
		{
			id: this_nodes_id,
			edges: [other_node_id, some_other_node_id],
			type: type_of_node(server, end user, etc),
			vulnerability_classs: [OPEN_TELNET, DEFAULT_MYSQL_CREDENTIALS] 
			traffic_generators: [list of traffic generation utilities to use and their targets]
		}
	]
}
```

## Image creator

This component takes a graph representation output by either the topology
generator or the vulnerability injector and attempts to create it.

Eventually it will use docker compose and dockerfiles to build vulnerable
images but this is a stretch goal.

## Setup

This project uses pipenv to handle dependencies. Run `pipenv install` to
install the project, then `pipenv shell` to run the python scripts in this
environment. 

To run the topology generator, run `python topology_generator.py`

To run the vulnerability injector, run `python injector.py`

For now, see the images as simple examples but don't try to use them, they are
just examples of how we can use docker to easily create our images.
