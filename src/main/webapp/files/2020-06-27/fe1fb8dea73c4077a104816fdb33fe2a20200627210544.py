#!/usr/bin/env python
""" generated source for module test """
from __future__ import print_function
class Words(object):
    """ generated source for class Words """
    key = HashMap()
    boundarySign = HashMap()
    operator = HashMap()
    KEY = "tag"
    OPERATOR = "op"
    STRING_CONST = "600"
    INT_CONST = "400"
    DOUBLE_CONST = "800"
    CHAR_CONST = "500"
    IDENTIFIER = "700"
    BOUNDARYSIGN = "jie"
    END = "end"
    UNIDEF = "weizhi"

    # sample
    # 
    # sample
    # sample
    id = int()
    word = None
    length = int()
    type_ = None
    attribute = None
    value = None
    address = int()
    line = int()
    flag = True

    def __init__(self, wordCount, word, line, type_):
        """ generated source for method __init__ """
        setId(wordCount)
        self.setWord(word)
        setValue(None)
        setLength(len(word))
        setType(None)
        self.attribute = self.UNIDEF
        if type_ == 0:
            self.attribute = self.BOUNDARYSIGN
        if type_ == 3:
            self.attribute = self.CHAR_CONST
        if type_ == 4:
            self.attribute = self.STRING_CONST
        iter = self.key.entrySet().iterator()
        while type_ == 6 and iter.hasNext():
            entry = iter.next()
            key = entry.getKey()
            val = str(entry.getValue())
            if val == word:
                self.attribute = self.KEY
                break
        if self.attribute == self.UNIDEF and type_ == 6:
            self.attribute = self.IDENTIFIER
        if self.attribute == self.UNIDEF and type_ == 0:
            iter = self.boundarySign.entrySet().iterator()
            while iter.hasNext():
                entry = iter.next()
                key = entry.getKey()
                val = str(entry.getValue())
                if val == word:
                    self.attribute = self.BOUNDARYSIGN
                    break
        if self.attribute == self.UNIDEF and type_ == 1:
            iter = self.operator.entrySet().iterator()
            while iter.hasNext():
                entry = iter.next()
                key = entry.getKey()
                val = str(entry.getValue())
                if val == word:
                    self.attribute = self.OPERATOR
                    break
        if self.attribute == self.UNIDEF and type_ == 5:
            if isInteger(word):
                setValue(word)
                self.attribute = self.INT_CONST
            else:
                setValue(word)
                self.attribute = self.DOUBLE_CONST
        self.setLine(line)
        setAddress(-1)
        self.flag = True

    @classmethod
    def isBinaryOperator(cls, op):
        """ generated source for method isBinaryOperator """
        flag = False
        iter = cls.operator.entrySet().iterator()
        while iter.hasNext():
            entry = iter.next()
            key = entry.getKey()
            val = str(entry.getValue())
            if val == op:
                flag = True
                break
        return flag

    @classmethod
    def isInteger(cls, word):
        """ generated source for method isInteger """
        i = 0
        flag = False
        if word.charAt(0) == '+' or word.charAt(0) == '-':
            i = 1
        while i < len(word):
            if Character.isDigit(word.charAt(i)):
                i += 1
                continue 
            else:
                break
            i += 1
        if i == len(word):
            flag = True
        return flag

    @classmethod
    def isChar(cls, word):
        """ generated source for method isChar """
        flag = False
        i = 0
        temp = word.charAt(i)
        if temp == '\'':
            while i < len(word):
                temp = word.charAt(i)
                if 0 <= temp and temp <= 255:
                    i += 1
                    continue 
                else:
                    pass
                i += 1
            if i + 1 == len(word) and word.charAt(i) == '\'':
                flag = True
        else:
            return flag
        return flag

    def getAttr(self):
        """ generated source for method getAttr """
        return self.attribute

    def setAttr(self, attribute):
        """ generated source for method setAttr """
        self.attribute = attribute

    def getWord(self):
        """ generated source for method getWord """
        return self.word

    def setWord(self, word):
        """ generated source for method setWord """
        self.word = word

    def getLine(self):
        """ generated source for method getLine """
        return self.line

    def setLine(self, line):
        """ generated source for method setLine """
        self.line = line

    def getId(self):
        """ generated source for method getId """
        return self.id

    def setId(self, id):
        """ generated source for method setId """
        self.id = id

    def getLength(self):
        """ generated source for method getLength """
        return self.length

    def setLength(self, length):
        """ generated source for method setLength """
        len(length)

    def getType(self):
        """ generated source for method getType """
        return self.type_

    def setType(self, type_):
        """ generated source for method setType """
        self.type_ = type_

    def getValue(self):
        """ generated source for method getValue """
        return self.value

    def setValue(self, value):
        """ generated source for method setValue """
        self.value = value

    def getAddress(self):
        """ generated source for method getAddress """
        return self.address

    def setAddress(self, address):
        """ generated source for method setAddress """
        self.address = address

