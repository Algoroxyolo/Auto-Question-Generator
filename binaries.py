from nltk.tree import Tree as Tree
import stanza

be_verb = ['is','am','was','are','were','can','could','will','would']
class Binary():
    def __init__(self):
        self.nlp=stanza.Pipeline(processors='tokenize,pos,constituency,lemma', tokenize_pretokenized=True)
        pass
    def main(self,text):
        '''
            Determine if the text is a Not sentence or not.
            Put the sentence into parse tree and through the tree
            inside the is_binary function, if it can be turned
            into a binary question, then turn it into a do question
            or is question.
        '''
        doc=self.nlp(text)
        text = doc.sentences[0]
        print(text.text)
        NOT=False
        if 'not' in text.text:
            NOT=True
        tree = Tree.fromstring(str(doc.sentences[0].constituency))
        isBinary=self.isBinary(tree)
        if not isBinary:
            print('can not form binary question!')
            return False
        return (self.question_type(tree,NOT))

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
        return is_binary
    
    def question_type(self, tree,NOT=False):
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
        '''
            Find verb;delete NOT; swap verb and noun
        '''
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
        '''
            Find verb;find verb tense; change verb tense into present
            Set do tense; add do in front 
        '''
        verb = sentence_by_chunk[verb_index]
        print(' '.join(sentence_by_chunk))
        tenses=self.nlp(verb).sentences[0].words[0].xpos
        print(tenses)
        if tenses=='VBP'or tenses=='VB':
            tense='present'
            person=1
        elif tenses=='VBN':
            tense='past'
            person=1
        elif tenses=='VBZ':
            tense='present'
            person=3
        else:
            print(verb,tenses)
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
        '''
            Spliting the sentences based on sentence structure.
        '''
        sentence_structure = []
        sentence_by_chunk = []
        for t in tree[0]:
            if t.label() == "VP":
                sentence_by_chunk += self.get_cur_layer(t)
                sentence_structure += ["VB", "OTHER"]
            else:
                sentence_by_chunk.append(" ".join(t.leaves()))
                sentence_structure.append(t.label())

        return (sentence_structure, sentence_by_chunk)

print(Binary().main('Thomas have kidney issues because he masterbate too much .'))


