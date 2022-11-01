from nltk.tree import Tree as Tree
from binaries import Binary
import stanza
class Why:
    def __init__(self,pipeline) -> None:
        self.nlp=pipeline
        pass
    def is_why(self, tree):
        for t in tree.subtrees(lambda t: t.label() == "SBAR"):
            if "because" in t.leaves() or "since" in t.leaves() or "so" in t.leaves():
                    return True
        return False
        
    def remove_SBAR(self, tree):
        '''
            This removes the subtree, but also stores
            the subtree inside answer, and it is ready
            to be used as an Answer.
        '''
        sentence_structure = []
        sentence_by_chunk = []
        answer=[]
        for t in tree[0]:
            if t.label() != "SBAR" and t.label() != "VP" and t.label() != ",":
                sentence_by_chunk.append(" ".join(t.leaves()))
                sentence_structure.append(t.label())
            elif t.label() == "VP":
                for subtree in t:
                    if subtree.label() != "SBAR":
                        sentence_by_chunk.append(" ".join(subtree.leaves()))
                        print(sentence_by_chunk)
                        sentence_structure.append(subtree.label())
                    else:
                        for subsubtree in subtree:
                            print('subsub',subsubtree.label())
                            answer.append(" ".join(subsubtree.leaves()))
        return (sentence_structure, sentence_by_chunk,answer)

    def main(self, text):
        tree = self.nlp(text[0]).sentences[0].constituency
        tree = Tree.fromstring(str(tree))
        print(tree)
        if not self.is_why(tree):
            print ("It could not be converted to why question.")
            return None 
        (sentence_structure, sentence_by_chunk,answer) = self.remove_SBAR(tree)
        sent = " ".join(sentence_by_chunk)
        answer=' '.join(answer)
        print(sent)
        sent = Binary().main(sent)
        print(sent)
        return ["Why " + sent,text[1],answer]
