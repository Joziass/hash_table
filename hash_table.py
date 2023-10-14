# -*- coding: utf-8 -*-


class Hash_table:
    def __init__(self, s):
        self.size = int(s* 0.1)
        self.T = [[[] for _ in range(self.size)] for _ in range(10)]
        
     
    def __hash_str(self, key_str):
        num = 0
        for c in key_str:
            num += ord(c)
        return num
    
    def __hash(self, key_str):
        key = self.__hash_str(key_str)
        return key % self.size
    
    def _10_hash(self, key_str):
        key = self.__hash_str(key_str)
        return key % 10
    
    def insert(self, key, value):
        pos = self._10_hash(key)
        pos2 = self.__hash(key)
        self.T[pos][pos2].append(value)
    
    def get(self, key):
        pos = self._10_hash(key)
        pos2 = self.__hash(key)
        L = self.T[pos][pos2]
        for value in L:
            if(value.nome == key):
                return value
        return None
            
    def print(self):
        print("{")
        for j in range(10):
            for i in range(self.size):
                alunos = self.T[j][i]
                _str = ""
                for aluno in alunos:
                    _str += aluno.to_string() + " "
                    print("[" + _str + "]")
        
        print("}")

