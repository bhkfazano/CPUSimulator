from TextProcessing import *

def main():
    processor = TextProcessing('poema.txt')
    a = processor.enventHandler("GET_UNPROCESSED_CHAR", 0)
    for i in a:
        print(i)
main()