def findDuplicateChars(word):
	hashMap = {}
	for c in word:
		if c in hashMap.keys():
	    	hashMap[c] = int(hashMap[c]) +1
		else:
			hashMap[c] = 1
	return hashMap
  
