from mininet.topo import Topo, Node

class MyTopo(Topo):
	# "Q-dos"
	def __init__(self, enable_all = True): 
		# "Custom topo for Q2"
		super(MyTopo, self).__init__()
		
		delay_constant = 1

		s11 = 11
		s12 = 12
		s14 = 14
		s16 = 16
		s18 = 18
		h13 = 13
		h15 = 15
		h17 = 17
		h19 = 19
		
		self.add_node( s11, Node( is_switch=True ) )
		self.add_node( s12, Node( is_switch=True ) )
		self.add_node( s14, Node( is_switch=True ) )
		self.add_node( s16, Node( is_switch=True ) )
		self.add_node( s18, Node( is_switch=True ) )

		self.add_node( h13, Node( is_switch=False ) )
		self.add_node( h15, Node( is_switch=False ) )
		self.add_node( h17, Node( is_switch=False ) )
		self.add_node( h19, Node( is_switch=False ) )
		
		self.add_edge( s12, s14, delay=delay_constant ) 
		self.add_edge( s11, s12, delay=delay_constant ) 
		self.add_edge( s11, s18, delay=delay_constant ) 
		self.add_edge( s16, s18, delay=delay_constant ) 
		self.add_edge( s16, s14, delay=delay_constant ) 
		self.add_edge( s14, s18, delay=delay_constant ) 
		self.add_edge( s12, s16, delay=delay_constant ) 
		self.add_edge( s12, s18, delay=delay_constant ) 
		self.add_edge( s18, h19, delay=delay_constant ) 
		self.add_edge( s16, h17, delay=delay_constant ) 
		self.add_edge( s14, h15, delay=delay_constant ) 
		self.add_edge( s12, h13, delay=delay_constant ) 
		
		self.enable_all()

topos = {'topo2': (lambda: MyTopo() ) }