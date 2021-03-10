from src.Hash import Hash

if __name__ == '__main__':
    text = "Nobody inspects the spammish repetition"
    h = Hash()
    result = h.hashing(text)
    print(result)
