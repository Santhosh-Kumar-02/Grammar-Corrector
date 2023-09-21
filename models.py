from transformers import AutoTokenizer, T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")

def model_pipelines(input_text):
  input_texted = 'Fix grammatical errors in this sentence:' + str(input_text)
  input_ids = tokenizer(input_texted, return_tensors="pt").input_ids
  outputs = model.generate(input_ids, max_length=256)
  edited_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
  return edited_text