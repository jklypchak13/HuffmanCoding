from character_counter import CharacterCounter

counter = CharacterCounter()

counter.add_text('hello')
counter.add_text('l')

print(counter.occurences('l'))
