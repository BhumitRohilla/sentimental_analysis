
class QueryConstructor:
    def __init__(self, hashTag, keyWords, handle):
        self.hashTag = hashTag
        self.keyWords = keyWords
        self.handle = handle

    def createQuery(self):
        query = ""
        if len(self.hashTag):
            query += " OR ".join(self.hashTag)

        if len(self.keyWords):
            keyWordQuery = ""
            for index, keyword in enumerate(self.keyWords):
                if index != 0:
                    keyWordQuery +=  " OR "
                keyWordQuery += f'"{keyword}"'
            
            if len(query) != 0:
                query += " OR " + keyWordQuery
        
        if len(self.handle):
            handleQuery = ""
            if len(self.handle):
                for index, handle in enumerate(self.handle): 
                    if index != 0:
                        handleQuery +=  " OR "
                    handleQuery += handle
                
                if len(query) != 0:
                    query += " OR " + handleQuery

        return query