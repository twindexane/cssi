story= '''The {1} little pigs, I {2} huff and puff and blow your {0} down'''

print story.format('house', 'Three', 'will')

noun = raw_input("Enter a noun: ")
num = raw_input("Enter a number: ")
verb = raw_input("Enter a verb: ")

print (story.format(noun, num, verb))
