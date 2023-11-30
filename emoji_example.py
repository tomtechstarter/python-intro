import emoji

text =  """
Hallo Du!:index_pointing_at_the_viewer:
Dies ist ein cooler:smiling_face_with_sunglasses: Emoji-Text:winking_face:"
"""

text2 = """
Wilkommen im Kino! 🍿
Dieser Film ist ab 18! 🔞
"""

emojized_text = emoji.emojize(text)
demojized_text2 = emoji.demojize(text2)

print("text:" + text)
print("emojized_text:" + emojized_text)
print("text2:" + text2)
print("demojized_text2:" + demojized_text2)

print(emoji.emojize(":winking_face_with_tongue:"))

# Emojis sind einfach Unicode Zeichen, welche wir mit \U oder direkt angeben können, ohne emoji Library 
# print("\U0001F603")
# print("😃")
# print("Lachendes gesicht mit lachenden Augen", "\N{grinning face with smiling eyes}" )
# print("\U0001F604")