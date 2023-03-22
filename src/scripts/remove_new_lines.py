# Open the input file for reading
with open('/Users/kevii/Desktop/clip_automation/podcast_transcript/pod1_no_time', 'r') as file:

    # Read the contents of the file
    text = file.read()

# Remove all new lines from the text
text = text.replace('\n', '')

# Open the output file for writing
with open('/Users/kevii/Desktop/clip_automation/podcast_transcript/pod1_no_time', 'w') as file:

    # Write the modified text to the output file
    file.write(text)
