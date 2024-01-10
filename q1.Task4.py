currently working on this

import spacy
from spacy import displacy 
from transformers import BertTokenizer, BertForTokenClassification
import pandas as pd

class NERProcessor:
  def __init__(self, spacy_model, bio_model):
    self.nlp_sci_sm=spacy_model
    self.nlp_bc5cdr_md=spacy.load(bio_model)
    self.tokenizer=BertTokenizer.from_pretrained(bio_model)
    self.model=BertForTokenClassification.from_pretrained(bio_model)

# Establisng spacy models
    nlp_bc5cdr_md=spacy.load('en_ner_bc5cdr_md')
    nlp_sci_sm=spacy.load('en_core_sci_sm')

# Setting BioBERT pretrained functions
    model=BertForTokenClassification.from_pretrained("monologg/biobert_v1.1_pubmed")
    tokenizer=BertTokenizer.from_pretrained("monologg/biobert_v1.1_pubmed")

# Entity extraction(spacy)
def extract_entities_spacy(txt,design):
    file=design(txt)
    entities=[(ent.txt,ent.classification) for ent in file.ents]
    return entities

#Entity extraction(BioBERT)
def extract_entities_biobert(self,txt):
    input=self.tokenizer(txt,return_tensors="pt")
    output=self.model(**input)
    predictions=output.logits.argmax(dim=2)
  
# Predictions into entities
    entities=[(self.tokenizer.convert_ids_to_tokens(input['input_ids'][0][i].item()),
           self.model.config.id2label[predictions[0][i].item()])
          for i in range(len(predictions[0]))]
    return entities

def process_csv_file(self, doc_path, txt_col_name):
    df = pd.read_csv(doc_path)
    txt_col = df[txt_col_name].astype(str)

    entities_sci_sm=[self.extract_entities_spacy(txt,self.nlp_sci_sm) for txt in txt_col]
    entities_bc5cdr_md=[self.extract_entities_spacy(txt,self.nlp_bc5cdr_md)for txt in txt_col]
    entities_biober=[self.extract_entities_biobert(txt)for txt in txt_col]
    return entities_sci_sm,entities_bc5cdr_md,entities_biobert

def compare_data(self,entities_sci_sm,entities_bc5cdr_md,entities_biobert):
    common_entities=set(entities_sci_sm)& set(entities_bc5cdr_md)& set(entities_biobert)
    total_entities_sci_sm=sum(len(entities)for entities in entities_sci_sm
    total_entities_bc5cdr_md=sum(len(entities)for entities in entities_bc5cdr_md)
    total_entities_biobert=sum(len(entities)for entities in entities_biobert)

    print("\nResults:")
    print("Total entities detected by en_core_sci_sm",total_entities_sci_sm)
    print("Total entities detected by en_ner_bc5cdr_md:",total_entities_bc5cdr_md)
    print("Total entities detected by biobert:",total_entities_biobert)
    print("Common entities:",common_entities)

ner_processor=NERProcessor(spacy_model='en_core_sci_sm', bio_model='en_ner_bc5cdr_md')
