class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for path in paths:
            files = path.split(' ')
            directory = files[0]
            for file in files[1:]:
                name, content = file.split('(')
                hashmap[content[:-1]].append(directory + '/' + name)                
        return [hashmap[content] for content in hashmap if len(hashmap[content]) > 1]
        