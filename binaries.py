from nltk.tree import Tree as Tree
import stanza

be_verb = ['is','am','was','are','were','can','could','will','would','']
class Binary():
    def __init__(self):
        self.nlp=stanza.Pipeline(processors='tokenize,pos,constituency,lemma', tokenize_pretokenized=True)
        pass
    def main(self,text):
        doc=self.nlp(text)
        text = doc.sentences[0]
        NOT=False
        if 'not' in text.text:
            NOT=True
        tree = Tree.fromstring(str(doc.sentences[0].constituency))
        isBinary=self.isBinary(tree)
        if not isBinary:
            print('can not form binary question!')
            return False
        return (self.bin_q_type(tree,NOT))

    def isBinary(self, tree):
        # can be binary question only if there is a noun and a verb
        NP = 0
        VP = 0
        for t in tree[0]:
            if t.label() == "NP":
                NP = 1
            if t.label() == "VP":
                VP = 1
        is_binary = NP and VP
        return (is_binary)
    
    def bin_q_type(self, tree,NOT=False):
        '''
            If the input has a be-verb we do a be-question
            else we do a 
        '''
        (sentence_structure, text) = self.get_sentence_structure(tree)
        verb_index = sentence_structure.index("VB")
        verb = text[verb_index]
        noun_index = sentence_structure.index("NP")
        if verb in be_verb:
            return self.be_question(text, verb_index, noun_index,NOT)
        else:
            return self.do_question(text, verb_index, noun_index,NOT)
    
    def be_question(self, sentence_by_chunk, verb_index, noun_index,NOT=False):
        verb = sentence_by_chunk[verb_index]
        if NOT:
            del sentence_by_chunk[verb_index+1]
        noun = sentence_by_chunk[noun_index]
        sentence_by_chunk[verb_index] = noun
        sentence_by_chunk[noun_index] = verb
        sentence_by_chunk[-1] = "?"
        sent = " ".join(sentence_by_chunk)
        return sent

    def do_question(self, sentence_by_chunk, verb_index, np_index,NOT=False):
        verb = sentence_by_chunk[verb_index]
        tenses=self.nlp(' '.join(sentence_by_chunk)).sentences[0].words[verb_index].xpos
        if tenses=='VBP':
            tense='present'
            person=1
        elif tenses=='VBD':
            tense='past'
            person=1
        elif tenses=='VBZ':
            tense='present'
            person=3
        else:
            #This means that the code have some problem
            return False
        present_verb=str(self.nlp(verb).sentences[0].words[0].lemma)
        sent = sentence_by_chunk
        sent[verb_index] = present_verb
        if tense == 'past':
            sent.insert(np_index, "did")
        elif tense == 'present' and person == 3:
            sent.insert(np_index, "does")
        else :
            sent.insert(np_index, "do")
        sent[-1]= "?"
        sent = " ".join(sent)
        return sent 
    
    def get_cur_layer(self,tree):
        '''
            This basically gets all the text in this
            particular layer
        '''
        res=[]
        for t in tree:
            res.append(" ".join(t.leaves()))
        return res
    
    def get_sentence_structure(self, tree):
        sentence_structure = []
        sentence_by_chunk = []
        for t in tree[0]:
            if t.label() == "VP":
                sentence_by_chunk += self.get_cur_layer(t)
                sentence_structure += ["VB", "OTHER"]
            else:
                sentence_by_chunk.append(" ".join(t.leaves()))
                sentence_structure.append(t.label())
        #print(sentence_structure, sentence_by_chunk)
        return (sentence_structure, sentence_by_chunk)

print(Binary().main('Is your name Sunaya .'))



