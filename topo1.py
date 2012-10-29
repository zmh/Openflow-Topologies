from mininet.topo import Topo, Node

class MyTopo(Topo):
	# "Q1"
	def __init__(self, enable_all = True): 
		# "Custom topo for Q1"
		super(MyTopo, self).__init__()
		
		s1 = 1
		s2 = 2
		s3 = 3
		s4 = 4
		s5 = 5
		h6 = 6
		h7 = 7
		h8 = 8
		h9 = 9
		h10 = 10
		
		self.add_node( s1, Node( is_switch=True ) )
		self.add_node( s2, Node( is_switch=True ) )
		self.add_node( s3, Node( is_switch=True ) )
		self.add_node( s4, Node( is_switch=True ) )
		self.add_node( s5, Node( is_switch=True ) )

		self.add_node( h6, Node( is_switch=False ) )
		self.add_node( h7, Node( is_switch=False ) )
		self.add_node( h8, Node( is_switch=False ) )
		self.add_node( h9, Node( is_switch=False ) )
		self.add_node( h10, Node( is_switch=False ) )

		self.add_edge( s1, h6, delay=100 ) 
		self.add_edge( s1, h7 )
		self.add_edge( s5, h9 )
		self.add_edge( s4, h10, delay=10 )
		self.add_edge( s3, h8, delay=5 )
		self.add_edge( s1, s2, delay=50 )
		self.add_edge( s2, s3, delay=20 )
		self.add_edge( s3, s4, delay=5 )
		self.add_edge( s2, s5 )

		self.enable_all()

topos = {'topo1': (lambda: MyTopo() ) }