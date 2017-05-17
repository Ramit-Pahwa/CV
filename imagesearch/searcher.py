import numpy

class Searcher:
	def __init__(self,index):
		self.index=index

	def search(self,queryFeatures):
		results={}
		for (k,features) in self.index.items():
			d=self.chi2distance(features,queryFeatures)
			results[k]=d
		# sort the list so min distance is top of the list
		results=sorted(results.items,key=itemgetter(1))
		# results=sorted([(v,k) for (k,v) in results.items()])
		return results


	def chi2distance(self,histA,histB,eps=1e-10):
		dist=0.5*np.sum([(a-b)**2/(a+b+eps) for (a,b) in zip(histA,histB)])
		return dist