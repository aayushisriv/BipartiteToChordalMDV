"""
@author- Aayushi Srivastava
This code converts bipartite graph directly into Chordal Graph using Minimum Degree Vertex heuristic


"""

import networkx as nx 
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
import copy
import random

import operator
import itertools

class BipartCh:

	def __init__(self,noNodes1, noNodes2,noEdges):
		self.noNodes1 = noNodes1
		self.noNodes2 = noNodes2
		self.noEdges = noEdges
		self.GEdgeList = []
		self.HEdgeList = []
		self.G = {}
		self.H = {}
		self.vertexList1 = []
		self.vertexList2 = []
		self.vertexLstcom = []
		self.NEdgeList = []	


	def createBipartiteGraph(self):
		"""create bipartite graph"""
		self.G = bipartite.gnmk_random_graph(self.noNodes1,self.noNodes2,self.noEdges)

		if type(self.G) is not dict:
			self.G = nx.to_dict_of_lists(self.G)
			print self.G
		for key,value in self.G.iteritems():
			for v in value:
				if key < v:
					e = []
					e.append(key)
					e.append(v)
					self.GEdgeList.append(e)
		self.G = nx.Graph(self.G)
		#self.checkChain(self.G)
		for i in range (0,self.noNodes1):
			self.vertexList1.append(i)
		for j in range(self.noNodes1,(self.noNodes1+self.noNodes2)):
			self.vertexList2.append(j)
			#print "M list",self.vertexList2
		self.vertexLstcom = self.vertexList1 + self.vertexList2
		print "Entire vertexlist : ",self.vertexLstcom
		self.plotBipartGraph(self.G)
		self.createChrdG(self.vertexLstcom)


	def plotBipartGraph(self, graphpl):
		"""plot bipartite graph""" 
		self.G = nx.Graph(self.G)
		GD = nx.Graph(self.G)
		pos = nx.spring_layout(GD)
		nx.draw(GD,pos,width=8.0,with_labels=True)
		plt.draw()
		plt.show()


	def createChrdG(self,vtlist):
		"""function to start MDV"""
		self.HEdgeList = copy.deepcopy(self.GEdgeList)
		self.H = copy.deepcopy(self.G)
		self.H = nx.Graph(self.H)

		print "Start Minimum Vertex Process"
		self.Minvertex(vtlist,self.HEdgeList,self.H)
		self.FinalGraph(self.G,self.NEdgeList,vtlist)
		print "End Minimum Vertex Process"
		return True
		#self.FinalGraph(self.G,self.NEdgeList,self.vertexList)



	def Minvertex(self,vertexList,edgeList, graphtoCons):
		"""MDV is applied on bipartite graph"""
		graphtoCons = nx.Graph(graphtoCons)
		self.H = nx.Graph(self.H)
		#isChordal = False
		#self.H = nx.Graph(self.H)
		random.shuffle(vertexList)
		self.H = nx.Graph(self.H)
		for v in vertexList:
			#print "check type"
			#print type(self.H)
			self.H = nx.Graph(self.H)
			dv = list(self.H.degree(self.H)) #list of tuples
			#print "see the list:"
			print dv
		#pd = len(dv)
		#print pd
			#print self.HEdgeList
			dvdict = dict(dv)
			#print "Dictionary of node-degree is", dvdict
			self.minv = dict(sorted(dvdict.items(), key=lambda kv:(kv[1], kv[0])))
			#print "Sorted dictionary of node-degree:",self.minv
			self.H = nx.to_dict_of_lists(self.H)
			#print "The dictionary looks like:", self.H
			mincp = copy.deepcopy(self.minv)
			try:
				for key,value in mincp.iteritems():
					if value < 2:
				#del minv[key]
						self.minv.pop(key)
				#print "Deleted"
				#print "Updates:",self.minv
				graphtoCons = nx.Graph(graphtoCons)
				self.H = nx.Graph(self.H)
				nodeH = self.H.nodes()
				#print "Old Nodes are:",nodeH
				#print "New nodes are",list(self.minv)
				self.H.add_nodes_from(list(self.minv))
				self.H.remove_nodes_from(list(list(set(nodeH) - set(list(self.minv)))))
				self.H = nx.to_dict_of_lists(self.H)
				#print "New Dictionary:",self.H
				self.m_vert = min(self.minv.keys(), key=(lambda k:self.minv[k]))
				#print type(self.m_vert)
				print "Minimum degree vertex is:",self.m_vert
				#print type(self.H)
				self.H = nx.Graph(self.H)
				#self.H = nx.Graph(self.H)
				print "The chosen Minimum vertex is", self.m_vert
				
				self.neb = list(self.H.neighbors(self.m_vert))
				print "Neighbors of the chosen vertex are:",self.neb
				neblen = len(self.neb)
				
				self.H = nx.Graph(self.H)
				self.H.remove_node(self.m_vert)
				self.neighbcomp(self.m_vert,self.H)

				self.H = nx.Graph(self.H)
			except ValueError as e:
				print "Dictionary is Empty now"
				break
		#self.FinalGraph(self.G,self.NEdgeList,self.vertexList)

	def neighbcomp(self,chosvert,graphtoRecreate):
		"""Making neighbors clique"""
		#eb = 0
		self.H = nx.Graph(self.H)
		nebcomb = list(itertools.combinations(self.neb,2))
		#print "See combinations:",nebcomb
		for p in nebcomb:
			v1 =  p[0]
			v2 = p[1]
			#print p
			if self.H.has_edge(*p) :
				#print p
				#print "Already edge is there"
				continue
			else:
				self.H.add_edge(*p)
				#print "Check this"
				self.NEdgeList.append(p)
				#print "My list", self.NEdgeList
				continue
		print "Edges added using Minimum Degree",len(self.NEdgeList)

		self.H= nx.to_dict_of_lists(self.H)
		#print "See change",self.H
		#self.graphtoRecreate = nx.to_dict_of_lists(graphtoRecreate)

	#def FG(self):
		#print "Run the graph once:"
		#self.FinalGraph(self.G,self.NEdgeList,self.vertexList)
		
	

	def FinalGraph(self,graphVerify,newaddedgelist,vertexlist):
		"""Plot chordal graph"""
		print "EdgeList verifying",newaddedgelist
		print "Total Edges added in Minimum Degree Process is ",len(newaddedgelist)
		GD = nx.Graph(self.G)
		pos = nx.spring_layout(GD)

		B = copy.deepcopy(self.G)
		B = nx.Graph(B)
		B.add_nodes_from(vertexlist)
		B.add_edges_from(newaddedgelist)
		B = nx.to_dict_of_lists(B)
		print "see B", B
		##Recognition----
		graph = nx.Graph(B)
		print type(B)
		if nx.is_chordal(graph):
			print "IT IS CHORDAL"
		else :
			print "NO IT IS NOT CHORDAL"
		#print "Draw graph"
		nx.draw_networkx_nodes(GD, pos, nodelist=vertexlist, node_color='red', node_size=300, alpha=0.8,label='Min degree')	
		nx.draw_networkx_edges(GD, pos, width=1.0, alpha=0.5)
		nx.draw_networkx_edges(GD, pos, edgelist=newaddedgelist, width=8.0, alpha=0.5, edge_color='blue',label='Min degree')
		nx.draw_networkx_labels(GD,pos)
		plt.draw()
		plt.show()	



"""Input from command prompt"""
val1 = int(raw_input("Enter no. of nodes in first part of graph:"))
val2 = int(raw_input("Enter no. of nodes in second part of graph:"))
val3 = int(raw_input("Enter no. of edges:"))
gvert = BipartCh(val1,val2,val3)
gvert.createBipartiteGraph() 