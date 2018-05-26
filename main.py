"""import nltk: natural language toolkit library"""
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize

"""This function return string with chunk named 'CLAUSE' after the sentence is chunked"""
def extract_string(psent):
  for subtree in psent.subtrees():
    if subtree.label() == 'CLAUSE':
      yield ' '.join(word for word, tag in subtree.leaves())

#*****************************************************************************************#

"""Main function starts here"""

"""Display the information"""
print("Currently this program can only detect simple sentence in format S + V + O and some WH-question like \"Who are you\"")
"""Input text"""
text = input("\n\nEnter text:\n");

"""Tokenize the text in words"""
A  = word_tokenize(text);


"""Get part of speech tag from tokenized word"""
B = nltk.pos_tag(A);


"""Define grammar for chunking"""

chunkGram = r"""Name: {<DT>?<JJ.?>*<NN.?>*}
                Verb: {<VB.?>+<RB.?>*}
                Verb_ph:{<Verb|MD>}
                Name_ph: {<Name|PRP$|PRP>}
                simp_clause: {<Name_ph><.>*<Verb_ph><Name_ph>?}
                wh_clause: {<WP|WRB><Verb_ph><Name_ph>*<Verb>?}
                modal_clause: {<Verb_ph><simp_clause>}
                CLAUSE: {<simp_clause|wh_clause|modal_clause>}
                """;


"""Chunking"""
chunkParser = nltk.RegexpParser(chunkGram);
chunked = chunkParser.parse(B);

"""Extracting chunk named "CLAUSE" and print it."""
for npstr in extract_string(chunked):
    print (npstr)
