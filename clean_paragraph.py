def clean_paragraph(paragraph):
    # Split the paragraph into words
    words = paragraph.split()
    
    # Process each word to remove underscores and '.pdf' extension
    cleaned_words = []
    for word in words:
        # Remove underscores
        word_no_underscores = word.replace('_', ' ')
        
        # Remove '.pdf' extension if present
        if word_no_underscores.endswith('.pdf'):
            word_no_underscores = word_no_underscores[:-4]
        
        cleaned_words.append(word_no_underscores)
    
    # Join the cleaned words back into a paragraph
    cleaned_paragraph = ' '.join(cleaned_words)
    
    return cleaned_paragraph

# Example usage:
input_paragraph = input("Enter a paragraph: ")
cleaned_paragraph = clean_paragraph(input_paragraph)
print("Cleaned paragraph:", cleaned_paragraph)













'''def clean_phrase(phrase):
    # Remove underscores
    phrase_no_underscores = phrase.replace('_', ' ')
    
    # Remove '.pdf' extension if present
    if phrase_no_underscores.endswith('.pdf'):
        phrase_no_underscores = phrase_no_underscores[:-4]
    
    return phrase_no_underscores

# Example usage:
input_phrase = input("Enter a phrase: ")
cleaned_phrase = clean_phrase(input_phrase)
print("Cleaned phrase:", cleaned_phrase)'''
