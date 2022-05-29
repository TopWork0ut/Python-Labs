from classes.publications import PrintedBook, AudioBook, Magazine


def main():
    printed_book = PrintedBook("PrintedBookCaption", False, "Fantasy", 200, "Coated Paper")
    print(printed_book)

    audio_book = AudioBook("AudioBookCaption", False, "Fantasy", 3, 2.5)
    print(audio_book)

    magazine = Magazine("MagazineCaption", "Documental", "Ukraine History")
    print(magazine)


if __name__ == '__main__':
    main()
