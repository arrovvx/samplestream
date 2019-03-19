import random

random.seed(319);

def pickSamples(samples, stream):
	
	count = 0
	item = stream.pop()
	for val in samples:
		samples[count] = item
		count += 1
		item = stream.pop()
		
	while True:
		replaceIdx = random.randint(0,count)
		if replaceIdx <= len(samples) - 1:
			samples[replaceIdx] = item
		
		try:
			count += 1
			item = stream.pop()
		except Exception:
			print(samples)
			print("end stream")
			break

	
pickSamples([11,12],[1,2,3,4,5,6,7])