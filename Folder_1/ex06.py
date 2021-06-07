text = "X-DSPAM-Confidence:    0.8475"
a = text.find(':')
b = text[a+1:]
print(float(b))
