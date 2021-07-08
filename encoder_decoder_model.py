from rich import inspect
from transformers import EncoderDecoderModel
# initialize a bert2bert from two pretrained BERT models. Note that the cross-attention layers will be randomly initialized
model = EncoderDecoderModel.from_encoder_decoder_pretrained('google/vit-base-patch16-224', 'roberta-base')
