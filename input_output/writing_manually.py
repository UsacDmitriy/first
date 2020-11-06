with open('test_binary', 'bw') as test_file:
    for numbers in range(21):
        test_file.write(bytes([numbers]))


with open('test_binary', 'br') as test_file:
    for number in test_file:
        print(number)